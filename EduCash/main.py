import flet as ft
from login import LoginPage
from cadastro import CadastroPage

def MainPage(page: ft.Page):
    def navigate_to_login(_):
        page.route = "/login" 
        page.update()
        
    def navigate_to_cadastro(_):
        page.route = "/cadastro" 
        page.update()

    porco_imagem = ft.Image(
        src="https://i.ibb.co/FV4k1tr/icone-educash.png",  
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN
    )

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
    
    botao_login = ft.ElevatedButton(
        text="Login",
        color="white",
        bgcolor="#886D9C",
        width=200,
        on_click=navigate_to_login  
    )
    
    botao_cadastro = ft.ElevatedButton(
        text="Cadastro",
        color="#886D9C",
        bgcolor="#F5E4B4",
        width=200,
        on_click=navigate_to_cadastro  
    )
    
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
    
    page.controls.clear() 
    page.add(pagina_principal)

import flet as ft
from login import LoginPage
from cadastro import CadastroPage
from inicial import InicialPage
from continuar import ContinuarPage
from novo import NovoPage
from perfil import PerfilPage
from editar import EditarPage

def MainPage(page: ft.Page):
    def navigate_to_login(_):
        page.route = "/login" 
        page.update()
        
    def navigate_to_cadastro(_):
        page.route = "/cadastro"  
        page.update()

    porco_imagem = ft.Image(
        src="https://i.ibb.co/FV4k1tr/icone-educash.png",  
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN
    )
    
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
    
    botao_login = ft.ElevatedButton(
        text="Login",
        color="white",
        bgcolor="#886D9C",
        width=200,
        on_click=navigate_to_login  
    )
    
    botao_cadastro = ft.ElevatedButton(
        text="Cadastro",
        color="#886D9C",
        bgcolor="#F5E4B4",
        width=200,
        on_click=navigate_to_cadastro 
    )
    
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
    
    page.controls.clear() 
    page.add(pagina_principal)

def main(page: ft.Page):
    page.title = "EduCash"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "#0C0473"

    def route_change(route):
        if page.route == "/login":
            LoginPage(page)
        elif page.route == "/cadastro":
            CadastroPage(page)
        elif page.route == "/inicial":
            InicialPage(page)
        elif page.route == "/continuar":
            ContinuarPage(page)
        elif page.route == "/novo":
            NovoPage(page)
        elif page.route == "/perfil":
            PerfilPage(page)
        elif page.route == "/editar":
            EditarPage(page)
        else:
            MainPage(page)

    page.on_route_change = route_change
    page.go("/")  

ft.app(target=main)