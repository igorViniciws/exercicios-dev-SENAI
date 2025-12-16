import flet as ft

def main(page: ft.Page):
    page.title = "Contador completo"
    # Definindo padding individualmente
    page.padding=ft.padding.only(top=40, left=20, right=20, bottom=20)

    # Zerando contagem ao abrir
    valor_contador = 0

    # Elementos da interface
    display_contador = ft.Text(
        value="0",
        size=48,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE,
        text_align=ft.TextAlign.CENTER
    )

    info_contador = ft.Text(
        value="Contador iniciado em 0",
        size=14,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.GREY_600,
        text_align=ft.TextAlign.CENTER
    )

    # Atualiza display e cor baseado no valor
    def atualizar_display():
        display_contador.value = str(valor_contador)

        # Se valor positivo
        if valor_contador > 0:
            display_contador.color = ft.Colors.GREEN
            info_contador.value ="Valor positivo"
        
        # Se valor negativo
        elif valor_contador < 0:
            display_contador.color = ft.Colors.RED
            info_contador.value ="Valor negativo"

        # Se valor zerado
        else:
            display_contador.color = ft.Colors.BLUE
            info_contador.value ="Contador zerado"

        # Atualiza a página pois houve uma mudança de valor
        page.update()

    # Função para incrementar o valor
    # "nonlocal" ->Diz ao Python que (valor_contador) não
    # é uma variável desta função e sim uma variável externa
    # definida na função main
    def incrementar(e):
        nonlocal valor_contador
        valor_contador += 1
        # Outra possibilidade
        # valor_contador = valor_contador + 1
        atualizar_display()

    # Função para decrementar o valor
    def decrementar(e):
        nonlocal valor_contador
        valor_contador -= 1
        atualizar_display()

    # Reset
    def resetar(e):
        nonlocal valor_contador
        valor_contador = 0
        atualizar_display()

    # Botões + Montagem da página principal
    page.add(
        ft.Column(
            controls=[
                ft.Text("🔢 Contador Completo", size=24, weight=ft.FontWeight.BOLD),
                display_contador,
                info_contador,
                ft.Row(
                    controls=[

                        # ft.ElevatedButton("➖", on_click=decrementar, width=60, height=60, bgcolor=ft.Colors.RED_400, color=ft.Colors.WHITE),
                        # ft.ElevatedButton("➕", on_click=incrementar, width=60, height=60, bgcolor=ft.Colors.GREEN_400, color=ft.Colors.WHITE)

                        # Versão botões quadrados
                        ft.ElevatedButton(
                            "➖",
                            on_click=decrementar,
                            width=60,
                            height=60,
                            bgcolor=ft.Colors.RED_400,
                            color=ft.Colors.WHITE,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=0)
                            )
                        ),
                        ft.ElevatedButton(
                            "➕",
                            on_click=incrementar,
                            width=60,
                            height=60,
                            bgcolor=ft.Colors.GREEN_400,
                            color=ft.Colors.WHITE,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=0)
                            )
                        )


                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=40
                ),
                ft.ElevatedButton("🔄 Reset", on_click=resetar, width=120, bgcolor=ft.Colors.BLUE_400, color=ft.Colors.WHITE),

            ],
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            spacing=20

        )
    )

ft.app(target=main)


    

        
