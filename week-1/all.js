const hamburger = document.querySelector(".hamburger");
const items = document.querySelector(".items");
const item = document.querySelectorAll('.item')

item.forEach(n => n.addEventListener("click", function () {
      hamburger.classList.remove("active");
      items.classList.remove("active"); 
}))

hamburger.addEventListener("click", function () {
      hamburger.classList.toggle("active");
      items.classList.toggle("active");
});