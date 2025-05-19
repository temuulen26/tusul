document.getElementById("newsForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const title = document.getElementById("title").value;
  const content = document.getElementById("content").value;

  const newsItem = document.createElement("div");
  newsItem.className = "news-item";
  newsItem.innerHTML = `<h3>${title}</h3><p>${content}</p>`;

  document.getElementById("newsList").prepend(newsItem); // хамгийн сүүлд биш, эхэнд нэмнэ

  this.reset();
});
