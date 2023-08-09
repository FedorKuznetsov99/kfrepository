const burger = document.querySelector('#burger');
const menu = document.querySelector('#menu');

burger.addEventListener('click', () => {
  menu.classList.toggle('disp');
});
// Получение ссылки на кнопку "header-bth"
var headerButton = document.querySelector('.header-button');

// Получение ссылки на элемент с классом "menu-title"
var menuTitle = document.querySelector('.menu-title');

// Добавление обработчика события клика на кнопку "header-bth"
headerButton.addEventListener('click', function(event) {
  event.preventDefault(); // Предотвращение перехода по ссылке

  // Прокручивание страницы к элементу с классом "menu-title"
  menuTitle.scrollIntoView({ behavior: 'smooth' });
});
// Получение ссылки на кнопку "header-bth"
var headerButton = document.querySelector('.menu-btn');
menu-title
// Получение ссылки на элемент с классом "menu-title"
var menuTitle = document.querySelector('.button');

// Добавление обработчика события клика на кнопку "header-bth"
headerButton.addEventListener('click', function(event) {
  event.preventDefault(); // Предотвращение перехода по ссылке

  // Прокручивание страницы к элементу с классом "menu-title"
  menuTitle.scrollIntoView({ behavior: 'smooth' });
});