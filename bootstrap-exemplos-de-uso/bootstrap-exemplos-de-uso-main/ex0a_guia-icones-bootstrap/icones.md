# Guia de Ícones no Bootstrap

## Introdução
O Bootstrap Icons é uma biblioteca de ícones gratuita com mais de 1,800 ícones. Esta biblioteca pode ser utilizada com o Bootstrap mas também funciona independentemente.

## Métodos de Instalação

### 1. Via CDN
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">
```

### 2. Via npm
```bash
npm i bootstrap-icons
```

### 3. Download
Baixe os arquivos em [icons.getbootstrap.com](https://icons.getbootstrap.com)

## Formas de Uso

### 1. Classe CSS
```html
<i class="bi bi-heart"></i> <!-- Ícone de coração -->
<i class="bi bi-heart-fill"></i> <!-- Ícone de coração preenchido -->
```

### 2. SVG
```html
<svg class="bi" width="32" height="32" fill="currentColor">
  <use xlink:href="bootstrap-icons.svg#heart"/>
</svg>
```

## Exemplos Práticos

### Ícones em Botões
```html
<!-- Botão com ícone -->
<button class="btn btn-primary">
  <i class="bi bi-search"></i> Pesquisar
</button>

<!-- Botão apenas com ícone -->
<button class="btn btn-danger">
  <i class="bi bi-trash"></i>
</button>
```

### Ícones em Formulários
```html
<div class="input-group mb-3">
  <span class="input-group-text">
    <i class="bi bi-person"></i>
  </span>
  <input type="text" class="form-control" placeholder="Username">
</div>
```

### Ícones em Cards
```html
<div class="card">
  <div class="card-body">
    <h5 class="card-title">
      <i class="bi bi-star-fill text-warning"></i> 
      Avaliação
    </h5>
    <p class="card-text">Conteúdo do card</p>
  </div>
</div>
```

### Ícones em Alertas
```html
<div class="alert alert-warning">
  <i class="bi bi-exclamation-triangle"></i>
  Atenção! Este é um alerta importante.
</div>
```

### Ícones em Links
```html
<a href="#" class="text-decoration-none">
  <i class="bi bi-envelope"></i> Contato
</a>
```

## Personalização

### Tamanho
```html
<!-- Usando classes de fonte -->
<i class="bi bi-alarm fs-1"></i> <!-- Extra grande -->
<i class="bi bi-alarm fs-2"></i> <!-- Grande -->
<i class="bi bi-alarm fs-3"></i> <!-- Médio -->
<i class="bi bi-alarm fs-4"></i> <!-- Pequeno -->
```

### Cor
```html
<i class="bi bi-heart text-danger"></i> <!-- Vermelho -->
<i class="bi bi-star text-warning"></i> <!-- Amarelo -->
<i class="bi bi-check text-success"></i> <!-- Verde -->
```

### Animação
```html
<!-- Rotação -->
<i class="bi bi-arrow-clockwise rotate"></i>

<style>
.rotate {
  animation: rotation 2s infinite linear;
}

@keyframes rotation {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(359deg);
  }
}
</style>
```

## Ícones Populares

### Navegação
```html
<i class="bi bi-house"></i> <!-- Casa -->
<i class="bi bi-gear"></i> <!-- Configurações -->
<i class="bi bi-person"></i> <!-- Usuário -->
<i class="bi bi-box-arrow-right"></i> <!-- Sair -->
```

### Mídia
```html
<i class="bi bi-play"></i> <!-- Play -->
<i class="bi bi-pause"></i> <!-- Pause -->
<i class="bi bi-stop"></i> <!-- Stop -->
<i class="bi bi-volume-up"></i> <!-- Volume -->
```

### Ações
```html
<i class="bi bi-pencil"></i> <!-- Editar -->
<i class="bi bi-trash"></i> <!-- Excluir -->
<i class="bi bi-plus"></i> <!-- Adicionar -->
<i class="bi bi-x"></i> <!-- Fechar -->
```

### Redes Sociais
```html
<i class="bi bi-facebook"></i> <!-- Facebook -->
<i class="bi bi-twitter"></i> <!-- Twitter -->
<i class="bi bi-instagram"></i> <!-- Instagram -->
<i class="bi bi-linkedin"></i> <!-- LinkedIn -->
```

## Boas Práticas

1. **Acessibilidade**
```html
<!-- Use aria-label para acessibilidade -->
<button class="btn btn-primary" aria-label="Pesquisar">
  <i class="bi bi-search"></i>
</button>

<!-- Ou use aria-hidden se o ícone for decorativo -->
<h1>Configurações <i class="bi bi-gear" aria-hidden="true"></i></h1>
```

2. **Performance**
- Carregue apenas os ícones que você precisa
- Considere usar SVG para melhor performance
- Use o CDN com cache para carregamento mais rápido

3. **Responsividade**
- Ajuste o tamanho dos ícones em diferentes breakpoints
- Use classes utilitárias do Bootstrap para controle responsivo

```html
<!-- Ícone responsivo -->
<i class="bi bi-star fs-4 fs-md-3 fs-lg-2"></i>
```

## Exemplos de Componentes Completos

### Barra de Navegação com Ícones
```html
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container">
    <a class="navbar-brand" href="#">
      <i class="bi bi-bootstrap-fill"></i> MeuSite
    </a>
    <div class="navbar-nav">
      <a class="nav-link" href="#"><i class="bi bi-house"></i> Home</a>
      <a class="nav-link" href="#"><i class="bi bi-person"></i> Perfil</a>
      <a class="nav-link" href="#"><i class="bi bi-envelope"></i> Mensagens</a>
    </div>
  </div>
</nav>
```

### Card de Produto com Ícones
```html
<div class="card">
  <div class="card-body">
    <h5 class="card-title">
      <i class="bi bi-bag"></i> Produto
    </h5>
    <p class="card-text">Descrição do produto</p>
    <div class="d-flex justify-content-between align-items-center">
      <button class="btn btn-primary">
        <i class="bi bi-cart-plus"></i> Comprar
      </button>
      <span>
        <i class="bi bi-star-fill text-warning"></i> 4.5
      </span>
    </div>
  </div>
</div>
```

## Recursos Adicionais
- [Biblioteca Completa de Ícones](https://icons.getbootstrap.com/)
- [Documentação Oficial](https://icons.getbootstrap.com/getting-started/)
- [GitHub do Projeto](https://github.com/twbs/icons)