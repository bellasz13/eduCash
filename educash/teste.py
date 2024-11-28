def PerfilPage(page: ft.Page, id):
    usuario = verificar_usuario(id)
    
    if not usuario:
        print("Usuário não encontrado!")
        page.snack_bar = ft.SnackBar(
            content=ft.Text("Usuário não encontrado!", color="white"),
            bgcolor="red",
        )
        page.snack_bar.open()
        return
    
    nome = usuario.get("nome", "Nome não informado")
    email = usuario.get("email", "Email não informado")
    telefone = usuario.get("telefone", "Telefone não informado")
    data_nascimento = usuario.get("data_nascimento", "Data de nascimento não informada")
    
    # Continue o código de construção da página

