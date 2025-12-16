<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Upload de Imagem</title>
</head>
<body>
    <form method="post" action="" enctype="multipart/form-data">
        <label for="imagem">Selecione uma imagem:</label>
        <input type="file" name="imagem" accept="image/*" required><br>

        <button type="submit">Upload</button>
    </form>

    <?php
        // Verifica se o formulário foi enviado
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            // Caminho onde as imagens serão salvas
            $diretorio_destino = 'uploads/';
        }

            // Se o caminho (diretório) não existir
            if(!is_dir($diretorio_destino)) {
                
                // Criar a pasta (Diretório) com permissões
                // de acesso total (codigo 0777) e possibilidade
                // de subdiretórios (opção true)
                mkdir($diretorio_destino, 0777, true);
            }

                // Armazena apenas o nome base do arquivo (Ex. foto.jpg)
                $nome_arquivo = basename($_FILES['imagem']['name']);

                // Constroi o caminho completo (Ex. uploads/foto.jpg)
                $caminho_completo = $diretorio_destino . $nome_arquivo;
 



        // Move o arquivo enviado para o diretório de destino
        if (move_uploaded_file($_FILES['imagem']['tmp_name'], $caminho_completo)) {
            echo "<p>Upload realizado com sucesso!</p>";
            echo "<img src='$caminho_completo' alt='Imagem enviada' style='max-width: 300px;'>";
        } else {
            echo "<p>Erro ao fazer upload do arquivo.</p>";
        }
    
    ?>
</body>
</html>
