# Comparação: Exercício 4 (fetch com Promises) vs. Exercício 9 (async/await)

**Objetivo:** Entender as diferenças e semelhanças entre as abordagens de requisições assíncronas usando `fetch` com Promises (Exercício 4) e `async/await` (Exercício 9).

---

## Descrição:

Ambos os exercícios abordam o conceito de **requisições assíncronas** em JavaScript, mas utilizam abordagens diferentes para lidar com a assincronicidade. O Exercício 4 usa `fetch` com Promises (`.then` e `.catch`), enquanto o Exercício 9 usa `async/await` para simplificar o código.

---

## Exercício 4: Requisições Assíncronas (fetch)

### Objetivo:
Ensinar como fazer requisições assíncronas básicas usando a API `fetch` e manipular respostas com Promises.

### Conceitos Ensinados:
1. **Uso de `fetch`:**
   - Faz requisições HTTP assíncronas.
2. **Manipulação de Respostas:**
   - Usa `.then` para processar a resposta e `.json()` para converter dados JSON.
3. **Tratamento de Erros:**
   - Usa `.catch` para capturar e tratar erros.

### Quando Usar:
- Ideal para iniciantes que estão aprendendo sobre requisições assíncronas.
- Mostra o fluxo básico de Promises e como encadear operações.

---

## Exercício 9: Buscar Dados de Usuário com Async/Await

### Objetivo:
Ensinar como usar `async/await` para simplificar o código assíncrono, tornando-o mais legível e fácil de entender.

### Conceitos Ensinados:
1. **Uso de `async/await`:**
   - Simplifica o código assíncrono, tornando-o mais parecido com código síncrono.
2. **Manipulação de Respostas:**
   - Usa `await` para esperar a resolução de Promises.
3. **Tratamento de Erros:**
   - Usa `try/catch` para capturar e tratar erros.

### Quando Usar:
- Ideal para quem já entende Promises e quer escrever código mais limpo e moderno.
- Útil em projetos maiores, onde a legibilidade e manutenção do código são importantes.

---

## Diferenças Principais:

| Característica               | Exercício 4 (fetch com Promises)          | Exercício 9 (async/await)                |
|------------------------------|-------------------------------------------|------------------------------------------|
| **Sintaxe**                  | Usa `.then` e `.catch`.                   | Usa `async/await` e `try/catch`.         |
| **Legibilidade**             | Código mais encadeado e menos linear.     | Código mais sequencial e legível.        |
| **Tratamento de Erros**      | Usa `.catch` para erros.                  | Usa `try/catch` para erros.              |
| **Complexidade**             | Mais simples, ideal para iniciantes.      | Um pouco mais avançado, mas mais moderno.|
| **Cenário de Uso**           | Introdução a requisições assíncronas.     | Aprimoramento de código assíncrono.      |

---

## Conclusão:

Ambos os exercícios são **complementares** e cobrem desde o básico até técnicas mais avançadas de programação assíncrona em JavaScript.

- **Exercício 4 (fetch com Promises):**
  - Introduz o conceito de requisições assíncronas.
  - Mostra o fluxo básico de Promises e como encadear operações.
  - Ideal para iniciantes.

- **Exercício 9 (async/await):**
  - Aprimora o código assíncrono, tornando-o mais legível e moderno.
  - Mostra como substituir o encadeamento de Promises por uma sintaxe mais limpa.
  - Ideal para quem já domina Promises e quer evoluir.

---

