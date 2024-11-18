import flet as ft

def CadastroPage(page: ft.Page):
    def back_to_home(_):
        page.route = "/"  # Volta para a tela inicial
        page.update()

# Imagem do porquinho
    porco_imagem = ft.Image(
        src="https://i.ibb.co/FV4k1tr/icone-educash.png",  
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN
    )
    
    # Título e subtítulo
    bem_vindo = ft.Text(
        "Que ótimo ter você conosco!",
        size=18,
        weight=ft.FontWeight.BOLD,
        color="white",
        text_align=ft.TextAlign.CENTER
    )
    instrucao = ft.Text(
        "Pronto para iniciar sua jornada financeira?",
        size=14,
        color="white",
        text_align=ft.TextAlign.CENTER
    )
    
    # campo de user
    campo_user = ft.TextField(
        hint_text="user",
        width=250,
        bgcolor="white",
        border_color="#886D9C"
    )
    
    # Campo de e-mail
    campo_email = ft.TextField(
        hint_text="email@email.com",
        width=250,
        bgcolor="white",
        border_color="#886D9C"
    )
    
    # Campo de senha
    campo_senha = ft.TextField(
        hint_text="senha",
        width=250,
        bgcolor="white",
        border_color="#886D9C",
        password=True
    )
    
    # Botão de criar
    botao_criar = ft.ElevatedButton(
        text="Criar",
        color="white",
        bgcolor="#886D9C",
        width=200,
        on_click=lambda _: print("Criar clicado!")
    )
    
    # Botão de voltar
    botao_voltar = ft.TextButton(
        text="Voltar",
        on_click=back_to_home,
        style=ft.ButtonStyle(color="white")
    )
    
    # Layout da página de login
    pagina_login = ft.Column(
        [
            botao_voltar,
            porco_imagem,
            bem_vindo,
            instrucao,
            campo_user,
            campo_email,
            campo_senha,
            botao_criar,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )
    
    # Adiciona o layout à página
    page.controls.clear()
    page.add(pagina_login)
