# Exercício 2: Alternância de Estilos

**Objetivo:** Ensinar como alternar estilos dinamicamente em elementos HTML usando JavaScript.

---

## Descrição:

Crie um botão que, ao ser clicado, alterna a cor de fundo de uma `div` entre duas cores. O objetivo é demonstrar como manipular estilos diretamente com JavaScript e usar condicionais para controlar a lógica de alternância.

---

## Passo 1: Estrutura HTML

1. **Botão de Alternância:**
   - Adicione um botão com o texto "Mudar Cor" para alternar a cor de fundo da `div`.
   - Atribua um identificador (`id`) ao botão para que ele possa ser acessado no JavaScript.

2. **Div Colorida:**
   - Crie uma `div` com um fundo colorido inicial (por exemplo, `lightblue`).
   - Defina um tamanho fixo para a `div` (por exemplo, 200x200 pixels) e adicione uma margem superior para separá-la do botão.

---

## Passo 2: Estilização Básica

1. **Estilo da Div:**
   - Defina uma largura e altura para a `div`.
   - Adicione uma cor de fundo inicial (por exemplo, `lightblue`).
   - Use margens para posicionar a `div` adequadamente na página.

---

## Passo 3: Funcionalidade com JavaScript

1. **Evento de Clique:**
   - Adicione um evento de clique ao botão "Mudar Cor".
   - Quando o botão for clicado, a cor de fundo da `div` deve alternar entre duas cores (por exemplo, `lightblue` e `lightcoral`).

2. **Alternância de Cores:**
   - Use uma condicional (`if/else`) para verificar a cor de fundo atual da `div`.
   - Se a cor atual for `lightblue`, altere-a para `lightcoral`. Caso contrário, altere-a de volta para `lightblue`.

---

## Passo 4: Interatividade e Feedback Visual

1. **Alternância de Cores:**
   - O usuário pode alternar a cor de fundo da `div` clicando no botão.
   - A mudança de cor é instantânea e fornece um feedback visual claro.

2. **Experiência do Usuário:**
   - O botão é simples e intuitivo, permitindo que o usuário interaja facilmente com a página.

---

## Explicação:

Este exercício ensina como manipular estilos diretamente com JavaScript, alternando a cor de fundo de um elemento HTML. Além disso, demonstra o uso de condicionais (`if/else`) para controlar a lógica de alternância.

- **Manipulação de Estilos:** A propriedade `style.backgroundColor` é usada para alterar a cor de fundo da `div`.
- **Condicionais:** A estrutura `if/else` verifica a cor atual e decide qual cor aplicar em seguida.
- **Feedback Visual:** A mudança de cor fornece um feedback visual imediato ao usuário.

---

