import flet as ft
import os

def main(page: ft.Page):
    page.title = "Calculadora de IMC"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.scroll = ft.ScrollMode.AUTO

    # --- Compatibilidade icons/colors (suporta ft.icons ou ft.Icons)
    ICONS = getattr(ft, "icons", None) or getattr(ft, "Icons", None)
    COLORS = getattr(ft, "colors", None) or getattr(ft, "Colors", None)
    if ICONS is None or COLORS is None:
        raise RuntimeError("Versão do flet não fornece 'icons' ou 'colors' (incompatível). Atualize o flet ou adapte manualmente.")

    def safe_icon(name, fallback=None):
        return getattr(ICONS, name, fallback)

    # --- helpers
    def parse_float_input(s: str):
        if s is None:
            raise ValueError("valor vazio")
        s = s.strip().replace(",", ".")
        if s == "":
            raise ValueError("valor vazio")
        return float(s)

    # UI placeholders (definidos abaixo)
    app_bar_title = ft.Text("Calculadora de IMC", size=22, weight=ft.FontWeight.W_500)
    title_text = ft.Text("Informe seus dados", size=20, weight=ft.FontWeight.W_500, text_align=ft.TextAlign.CENTER)
    result_text = ft.Text("", size=18, weight=ft.FontWeight.W_500, text_align=ft.TextAlign.CENTER)

    # Inputs
    weight_input = ft.TextField(
        label="Peso (kg)",
        prefix_icon=safe_icon("FITNESS_CENTER"),
        keyboard_type=ft.KeyboardType.NUMBER,
        width=300,
        border=ft.InputBorder.UNDERLINE,
    )

    height_input = ft.TextField(
        label="Altura (m) — ex: 1.80 (ou 180)",
        prefix_icon=safe_icon("STRAIGHTEN", safe_icon("HEIGHT")),
        keyboard_type=ft.KeyboardType.NUMBER,
        width=300,
        border=ft.InputBorder.UNDERLINE,
    )

    # Função de cálculo IMC
    def calculate_imc(e):
        try:
            w = parse_float_input(weight_input.value)
            h = parse_float_input(height_input.value)
            # se digitar em cm (ex: 180), converte para metros
            if h > 3:
                h = h / 100.0
            if h <= 0 or w <= 0:
                result_text.value = "Por favor, insira valores válidos (>0)."
            else:
                imc = w / (h * h)
                # intervalos corretos
                if imc < 18.5:
                    category = "Abaixo do peso"
                elif imc <= 24.9:
                    category = "Peso normal"
                elif imc <= 29.9:
                    category = "Sobrepeso"
                else:
                    category = "Obesidade"
                result_text.value = f"IMC: {imc:.2f}\nCategoria: {category}"
        except Exception:
            result_text.value = "Por favor, insira números válidos (use ponto ou vírgula)."
        page.update()

    def clear_fields(e):
        weight_input.value = ""
        height_input.value = ""
        result_text.value = ""
        page.update()

    # container principal (guardamos a referência pra alterar bgcolor)
    main_container = ft.Container(
        padding=ft.padding.symmetric(horizontal=24, vertical=10),
    )

    # Atualiza cores conforme tema
    def update_colors():
        is_dark = page.theme_mode == ft.ThemeMode.DARK
        app_bar_title.color = COLORS.WHITE if is_dark else COLORS.BLACK
        title_text.color = COLORS.WHITE if is_dark else COLORS.BLACK
        result_text.color = COLORS.WHITE if is_dark else COLORS.BLACK

        # fundo do container
        main_container.bgcolor = COLORS.BLACK if is_dark else (COLORS.WHITE if hasattr(COLORS, "WHITE") else None)

        # inputs: alguns temas não mudam background automaticamente, mas podemos deixar legível
        # não mexemos em todas propriedades (evita incompatibilidade entre versões)
        page.update()

    # alterna tema e aplica cores
    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        # ícone do botão (LIGHT_MODE quando está dark para indicar o que vai acontecer)
        theme_icon.icon = safe_icon("LIGHT_MODE") if page.theme_mode == ft.ThemeMode.DARK else safe_icon("DARK_MODE")
        update_colors()
        page.update()

    # botão tema
    theme_icon = ft.IconButton(
        icon=safe_icon("DARK_MODE"),
        tooltip="Alternar tema",
        on_click=toggle_theme,
    )

    # appbar
    page.appbar = ft.AppBar(title=app_bar_title, bgcolor=(COLORS.TRANSPARENT if hasattr(COLORS, "TRANSPARENT") else None), actions=[theme_icon])

    # botões (estilo simples e compatível)
    calc_btn = ft.ElevatedButton(
        "Calcular IMC",
        on_click=calculate_imc,
        style=ft.ButtonStyle(
            bgcolor="#673AB7",
            color=COLORS.WHITE if hasattr(COLORS, "WHITE") else None,
            shape=ft.RoundedRectangleBorder(radius=25),
        )
    )

    clear_btn = ft.ElevatedButton(
        "Limpar",
        on_click=clear_fields,
        style=ft.ButtonStyle(
            bgcolor="#FF5252",
            color=COLORS.WHITE if hasattr(COLORS, "WHITE") else None,
            shape=ft.RoundedRectangleBorder(radius=25),
        )
    )

    # monta conteúdo dentro do container
    main_container.content = ft.Column(
        controls=[
            title_text,
            ft.Container(height=10),
            weight_input,
            ft.Container(height=10),
            height_input,
            ft.Container(height=10),
            result_text,
            ft.Container(height=10),
            ft.Row(controls=[calc_btn, clear_btn], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
            ft.Container(height=10),
            ft.Image(src="Senai.png", height=50, fit=ft.ImageFit.CONTAIN) if os.path.exists("Senai.png") else ft.Text("Imagem Senai.png não encontrada"),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=12,
    )

    # adiciona container à página
    page.add(main_container)

    # aplica cores iniciais
    update_colors()

ft.app(target=main)
