import flet as ft

def NovoPage(page: ft.Page):
    def voltar_para_inicial(_):
        print("Voltando para a tela inicial...")
        page.go("/inicial")
        
    def ir_continuar(_):
        print("Indo para a tela continuar...")
        page.go("/continuar")

    cabecalho = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    icon_size=30,
                    icon_color="#0C0473",
                    on_click=voltar_para_inicial,
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
        expand=False,
    )

    texto_balao = ft.Text(
        "Olá! Espero que esteja preparado para nossa jornada de muito aprendizado!\n\n"
        "Nosso jogo funcionará da seguinte forma: na página a seguir, você verá a tela inicial do jogo, "
        "onde você iniciará o seu aprendizado a partir do capítulo 1 e ao completar um capítulo "
        "você irá realizar um quiz e, por fim, os desafios extras!",
        size=14,
        color="#0C0473",
        text_align=ft.TextAlign.JUSTIFY,
        selectable=False,
    )

    balao_fala = ft.Container(
        content=texto_balao,
        padding=ft.padding.all(20),
        width=300,
        bgcolor="#F5E4B4",
        border_radius=20,
        border=ft.border.all(2, color="#0C0473"),
    )

    personagem = ft.Image(
        src="https://i.postimg.cc/1XNh9dd8/personagem.png",  
        width=200,
        height=200,
        fit=ft.ImageFit.CONTAIN,
    )

    botao_avancar = ft.ElevatedButton(
        text="Avançar",
        icon=ft.icons.ARROW_FORWARD,
        icon_color="white",
        bgcolor="#886D9C",
        color="white",
        on_click=ir_continuar,
    )

    layout_inferior = ft.Column(
        [
            ft.Row(
                [
                    ft.Container(
                        content=personagem,
                        alignment=ft.alignment.center,
                    ),
                    balao_fala,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            ft.Container(
                content=botao_avancar,
                alignment=ft.alignment.center,
                margin=ft.margin.only(top=20),
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
    )

    layout_completo = ft.Column(
        [
            cabecalho,
            ft.Container(
                content=layout_inferior,
                bgcolor="#0C0473",
                expand=True,
                padding=ft.padding.all(20),
            ),
        ],
        spacing=0,
        expand=True,
    )

    page.controls.clear()
    page.add(layout_completo)
    