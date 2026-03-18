/**
 * data_loader_v1.js
 *
 * 新しい event / statement 構造を将来読み込むための
 * 最小限のデータローダー。
 *
 * ※ 現時点では logs.html からは呼び出さない
 * ※ 表示・評価・整形ロジックは一切含めない
 */

async function loadEventIndex() {
  const response = await fetch('./data/events/index.json');
  if (!response.ok) {
    throw new Error('Failed to load event index');
  }
  return response.json();
}

async function loadEventData(eventFilePath) {
  const response = await fetch(eventFilePath);
  if (!response.ok) {
    throw new Error('Failed to load event data: ' + eventFilePath);
  }
  return response.json();
}

// 将来利用用（現時点では未使用）
window.__factcheckDataLoader = {
  loadEventIndex,
  loadEventData
};
