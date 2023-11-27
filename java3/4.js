const target = document.getElementById('target');
const students = [
  { id: '2345768', name: 'John' },
  { id: '2134657', name: 'Paul' },
  { id: '5423679', name: 'Jones' },
];
const select = document.createElement('select');
for (let i = 0; i < students.length; i++) {
  const option = document.createElement('option');
  option.value = students[i].id;
  option.textContent = students[i].name;
  select.appendChild(option);
}
target.appendChild(select);
const section = document.querySelector('section');
const picArray = [  {    title: 'Title 1',    medium_image: 'medium_image_1.jpg',    large_image: 'large_image_1.jpg',    caption: 'Caption 1',    description: 'Description 1',  },  {    title: 'Title 2',    medium_image: 'medium_image_2.jpg',    large_image: 'large_image_2.jpg',    caption: 'Caption 2',    description: 'Description 2',  },  // more items...];

for (let i = 0; i < picArray.length; i++) {
  const article = document.createElement('article');
  article.classList.add('card');
  const h2 = document.createElement('h2');
  h2.textContent = picArray[i].title;
  const figure = document.createElement('figure');
  const img = document.createElement('img');
  img.src = picArray[i].medium_image;
  img.alt = picArray[i].title;
  const figcaption = document.createElement('figcaption');
  figcaption.textContent = picArray[i].caption;
  const p = document.createElement('p');
  p.textContent = picArray[i].description;
  figure.appendChild(img);
  figure.appendChild(figcaption);
  article.appendChild(h2);
  article.appendChild(figure);
  article.appendChild(p);
  section.appendChild(article);
}