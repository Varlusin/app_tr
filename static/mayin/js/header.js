const lengButton = document.querySelector("#ln-select");
const lengMenu = document.querySelector("#ln-menu");
const lgOne = document.querySelector("#lg-one");
const lgTwo = document.querySelector("#lg-two");
const url = window.location.href;
const hst = window.location.host;
const lnCode = url.split(hst)[1].slice(0, 3);
const urll = url.split("/");
let stateLengMenu = 1;

function renderLengMenu() {
  if (lnCode === "/ru") {
    lgOne.insertAdjacentHTML("beforeend", "<p>ՀՅ</p>");
    lgOne.addEventListener("click", () => {
      urll.splice(3, 1);
      window.open(urll.join("/"), "_self");
    });
    lgTwo.insertAdjacentHTML("beforeend", "<p>EN</p>");
    lgTwo.addEventListener("click", () => {
      urll[3] = "en";
      window.open(urll.join("/"), "_self");
    });
  } else {
    if (lnCode === "/en") {
      lgOne.insertAdjacentHTML("beforeend", "<p>ՀՅ</p>");
      lgOne.addEventListener("click", () => {
        urll.splice(3, 1);
        window.open(urll.join("/"), "_self");
      });
      lgTwo.insertAdjacentHTML("beforeend", "<p>РУ</p>");
      lgTwo.addEventListener("click", () => {
        urll[3] = "ru";
        window.open(urll.join("/"), "_self");
      });
    } else {
      lgOne.insertAdjacentHTML("beforeend", "<p>РУ</p>");
      lgOne.addEventListener("click", () => {
        urll.splice(3, 0, "ru");
        window.open(urll.join("/"), "_self");
      });
      lgTwo.insertAdjacentHTML("beforeend", "<p>EN</p>");
      lgTwo.addEventListener("click", () => {
        urll.splice(3, 0, "en");
        window.open(urll.join("/"), "_self");
      });
    }
  }
}
renderLengMenu();

function selectLenguage() {
  if (stateLengMenu === 1) {
    lengMenu.style.cssText = "opacity:1; visibility: visible;";
    stateLengMenu = 0;
  } else {
    lengMenu.style.cssText = "opacity:0; visibility: hidden;";
    stateLengMenu = 1;
  }
}

lengButton.addEventListener("click", selectLenguage);
