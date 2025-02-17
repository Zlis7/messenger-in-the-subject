(function() {
    'use strict';

    const url = new URL(window.location.href);
    const params = new URLSearchParams(url.search);
    const messageContentInURL = params.get('message', '')
    let currentRegisterContent = 'Для безопасности сервиса вам придет письмо на почту с подтверждением. Поддерживаются только адресы @yandex.ru.'

    if (messageContentInURL != null){
        document.querySelector('.message').style.display = 'block';
    } else {
        document.querySelector('.message').style.display = 'none';
    }

    document.querySelector('.trust_registration_checkbox').addEventListener('change', (event) => {
        if (event.target.checked) {
            currentRegisterContent = 'Регистрация без проверки означает, что вы получите доступ к системе только с помощью администратора.';
        } else {
            currentRegisterContent = 'Для безопасности сервиса вам придет письмо на почту с подтверждением. Поддерживаются только адресы @yandex.ru.';
        }

        document.querySelector('.message').children[0].textContent = currentRegisterContent
    });

    document.querySelector('.change-form').addEventListener('click', (event) => {
        const checkbox = document.querySelector('.trust_registration_checkbox');
        const message = document.querySelector('.message');

        if (event.target.textContent == 'Регистрация'){
            event.target.textContent = 'Авторизация';
            document.querySelector('.for-register').style.display = 'block';
            document.querySelector('main').style.height = '350px';
            document.querySelector('.act-form').value = 'registration';
            document.querySelector('.button-submit-form').textContent = 'Зарегистрироваться';

            message.children[0].textContent = currentRegisterContent;
            message.style.display = 'block';

        } else{

            if (messageContentInURL != null){
                message.children[0].textContent = messageContentInURL;
            } else{
                 message.style.display = 'none';
            }

            event.target.textContent = 'Регистрация';
            document.querySelector('.for-register').style.display = 'none';
            document.querySelector('main').style.height = '300px';
            document.querySelector('.act-form').value = 'login';
            document.querySelector('.button-submit-form').textContent = 'Войти';
        }
    })

    document.querySelector('form').addEventListener('submit', (event) => {
        event.preventDefault();
        const email = document.querySelector('#email').value;

        if (email.includes("@yandex.ru")){
            event.target.submit()
        } else {
            alert("Поддерживаются только адресы @yandex.ru")
        }
    })
})();