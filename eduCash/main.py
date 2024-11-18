import flet as ft
from login import LoginPage
from cadastro import CadastroPage

def MainPage(page: ft.Page):
    def navigate_to_login(_):
        page.route = "/login"  # Define a rota para a tela de login
        page.update()
        
    def navigate_to_cadastro(_):
        page.route = "/cadastro"  # Define a rota para a tela de cadastro
        page.update()

    # Imagem do porquinho
    porco_imagem = ft.Image(
        src="https://i.ibb.co/FV4k1tr/icone-educash.png",  
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN
    )
    
    # Título e instruções
    bem_vindo = ft.Text(
        "Bem-vindo(a) ao EduCash",
        size=20,
        weight=ft.FontWeight.BOLD,
        color="white"
    )
    instrucao = ft.Text(
        "Se deseja aprimorar sua vida financeira, faça login ou crie uma conta:",
        size=14,
        color="white",
        text_align=ft.TextAlign.CENTER
    )
    
    # Botão de login
    botao_login = ft.ElevatedButton(
        text="Login",
        color="white",
        bgcolor="#886D9C",
        width=200,
        on_click=navigate_to_login  # Navega para a tela de login
    )
    
# Botão de cadastro
    botao_cadastro = ft.ElevatedButton(
        text="Cadastro",
        color="#886D9C",
        bgcolor="#F5E4B4",
        width=200,
        on_click=navigate_to_cadastro  # Navega para a tela de login
    )
    
    # Layout da página inicial
    pagina_principal = ft.Column(
        [
            porco_imagem,
            bem_vindo,
            instrucao,
            botao_login,
            botao_cadastro
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=10
    )
    
    # Adiciona o layout à página
    page.controls.clear()  # Limpa os controles atuais
    page.add(pagina_principal)

# Função principal que configura as rotas
def main(page: ft.Page):
    page.title = "EduCash"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#0C0473"

    # Configura as rotas
    def route_change(route):
        if page.route == "/":
            MainPage(page)  # Tela inicial
        elif page.route == "/login":
            LoginPage(page)  # Tela de login
        elif page.route == "/cadastro":
            CadastroPage(page)  # Tela de cadastro
        page.update()

    # Adiciona a escuta de rotas
    page.on_route_change = route_change
    page.go("/")  # Define a rota inicial

ft.app(target=main)
