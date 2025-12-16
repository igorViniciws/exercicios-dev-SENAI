# Exercício 3: Botões com Bootstrap e Ícones

**Objetivo:** Ensinar como criar e estilizar botões utilizando o Bootstrap, incluindo a adição de ícones com a biblioteca Bootstrap Icons.

---

## Descrição:

Crie uma série de botões estilizados com o Bootstrap, demonstrando diferentes estilos e cores disponíveis. Além disso, adicione ícones aos botões utilizando a biblioteca Bootstrap Icons para melhorar a interface e a usabilidade.

---

## Passo 1: Estrutura HTML

1. **Configuração do Documento:**
   - Crie um documento HTML básico com a estrutura `<!DOCTYPE html>`.
   - Adicione as meta tags necessárias, como `charset` e `viewport`.
   - Inclua o link para o CSS do Bootstrap via CDN.
   - Adicione o link para a biblioteca de ícones do Bootstrap Icons.

2. **Container Principal:**
   - Adicione um `div` com a classe `container` para criar um container centralizado.
   - Utilize a classe `d-flex` para ativar o layout flexbox e `justify-content-center` para centralizar os botões horizontalmente.
   - Adicione margem no topo (`mt-3`) para espaçamento.

3. **Botões Básicos:**
   - Crie uma série de botões com as classes `btn` e `btn-*`, onde `*` representa as cores disponíveis no Bootstrap (ex: `btn-primary`, `btn-secondary`, etc.).
   - Adicione margem à esquerda (`ms-3`) para espaçamento entre os botões.

4. **Botões com Ícones:**
   - Crie um segundo container para botões que incluem ícones.
   - Utilize a classe `bi` para adicionar ícones da biblioteca Bootstrap Icons dentro dos botões.
   - Combine texto e ícones ou use apenas ícones para criar botões mais intuitivos.

---

## Passo 2: Funcionalidade com Bootstrap

1. **Estilização de Botões:**
   - O Bootstrap oferece classes pré-definidas para estilizar botões, como `btn-primary`, `btn-secondary`, `btn-success`, etc., que aplicam cores e estilos consistentes.
   - A classe `btn` é obrigatória para aplicar o estilo básico de botão.

2. **Ícones com Bootstrap Icons:**
   - A biblioteca Bootstrap Icons fornece uma ampla variedade de ícones que podem ser facilmente integrados aos botões.
   - Use a classe `bi` seguida do nome do ícone (ex: `bi-search`, `bi-trash`) para adicionar ícones.

3. **Layout Flexbox:**
   - A classe `d-flex` ativa o layout flexbox, permitindo alinhar e distribuir os botões de forma eficiente.
   - A classe `justify-content-center` centraliza os botões horizontalmente no container.

---

## Passo 3: Interatividade e Feedback Visual

1. **Cores e Estilos:**
   - Os botões têm cores distintas que indicam diferentes ações ou estados (ex: primário, sucesso, perigo).
   - A estilização consistente melhora a usabilidade e a experiência do usuário.

2. **Ícones:**
   - Os ícones adicionam significado visual aos botões, tornando-os mais intuitivos e amigáveis.
   - Botões com ícones podem ser usados para ações específicas, como "Pesquisar" ou "Excluir".

3. **Responsividade:**
   - O layout flexbox garante que os botões se ajustem corretamente em diferentes tamanhos de tela.

---

## Explicação:

Este exercício ensina como criar botões estilizados com o Bootstrap e como adicionar ícones utilizando a biblioteca Bootstrap Icons. O foco é na criação de interfaces intuitivas e visualmente atraentes.

- **Botões:** As classes `btn` e `btn-*` são usadas para estilizar botões com cores e estilos pré-definidos.
- **Ícones:** A classe `bi` é usada para adicionar ícones da biblioteca Bootstrap Icons.
- **Layout Flexbox:** As classes `d-flex` e `justify-content-center` são usadas para alinhar e centralizar os botões.

---

Este exercício é uma introdução prática à criação de botões estilizados e à integração de ícones em projetos web utilizando o Bootstrap e Bootstrap Icons.