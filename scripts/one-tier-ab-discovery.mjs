#!/usr/bin/env node
/**
 * ONE モデル: Tier A/B 観測マスター × 興行 JSON から、
 * YouTube 上の「候補一次情報（動画 URL）」を列挙する。
 *
 * 使い方:
 *   node scripts/one-tier-ab-discovery.mjs --event data/events/one-173.json
 *   node scripts/one-tier-ab-discovery.mjs --event data/events/one-173.json --master data/observation-masters/one-tier-ab-v1.json --out reports/one-173-discovery.json
 *
 * モード:
 *   --mode auto   YOUTUBE_API_KEY があれば api、なければ rss（古い興行では rss は取りこぼし大）
 *   --mode api    Data API v3 必須（過去興行の網羠に推奨）
 *   --mode rss    チャンネル RSS の直近エントリのみ（無料・API 不要・履歴浅い）
 *   --mode manual 検索用 URL のみ生成（キー不要）
 *
 * 環境変数:
 *   YOUTUBE_API_KEY  YouTube Data API v3 キー（mode api / auto で使用）
 */

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = dirname(fileURLToPath(import.meta.url));
const REPO_ROOT = resolve(__dirname, "..");

function parseArgs(argv) {
  const out = {
    event: null,
    master: resolve(REPO_ROOT, "data/observation-masters/one-tier-ab-v1.json"),
    mode: "auto",
    out: null,
    daysBefore: null,
    daysAfter: null,
    forceOrg: false,
  };
  for (let i = 2; i < argv.length; i++) {
    const a = argv[i];
    if (a === "--event" && argv[i + 1]) out.event = resolve(REPO_ROOT, argv[++i]);
    else if (a === "--master" && argv[i + 1]) out.master = resolve(REPO_ROOT, argv[++i]);
    else if (a === "--mode" && argv[i + 1]) out.mode = argv[++i];
    else if (a === "--out" && argv[i + 1]) out.out = resolve(REPO_ROOT, argv[++i]);
    else if (a === "--days-before" && argv[i + 1]) out.daysBefore = Number(argv[++i]);
    else if (a === "--days-after" && argv[i + 1]) out.daysAfter = Number(argv[++i]);
    else if (a === "--force-org") out.forceOrg = true;
    else if (a === "--help" || a === "-h") out.help = true;
  }
  return out;
}

function loadJson(path) {
  return JSON.parse(readFileSync(path, "utf8"));
}

function collectBoutKeywords(cards) {
  const terms = new Set();
  for (const card of cards || []) {
    for (const bout of card.bouts || []) {
      if (bout.red) terms.add(String(bout.red).trim());
      if (bout.blue) terms.add(String(bout.blue).trim());
    }
  }
  return [...terms];
}

function buildSearchQuery(eventName, extraTerms, maxLen = 180) {
  const parts = [eventName, ...extraTerms].filter(Boolean);
  const q = [...new Set(parts)].join(" ");
  return q.length > maxLen ? q.slice(0, maxLen) : q;
}

function eventWindowISO(eventDateStr, daysBefore, daysAfter) {
  const mid = new Date(`${eventDateStr}T12:00:00+09:00`);
  const start = new Date(mid.getTime() - daysBefore * 86400000);
  const end = new Date(mid.getTime() + daysAfter * 86400000);
  return { startISO: start.toISOString(), endISO: end.toISOString() };
}

async function ytApiGet(url) {
  const res = await fetch(url);
  const data = await res.json();
  if (!res.ok) {
    const msg = data?.error?.message || res.statusText;
    throw new Error(`YouTube API: ${msg}`);
  }
  return data;
}

async function resolveChannelId(apiKey, handleRaw) {
  const handle = String(handleRaw || "").replace(/^@/, "");
  if (!handle) return null;
  const url = new URL("https://www.googleapis.com/youtube/v3/channels");
  url.searchParams.set("part", "id,snippet");
  url.searchParams.set("forHandle", handle);
  url.searchParams.set("key", apiKey);
  const data = await ytApiGet(url.toString());
  const id = data.items?.[0]?.id;
  return id || null;
}

/**
 * API キーなしの救済用。YouTube の HTML 構造変更で壊れうるため、取れた場合はマスターに channel_id を固定保存推奨。
 */
