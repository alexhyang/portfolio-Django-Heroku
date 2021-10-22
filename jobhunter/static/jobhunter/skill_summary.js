$(function () {
  loadPage();
});

function loadPage() {
  fetch("/jobhunter-app/skills/fetch")
    .then((response) => response.json())
    .then((results) => {
      addToPage(results);
    });
}

function addToPage(results) {
  // add response results to page
  const ul = document.querySelector("#cloud");
  for (var key in results) {
    const count = results[key];
    const skillElem = document.createElement("li");
    skillElem.setAttribute("data-weight", count);
    skillElem.style.setProperty("--size", Math.log(count) * 2 + 1);
    skillElem.innerHTML = key;
    ul.append(skillElem);
  }
}