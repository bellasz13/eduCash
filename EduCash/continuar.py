import flet as ft

def ContinuarPage(page: ft.Page):
    def voltar_para_inicial(_):
        print("Voltando para a tela inicial...")
        page.go("/inicial")
        
    def ir_para_perfil(_):
        print("Abrindo perfil...")
        page.go("/perfil")

    def selecionar_capitulo(e):
        capitulo_selecionado = e.control.data  
        print(f"Capítulo selecionado: {capitulo_selecionado}")
        page.go(f"/capitulo{capitulo_selecionado}")

    cabecalho = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    icon_size=24,
                    icon_color="#0C0473",
                    on_click=voltar_para_inicial,
                ),
                ft.Text(
                    "EduCash",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#0C0473",
                ),
                ft.IconButton(
                    icon=ft.icons.ACCOUNT_CIRCLE,
                    icon_size=30,
                    icon_color="#0C0473",
                    on_click=ir_para_perfil, 
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=20, vertical=10),
        bgcolor="#F5E4B4",  
        height=60,
        expand=False,
    )

    capitulos = []
    for i in range(1, 11):  
        capitulos.append(
            ft.ElevatedButton(
                text=f"Capítulo {i}",
                color="#0C0473",  
                bgcolor="#F5E4B4",  
                width=300,
                height=50,
                data=i,  
                on_click=selecionar_capitulo,  
            )
        )

    conteudo_scroll = ft.Container(
        content=ft.ListView(
            controls=capitulos,
            spacing=10,
            padding=ft.padding.all(20),
            expand=True,
        ),
        bgcolor="#0C0473",  
        expand=True,
    )

    layout_completo = ft.Column(
        [
            cabecalho,       
            conteudo_scroll, 
        ],
        spacing=0,
        expand=True,
    )

    page.controls.clear()
    page.add(layout_completo)