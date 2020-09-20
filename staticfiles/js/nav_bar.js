const navbarBtn = document.querySelector('.header__btn');
const navbarLink = document.querySelector('.navbar__links');


navbarBtn.addEventListener('click', function () {
    let value = navbarLink.classList.contains('navBarCollapse');
    if (value) {
        navbarLink.classList.remove('navBarCollapse');
        navbarBtn.classList.remove('btnChange')
    }
    else {
        navbarLink.classList.add('navBarCollapse');
        navbarBtn.classList.add('btnChange')
    }
});