# Exercício 1: Manipulação Básica do DOM

**Objetivo:** Ensinar como selecionar e modificar elementos do DOM (Document Object Model) usando JavaScript.

---

## Descrição:

Crie um botão e um parágrafo em HTML. Ao clicar no botão, o texto do parágrafo deve mudar para "Olá, Mundo!". O objetivo é demonstrar como selecionar elementos, adicionar eventos e modificar o conteúdo do DOM.

---

## Passo 1: Estrutura HTML

1. **Botão:**
   - Adicione um botão com o texto "Clique aqui".
   - Atribua um identificador (`id`) ao botão para que ele possa ser acessado no JavaScript.

2. **Parágrafo:**
   - Crie um parágrafo (`<p>`) com um texto inicial (por exemplo, "Texto inicial").
   - Atribua um identificador (`id`) ao parágrafo para que ele possa ser acessado no JavaScript.

---

## Passo 2: Funcionalidade com JavaScript

1. **Seleção de Elementos:**
   - Use `document.querySelector` para selecionar o botão e o parágrafo com base em seus identificadores (`id`).

2. **Evento de Clique:**
   - Adicione um evento de clique ao botão usando `addEventListener`.
   - Quando o botão for clicado, o texto do parágrafo deve ser alterado para "Olá, Mundo!".

3. **Modificação de Conteúdo:**
   - Use a propriedade `textContent` para alterar o texto do parágrafo.

---

## Passo 3: Interatividade e Feedback Visual

1. **Mudança de Texto:**
   - O usuário pode clicar no botão para alterar o texto do parágrafo.
   - A mudança de texto é instantânea e fornece um feedback visual claro.

2. **Experiência do Usuário:**
   - O botão é simples e intuitivo, permitindo que o usuário interaja facilmente com a página.

---

## Explicação:

Este exercício ensina os conceitos básicos de manipulação do DOM, incluindo seleção de elementos, adição de eventos e modificação de conteúdo.

- **Seleção de Elementos:** `document.querySelector` é usado para selecionar elementos do DOM com base em seus identificadores (`id`).
- **Eventos:** `addEventListener` é usado para adicionar um evento de clique ao botão.
- **Modificação de Conteúdo:** A propriedade `textContent` é usada para alterar o texto de um elemento.

---
