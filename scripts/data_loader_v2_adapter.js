/*
====================================================
data_loader_v2_adapter.js

目的：
既存 logs.html の表示構造を壊さずに、
v2 データ構造（event index / event JSON）を
読み替えるための「中間アダプター」。

このファイル単体では何もしない。
logs.html 側から明示的に呼ばれたときのみ機能する。

ルール：
・表示ロジックは持たない
・評価・加工・解釈は行わない
・v2 構造を v1 表示形式に「合わせるだけ」
====================================================
*/

async function loadEventsV2ForLegacyView() {
  const indexRes = await fetch('./data/events/index.json');
  const indexData = await indexRes.json();

  const results = [];

  for (const ev of indexData.events) {
    const evRes = await fetch(`./data/events/${ev.event_file}`);
    const evData = await evRes.json();

    results.push({
      event: {
        id: evData.event_id,
        title: evData.event_name,
        file: `./data/events/${ev.event_file}`
      },
      data: evData
    });
  }

  return results;
}

// まだ export も使用もしない
// 差し替え工程で初めて利用する