async function scrapeChannelIdFromHandle(handleRaw) {
  const handle = String(handleRaw || "").replace(/^@/, "");
  if (!handle) return null;
  const pageUrl = `https://www.youtube.com/@${encodeURIComponent(handle)}`;
  const res = await fetch(pageUrl, {
    headers: {
      "User-Agent":
        "Mozilla/5.0 (compatible; ForecastCheckBot/1.0; +https://github.com/) AppleWebKit/537.36",
      "Accept-Language": "ja,en;q=0.9",
    },
  });
  if (!res.ok) return null;
  const html = await res.text();
  const m =
    html.match(/"channelId":"(UC[A-Za-z0-9_-]{20,})"/) ||
    html.match(/"browseId":"(UC[A-Za-z0-9_-]{20,})"/) ||
    html.match(/channel_id=([A-Za-z0-9_-]{20,})/);
  return m ? m[1] : null;
}

async function searchChannelVideos(apiKey, channelId, publishedAfter, publishedBefore, q) {
  const out = [];
  let pageToken = null;
  do {
    const url = new URL("https://www.googleapis.com/youtube/v3/search");
    url.searchParams.set("part", "snippet");
    url.searchParams.set("channelId", channelId);
    url.searchParams.set("type", "video");
    url.searchParams.set("order", "date");
    url.searchParams.set("maxResults", "50");
    url.searchParams.set("publishedAfter", publishedAfter);
    url.searchParams.set("publishedBefore", publishedBefore);
    if (q) url.searchParams.set("q", q);
    url.searchParams.set("key", apiKey);
    if (pageToken) url.searchParams.set("pageToken", pageToken);
    const data = await ytApiGet(url.toString());
    for (const it of data.items || []) {
      const vid = it.id?.videoId;
      if (!vid) continue;
      out.push({
        videoId: vid,
        title: it.snippet?.title || "",
        publishedAt: it.snippet?.publishedAt || "",
        url: `https://www.youtube.com/watch?v=${vid}`,
      });
    }
    pageToken = data.nextPageToken || null;
  } while (pageToken);
  return out;
}

function parseYoutubeFeedEntries(xml) {
  const entries = [];
  const re = /<entry>([\s\S]*?)<\/entry>/g;
  let m;
  while ((m = re.exec(xml))) {
    const block = m[1];
    const vid =
      (block.match(/<yt:videoId>([^<]+)<\/yt:videoId>/) || [])[1] ||
      (block.match(/\/watch\?v=([A-Za-z0-9_-]{6,})/) || [])[1];
    const published = (block.match(/<published>([^<]+)<\/published>/) || [])[1];
    const title = (block.match(/<title>([^<]*)<\/title>/) || [])[1];
    if (vid && published) {
      entries.push({
        videoId: vid,
        title: title || "",
        publishedAt: published,
        url: `https://www.youtube.com/watch?v=${vid}`,
      });
    }
  }
  return entries;
}

async function fetchRssForChannel(channelId) {
  const feedUrl = `https://www.youtube.com/feeds/videos.xml?channel_id=${encodeURIComponent(channelId)}`;
  const res = await fetch(feedUrl);
  if (!res.ok) throw new Error(`RSS fetch failed ${res.status}: ${feedUrl}`);
  const xml = await res.text();
  return parseYoutubeFeedEntries(xml);
}

function filterByWindow(videos, startISO, endISO) {
  const t0 = new Date(startISO).getTime();
  const t1 = new Date(endISO).getTime();
  return videos.filter((v) => {
    const t = new Date(v.publishedAt).getTime();
    return t >= t0 && t <= t1;
  });
}

function manualChannelUrl(channelId, handle) {
  if (channelId) return `https://www.youtube.com/channel/${channelId}/videos`;
  if (handle) return `https://www.youtube.com/@${String(handle).replace(/^@/, "")}/videos`;
  return null;
}

function youtubeResultsSearchUrl(query) {
  return `https://www.youtube.com/results?search_query=${encodeURIComponent(query)}`;
}

function flattenObservers(master) {
  const list = [];
  for (const o of master.tier_a_observers || []) list.push({ ...o, _tier: "A" });
  for (const o of master.tier_b_observers || []) list.push({ ...o, _tier: o.tier || "B" });
  return list;
}

