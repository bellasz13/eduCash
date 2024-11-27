import flet as ft

def Capitulo6Page(page: ft.Page):
    def voltar_para_anterior(_):
        print("Voltando para a página anterior...")
        page.go("/continuar")

    def abrir_subcapitulo(subcapitulo):
        print(f"Abrindo o subcapítulo {subcapitulo}...")

    cabecalho = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    icon_color="#0C0473",
                    icon_size=24,
                    on_click=voltar_para_anterior,
                ),
                ft.Text(
                    "EduCash",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#0C0473",
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=20, vertical=10),
        bgcolor="#F5E4B4",
        height=60, 
    )

    titulo_capitulo = ft.Text(
        "Capítulo 1: Fundamentos e Mentalidade",
        size=18,
        weight=ft.FontWeight.BOLD,
        color="white",
        text_align=ft.TextAlign.CENTER,
    )

    subcapitulos = [
        "Imóveis como investimento: vantagens e desvantagens",
        "Financiamento imobiliário: como funciona?",
        "Planejamento sucessório: protegendo seu patrimônio",
        "Seguro de vida e outros seguros importantes",
        "Aluguel x compra de imóvel: qual a melhor opção?",
        "Quiz",
        "Desafio ",
    ]

    subcapitulo_index = 0

    subcapitulo_display = ft.Container(
        width=200,
        height=200,
        bgcolor="#F5E4B4",
        border_radius=10,
        padding=ft.padding.all(10),
        alignment=ft.alignment.center,
        on_click=lambda _: abrir_subcapitulo(subcapitulos[subcapitulo_index]),
    )

    def atualizar_subcapitulo():
        subcapitulo_display.content = ft.Column(
            [
                ft.Text(
                    str(subcapitulo_index + 1),
                    size=32,
                    weight=ft.FontWeight.BOLD,
                    color="#0C0473",
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Text(
                    subcapitulos[subcapitulo_index],
                    size=16,
                    weight=ft.FontWeight.W_900,
                    color="#0C0473",
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        page.update()

    def proximo_subcapitulo(_):
        nonlocal subcapitulo_index
        if subcapitulo_index < len(subcapitulos) - 1:
            subcapitulo_index += 1
            atualizar_subcapitulo()

    def subcapitulo_anterior(_):
        nonlocal subcapitulo_index
        if subcapitulo_index > 0:
            subcapitulo_index -= 1
            atualizar_subcapitulo()

    navegacao = ft.Row(
        [
            ft.IconButton(
                icon=ft.icons.ARROW_BACK,
                icon_color="white",
                icon_size=28,
                on_click=subcapitulo_anterior,
            ),
            subcapitulo_display,
            ft.IconButton(
                icon=ft.icons.ARROW_FORWARD,
                icon_color="white",
                icon_size=28,
                on_click=proximo_subcapitulo,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    layout_central = ft.Column(
        [
            titulo_capitulo,
            ft.Container(height=40),  
            navegacao,
        ],
        alignment=ft.MainAxisAlignment.CENTER,  
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  
        expand=True,  
    )

    layout_principal = ft.Column(
        [
            cabecalho,  
            layout_central,  
        ],
        alignment=ft.MainAxisAlignment.START,  
        expand=True,
    )

    container_principal = ft.Container(
        content=layout_principal,
        bgcolor="#0C0473",
        expand=True,
    )

    atualizar_subcapitulo()

    page.controls.clear()
    page.add(container_principal)