import flet as ft 

def main(pagina: ft.Page):
    pagina.title = "EduCash"
    pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    pagina.bgcolor = "#0C0473"

    #ir login
    def go_to_login(e):
        pagina.views.append(create_login_view())
        pagina.update()

    #ir tela de cadastro
    def go_to_signup(e):
        pagina.views.append(create_signup_view())
        pagina.update()

    #voltar tela anterior
    def go_back(e):
        if len(pagina.views) > 1:
            pagina.views.pop()
            pagina.update()

    #tela inicial
    def create_home_view():
        return ft.View(
            controls=[
                ft.Column(
                    [
                        ft.Image(
                            src="https://i.ibb.co/FV4k1tr/icone-educash.png",  
                            width=100,
                            height=100,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Text("Bem-vindo(a) ao EduCash", size=20, weight=ft.FontWeight.BOLD, color="white"),
                        ft.Text(
                            "Se deseja aprimorar sua vida financeira, faça login ou crie uma conta:",
                            size=14, color="white", text_align=ft.TextAlign.CENTER
                        ),
                        ft.ElevatedButton(text="Login", color="white", bgcolor="#886D9C", width=200, on_click=go_to_login),
                        ft.ElevatedButton(text="Criar conta", color="#886D9C", bgcolor="#F5E4B4", width=200, on_click=go_to_signup),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                )
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            vertical_alignment=ft.MainAxisAlignment.CENTER
        )

    #tela login
    def create_login_view():
        return ft.View(
            controls=[
                ft.Column(
                    [
                        ft.Row([ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=go_back)], alignment=ft.MainAxisAlignment.START),
                        ft.Image(
                            src="https://i.ibb.co/FV4k1tr/icone-educash.png", 
                            width=100,
                            height=100,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Text(
                            "Seja bem-vindo(a) de volta à sua jornada financeira!",
                            size=16, weight=ft.FontWeight.BOLD, color="white"
                        ),
                        ft.Text("Pronto para mais aprendizados e conquistas?", size=14, color="white", text_align=ft.TextAlign.CENTER),
                        ft.TextField(label="Email", hint_text="email@email.com", prefix_icon=ft.icons.EMAIL, width=250),
                        ft.TextField(label="Senha", hint_text="senha", prefix_icon=ft.icons.LOCK, password=True, width=250),
                        ft.TextButton("Esqueceu a senha?", on_click=lambda e: print("Redefinir senha")),
                        ft.ElevatedButton(text="Entrar", color="white", bgcolor="#7A5C91", width=200, on_click=lambda e: print("Entrar clicked")),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                )
            ]
        )

    #tela cadastro
    def create_signup_view():
        return ft.View(
            controls=[
                ft.Column(
                    [
                        ft.Row([ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=go_back)], alignment=ft.MainAxisAlignment.START),
                        ft.Image(
                            src="https://i.ibb.co/FV4k1tr/icone-educash.png", 
                            width=100,
                            height=100,
                            fit=ft.ImageFit.CONTAIN
                        ),
                        ft.Text("Que ótimo ter você conosco!", size=16, weight=ft.FontWeight.BOLD, color="white"),
                        ft.Text("Pronto para iniciar sua jornada?", size=14, color="white", text_align=ft.TextAlign.CENTER),
                        ft.TextField(label="Usuário", hint_text="user", prefix_icon=ft.icons.PERSON, width=250),
                        ft.TextField(label="Email", hint_text="email@email.com", prefix_icon=ft.icons.EMAIL, width=250),
                        ft.TextField(label="Senha", hint_text="senha", prefix_icon=ft.icons.LOCK, password=True, width=250),
                        ft.ElevatedButton(text="Criar", color="white", bgcolor="#7A5C91", width=200, on_click=lambda e: print("Criar conta clicked")),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                )
            ]
        )

    # carrega
    pagina.views.append(create_home_view())
    pagina.update()
    

#executa o appp
ft.app(target=main)