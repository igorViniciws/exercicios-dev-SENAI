# Exercício 7: Validação de Formulário

**Objetivo:** Ensinar como implementar validação de formulários em HTML e JavaScript, garantindo que os dados inseridos pelo usuário sejam corretos e fornecendo feedback visual.

---

## Descrição:

Crie um formulário de cadastro simples com validação de campos como nome, e-mail e senha. O objetivo é garantir que os dados inseridos pelo usuário atendam a critérios específicos e fornecer feedback visual em caso de erros.

---

## Passo 1: Estrutura do Formulário

1. **Campos do Formulário:**
   - Adicione campos para o nome, e-mail e senha.
   - Utilize `<input>` com os tipos apropriados (`text`, `email`, `password`).
   - Adicione elementos `<span>` para exibir mensagens de erro abaixo de cada campo.

2. **Botão de Envio:**
   - Adicione um botão do tipo `submit` para enviar o formulário.

3. **Estilização Básica:**
   - Defina estilos para as mensagens de erro, como cor vermelha e tamanho de fonte menor.

---

## Passo 2: Validação dos Campos

1. **Evento de Envio:**
   - Adicione um evento de `submit` ao formulário para interceptar o envio e realizar a validação antes de processar os dados.

2. **Validação do Nome:**
   - Verifique se o campo de nome não está vazio.
   - Se estiver vazio, exiba uma mensagem de erro informando que o nome é obrigatório.

3. **Validação do E-mail:**
   - Verifique se o campo de e-mail não está vazio e se contém o caractere `@`.
   - Se o e-mail for inválido, exiba uma mensagem de erro.

4. **Validação da Senha:**
   - Verifique se a senha tem pelo menos 6 caracteres.
   - Se a senha for muito curta, exiba uma mensagem de erro.

5. **Feedback Visual:**
   - Atualize o conteúdo dos elementos `<span>` abaixo de cada campo para exibir as mensagens de erro, se houver.

---

## Passo 3: Submissão do Formulário

1. **Verificação de Validade:**
   - Se todos os campos forem válidos, exiba uma mensagem de sucesso (por exemplo, um `alert`) e limpe o formulário.
   - Caso contrário, impeça o envio do formulário e mantenha as mensagens de erro visíveis.

2. **Reset do Formulário:**
   - Após uma submissão bem-sucedida, limpe os campos do formulário para permitir um novo cadastro.

---

## Explicação:

Este exercício ensina como validar formulários de forma eficiente, garantindo que os dados inseridos pelo usuário atendam a critérios específicos antes de serem processados.

- **Validação de Formulários:** Verifica se os dados inseridos são válidos e atendem aos requisitos.
- **Condicionais:** Usadas para verificar se os campos estão preenchidos corretamente.
- **Feedback Visual:** Mensagens de erro são exibidas abaixo dos campos para informar o usuário sobre problemas específicos.
- **Interceptação do Envio:** O evento de `submit` é interceptado para realizar a validação antes de enviar os dados.

---

