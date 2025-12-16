# API REST de Tarefas em PHP (Railway + MySQL)

API REST simples desenvolvida em PHP para gerenciamento de tarefas, utilizando banco de dados MySQL hospedado na nuvem via Railway.

## Objetivo
Demonstrar a criação de uma API backend funcional com PHP, incluindo conexão com banco em nuvem, criação automática de tabela e endpoints REST.

## Funcionalidades
- API REST com resposta em JSON
- Suporte a CORS (GET e POST)
- Criação automática da tabela de tarefas
- Inserção de dados de teste quando o banco está vazio
- Listagem de tarefas ordenadas por data
- Criação de novas tarefas via POST
- Tratamento de erros com HTTP Status Code

## Estrutura da Tabela
Tabela **tarefas**:
- `id` (INT, chave primária)
- `titulo` (VARCHAR, obrigatório)
- `descricao` (TEXT)
- `concluida` (BOOLEAN)
- `criada_em` (TIMESTAMP)

## Tecnologias Utilizadas
- PHP (PDO)
- MySQL
- Railway (deploy em nuvem)
- JSON
- API REST

## Segurança e Boas Práticas
- Uso de variáveis de ambiente para credenciais
- PDO com tratamento de exceções
- Charset UTF-8 para suporte completo a caracteres
- Headers HTTP configurados corretamente

## Endpoints
- **GET /**  
  Retorna todas as tarefas cadastradas

- **POST /**  
  Cria uma nova tarefa  
  ```json
  {
    "titulo": "Minha tarefa",
    "descricao": "Descrição opcional"
  }

