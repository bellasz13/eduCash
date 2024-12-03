import flet as ft

def SuportePage(page: ft.Page):

    def voltar_para_anterior(_):
        page.go("/perfil")
    
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
                    "Suporte",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#0C0473",  
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        height=60,
        bgcolor="#F5E4B4",
        padding=ft.padding.symmetric(horizontal=15),
    )

    def criar_bloco(titulo, texto):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        titulo,
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color="#0C0473",  
                    ),
                    ft.Text(
                        texto,
                        size=14,
                        color="#0C0473",  
                    ),
                ],
                spacing=10,
            ),
            bgcolor="#F5E4B4",  
            border_radius=ft.border_radius.all(8),
            padding=15,
            margin=ft.margin.symmetric(vertical=10, horizontal=10),
        )

    blocos_informacoes = [
        criar_bloco(
            "Qual o objetivo do Educash?",
            "O objetivo principal do aplicativo de educação financeira EduCash é promover o aprendizado e a prática de habilidades financeiras essenciais para jovens e adultos. Isso incluiria ajudar os usuários a desenvolver hábitos saudáveis de gestão financeira, investir de forma consciente e alcançar seus objetivos financeiros de curto e longo prazo.",
        ),
        criar_bloco(
            "Como acessar os recursos?",
            "Você pode acessar os recursos diretamente no menu principal do aplicativo. Certifique-se de estar logado para ter acesso completo às funcionalidades personalizadas.",
        ),
        criar_bloco(
            "Preciso pagar pelo Educash?",
            "O Educash é gratuito para acesso a todos os conteúdos. Há opções premium para quem deseja explorar funcionalidades avançadas.",
        ),
        criar_bloco(
            "Dúvidas ou reclamações",
            "Em caso de mais dúvidas, reclamações ou sugestões, entre em contato com o nosso Suporte: suporte.educash@gmail.com",
        ),
    ]

    conteudo = ft.Column(
        blocos_informacoes,
        scroll=ft.ScrollMode.AUTO,
    )

    layout = ft.Column(
        [
            cabecalho, 
            ft.Container(content=conteudo, expand=True),  
        ],
        expand=True,
    )

    container_principal = ft.Container(
        content=layout,
        expand=True,
        bgcolor="#0C0473", 
    )

    page.controls.clear()
    page.add(container_principal)
