import flet as ft

def PerfilPage(page: ft.Page):
    
    def voltar_para_anterior(_):
        print("Voltando para a página anterior...")
        page.go("/inicial")  
        
    def editar_perfil(_):
        print("Editar perfil clicado!")
        page.go("/editar")

    def suporte(_):
        print("Suporte clicado!")

    def sair(_):
        print("Sair clicado!")
        page.go("/")  

    cabecalho = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    icon_color="white",
                    icon_size=24,
                    on_click=voltar_para_anterior,
                ),
                ft.Text(
                    "Meu perfil",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),
                ft.IconButton(
                    icon=ft.icons.NOTIFICATIONS,
                    icon_color="white",
                    icon_size=24,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        height=60,
        bgcolor="#0C0473",  
        padding=ft.padding.symmetric(horizontal=15),
    )

    icone_perfil = ft.Icon(
        name=ft.icons.ACCOUNT_CIRCLE,
        size=100,
        color="white",
    )
    nome_usuario = ft.Text(
        "Nome",
        size=18,
        color="white",
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    email_usuario = ft.Text(
        "email@email.com",
        size=14,
        color="white",
        text_align=ft.TextAlign.CENTER,
    )
    perfil_info = ft.Column(
        [
            icone_perfil,
            nome_usuario,
            email_usuario,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=5,
    )

    titulo_conquistas = ft.Text(
        "Conquistas",
        size=16,
        color="white",
        weight=ft.FontWeight.BOLD,
    )
    conquistas = ft.Row(
        [
            ft.Container(
                content=ft.Icon(ft.icons.EMOJI_EVENTS, size=50, color="#F5E4B4"),
                width=100,
                height=100,
                bgcolor="white",
                border_radius=ft.border_radius.all(10),
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=ft.Icon(ft.icons.STAR, size=50, color="#F5E4B4"),
                width=100,
                height=100,
                bgcolor="white",
                border_radius=ft.border_radius.all(10),
                alignment=ft.alignment.center,
            ),
            ft.Container(
                content=ft.Icon(ft.icons.LANDSCAPE, size=50, color="#F5E4B4"),
                width=100,
                height=100,
                bgcolor="white",
                border_radius=ft.border_radius.all(10),
                alignment=ft.alignment.center,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10,
    )
    conquistas_secao = ft.Column(
        [titulo_conquistas, conquistas],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    titulo_configuracao = ft.Text(
        "Configurações",
        size=16,
        color="white",
        weight=ft.FontWeight.BOLD,
    )

    botao_editar = ft.ElevatedButton(
        text="Editar Perfil",
        width=200,
        color="white",
        bgcolor="#886D9C",
        on_click=editar_perfil
    )
    botao_suporte = ft.ElevatedButton(
        text="Suporte",
        width=200,
        color="white",
        bgcolor="#886D9C",
        on_click=suporte,
    )
    botao_sair = ft.ElevatedButton(
        text="Sair",
        width=200,
        color="white",
        bgcolor="#FF5757",
        on_click=sair,
    )
    configuracoes_secao = ft.Column(
        [
            titulo_configuracao,
            botao_editar,
            botao_suporte,
            botao_sair,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    layout = ft.Column(
        [
            cabecalho,
            perfil_info,
            conquistas_secao,
            configuracoes_secao,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
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