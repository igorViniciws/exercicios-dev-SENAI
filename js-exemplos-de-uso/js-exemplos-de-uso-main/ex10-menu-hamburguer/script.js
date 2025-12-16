// Seleciona o ícone do menu e a lista de navegação pelo ID
const menuIcon = document.getElementById('menu-icon');
const navList = document.getElementById('nav-list');

// Adiciona um evento de clique ao ícone do menu
menuIcon.addEventListener('click', () => {
  // Alterna a classe "active" na lista de navegação
  navList.classList.toggle('active');
});