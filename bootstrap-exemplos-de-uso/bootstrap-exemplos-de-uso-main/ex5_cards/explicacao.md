# Exercício 5: Cards com Bootstrap

**Objetivo:** Criar cards responsivos utilizando o framework Bootstrap, demonstrando o uso de grid system e componentes do Bootstrap.

---
## Descrição:
Neste exercício, você criará dois cards responsivos usando Bootstrap, que se adaptam a diferentes tamanhos de tela. Cada card contém um título, texto e um botão, demonstrando a versatilidade dos componentes do Bootstrap.

---
## Passo 1: Configuração Inicial
1. **Dependências do Bootstrap:**
   - Incluir o CSS do Bootstrap via CDN no `head`
   - Adicionar o JavaScript do Bootstrap no final do `body`
2. **Meta Tags:**
   - Configurar charset e viewport para responsividade
   - Definir o idioma do documento como português

---
## Passo 2: Estrutura do Container
1. **Container Principal:**
   - Usar a classe `container` para centralizar o conteúdo
   - Adicionar margem superior com a classe `mt-3`
2. **Sistema de Grid:**
   - Criar uma linha com a classe `row`
   - Dividir em duas colunas usando `col-sm-6`

---
## Passo 3: Criação dos Cards
1. **Card Base:**
   - Utilizar a classe `card` para o container principal
   - Adicionar `card-body` para o conteúdo interno
2. **Elementos Internos:**
   - **Título:** Usar `card-title` em um `h5`
   - **Texto:** Aplicar `card-text` em um `p`
   - **Botão:** Combinar classes `btn` e `btn-primary` ou `btn-secondary`

---
## Passo 4: Responsividade e Layout
1. **Comportamento Responsivo:**
   - Em telas maiores que 576px: cards lado a lado
   - Em telas menores: cards empilhados
2. **Espaçamento:**
   - Margem superior no container para espaçamento
   - Espaçamento automático entre os cards

---
## Conceitos Importantes:
1. **Grid System:**
   - O Bootstrap usa um sistema de 12 colunas
   - `col-sm-6` divide a tela em duas partes iguais
   - Breakpoint 'sm' ativa em 576px

2. **Classes de Componentes:**
   - `card`: container flex para conteúdo
   - `card-body`: padding e estrutura interna
   - `card-title`: estilização de títulos
   - `card-text`: formatação de parágrafos

3. **Classes Utilitárias:**
   - `mt-3`: margin-top de 1rem
   - `container`: centralização e largura máxima
   - `row`: wrapper flex para colunas

---
## Personalizações Possíveis:
1. **Variações de Estilo:**
   - Diferentes cores de botões (success, danger, warning)
   - Adição de bordas ou sombras aos cards
   - Inclusão de imagens no topo dos cards

2. **Melhorias de Layout:**
   - Ajuste do número de colunas
   - Adição de footers nos cards
   - Inclusão de badges ou ícones

3. **Interatividade:**
   - Hover effects nos cards
   - Animações nos botões
   - Links dinâmicos

---
## Dicas de Desenvolvimento:
1. **Boas Práticas:**
   - Mantenha a estrutura HTML semântica
   - Use classes Bootstrap ao invés de CSS customizado
   - Teste em diferentes tamanhos de tela

2. **Acessibilidade:**
   - Mantenha textos legíveis
   - Use cores com contraste adequado
   - Inclua atributos ARIA quando necessário

3. **Performance:**
   - Carregue o Bootstrap via CDN
   - Minimize o uso de estilos customizados
   - Otimize imagens se utilizadas