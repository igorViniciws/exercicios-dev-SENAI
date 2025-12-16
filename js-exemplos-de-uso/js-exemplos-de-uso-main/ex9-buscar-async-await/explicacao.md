# Exercício 9: Buscar Dados de Usuário com Async/Await

**Objetivo:** Entender como fazer uma requisição assíncrona a uma API usando `async/await`, exibir os dados na página e tratar erros de forma adequada.

---

## Passo 1: Estrutura HTML

Crie a estrutura básica da página, que inclui um botão para buscar os dados do usuário e uma área para exibir os dados retornados.

1. **Botão "Buscar Usuário":**
   - Adicione um botão com o texto "Buscar Usuário" e um identificador (`id`) para que ele possa ser acessado no JavaScript.

2. **Área de Exibição de Dados:**
   - Crie um elemento (por exemplo, uma `div`) para exibir os dados do usuário. Esse elemento também deve ter um identificador (`id`) para ser manipulado via JavaScript.

---

## Passo 2: Requisição à API com Async/Await

Agora, vamos implementar a lógica para buscar os dados do usuário de uma API e exibi-los na página.

1. **Evento de Clique:**
   - Adicione um evento de clique ao botão "Buscar Usuário". Quando o botão for clicado, uma função assíncrona será executada.

2. **Requisição à API:**
   - Use `fetch` para fazer uma requisição à API. A URL da API pode ser, por exemplo, `https://jsonplaceholder.typicode.com/users/5`, que retorna os dados de um usuário específico.
   - Utilize `await` para aguardar a resposta da API.

3. **Tratamento da Resposta:**
   - Verifique se a resposta da API foi bem-sucedida (`response.ok`). Caso contrário, lance um erro.
   - Converta a resposta para JSON usando `await response.json()`.

4. **Exibição dos Dados:**
   - Exiba os dados do usuário (como nome, e-mail e telefone) na área reservada para isso, atualizando o conteúdo do elemento HTML.

---

## Passo 3: Tratamento de Erros

Erros durante a requisição devem ser tratados para garantir uma boa experiência do usuário.

1. **Bloco Try/Catch:**
   - Use um bloco `try/catch` para capturar erros que possam ocorrer durante a requisição ou o processamento dos dados.

2. **Exibição de Erros:**
   - Se ocorrer um erro, exiba uma mensagem de erro na página, utilizando uma cor destacada (por exemplo, vermelho).
   - Adicione o erro ao console para facilitar o debugging.

---

## Explicação:

Este exercício demonstra como fazer uma requisição assíncrona a uma API usando `async/await`, uma abordagem moderna e legível para lidar com operações assíncronas em JavaScript.

- **Async/Await:** Simplifica o trabalho com Promises, permitindo que o código assíncrono seja escrito de forma mais clara e sequencial.
- **Fetch API:** Usada para fazer requisições HTTP e obter dados de uma API.
- **Tratamento de Erros:** O bloco `try/catch` é essencial para capturar e tratar erros que possam ocorrer durante a requisição ou o processamento dos dados.

---

