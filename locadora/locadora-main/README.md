# Sistema de Locadora de Veículos

Projeto de um sistema simples de locadora desenvolvido em PHP com MySQL, focado em autenticação de usuários, controle de acesso e gerenciamento de veículos.

## Objetivo
Simular o funcionamento básico de uma locadora, aplicando conceitos de banco de dados relacional, autenticação segura e controle de disponibilidade de veículos.

## Banco de Dados
O sistema utiliza o banco **locadora_db**, configurado com UTF-8 para suporte completo a caracteres.

### Tabelas
- **usuarios**
  - Armazena usuários do sistema
  - Possui controle de perfil (admin ou usuário)
  - Senhas armazenadas com `password_hash()` para segurança

- **veiculos**
  - Cadastro de veículos disponíveis para locação
  - Controle de tipo, modelo, placa e disponibilidade

## Usuários Padrão
- **Admin**
  - Usuário: `admin`
  - Senha: `admin123`
  - Perfil: administrador

- **Usuário**
  - Usuário: `usuario`
  - Senha: `user123`
  - Perfil: usuário comum

## Veículos de Demonstração
O banco já vem populado com carros e motos para facilitar testes do sistema.

## Tecnologias Utilizadas
- PHP
- MySQL
- SQL
- phpMyAdmin (ambiente local)

## Aprendizados
- Criação e modelagem de banco de dados
- Relacionamento entre usuários e recursos do sistema
- Autenticação segura com hash de senha
- Controle de permissões por perfil
- Lógica de disponibilidade de veículos

