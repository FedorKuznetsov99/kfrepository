document.addEventListener('DOMContentLoaded', function () {
    const switchButton = document.getElementById('switch-language');
    const elementsToTranslate = document.querySelectorAll('[data-ru], [data-en]');

    let isRussian = true; // Флаг для отслеживания текущего языка

    function toggleLanguage() {
        isRussian = !isRussian;

        // Переключение текста между языками
        elementsToTranslate.forEach(function (element) {
            if (isRussian) {
                element.textContent = element.getAttribute('data-ru');
            } else {
                element.textContent = element.getAttribute('data-en');
            }
        });

        // Изменение текста на кнопке
        switchButton.textContent = isRussian ? 'Switch to English' : 'Переключить на русский';
    }

    switchButton.addEventListener('click', toggleLanguage);
});
