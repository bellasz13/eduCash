import flet as ft
import mysql.connector

def EditarPage(page: ft.Page): 

    def voltar_para_anterior(_):
        print("Voltando para a página anterior...")
        page.go("/perfil")

    def carregar_dados_usuario():
        try:
            conexao = mysql.connector.connect(
                host="localhost",  
                user="root",  
                password="isabella2005", 
                database="educash"  
            )  
            cursor = conexao.cursor()

            cursor.execute("SELECT nome, email FROM cadastro WHERE id = %s", (id,))
            cadastro = cursor.fetchone()

            cursor.execute("SELECT data_nascimento, telefone FROM extra WHERE id_usuario = %s", (id,))
            extra = cursor.fetchone()

            if cadastro:
                campo_nome.value = cadastro[0]
                campo_email.value = cadastro[1]

            if extra:
                campo_nascimento.value = extra[0] if extra[0] else ""
                campo_telefone.value = extra[1] if extra[1] else ""

            page.update() 
        except mysql.connector.Error as err:
            print(f"Erro ao carregar dados do banco de dados: {err}")
        finally:
            if 'conexao' in locals() and conexao.is_connected():
                conexao.close()

    def salvar_alteracoes(_):
        try:
            conexao = mysql.connector.connect(
                host="localhost",  
                user="root",  
                password="isabella2005", 
                database="educash"
            )
            cursor = conexao.cursor()

            cursor.execute(
                "UPDATE cadastro SET nome = %s, email = %s WHERE id = %s",
                (campo_nome.value, campo_email.value, id)
            )

            cursor.execute(
                """
                INSERT INTO extra (id_usuario, data_nascimento, telefone)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE
                data_nascimento = VALUES(data_nascimento), telefone = VALUES(telefone)
                """,
                (
                    id,
                    campo_nascimento.value,
                    campo_telefone.value
                )
            )

            conexao.commit()
            print("Alterações salvas com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro ao salvar alterações no banco de dados: {err}")
        finally:
            if 'conexao' in locals() and conexao.is_connected():
                conexao.close()

    def excluir_perfil(_):
        try:
            conexao = mysql.connector.connect(
                host="localhost",  
                user="root",  
                password="isabella2005", 
                database="educash"
            )
            cursor = conexao.cursor()

            cursor.execute("DELETE FROM extra WHERE id_usuario = %s", (id,))
            cursor.execute("DELETE FROM cadastro WHERE id = %s", (id,))

            conexao.commit()
            print("Perfil excluído com sucesso!")
            page.go("/")  
        except mysql.connector.Error as err:
            print(f"Erro ao excluir perfil: {err}")
        finally:
            if 'conexao' in locals() and conexao.is_connected():
                conexao.close()

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
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        padding=ft.padding.all(10),
    )

    campo_nome = ft.TextField(
        label="Nome de usuário",
        value="",
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
        value="",
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
        content=ft.Column(
            [
                layout,
            ],
            scroll=ft.ScrollMode.AUTO,  
        ),
        bgcolor="#0C0473",
        expand=True,
        padding=ft.padding.all(20),
    )

    page.controls.clear()
    page.add(container_principal)
    carregar_dados_usuario()
