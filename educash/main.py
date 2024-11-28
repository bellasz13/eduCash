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
from capitulo1 import Capitulo1Page
from capitulo1_1 import Capitulo1_1Page
from capitulo1_2 import Capitulo1_2Page
from capitulo1_3 import Capitulo1_3Page
from capitulo1_4 import Capitulo1_4Page
from capitulo1_5 import Capitulo1_5Page
from capitulo2 import Capitulo2Page
from capitulo3 import Capitulo3Page
from capitulo4 import Capitulo4Page
from capitulo5 import Capitulo5Page
from capitulo6 import Capitulo6Page
from capitulo7 import Capitulo7Page
from capitulo8 import Capitulo8Page
from capitulo9 import Capitulo9Page
from capitulo10 import Capitulo10Page
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
    
    usuario_logado = None

    def route_change(route):
        
        nonlocal usuario_logado
        
        if page.route == "/login":
            def on_login_success(usuario):
                nonlocal usuario_logado
                usuario_logado = usuario
                print("Login bem-sucedido! Usuário:", usuario)
                page.go("/inicial")
            
            LoginPage(page, on_login_success=on_login_success)
            
        elif page.route == "/cadastro":
            CadastroPage(page)
        elif page.route == "/inicial":
            if usuario_logado:
                InicialPage(page)
            else:
                page.go("/login")
        elif page.route == "/continuar":
            ContinuarPage(page)
        elif page.route == "/novo":
            NovoPage(page)
        elif page.route == "/capitulo1":
            Capitulo1Page(page)
        elif page.route == "/capitulo1_1":
            Capitulo1_1Page(page)
        elif page.route == "/capitulo2":
            Capitulo2Page(page)
        elif page.route == "/capitulo3":
            Capitulo3Page(page)
        elif page.route == "/capitulo4":
            Capitulo4Page(page)
        elif page.route == "/capitulo5":
            Capitulo5Page(page)
        elif page.route == "/capitulo6":
            Capitulo6Page(page)
        elif page.route == "/capitulo7":
            Capitulo7Page(page)
        elif page.route == "/capitulo8":
            Capitulo8Page(page)
        elif page.route == "/capitulo9":
            Capitulo9Page(page)
        elif page.route == "/capitulo10":
            Capitulo10Page(page)
        elif page.route == "/perfil":
            if usuario_logado:
                PerfilPage(page, id=usuario_logado['id'])
            else:
                page.go("/login")
        elif page.route == "/editar":
            if usuario_logado:
                EditarPage(page, id=usuario_logado['id'])
            else:
                page.go("/login")
        else:
            MainPage(page)

    page.on_route_change = route_change
    page.go("/")  

ft.app(target=main)