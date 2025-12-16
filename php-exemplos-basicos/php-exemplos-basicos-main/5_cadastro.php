<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Cadastro de Usuário</title>
</head>
<body>
    <form method="post" action="">
        <label for="nome">Nome:</label>
        <input type="text" name="nome" required><br>

        <label for="senha">Senha:</label>
        <input type="password" name="senha" required><br>

        <button type="submit">Cadastrar</button>
    </form>
    <?php

    // Verifica se o formulário foi enviado
    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        // Recebe os valores
        $nome =$_POST['nome'];
        $senha =$_POST['senha'];

        // Abre/Cria arquivo (usuarios.txt) para guardar os dados
        $arquivo = fopen('usuarios.txt', 'a');

        // Cria uma linha com nome e senha separados por ;
        $linha = $nome . ';'. $senha . "\n";

        // Escrever a linha no arquivo
        fwrite($arquivo, $linha);

        // Fechar o arquivo
        fclose($arquivo);

        // Mensagem
        echo "<p>Usuário cadastrado com sucesso!</p>";

    }
    
    ?>
</body>
</html> 
