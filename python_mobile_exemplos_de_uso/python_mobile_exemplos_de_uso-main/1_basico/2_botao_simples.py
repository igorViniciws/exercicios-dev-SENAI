import flet as ft

def main(page: ft.Page):
    page.title="Meu primeiro botão"
    page.padding=20

    # Criando mensagem que será modificada pelo botão
    mensagem = ft.Text(
        value="Clique no botão abaixo! 👇",
        size=20,
        text_align=ft.TextAlign.CENTER
    )

    def botao_clicado(evento):
        # Função será executada ao se clicar no botão
        # Obs: Parâmetro 'evento' contém informações 
        # sobre o clique

        # Mudando a mensagem (texto)
        mensagem.value = "🎉 Parabéns Você clicou no botão!"
        mensagem.color =  ft.Colors.GREEN

        # Atualizar a página
        page.update()

    # Criando o botão
    meu_botao = ft.ElevatedButton(
        text="Clique em mim!", #Texto que aparece no botão
        on_click=botao_clicado, # Ao clicar executa a função 'botao_clicado'
        width=200, #Largura
        height=50, #Altura
        color=ft.Colors.WHITE, #Cor do texto
       # bgcolor=ft.Colors.BLUE Cor de fundo do botão
        bgcolor="#4caf50" #Cor de fundo do botão
    )

    # Adicionando os elementos à página
    page.add(mensagem)
    page.add(meu_botao)


ft.app(target=main)
