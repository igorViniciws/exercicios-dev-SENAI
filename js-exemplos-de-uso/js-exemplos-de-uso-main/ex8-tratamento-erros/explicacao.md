# Exercício 8: Divisão de Números com Tratamento de Erros

**Objetivo:** Entender como usar `try/catch` para tratar erros em operações matemáticas, como divisão por zero e entradas inválidas, e exibir os resultados ou erros na página e no console.

---

## Passo 1: Estrutura HTML

Crie a estrutura básica da página, que inclui campos para inserir dois números, um botão para calcular a divisão e uma área para exibir o resultado ou mensagens de erro.

1. **Campos de Entrada:**
   - Adicione dois campos de entrada (`<input type="number">`) para que o usuário insira os números.
   - Atribua identificadores (`id`) a esses campos para que possam ser acessados no JavaScript.

2. **Botão "Calcular Divisão":**
   - Adicione um botão com o texto "Calcular Divisão" e um identificador (`id`) para que ele possa ser acessado no JavaScript.

3. **Área de Exibição de Resultado:**
   - Crie um elemento (por exemplo, um parágrafo `<p>`) para exibir o resultado da divisão ou mensagens de erro. Esse elemento também deve ter um identificador (`id`).

---

## Passo 2: Lógica de Cálculo e Tratamento de Erros

Agora, vamos implementar a lógica para calcular a divisão e tratar possíveis erros.

1. **Evento de Clique:**
   - Adicione um evento de clique ao botão "Calcular Divisão". Quando o botão for clicado, uma função será executada.

2. **Validação das Entradas:**
   - Verifique se os valores inseridos nos campos de entrada são números válidos. Caso contrário, lance um erro com uma mensagem adequada.

3. **Divisão por Zero:**
   - Verifique se o segundo número é zero. Caso seja, lance um erro informando que a divisão por zero não é permitida.

4. **Cálculo da Divisão:**
   - Se as entradas forem válidas, calcule a divisão do primeiro número pelo segundo.

5. **Exibição do Resultado:**
   - Exiba o resultado da divisão na área reservada para isso.

---

## Passo 3: Tratamento de Erros com Try/Catch

Erros durante o cálculo devem ser tratados para garantir uma boa experiência do usuário.

1. **Bloco Try/Catch:**
   - Use um bloco `try/catch` para capturar erros que possam ocorrer durante a validação das entradas ou o cálculo da divisão.

2. **Exibição de Erros:**
   - Se ocorrer um erro, exiba uma mensagem de erro na página, utilizando uma formatação adequada (por exemplo, cor vermelha).
   - Adicione o erro ao console para facilitar o debugging.

3. **Bloco Finally:**
   - Use o bloco `finally` para executar código que deve ser rodado independentemente de ocorrer um erro ou não. Por exemplo, uma mensagem de "Operação concluída" no console.

---

## Explicação:

Este exercício demonstra como usar `try/catch` para tratar erros em operações matemáticas, como divisão por zero e entradas inválidas. Além disso, mostra como exibir resultados ou mensagens de erro na página e no console.

- **Try/Catch:** Usado para capturar e tratar erros que possam ocorrer durante a execução do código.
- **Validação de Entradas:** Garante que os valores inseridos pelo usuário sejam números válidos.
- **Divisão por Zero:** Um erro comum que deve ser tratado para evitar comportamentos inesperados.
- **Finally:** Bloco opcional que é executado sempre, independentemente de ocorrer um erro ou não.

---

