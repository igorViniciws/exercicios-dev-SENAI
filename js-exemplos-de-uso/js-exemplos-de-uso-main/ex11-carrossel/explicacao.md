# Exercício 11: Carrossel de Imagens

**Objetivo:** Entender como criar um carrossel de imagens simples usando HTML, CSS e JavaScript.

---

## Passo 1: Estrutura HTML

Crie a estrutura básica do carrossel. O carrossel será composto por uma lista de imagens e botões de navegação. A lista de imagens deve estar dentro de um container, e os botões de navegação (anterior e próximo) devem ser posicionados ao lado do container.

---

## Passo 2: Estilização com CSS

Agora, vamos estilizar o carrossel para que as imagens sejam exibidas uma de cada vez, com botões de navegação.

1. **Container do Carrossel:**
   - Defina um tamanho máximo para o container e garanta que ele ocupe o espaço centralizado na página.
   - Use `overflow: hidden` para esconder as imagens que não estão ativas.

2. **Imagens:**
   - As imagens devem ocupar 100% da largura do container e ser exibidas uma de cada vez.
   - Use `display: none` para esconder todas as imagens por padrão e `display: block` para mostrar apenas a imagem ativa.

3. **Botões de Navegação:**
   - Posicione os botões fora do container da imagem, à esquerda e à direita.
   - Use `position: absolute` para garantir que os botões fiquem sobrepostos ao carrossel.
   - Adicione estilos para que os botões sejam visíveis e interativos.

---

## Passo 3: Interatividade com JavaScript

Agora, vamos adicionar a funcionalidade de navegação entre as imagens.

1. **Troca de Imagens:**
   - Crie uma função para mostrar a imagem ativa, alternando a classe `active` entre as imagens.
   - Implemente a lógica para avançar para a próxima imagem e voltar para a anterior.

2. **Navegação Automática:**
   - Use `setInterval` para trocar automaticamente as imagens a cada 5 segundos.
   - Pause a troca automática quando o usuário interagir com os botões de navegação.

3. **Eventos de Clique:**
   - Adicione eventos de clique aos botões para permitir a navegação manual.
   - Reinicie o intervalo de troca automática após cada interação do usuário.

4. **Pausar ao Passar o Mouse:**
   - Pause a troca automática quando o mouse estiver sobre o carrossel e retome quando o mouse sair.

---

## Explicação:

O carrossel é uma técnica para exibir várias imagens (ou outros conteúdos) em um espaço limitado, permitindo que o usuário navegue entre elas.

- **CSS:** Controla a disposição das imagens (`display: flex`) e a transição entre elas (`transition: transform`). Também posiciona os botões de navegação fora do container da imagem.
- **JavaScript:** Controla a lógica de navegação, alternando a classe `active` para exibir a imagem correta. Implementa a troca automática de imagens e a navegação manual com os botões.

---
