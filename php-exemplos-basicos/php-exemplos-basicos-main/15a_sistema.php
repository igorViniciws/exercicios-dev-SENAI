<?php
// Página de login (15a_sistema.php)
session_start();

// Verifica se o formulário foi enviado
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $usuario = $_POST['usuario'];
    $senha = $_POST['senha'];

    // Compara os dados (Verifica se são válidos)
    if ($usuario =='Max Verstappen' && $senha == '123') {

        // Se sim (Salva o nome do usuario)
        $_SESSION['usuario'] = $usuario;


        // Redireciona para a pagina (Restrita)
        header("location: 15b_restrita.php");
        exit();

    } else {

        // Senão (Informa o usuario do problema)
        $erro = "Usuário ou senha incorretos!";
    }

}


?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <form method="post" action="">
        <label for="usuario">Usuário:</label>
        <input type="text" name="usuario" required><br>

        <label for="senha">Senha:</label>
        <input type="password" name="senha" required><br>

        <button type="submit">Entrar</button>
    </form>

    <?php
    if (isset($erro)) {
        echo "<p style='color: red;'>$erro</p>";
    }
    ?>
</body>
</html>
