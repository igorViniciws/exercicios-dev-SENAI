<?php
// Página de logout (15c_logout.php)


session_start();

// Finaliza a sessão
session_destroy();

// Redireciona forçando um novo login
header("Location: 15a_sistema.php")


?>
