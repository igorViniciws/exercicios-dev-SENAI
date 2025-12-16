# Guia Básico do Bootstrap

## Introdução
Bootstrap é um framework front-end que facilita o desenvolvimento de sites responsivos e móveis. Este guia cobre os conceitos fundamentais e componentes mais utilizados do Bootstrap.

## Instalação
Você pode incluir o Bootstrap de duas maneiras:

### 1. Via CDN (mais comum)
```html
<!-- CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">

<!-- JavaScript (coloque antes do fechamento do body) -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
```

### 2. Via Download
Baixe os arquivos em [getbootstrap.com](https://getbootstrap.com)

## Sistema de Grid
O Bootstrap usa um sistema de grid de 12 colunas para layout responsivo.

### Classes de Grid Básicas
- `.container` ou `.container-fluid`
- `.row`
- `.col`, `.col-sm`, `.col-md`, `.col-lg`, `.col-xl`

### Exemplo de Grid
```html
<div class="container">
  <div class="row">
    <div class="col-md-6">Coluna 1</div>
    <div class="col-md-6">Coluna 2</div>
  </div>
</div>
```

## Classes Utilitárias

### Margens (m-)
- `m-*`: Todas as direções
- `mt-*`: Topo
- `mb-*`: Base
- `ms-*`: Esquerda
- `me-*`: Direita
- `mx-*`: Horizontal
- `my-*`: Vertical

### Padding (p-)
- `p-*`: Todas as direções
- `pt-*`: Topo
- `pb-*`: Base
- `ps-*`: Esquerda
- `pe-*`: Direita
- `px-*`: Horizontal
- `py-*`: Vertical

*Valores (*):`0`, `1`(0.25rem), `2`(0.5rem), `3`(1rem), `4`(1.5rem), `5`(3rem)

### Cores
#### Texto
- `text-primary`: Azul
- `text-secondary`: Cinza
- `text-success`: Verde
- `text-danger`: Vermelho
- `text-warning`: Amarelo
- `text-info`: Azul claro
- `text-light`: Claro
- `text-dark`: Escuro

#### Background
- `bg-primary`
- `bg-secondary`
- `bg-success`
- `bg-danger`
- `bg-warning`
- `bg-info`
- `bg-light`
- `bg-dark`

### Display
- `d-none`: Oculto
- `d-block`: Block
- `d-inline`: Inline
- `d-inline-block`: Inline-block
- `d-flex`: Flex
- `d-grid`: Grid

### Flexbox
- `justify-content-start`
- `justify-content-center`
- `justify-content-end`
- `align-items-start`
- `align-items-center`
- `align-items-end`

### Texto
- `text-start`: Alinhado à esquerda
- `text-center`: Centralizado
- `text-end`: Alinhado à direita
- `fw-bold`: Negrito
- `fst-italic`: Itálico
- `text-uppercase`: Maiúsculas
- `text-lowercase`: Minúsculas

## Componentes Principais

### Botões
```html
<button class="btn btn-primary">Primário</button>
<button class="btn btn-secondary">Secundário</button>
<button class="btn btn-success">Sucesso</button>
<button class="btn btn-danger">Perigo</button>
```

### Cards
```html
<div class="card">
  <div class="card-body">
    <h5 class="card-title">Título</h5>
    <p class="card-text">Conteúdo do card.</p>
    <a href="#" class="btn btn-primary">Botão</a>
  </div>
</div>
```

### Formulários
```html
<form>
  <div class="mb-3">
    <label class="form-label">Email</label>
    <input type="email" class="form-control">
  </div>
  <button type="submit" class="btn btn-primary">Enviar</button>
</form>
```

### Navbar
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container">
    <a class="navbar-brand" href="#">Logo</a>
    <div class="navbar-nav">
      <a class="nav-link active" href="#">Home</a>
      <a class="nav-link" href="#">Sobre</a>
    </div>
  </div>
</nav>
```

## Breakpoints Responsivos
- `xs`: < 576px
- `sm`: ≥ 576px
- `md`: ≥ 768px
- `lg`: ≥ 992px
- `xl`: ≥ 1200px
- `xxl`: ≥ 1400px

## Boas Práticas
1. Sempre use o sistema de grid para layouts
2. Utilize classes utilitárias em vez de CSS personalizado quando possível
3. Mantenha a estrutura HTML semântica
4. Teste em diferentes tamanhos de tela
5. Use componentes do Bootstrap em vez de criar do zero

## Dicas de Performance
1. Use apenas os componentes necessários
2. Considere carregar o CSS antes do conteúdo
3. Carregue o JavaScript no final do body
4. Use o sistema de grid com moderação em elementos aninhados

## Acessibilidade
1. Use atributos ARIA quando necessário
2. Mantenha a ordem lógica do conteúdo
3. Use cores com contraste adequado
4. Inclua textos alternativos em imagens

## Recursos Adicionais
- [Documentação Oficial do Bootstrap](https://getbootstrap.com/docs/)
- [Bootstrap Icons](https://icons.getbootstrap.com/)
- [Bootstrap Themes](https://themes.getbootstrap.com/)
- [Bootstrap GitHub](https://github.com/twbs/bootstrap)