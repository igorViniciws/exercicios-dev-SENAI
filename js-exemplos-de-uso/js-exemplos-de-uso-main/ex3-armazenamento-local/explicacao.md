# Exercício 3: Armazenamento Local (localStorage)

**Objetivo:** Ensinar como usar o `localStorage` para salvar e restaurar preferências do usuário, como o tema (modo claro/escuro) de uma página.

---

## Descrição:

Crie um botão que alterna entre o modo claro e escuro de uma página. A preferência do usuário é salva no `localStorage` e restaurada automaticamente ao carregar a página.

---

## Passo 1: Estrutura HTML

1. **Botão de Alternância:**
   - Adicione um botão com o texto "Modo Escuro" para alternar entre os temas.
   - Atribua um identificador (`id`) ao botão para que ele possa ser acessado no JavaScript.

2. **Estilos para Modo Claro e Escuro:**
   - Defina estilos CSS para o modo claro (padrão) e o modo escuro (usando uma classe `.dark-mode`).
   - Adicione transições suaves para garantir uma experiência agradável ao alternar entre os temas.

---

## Passo 2: Funcionalidade com JavaScript

1. **Verificar Preferência Salva:**
   - Ao carregar a página, verifique se há uma preferência salva no `localStorage` (por exemplo, `mode: 'dark'`).
   - Se a preferência for o modo escuro, aplique a classe `.dark-mode` ao `body` e atualize o texto do botão.

2. **Alternância de Temas:**
   - Adicione um evento de clique ao botão para alternar entre os temas.
   - Use `classList.toggle` para adicionar ou remover a classe `.dark-mode` do `body`.

3. **Salvar Preferência:**
   - Quando o tema for alterado, salve a preferência no `localStorage` (por exemplo, `mode: 'dark'` ou `mode: 'light'`).
   - Atualize o texto do botão para refletir o tema atual.

---

## Passo 3: Interatividade e Feedback Visual

1. **Alternância de Temas:**
   - O usuário pode alternar entre os temas clicando no botão.
   - A mudança de tema é instantânea e suave, graças às transições CSS.

2. **Persistência de Preferência:**
   - A preferência do usuário é salva no `localStorage` e restaurada automaticamente ao recarregar a página.
   - Isso garante uma experiência consistente para o usuário.

---

## Explicação:

Este exercício ensina como usar o `localStorage` para salvar e restaurar preferências do usuário, como o tema de uma página. Além disso, demonstra como alternar classes CSS dinamicamente para alterar a aparência da página.

- **localStorage:** Usado para armazenar dados no navegador do usuário, permitindo que as preferências sejam salvas entre sessões.
- **Alternância de Classes:** A classe `.dark-mode` é adicionada ou removida do `body` para alternar entre os temas.
- **Feedback Visual:** O texto do botão é atualizado para refletir o tema atual, e as transições CSS garantem uma mudança suave.

---
