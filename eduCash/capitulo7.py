import flet as ft

def Capitulo7Page(page: ft.Page):
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
        ),
        height=60,
        bgcolor="#F5E4B4",
        padding=ft.padding.symmetric(horizontal=15),
    )

    titulo_capitulo = ft.Text("Capítulo 7: Impostos e Planejamento Tributário",
        size=18,
        weight=ft.FontWeight.BOLD,
        color="white",
        text_align=ft.TextAlign.CENTER,
    )

    subcapitulos = [
        "Imposto de Renda Pessoa Física (IRPF): Como declarar seus rendimentos e deduções, prazos e penalidades",
        "Impostos sobre a propriedade: IPTU, IPVA e outros impostos relacionados a bens imóveis e veículos",
        "Planejamento tributário: Estratégias legais para reduzir a carga tributária.",
        "Impostos sobre heranças e doações: Como funcionam e como se planejar para minimizá-los",
        "Incentivos fiscais: Programas governamentais que oferecem benefícios fiscais para determinadas atividades",
        "Quiz",
        "Desafio",
    ]

    caixas = []
    for i, subcapitulo in enumerate(subcapitulos, start=1):
        caixa = ft.ElevatedButton(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            str(i),
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color="#0C0473",
                        ),
                        ft.Text(
                            subcapitulo,
                            size=14,
                            color="#0C0473",
                            text_align=ft.TextAlign.CENTER,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                width=200,
                height=200,
                bgcolor="#F5E4B4",
                border_radius=10,
                padding=ft.padding.all(10),
            ),
            on_click=lambda e, s=i: abrir_subcapitulo(s),
        )
        caixas.append(caixa)

    lista_subcapitulos = ft.Row(
        caixas,
        alignment=ft.MainAxisAlignment.START,
        spacing=10,
        scroll=ft.ScrollMode.ALWAYS,  
    )

    layout = ft.Column(
        [
            cabecalho,
            ft.Container(height=20),  
            titulo_capitulo,
            ft.Container(height=20),  
            lista_subcapitulos,
        ],
        alignment=ft.MainAxisAlignment.START,
        spacing=15,
        expand=True,
    )

    container_principal = ft.Container(
        content=layout,
        bgcolor="#0C0473",
        expand=True,
        padding=ft.padding.all(20),
    )

    page.controls.clear()
    page.add(container_principal)