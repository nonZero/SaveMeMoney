console.log('START JS FILE');

for (const el of document.querySelectorAll('.likes')) {
  el.addEventListener('click', (event) => {
    const counter = el.querySelector(".counter");
    const v = +counter.textContent;
    counter.textContent = v + 1;
  });
}

const h1 = document.querySelector('h1');

h1.addEventListener('click', () => {
  console.log('>>>> 1');
  h1.style.backgroundColor = 'black';
  setTimeout(() => {
    console.log('!!!!!');
    h1.style.backgroundColor = 'pink';
  }, 2000);
  console.log('>>>> 2');
});

for (const el of document.querySelectorAll('.btn-star')) {
  el.addEventListener('click', (event) => {
    console.log(el);
    event.preventDefault();
    const star = el.querySelector(".bi-star");
    // debugger;
    console.log(star);
    star.classList.add("bi-star-fill");
    star.classList.remove("bi-star");
  });
}

// console.log(document.querySelectorAll('tr'));

console.log('END JS FILE');
