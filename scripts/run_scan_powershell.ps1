# UTF-8: リポジトリルートから実行。Python が無い環境用の同等スキャン。
$ErrorActionPreference = "Stop"
$Root = Split-Path $PSScriptRoot -Parent
$rawEnv = Get-Content -LiteralPath (Join-Path $Root ".env") -Raw -Encoding UTF8
if ($rawEnv -notmatch "YOUTUBE_API_KEY\s*=\s*(\S+)") {
  throw ".env に YOUTUBE_API_KEY がありません"
}
$key = $Matches[1].Trim()

$chPath = Join-Path $Root "data\observation-masters\boxing-youtube-channels-v1.json"
$chData = Get-Content -LiteralPath $chPath -Raw -Encoding UTF8 | ConvertFrom-Json
$variantPath = Join-Path $Root "data\tmp\query_variants_lines.txt"
$variants = @(Get-Content -LiteralPath $variantPath -Encoding UTF8 | ForEach-Object { $_.Trim() } | Where-Object { $_ })

$matchDate = "2024-02-24"
$daysBefore = 30
$md = [datetime]::ParseExact($matchDate, "yyyy-MM-dd", $null)
$start = $md.AddDays(-$daysBefore)
$end = $md.AddDays(-1)
$publishedAfter = $start.ToString("yyyy-MM-dd") + "T00:00:00Z"
$publishedBefore = $end.ToString("yyyy-MM-dd") + "T00:00:00Z"

function Title-Ok([string]$t) {
  return ($t.Contains("予想") -or $t.Contains("勝敗"))
}

$report = [ordered]@{
  base_query       = "アレハンドロ・サンティアゴ 中谷潤人"
  query_variants   = $variants
  match_date       = $matchDate
  published_window = @{ days_before = $daysBefore; end_before_match_days = 1 }
  title_filter     = @{ enabled = $true; title_must_contain_any_of = @("予想", "勝敗") }
  channels         = [System.Collections.ArrayList]@()
}

foreach ($row in $chData.channels) {
  $cid = $row.channel_id
  $lab = $row.label
  $videos = [System.Collections.ArrayList]@()
  $seen = @{}
  $used = [System.Collections.ArrayList]@()
  $chErr = $null
  foreach ($q in $variants) {
    if ($videos.Count -ge 3) { break }
    $enc = [System.Uri]::EscapeDataString($q)
    $uri = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=$cid&q=$enc&publishedAfter=$publishedAfter&publishedBefore=$publishedBefore&type=video&maxResults=50&key=$key"
    try {
      $r = Invoke-RestMethod -Uri $uri -Method Get
    } catch {
      $chErr = $_.Exception.Message
      break
    }
    $got = $false
    foreach ($item in $r.items) {
      if ($videos.Count -ge 3) { break }
      $title = $item.snippet.title
      if (-not (Title-Ok $title)) { continue }
      $vid = $item.id.videoId
      if (-not $vid -or $seen.ContainsKey($vid)) { continue }
      $seen[$vid] = $true
      $got = $true
      [void]$videos.Add(@{
          title       = $title
          url         = "https://www.youtube.com/watch?v=$vid"
          publishedAt = $item.snippet.publishedAt
          title_matches_prediction_focus = $true
        })
    }
    if ($got -and $used -notcontains $q) { [void]$used.Add($q) }
  }
  if ($chErr) {
    [void]$report.channels.Add(@{ label = $lab; channel_id = $cid; error = $chErr; queries_used = @(); videos = @() })
  } else {
    [void]$report.channels.Add(@{ label = $lab; channel_id = $cid; queries_used = @($used); videos = @($videos) })
  }
}

$outFile = Join-Path $Root "data\tmp\boxing-2024-02-24-event-06-scan.json"
$null = New-Item -ItemType Directory -Force -Path (Split-Path $outFile)
$report | ConvertTo-Json -Depth 10 | Set-Content -LiteralPath $outFile -Encoding UTF8
Write-Output "WROTE $outFile"
