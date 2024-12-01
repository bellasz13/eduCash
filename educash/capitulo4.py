import flet as ft

def Capitulo4Page(page: ft.Page):
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
        "Capítulo 4: Poupança e Investimentos",
        size=18,
        weight=ft.FontWeight.BOLD,
        color="white",
        text_align=ft.TextAlign.CENTER,
    )

    subcapitulos = [
        "A importância de construir uma reserva de emergência",
        "Diferentes tipos de investimentos: qual o melhor para você?",
        "Entendendo os riscos e retornos dos investimentos",
        "Planejamento financeiro a longo prazo: aposentadoria e outros objetivo",
        "Impostos sobre investimentos: o que você precisa saber",
        "Quiz",
        "Desafio",
    ]

    def criar_bloco_conteudo(index, conteudo):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        f" {index + 1}",
                        size=24,
                        weight=ft.FontWeight.BOLD,
                        color="#0C0473",  # Cor do título
                    ),
                    ft.Text(
                        conteudo,
                        size=16,
                        weight=ft.FontWeight.NORMAL,
                        color="#0C0473",  # Cor do texto
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            width=200,
            height=200,
            bgcolor="#F5E4B4",  
            border_radius=10,
            padding=ft.padding.all(10),
            alignment=ft.alignment.center,
            on_click=lambda _: abrir_subcapitulo,
    )

    blocos_conteudo = ft.Column(
        [
            criar_bloco_conteudo(i, subcapitulos[i]) for i in range(len(subcapitulos))
        ],  
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    layout = ft.Column(
        [
            cabecalho,  
            titulo_capitulo,
            ft.Container(height=20),  
            blocos_conteudo,  
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )

    container_principal = ft.Container(
        content=ft.Column(
            [
                layout,
            ],
            scroll=ft.ScrollMode.AUTO,  
        ),
        bgcolor="#0C0473",
        expand=True,
        padding=ft.padding.all(20),
    )

    page.controls.clear()
    page.add(container_principal)