async function main() {
  const args = parseArgs(process.argv);
  if (args.help || !args.event) {
    console.error(`Usage: node scripts/one-tier-ab-discovery.mjs --event data/events/one-173.json [options]\n`);
    process.exit(args.help ? 0 : 1);
  }

  const event = loadJson(args.event);
  const master = loadJson(args.master);
  const orgEvent = event.event_meta?.organization;
  if (master.organization && orgEvent && master.organization !== orgEvent && !args.forceOrg) {
    console.error(
      `Organization mismatch: master=${master.organization} event=${orgEvent} (use --force-org to ignore)`
    );
    process.exit(1);
  }

  const db = master.date_window_defaults || {};
  const daysBefore = args.daysBefore ?? db.days_before ?? 14;
  const daysAfter = args.daysAfter ?? db.days_after ?? 3;
  const dateStr = event.event_meta?.date;
  if (!dateStr) {
    console.error("event.event_meta.date missing");
    process.exit(1);
  }

  const { startISO, endISO } = eventWindowISO(dateStr, daysBefore, daysAfter);
  const eventName = event.event_meta?.event_name || event.event_id;
  const boutTerms = collectBoutKeywords(event.cards);
  const baseKeywords = [event.event_id, eventName, ...boutTerms];

  const apiKey = process.env.YOUTUBE_API_KEY || "";
  let mode = args.mode;
  if (mode === "auto") mode = apiKey ? "api" : "rss";

  if (mode === "api" && !apiKey) {
    console.error("mode=api requires YOUTUBE_API_KEY");
    process.exit(1);
  }

  const observers = flattenObservers(master);
  const report = {
    generated_at: new Date().toISOString(),
    master_id: master.master_id,
    event_id: event.event_id,
    event_name: eventName,
    event_date: dateStr,
    window: { start: startISO, end: endISO, days_before: daysBefore, days_after: daysAfter },
    mode,
    keywords: baseKeywords,
    observers: [],
    coverage: {
      channel_scans: 0,
      videos_total: 0,
      channels_resolved_via_api: 0,
      channels_resolved_via_scrape: 0,
    },
  };

  for (const obs of observers) {
    const tier = obs._tier;
    const extra = obs.extra_query_terms || [];
    const q = buildSearchQuery(eventName, [...baseKeywords.slice(0, 5), ...extra]);
    const row = {
      observer_id: obs.observer_id,
      tier,
      predictor_name: obs.predictor_name,
      scan_targets: [],
    };

    for (const t of obs.youtube_scan_targets || []) {
      const handle = t.youtube_handle || "";
      let channelId = t.youtube_channel_id || "";

      if (mode === "manual") {
        row.scan_targets.push({
          label: t.label,
          role: t.role,
          youtube_handle: handle || null,
          youtube_channel_id: channelId || null,
          channel_videos_url: manualChannelUrl(channelId, handle),
          youtube_search_url: youtubeResultsSearchUrl(q),
          note: "manual: ブラウザで期間を絞り込み、一次情報を確認してから statements に反映",
        });
        continue;
      }

      if (!channelId && handle && mode === "api") {
        channelId = await resolveChannelId(apiKey, handle);
        if (channelId) report.coverage.channels_resolved_via_api++;
      }

      if (!channelId && handle && (mode === "rss" || mode === "auto")) {
        channelId = await scrapeChannelIdFromHandle(handle);
        if (channelId) report.coverage.channels_resolved_via_scrape++;
      }

      if (!channelId) {
        row.scan_targets.push({
          label: t.label,
          role: t.role,
          error: "youtube_channel_id 未設定。マスターに ID を入れるか、handle + YOUTUBE_API_KEY で解決してください。",
          youtube_handle: handle || null,
          channel_videos_url: manualChannelUrl("", handle),
          youtube_search_url: youtubeResultsSearchUrl(q),
        });
        continue;
      }

      let videos = [];
      try {
        if (mode === "api") {
          videos = await searchChannelVideos(apiKey, channelId, startISO, endISO, q);
        } else {
          const all = await fetchRssForChannel(channelId);
          videos = filterByWindow(all, startISO, endISO);
        }
      } catch (e) {
        row.scan_targets.push({
          label: t.label,
          role: t.role,
          youtube_channel_id: channelId,
          error: String(e.message || e),
        });
        continue;
      }

      report.coverage.videos_total += videos.length;
      report.coverage.channel_scans++;

      row.scan_targets.push({
        label: t.label,
        role: t.role,
        youtube_channel_id: channelId,
        search_query_used: mode === "api" ? q : null,
        videos_in_window: videos,
        rss_limit_note:
          mode === "rss"
            ? "RSS は直近約15件のみ。興行が古いとウィンドウ内が空でも、実際には動画がある場合があります。mode=api を推奨。"
            : null,
      });
    }

    report.observers.push(row);
  }

  const text = JSON.stringify(report, null, 2);
  if (args.out) {
    mkdirSync(dirname(args.out), { recursive: true });
    writeFileSync(args.out, text, "utf8");
    console.error(`Wrote ${args.out}`);
  }
  console.log(text);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
