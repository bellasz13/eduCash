import flet as ft

def InicialPage(page: ft.Page):
    def continuar_jogo(_):
        print("Continuar jogo clicado!")
        page.snack_bar = ft.SnackBar(content=ft.Text("Continuando jogo..."))
        page.snack_bar.open()

    def novo_jogo(_):
        print("Novo jogo clicado!")
        page.snack_bar = ft.SnackBar(content=ft.Text("Novo jogo iniciado!"))
        page.snack_bar.open()

    cabecalho = ft.Container(
        content=ft.Row(
            [
                ft.Text(
                    "EduCash",
                    size=24,
                    weight=ft.FontWeight.BOLD,
                    color="#0C0473",
                ),
                ft.Icon(ft.icons.ACCOUNT_CIRCLE, color="#0C0473", size=30),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=20, vertical=10),
        bgcolor="#F5E4B4",
        height=60,
        expand=False,
    )

    botao_continuar = ft.ElevatedButton(
        text="Continuar",
        color="white",
        bgcolor="#886D9C",
        width=200,
        icon=ft.icons.PLAY_ARROW,
        on_click=continuar_jogo,
    )

    botao_novo_jogo = ft.ElevatedButton(
        text="Novo Jogo",
        color="#886D9C",
        bgcolor="#F5E4B4",
        width=200,
        icon=ft.icons.ADD_CIRCLE_OUTLINE,
        on_click=novo_jogo,
    )

    conteudo_central = ft.Container(
        content=ft.Column(
            [botao_continuar, botao_novo_jogo],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        ),
        alignment=ft.alignment.center,
        expand=True,
    )

    layout_completo = ft.Column(
        [
            cabecalho,
            ft.Stack(
                [
                    ft.Container(
                        expand=True,
                        image_src="https://i.ibb.co/LCP6mzw", 
                        image_fit=ft.ImageFit.COVER,
                    ),
                    conteudo_central,
                ]
            ),
        ],
        spacing=0,
        expand=True,
    )

    page.controls.clear()
    page.add(layout_completo)
