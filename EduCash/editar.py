import flet as ft

def EditarPage(page: ft.Page):
    def voltar_para_anterior(_):
        print("Voltando para a página anterior...")
        page.go("/perfil")

    def salvar_alteracoes(_):
        print("Alterações salvas!")

    def excluir_perfil(_):
        print("Perfil excluído!")

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
                    "Editar perfil",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        height=60,
        bgcolor="#0C0473",
        padding=ft.padding.symmetric(horizontal=15),
    )

    icone_perfil = ft.Container(
        content=ft.Column(
            [
                ft.Icon(
                    ft.icons.ACCOUNT_CIRCLE,
                    size=100,
                    color="#F5E4B4",
                ),
                ft.Icon(
                    ft.icons.EDIT,
                    size=20,
                    color="#F5E4B4",
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        padding=ft.padding.all(10),
    )

    campo_nome = ft.TextField(
        label="Nome de usuário",
        value="user",
        bgcolor="#0C0473",
        color="white",
        border_color="#F5E4B4",
        label_style=ft.TextStyle(color="#F5E4B4"),
        width=300,
    )
    campo_nascimento = ft.TextField(
        label="Data de nascimento",
        hint_text="dd/mm/aaaa",
        bgcolor="#0C0473",
        color="white",
        border_color="#F5E4B4",
        label_style=ft.TextStyle(color="#F5E4B4"),
        width=300,
    )
    campo_telefone = ft.TextField(
        label="Telefone",
        hint_text="(00) 0 0000 - 0000",
        bgcolor="#0C0473",
        color="white",
        border_color="#F5E4B4",
        label_style=ft.TextStyle(color="#F5E4B4"),
        width=300,
    )
    campo_email = ft.TextField(
        label="Email",
        value="email@email.com",
        bgcolor="#0C0473",
        color="white",
        border_color="#F5E4B4",
        label_style=ft.TextStyle(color="#F5E4B4"),
        width=300,
    )

    botao_salvar = ft.ElevatedButton(
        text="Salvar alterações",
        bgcolor="#F5E4B4",
        color="#0C0473",
        width=200,
        on_click=salvar_alteracoes,
    )

    botao_excluir = ft.ElevatedButton(
        text="Excluir perfil",
        color="white",
        bgcolor="#F44336",  
        width=200,
        on_click=excluir_perfil,
    )
    layout = ft.Column(
        [
            cabecalho,
            icone_perfil,
            campo_nome,
            campo_nascimento,
            campo_telefone,
            campo_email,
            ft.Container(height=20),  
            botao_salvar,
            ft.Container(height=10),  
            botao_excluir,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=15,
        expand=True,
    )

    container_principal = ft.Container(
        content=layout,
        bgcolor="#0C0473",
        expand=True,
        padding=ft.padding.all(20),
    )

    page.controls.clear()
    page.add(container_principal)