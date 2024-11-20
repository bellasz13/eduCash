import flet as ft

def CadastroPage(page: ft.Page):
    def criar_usuario(_):
        print("Usuário cadastrado com sucesso!")
        page.go("/inicial")  

    def voltar_ao_main(_):
        print("Voltando ao menu principal...")
        page.go("/")  

    porco_imagem = ft.Image(
        src="https://i.ibb.co/FV4k1tr/icone-educash.png",  
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    texto = ft.Text(
        "Que ótimo ter você conosco!\n\n" 
        "Pronto para iniciar sua jornada?",
        size=18,
        color="white",
        text_align=ft.TextAlign.CENTER
    )

    campo_user = ft.TextField(
        label="Usuário",
        width=250,
        bgcolor="white",
        border_color="#886D9C",
        color="#0C0473",
    )

    campo_email = ft.TextField(
        label="E-mail",
        width=250,
        bgcolor="white",
        border_color="#886D9C",
        color="#0C0473",
    )

    campo_senha = ft.TextField(
        label="Senha",
        width=250,
        bgcolor="white",
        border_color="#886D9C",
        color="#0C0473",
        password=True,
    )

    botao_criar = ft.ElevatedButton(
        text="Criar Conta",
        color="white",
        bgcolor="#886D9C",
        width=200,
        on_click=criar_usuario,
    )

    botao_voltar = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        icon_size=30,
        icon_color="white",
        on_click=voltar_ao_main,
    )

    layout_cadastro = ft.Column(
        [
            ft.Row(
                [
                    botao_voltar,
                ],
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            porco_imagem,
            texto,
            campo_user,
            campo_email,
            campo_senha,
            botao_criar,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
    )

    layout_completo = ft.Container(
        content=layout_cadastro,
        bgcolor="#0C0473",  
        expand=True,
        padding=ft.padding.symmetric(horizontal=20, vertical=40),
    )

    page.controls.clear()
    page.add(layout_completo)
