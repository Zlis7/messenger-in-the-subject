(function() {
    'use strict';

    function open_chat(id_chat){

    }

    window.onload = function() {
        const url = new URL(window.location.href);
        const params = new URLSearchParams(url.search);
        const id_chat = params.get('id', '')

        if (id_chat != null){
            document.querySelector('main').style.display = 'flex';
            document.querySelector('.main-chat').style.display = 'flex';
            document.querySelector('.id-chat').value = id_chat
        } else{
            document.querySelector('main').style.display = 'none';
        }

        const contactItems = document.querySelectorAll('.item-contact');

        contactItems.forEach(item => {
          item.addEventListener('click', function() {
            window.location.href = `?id=${item.id}`;
          });
        });

        const container = document.querySelector('.content-contact');
        container.scrollTop = container.scrollHeight;
    };

    document.querySelector('.open-settings').addEventListener('click', (event) => {
        document.querySelector('main').style.display = 'flex';
        document.querySelector('.main-settings').style.display = 'flex';
        document.querySelector('.main-chat').style.display = 'none';
    })

    document.querySelector('.menu-close-main').addEventListener('click', (event) => {
        document.querySelector('main').style.display = 'none';
        document.querySelector('.main-chat').style.display = 'none';
        document.querySelector('.main-settings').style.display = 'none';
    })

    document.querySelector('.close-settings').addEventListener('click', (event) => {
        document.querySelector('main').style.display = 'none';
        document.querySelector('.main-settings').style.display = 'none';
    })

    document.querySelector('.reload-page').addEventListener('click', (event) => {
        window.location.reload();
    })

    document.querySelector('.search-form').addEventListener('submit', (event) => {
        event.preventDefault();
        window.location.href = `?id=${event.target.children[0].value}`;
    })

    document.querySelector('.item-contact').addEventListener('click', (event) => {
        console.log(this.id);
    })

})();