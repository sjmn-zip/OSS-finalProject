const feed = document.querySelector("#feed");

// ① 사진 자리: 사진이 있으면 이미지, 없으면 분류 이름
function createPhoto(item) {
  if (item.photo) {
    return `<img class="card-photo" src="${item.photo}" alt="${item.name}">`;
  }
  return `<div class="card-photo">${item.category
    }</div>`;
}
// ② 분실물 1개 → 카드 HTML 1개
function createCard(item) {
  return `
    <div class="card">
      ${createPhoto(item)
    }
      <div class="card-body">
        <span class="card-badge">보관중</span>
        <span class="card-badge">${item.category
    }</span>
        <h3 class="card-title">${item.name
    }</h3>
        <p class="card-meta">${item.date
    } · ${item.place
    } 보관</p>
      </div>
    </div>
  `;
}
// ③ 카드 목록 그리기 (팀 약속: renderFeed)
function renderFeed(items) {
  if (items.length === 0) {
    feed.innerHTML = `<p class="feed-message">찾는 분실물이 없습니다</p>`;
    return;
  }
  feed.innerHTML = items.map(createCard).join("");
}
// ④ JSON 파일 가져오기 (팀 약속: loadItems)
async function loadItems() {
  const response = await fetch("//파일이름");
  if (!response.ok) {
    throw new Error(`파일을 불러오지 못했습니다 (${response.status
      })`);
  }
  return await response.json();
}
// ⑤ 시작: 가져와서 그리기, 실패하면 안내 문구
async function start() {
  try {
    const items = await loadItems();
    renderFeed(items);
  } catch (error) {
    feed.innerHTML = `<p class="feed-message">분실물을 불러오지 못했습니다</p>`;
    console.error(error);
  }
}

start();