/**
 * data_loader_v1.js
 *
 * event / statement 構造のJSONを読み込むための
 * 最小限のデータローダー。
 *
 * ※ logs.html はまだ未使用
 * ※ 表示・評価・解釈ロジックは含めない
 */

async function loadEventIndex() {
  const response = await fetch('./data/events/index.json');
  if (!response.ok) {
    throw new Error('Failed to load event index');
  }
  return response.json();
}

async function loadEventData(eventFilePath) {
  // 先頭の "/" があっても安全に読む
  const normalizedPath =
    typeof eventFilePath === 'string' && eventFilePath.startsWith('/')
      ? eventFilePath.slice(1)
      : eventFilePath;

  const response = await fetch(normalizedPath);
  if (!response.ok) {
    throw new Error('Failed to load event data: ' + normalizedPath);
  }
  return response.json();
}

// 将来利用用（現時点では未使用）
window.__factcheckDataLoader = {
  loadEventIndex,
  loadEventData
};
