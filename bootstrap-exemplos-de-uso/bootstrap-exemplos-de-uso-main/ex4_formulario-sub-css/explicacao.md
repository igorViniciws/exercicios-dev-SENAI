# Exercício 4: Formulário Customizado com Bootstrap

**Objetivo:** Ensinar como criar um formulário estilizado e responsivo utilizando o Bootstrap, com personalizações de CSS para melhorar a aparência e a interatividade.

---

## Descrição:

Crie um formulário personalizado com campos para email, username e senha, utilizando o Bootstrap para a estrutura básica e CSS customizado para estilização avançada. O objetivo é demonstrar como combinar o Bootstrap com CSS personalizado para criar interfaces modernas e interativas.

---

## Passo 1: Estrutura HTML

1. **Configuração do Documento:**
   - Crie um documento HTML básico com a estrutura `<!DOCTYPE html>`.
   - Adicione as meta tags necessárias, como `charset` e `viewport`.
   - Inclua o link para o CSS do Bootstrap via CDN.
   - Adicione o link para a biblioteca de ícones do Bootstrap Icons.
   - Inclua um arquivo CSS customizado (`styles.css`) para estilizações adicionais.

2. **Container Principal:**
   - Adicione um `div` com a classe `container` para criar um container centralizado.
   - Adicione margem no topo (`mt-3`) para espaçamento.

3. **Formulário:**
   - Crie um formulário com a classe `custom-form` para aplicar estilos personalizados.
   - Adicione campos para email, username e senha, utilizando as classes do Bootstrap para estruturação e estilização básica.

4. **Campos do Formulário:**
   - **Email:** Use um `input` do tipo `email` com a classe `form-control` e um `label` associado.
   - **Username:** Utilize um `input-group` para adicionar um ícone ao campo de texto.
   - **Senha:** Use um `input` do tipo `password` com a classe `form-control` e um `label` associado.

5. **Botão de Envio:**
   - Adicione um botão do tipo `submit` com classes do Bootstrap e CSS customizado para estilização avançada.

---

## Passo 2: Funcionalidade com Bootstrap

1. **Estrutura do Formulário:**
   - O Bootstrap fornece classes como `form-control` e `form-label` para estilizar inputs e labels de forma consistente.
   - A classe `input-group` é usada para agrupar um ícone com um campo de texto.

2. **Responsividade:**
   - O sistema de grid do Bootstrap garante que o formulário seja responsivo e se ajuste a diferentes tamanhos de tela.
   - A classe `col-sm-6` define que os campos ocuparão metade da largura do container em dispositivos com tela pequena ou maior.

3. **Ícones:**
   - A biblioteca Bootstrap Icons é usada para adicionar ícones ao campo de username, melhorando a usabilidade e a aparência.

---

## Passo 3: Estilização com CSS Customizado

1. **Formulário:**
   - A classe `custom-form` aplica um gradiente de cores e bordas arredondadas ao formulário.
   - O padding é ajustado para garantir um espaçamento interno adequado.

2. **Inputs:**
   - A classe `custom-input` personaliza a borda, o background e o efeito de foco dos inputs.
   - O efeito de transformação (`transform: scale(1.02)`) é aplicado quando o input está em foco.

3. **Ícone do Username:**
   - A classe `custom-icon` define a cor de fundo e remove a borda do ícone.

4. **Botão de Envio:**
   - A classe `custom-button` aplica um gradiente de cores, bordas arredondadas e efeitos de hover ao botão.
   - O efeito de transformação (`transform: translateY(-5px)`) e sombra (`box-shadow`) são aplicados ao passar o mouse sobre o botão.

---

## Passo 4: Interatividade e Feedback Visual

1. **Cores e Gradientes:**
   - O uso de gradientes e cores vibrantes torna o formulário visualmente atraente.
   - As cores dos inputs e botões são escolhidas para proporcionar um bom contraste e legibilidade.

2. **Efeitos de Hover e Foco:**
   - Efeitos de hover e foco são aplicados para melhorar a interatividade e fornecer feedback visual ao usuário.
   - O botão de envio se move ligeiramente para cima e ganha uma sombra ao passar o mouse.

3. **Ícones:**
   - O ícone no campo de username adiciona um toque visual e melhora a usabilidade.

---

## Explicação:

Este exercício ensina como criar um formulário responsivo e estilizado utilizando o Bootstrap e CSS customizado. O foco é na combinação de funcionalidades do Bootstrap com personalizações de CSS para criar interfaces modernas e interativas.

- **Bootstrap:** Fornece a estrutura básica e a responsividade do formulário.
- **CSS Customizado:** Adiciona estilos avançados, como gradientes, bordas personalizadas e efeitos de hover.
- **Ícones:** Melhoram a usabilidade e a aparência do formulário.

---

Este exercício é uma introdução prática à criação de formulários responsivos e estilizados, combinando o poder do Bootstrap com a flexibilidade do CSS personalizado.