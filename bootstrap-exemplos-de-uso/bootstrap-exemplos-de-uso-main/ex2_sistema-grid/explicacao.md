# Exercício 2: Grid com Bootstrap

**Objetivo:** Ensinar como utilizar o sistema de grid do Bootstrap para criar layouts responsivos.

---

## Descrição:

Crie uma estrutura de grid com duas colunas utilizando o Bootstrap. O objetivo é demonstrar como o sistema de grid do Bootstrap funciona e como ele pode ser usado para criar layouts responsivos que se adaptam a diferentes tamanhos de tela.

---

## Passo 1: Estrutura HTML

1. **Configuração do Documento:**
   - Crie um documento HTML básico com a estrutura `<!DOCTYPE html>`.
   - Adicione as meta tags necessárias, como `charset` e `viewport`.
   - Inclua o link para o CSS do Bootstrap via CDN.

2. **Container:**
   - Adicione um `div` com a classe `container`. Esta classe é usada para criar um container centralizado e responsivo.

3. **Row:**
   - Dentro do container, adicione um `div` com a classe `row`. Esta classe é usada para criar uma linha que contém as colunas.

4. **Colunas:**
   - Dentro da linha, adicione dois `div`s com a classe `col-sm-6`. Esta classe define que cada coluna ocupará 50% da largura da linha em dispositivos com tela pequena (small) ou maior.
   - Adicione classes de background (`bg-primary` e `bg-secondary`) e estilos de texto (`text-white`) para diferenciar visualmente as colunas.
   - Adicione padding (`p-3`) para dar um espaçamento interno às colunas.

---

## Passo 2: Funcionalidade com Bootstrap

1. **Grid System:**
   - O Bootstrap utiliza um sistema de grid de 12 colunas. As classes `col-sm-6` indicam que cada coluna deve ocupar 6 das 12 colunas disponíveis, resultando em duas colunas de largura igual.
   - O prefixo `sm` indica que o layout de duas colunas será aplicado em dispositivos com tela pequena (small) ou maior. Em dispositivos menores, as colunas podem se empilhar verticalmente.

2. **Responsividade:**
   - O sistema de grid do Bootstrap é responsivo por padrão. Isso significa que o layout se ajusta automaticamente conforme o tamanho da tela do dispositivo.
   - O uso de classes como `col-sm-6` garante que o layout seja adaptável e consistente em diferentes dispositivos.

---

## Passo 3: Interatividade e Feedback Visual

1. **Visualização das Colunas:**
   - As colunas são visualmente distintas devido às classes de background e texto aplicadas.
   - O padding (`p-3`) proporciona um espaçamento interno que melhora a legibilidade e a estética.

2. **Experiência do Usuário:**
   - O layout é simples e intuitivo, permitindo que o usuário visualize claramente a divisão das colunas.
   - A responsividade garante uma boa experiência em dispositivos móveis e desktops.

---

## Explicação:

Este exercício ensina os conceitos básicos do sistema de grid do Bootstrap, incluindo a criação de containers, linhas e colunas, e como utilizar classes para controlar o layout e a responsividade.

- **Container:** A classe `container` é usada para criar um container centralizado e responsivo.
- **Row:** A classe `row` é usada para criar uma linha que contém as colunas.
- **Colunas:** As classes `col-sm-6` são usadas para definir colunas que ocupam metade da largura da linha em dispositivos com tela pequena ou maior.
- **Responsividade:** O sistema de grid do Bootstrap é responsivo por padrão, ajustando o layout conforme o tamanho da tela.

---