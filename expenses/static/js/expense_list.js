console.log('START JS FILE');

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

for (const el of document.querySelectorAll('.likes')) {
  el.addEventListener('click', (event) => {
    const counter = el.querySelector('.counter');
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

for (const el of document.querySelectorAll('.like')) {
  el.addEventListener('click', (event) => {
    console.log(el);
    event.preventDefault();
    const star = el.querySelector('.bi-star');
    const url = el.form.action;
    const csrftoken = getCookie('csrftoken');
    star.classList.remove('bi-star');
    star.classList.add('bi-arrow-repeat');
    fetch(url, {
      method: 'POST',
      headers: {'X-CSRFToken': csrftoken},
      mode: 'same-origin',
    }).then(r => r.text()).then(s => {
      star.classList.remove('bi-arrow-repeat');
      star.classList.add('bi-star-fill');
    });
    console.log(star);
  });
}

// console.log(document.querySelectorAll('tr'));

console.log('END JS FILE');
