# Exercício 6: Lista de Tarefas

**Objetivo:** Ensinar manipulação de arrays e eventos, criando uma lista de tarefas onde o usuário pode adicionar, remover e marcar tarefas como concluídas.

---

## Descrição:

Crie uma lista de tarefas interativa onde o usuário pode:
- Adicionar novas tarefas.
- Marcar tarefas como concluídas.
- Visualizar as tarefas em uma lista.

---

## Passo 1: Estrutura HTML

1. **Campo de Entrada:**
   - Adicione um campo de texto (`<input>`) para que o usuário insira novas tarefas.
   - Defina um `placeholder` para orientar o usuário.

2. **Botão de Adicionar:**
   - Adicione um botão para permitir que o usuário adicione a tarefa à lista.

3. **Lista de Tarefas:**
   - Crie uma lista não ordenada (`<ul>`) para exibir as tarefas.
   - Cada tarefa será representada por um item de lista (`<li>`).

4. **Estilização Condicional:**
   - Adicione uma classe CSS (por exemplo, `.completed`) para estilizar tarefas concluídas (por exemplo, com texto riscado e cor cinza).

---

## Passo 2: Funcionalidade com JavaScript

1. **Adicionar Tarefas:**
   - Adicione um evento de clique ao botão "Adicionar".
   - Quando o botão for clicado, verifique se o campo de entrada não está vazio.
   - Crie um novo item de lista (`<li>`) com o texto da tarefa e adicione-o à lista.

2. **Marcar Tarefas como Concluídas:**
   - Adicione um evento de clique a cada item de lista.
   - Quando o item for clicado, alterne a classe `.completed` para marcar ou desmarcar a tarefa como concluída.

3. **Limpar Campo de Entrada:**
   - Após adicionar uma tarefa, limpe o campo de entrada para permitir a inserção de uma nova tarefa.

---

## Passo 3: Interatividade e Feedback Visual

1. **Feedback Visual:**
   - Tarefas concluídas devem ser estilizadas com texto riscado e cor cinza.
   - Tarefas não concluídas devem ser exibidas normalmente.

2. **Experiência do Usuário:**
   - Garanta que o campo de entrada seja limpo após a adição de uma tarefa.
   - Permita que o usuário marque e desmarque tarefas com um único clique.

---

## Explicação:

Este exercício ensina conceitos importantes de manipulação de arrays e eventos em JavaScript, além de estilização condicional com CSS.

- **Manipulação de Arrays:** Adicionar novos elementos (tarefas) a uma lista dinâmica.
- **Eventos:** Usar eventos de clique para adicionar tarefas e marcar/desmarcar como concluídas.
- **Estilização Condicional:** Aplicar classes CSS dinamicamente para fornecer feedback visual ao usuário.

---

