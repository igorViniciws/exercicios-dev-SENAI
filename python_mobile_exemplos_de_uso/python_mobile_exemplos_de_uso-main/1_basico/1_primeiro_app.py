#   📱
import flet as ft

def main(page: ft.Page):
    # Função principal (Tela inicial)

    # Configurações básicas da página
    page.title = "Meu primeiro App Flet"
    page.padding = 20

    # Criando um texto (Primeiro elemento)
    meu_texto = ft.Text(
        value="🎉 Hello world! (Primeiro app com flet!)",
        size=24, #Tamanho da fonte
        color=ft.Colors.BLUE, #Cor da Fonte
        weight=ft.FontWeight.BOLD, #Negrito
        text_align=ft.TextAlign.CENTER #Alinhamento centralizado
    )

    # Adicionando o texto à página
    page.add(meu_texto)

# Inicia o aplicativo
ft.app(target=main)

