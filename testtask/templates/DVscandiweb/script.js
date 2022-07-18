'use strict';
let cancel = document.querySelector('#cancel');
let submit = document.querySelector('#submit');
let form = document.querySelector('form');
let name = document.querySelector('#name');
let price = document.querySelector('#price');
let sku = document.querySelector('#sku');
let dvd = document.querySelector('#DVD');
let dvdEle = document.querySelector('#DVD-ele');
let furniture = document.querySelector('#Furniture');
let furnitureEle = document.querySelector('#Furniture-ele');
let book = document.querySelector('#Book');
let bookEle = document.querySelector('#Book-ele');
let productType = document.querySelector('#productType');



productType.addEventListener('change', function(e) {
    if (e.target.value === 'DVD') {

        dvdEle.style.display = 'block';
        bookEle.style.display = 'none';
        furnitureEle.style.display = 'none';
    } else if (e.target.value === 'Book') {

        bookEle.style.display = 'block';
        dvdEle.style.display = 'none';
        furnitureEle.style.display = 'none';

    } else if (e.target.value === 'Furniture') {

        furnitureEle.style.display = 'block';
        dvdEle.style.display = 'none';
        bookEle.style.display = 'none';
       
        
    }
}
)

cancel.addEventListener('click', function(e) {

    form.reset()
    location.href='productList.html';
    }
)


submit.addEventListener('click', function(e) {
        if (!name.value || !sku.value || !price.value) {
            alert('Please fill out all fields');
            e.preventDefault();
        }else{
         form.submit();
            location.href='productList.html';
        }
    }
    )