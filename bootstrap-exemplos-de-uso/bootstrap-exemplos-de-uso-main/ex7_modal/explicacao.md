# Exercício 7: Modal com Bootstrap

**Objetivo:** Criar um modal interativo utilizando Bootstrap, demonstrando a implementação de janelas modais responsivas e seus componentes.

---
## Descrição:
Este exercício demonstra a criação de um modal Bootstrap, que é uma janela de diálogo que aparece sobreposta ao conteúdo principal da página. O modal inclui um cabeçalho, corpo e rodapé, com botões para interação do usuário.

---
## Passo 1: Configuração Inicial
1. **Dependências Bootstrap:**
   - Incluir CSS do Bootstrap via CDN
   - Adicionar JavaScript do Bootstrap no final do body
2. **Estrutura Base:**
   - Container principal com margem superior
   - Botão de acionamento do modal

---
## Passo 2: Botão de Acionamento
1. **Estrutura do Botão:**
   - Classe `btn btn-primary`
   - Atributos de dados para controle do modal:
     - `data-bs-toggle="modal"`
     - `data-bs-target="#exemploModal"`
2. **Posicionamento:**
   - Dentro de um container com margem
   - Alinhamento adequado na página

---
## Passo 3: Estrutura do Modal
1. **Container do Modal:**
   - Classe principal `modal fade`
   - ID correspondente ao target do botão
2. **Componentes Internos:**
   - `modal-dialog` para dimensionamento
   - `modal-content` para o conteúdo
   - Divisões para header, body e footer

---
## Passo 4: Elementos do Modal
1. **Cabeçalho (Header):**
   - Título do modal
   - Botão de fechar (×)
2. **Corpo (Body):**
   - Conteúdo principal
   - Texto ou elementos HTML
3. **Rodapé (Footer):**
   - Botão de fechamento
   - Botão de ação principal

---
## Conceitos Importantes:
1. **Classes Essenciais:**
   - `modal`: Container principal
   - `modal-dialog`: Dimensionamento e posicionamento
   - `modal-content`: Estrutura do conteúdo
   - `modal-header`, `modal-body`, `modal-footer`: Seções do modal

2. **Atributos de Dados:**
   - `data-bs-toggle`: Tipo de comportamento
   - `data-bs-target`: Alvo do modal
   - `data-bs-dismiss`: Ação de fechamento

3. **Botões e Interações:**
   - Botões com classes específicas
   - Ações de fechamento automático
   - Personalização de comportamentos

---
## Explicação:
Este exercício demonstra a implementação de um modal Bootstrap, um componente essencial para interfaces modernas. O foco está na criação de interações dinâmicas e responsivas.

- **Estrutura Modular:** Divide o modal em seções lógicas (header, body, footer) para melhor organização do conteúdo.
- **Interatividade:** Utiliza JavaScript embutido do Bootstrap para controlar o comportamento do modal.
- **Design Responsivo:** Adapta-se automaticamente a diferentes tamanhos de tela.
- **Customização:** Permite personalização através das classes do Bootstrap.
- **Acessibilidade:** Implementa recursos de acessibilidade padrão do Bootstrap para melhor usabilidade.