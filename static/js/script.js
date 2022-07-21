'use strict';
window.addEventListener("DOMContentLoaded", function (event) {
    let dvd_size_input = document.querySelector('#size')
    let book_weight_input = document.querySelector('#weight')
    let furniture_height_input = document.querySelector('#height')
    let furniture_width_input = document.querySelector('#width')
    let furniture_length_input = document.querySelector('#length')

    let dvd_div = document.querySelector('#DVDchoice');
    let furniture_div = document.querySelector('#Furniturechoice');
    let book_div = document.querySelector('#Bookchoice');
    let productType = document.querySelector('#producttype');

    function hide_furniture() {
        furniture_div.classList.add('d-none');
        furniture_height_input.value = '';
        furniture_width_input.value = '';
        furniture_length_input.value = '';
        furniture_height_input.removeAttribute('required');
        furniture_width_input.removeAttribute('required');
        furniture_length_input.removeAttribute('required');
    }
    function hide_book() {
        book_div.classList.add('d-none');
        book_weight_input.value = '';
        book_weight_input.removeAttribute('required');
    }
    function hide_dvd() {
        dvd_div.classList.add('d-none');
        dvd_size_input.value = '';
        dvd_size_input.removeAttribute('required');
    }

    productType.addEventListener('change', function () {
            if (this.value === 'DVD') {
                dvd_div.classList.remove('d-none');
                dvd_size_input.setAttribute('required', true);
                hide_book();
                hide_furniture();
            } else if (this.value === 'Book') {
                book_div.classList.remove('d-none');
                book_weight_input.setAttribute('required', true);
                hide_dvd();
                hide_furniture();

            } else if (this.value === 'Furniture') {
                furniture_div.classList.remove('d-none');
                furniture_height_input.setAttribute('required', true);
                furniture_width_input.setAttribute('required', true);
                furniture_length_input.setAttribute('required', true);
                hide_book();
                hide_dvd();
            }
        }
    )
    let change_event = new Event('change');

    if (producttype.value !== ''){
        producttype.dispatchEvent(change_event);
    }
})

