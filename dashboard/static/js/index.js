let searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = ()  => {
    searchForm.classList.toggle('active');
    navbar.classList.remove('active');

}

let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = ()  => {
    searchForm.classList.remove('active');
    navbar.classList.toggle('active');
}

window.onscroll = () =>{
    searchForm.classList.remove('active');
    navbar.classList.toggle('active');
}


const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

