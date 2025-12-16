# Exercício 10: Menu Hamburguer

**Objetivo:** Entender como criar um menu hamburguer responsivo usando HTML, CSS e JavaScript.

---

## Passo 1: Estrutura HTML

Crie a estrutura básica do menu hamburguer. O menu será composto por um ícone de hamburguer e uma lista de links que será exibida quando o ícone for clicado.

1. **Ícone de Hamburguer:**
   - Use um ícone de hamburguer (por exemplo, `&#9776;` ou um ícone de uma biblioteca como Font Awesome).
   - Adicione um identificador (`id`) para o ícone, que será usado no JavaScript.

2. **Lista de Links:**
   - Crie uma lista de links (`<ul>` com `<li>`) que representará o menu de navegação.
   - Adicione uma classe para controlar a visibilidade da lista com CSS.

---

## Passo 2: Estilização com CSS

Agora, vamos estilizar o menu para que ele seja responsivo. O menu hamburguer será exibido apenas em telas pequenas.

1. **Menu em Telas Grandes:**
   - Em telas grandes, o menu deve ser exibido normalmente, com os links dispostos horizontalmente.

2. **Menu em Telas Pequenas:**
   - Em telas pequenas, o ícone de hamburguer deve ser exibido, e a lista de links deve estar oculta por padrão (`display: none`).
   - Quando o menu estiver ativo, a lista de links deve ser exibida verticalmente (`display: flex` ou `display: block`).

3. **Transições e Estilos:**
   - Adicione transições suaves para abrir e fechar o menu.
   - Estilize o ícone de hamburguer e os links para garantir uma boa experiência do usuário.

---

## Passo 3: Interatividade com JavaScript

Agora, vamos adicionar a funcionalidade de abrir e fechar o menu hamburguer ao clicar no ícone.

1. **Evento de Clique:**
   - Adicione um evento de clique ao ícone de hamburguer.
   - Quando o ícone for clicado, alterne a visibilidade da lista de links, adicionando ou removendo uma classe (por exemplo, `active`).

2. **Fechar o Menu:**
   - Adicione a funcionalidade para fechar o menu ao clicar em um link ou ao rolar a página.
   - Garanta que o menu seja fechado automaticamente em interações que não envolvam o ícone.

---

## Explicação:

O menu hamburguer é uma técnica comum em design responsivo para ocultar o menu de navegação em telas pequenas e exibi-lo quando o usuário clica no ícone de hamburguer.

- **CSS:** Controla a visibilidade do menu (`display: none` ou `display: flex`) com base no tamanho da tela. Também define a aparência e a disposição dos elementos do menu.
- **JavaScript:** Adiciona a interatividade, alternando a classe `active` que controla a visibilidade do menu. Permite que o menu seja aberto e fechado dinamicamente.

---
