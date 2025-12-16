# Exercício 5: Animação Simples com JavaScript

**Objetivo:** Ensinar como criar animações simples com JavaScript, manipulando o posicionamento de elementos na página.

---

## Descrição:

Crie uma animação simples onde uma `div` se move horizontalmente na tela ao clicar em um botão. O objetivo é demonstrar como manipular o posicionamento de elementos usando JavaScript.

---

## Passo 1: Estrutura HTML

1. **Botão de Controle:**
   - Adicione um botão com o texto "Mover" para iniciar a animação.
   - Atribua um identificador (`id`) ao botão para que ele possa ser acessado no JavaScript.

2. **Elemento para Animar:**
   - Crie uma `div` que será animada.
   - Defina um tamanho e uma cor de fundo para a `div` para torná-la visível.
   - Use `position: relative` para permitir o controle do posicionamento via JavaScript.

---

## Passo 2: Estilização Básica

1. **Estilo da `div`:**
   - Defina uma largura e altura para a `div`.
   - Adicione uma cor de fundo para destacar o elemento na página.
   - Use `position: relative` para permitir a manipulação da propriedade `left`.

2. **Margem:**
   - Adicione uma margem superior para separar a `div` do botão.

---

## Passo 3: Funcionalidade com JavaScript

1. **Evento de Clique:**
   - Adicione um evento de clique ao botão "Mover".
   - Quando o botão for clicado, a `div` deve se mover horizontalmente.

2. **Controle de Posição:**
   - Use uma variável para armazenar a posição atual da `div`.
   - A cada clique, incremente a posição em 50 pixels.
   - Atualize a propriedade `left` da `div` com o novo valor da posição.

---

## Passo 4: Interatividade e Feedback Visual

1. **Movimento Horizontal:**
   - A `div` deve se mover para a direita a cada clique no botão.
   - O movimento é controlado pela propriedade `left`, que define a distância do elemento em relação à borda esquerda do contêiner.

2. **Feedback Visual:**
   - O usuário verá a `div` se movendo na tela, proporcionando uma experiência interativa e visualmente clara.

---

## Explicação:

Este exercício ensina como criar animações simples usando JavaScript para manipular o posicionamento de elementos na página.

- **Manipulação de Posicionamento:** A propriedade `left` é usada para controlar a posição horizontal de um elemento com `position: relative`.
- **Variáveis de Estado:** Uma variável é usada para armazenar e atualizar a posição atual da `div`.
- **Eventos:** O evento de clique no botão dispara a atualização da posição da `div`.

---

