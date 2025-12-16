# Exercício 4: Requisições Assíncronas (fetch)

**Objetivo:** Ensinar como fazer requisições assíncronas usando a API `fetch` para buscar dados de uma API e exibi-los na página.

---

## Descrição:

Crie um botão que, ao ser clicado, faz uma requisição assíncrona a uma API e exibe o resultado em um parágrafo. O objetivo é demonstrar como usar `fetch` para buscar dados e manipular a resposta.

---

## Passo 1: Estrutura HTML

1. **Botão de Busca:**
   - Adicione um botão com o texto "Buscar Dados" para iniciar a requisição.
   - Atribua um identificador (`id`) ao botão para que ele possa ser acessado no JavaScript.

2. **Área de Exibição:**
   - Crie um parágrafo (`<p>`) para exibir os dados retornados pela API.
   - Atribua um identificador (`id`) ao parágrafo para que ele possa ser atualizado dinamicamente.

---

## Passo 2: Funcionalidade com JavaScript

1. **Evento de Clique:**
   - Adicione um evento de clique ao botão "Buscar Dados".
   - Quando o botão for clicado, uma requisição assíncrona será feita à API.

2. **Requisição com `fetch`:**
   - Use a função `fetch` para fazer uma requisição GET à API (por exemplo, `https://jsonplaceholder.typicode.com/todos/1`).
   - Converta a resposta para JSON usando o método `.json()`.

3. **Exibição dos Dados:**
   - Atualize o conteúdo do parágrafo com os dados retornados pela API (por exemplo, o título de uma tarefa).

4. **Tratamento de Erros:**
   - Use `.catch` para capturar e tratar erros que possam ocorrer durante a requisição.
   - Exiba uma mensagem de erro no parágrafo caso a requisição falhe.

---

## Passo 3: Interatividade e Feedback Visual

1. **Feedback Visual:**
   - Quando a requisição for bem-sucedida, o parágrafo exibirá os dados retornados pela API.
   - Em caso de erro, o parágrafo exibirá uma mensagem de erro clara.

2. **Experiência do Usuário:**
   - O botão fornece uma interação simples e direta para buscar dados.
   - O usuário recebe feedback imediato sobre o resultado da requisição.

---

## Explicação:

Este exercício ensina como fazer requisições assíncronas usando a API `fetch`, manipular respostas JSON e tratar erros de forma adequada.

- **Requisições Assíncronas:** A função `fetch` é usada para buscar dados de uma API de forma assíncrona.
- **Manipulação de Respostas:** A resposta da API é convertida para JSON e os dados são exibidos na página.
- **Tratamento de Erros:** O método `.catch` é usado para capturar e tratar erros que possam ocorrer durante a requisição.

---

