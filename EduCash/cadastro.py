import flet as ft

def CadastroPage(page: ft.Page):
    def criar_usuario(_):
        print("Usuário cadastrado com sucesso!")
        page.go("/inicial")  
        
    def voltar_ao_main(_):
        page.go("/")  

    porco_imagem = ft.Image(
        src="https://i.ibb.co/FV4k1tr/icone-educash.png",  
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN,
    )

    titulo = ft.Text(
        "Cadastro",
        size=20,
        weight=ft.FontWeight.BOLD,
        color="white",
    )

    campo_user = ft.TextField(
        hint_text="Usuário",
        width=250,
        bgcolor="white",
        border_color="#886D9C",
    )

    campo_email = ft.TextField(
        hint_text="E-mail",
        width=250,
        bgcolor="white",
        border_color="#886D9C",
    )

    campo_senha = ft.TextField(
        hint_text="Senha",
        width=250,
        bgcolor="white",
        border_color="#886D9C",
        password=True,
    )

    botao_criar = ft.ElevatedButton(
        text="Criar",
        color="white",
        bgcolor="#886D9C",
        width=200,
        on_click=criar_usuario,
    )

    botao_voltar = ft.TextButton(
        text="Voltar",
        on_click=voltar_ao_main,
        style=ft.ButtonStyle(color="white"),
    )

    layout_cadastro = ft.Column(
        [
            botao_voltar,
            porco_imagem,
            titulo,
            campo_user,
            campo_email,
            campo_senha,
            botao_criar,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10,
    )

    page.controls.clear()
    page.add(layout_cadastro)