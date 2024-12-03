import flet as ft
import mysql.connector

def verificar_usuario(id):
    try:
        conexao = mysql.connector.connect(
            host="localhost",  
            user="root",  
            password="isabella2005", 
            database="educash"  
        )  
        
        cursor1 = conexao.cursor()
        cursor1.execute("SELECT nome, email FROM cadastro WHERE id = %s", (id,))
        cadastro = cursor1.fetchone()
        cursor1.close()

        cursor2 = conexao.cursor()
        cursor2.execute("SELECT telefone, data_nascimento FROM extra WHERE id = %s", (id,))
        extra = cursor2.fetchone()
        cursor2.close()

        resultado = {}
        if cadastro:
            resultado["nome"] = cadastro[0]
            resultado["email"] = cadastro[1]
        if extra:
            resultado["telefone"] = extra[0]
            resultado["data_nascimento"] = extra[1]

        return resultado if resultado else None
    except mysql.connector.Error as err:
        print(f"Erro ao acessar o banco de dados: {err}")
        return None
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()

def EditarPage(page: ft.Page, id):
    usuario = verificar_usuario(id)
    
    nome = usuario["nome"] if usuario and "nome" in usuario else "Nome não informado"
    email = usuario["email"] if usuario and "email" in usuario else "Email não informado"
    telefone = usuario["telefone"] if usuario and "telefone" in usuario else "Telefone não informado"
    data_nascimento = usuario["data_nascimento"] if usuario and "data_nascimento" in usuario else "Data de nascimento não informada"
    
    def voltar_para_anterior(_):
        page.go("/perfil")
    
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
                (nome.value, email.value, id)
            )

            cursor.execute(
                """
                INSERT INTO extra (id, data_nascimento, telefone)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE
                data_nascimento = %s, telefone = %s
                """,
                (
                    id,
                    data_nascimento.value,
                    telefone.value,
                    data_nascimento.value,
                    telefone.value
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

            cursor.execute("DELETE FROM extra WHERE id = %s", (id,))
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

    nome = ft.TextField(
        label="Nome de usuário",
        value=nome,
        bgcolor="#0C0473",
        color="white",
        border_color="#F5E4B4",
        label_style=ft.TextStyle(color="#F5E4B4"),
        width=300,
    )
    data_nascimento = ft.TextField(
        label="Data de nascimento",
        value=data_nascimento,
        hint_text="dd/mm/aaaa",
        bgcolor="#0C0473",
        color="white",
        border_color="#F5E4B4",
        label_style=ft.TextStyle(color="#F5E4B4"),
        width=300,
    )
    telefone = ft.TextField(
        label="Telefone",
        value=telefone,
        hint_text="(00) 0 0000 - 0000",
        bgcolor="#0C0473",
        color="white",
        border_color="#F5E4B4",
        label_style=ft.TextStyle(color="#F5E4B4"),
        width=300,
    )
    email = ft.TextField(
        label="Email",
        value=email,
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
            nome,
            data_nascimento,
            telefone,
            email,
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
