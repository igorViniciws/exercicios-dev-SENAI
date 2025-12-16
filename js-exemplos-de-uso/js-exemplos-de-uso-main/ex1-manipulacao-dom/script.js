// Seleciona o elemento do botão no DOM usando o ID "myButton" e armazena na variável 'button'

const button = document.querySelector('#myButton');

// Seleciona o elemento de parágrafo no DOM usando o ID "myText" e armazena na variável 'text'

const text = document.querySelector('#myText');


// Adiciona um "ouvinte" de evento ao botão. Quando o botão for clicado, a função dentro do 'addEventListener' será executada

button.addEventListener('click', () => {
    text.textContent = 'Olá, Mundo!';
});