import flet as ft
from database import verificar_usuario

def LoginPage(page: ft.Page):
    def autenticar_usuario(_):
        usuario = campo_user.value
        senha = campo_senha.value

        if usuario and senha:
            try:
                if verificar_usuario(usuario, senha):
                    ft.SnackBar(
                        text="Login realizado com sucesso!", 
                        open=True
                    ).open = True
                    page.go("/inicial")  
                else:
                    ft.SnackBar(
                        text="Usuário ou senha incorretos!", 
                        open=True
                    ).open = True
            except Exception as e:
                ft.SnackBar(
                    text=f"Erro ao autenticar: {e}", 
                    open=True
                ).open = True
        else:
            ft.SnackBar(
                content="Preencha todos os campos!",
                open=True
            ).open = True


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
        "Seja bem-vindo(a) de volta à sua jornada financeira!\n\n" 
        "Pronto para mais aprendizados e conquistas?",
        size=15,
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

    campo_senha = ft.TextField(
        label="Senha",
        width=250,
        bgcolor="white",
        border_color="#886D9C",
        color="#0C0473",
        password=True,
    )

    botao_entrar = ft.ElevatedButton(
        text="Entrar",
        color="white",
        bgcolor="#886D9C",
        width=200,
        on_click=autenticar_usuario,
    )

    botao_voltar = ft.IconButton(
        icon=ft.icons.ARROW_BACK,
        icon_size=30,
        icon_color="white",
        on_click=voltar_ao_main,
    )

    layout_login = ft.Column(
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
            campo_senha,
            botao_entrar,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
    )

    layout_completo = ft.Container(
        content=layout_login,
        bgcolor="#0C0473",  
        expand=True,
        padding=ft.padding.symmetric(horizontal=20, vertical=40),
    )

    page.controls.clear()
    page.add(layout_completo)
