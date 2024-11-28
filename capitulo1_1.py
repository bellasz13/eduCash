import flet as ft

def Capitulo1_1Page(page: ft.Page, subcapitulo_index: int):
   
    conteudos = [
        "Subcapítulo 1: O que é educação financeira e por que ela é importante? \n\nAqui vai o conteúdo do primeiro subcapítulo...",
        "Subcapítulo 2: A relação entre dinheiro e felicidade: mitos e verdades \n\nAqui vai o conteúdo do segundo subcapítulo...",
        "Subcapítulo 3: Mentalidade de riqueza: cultivando hábitos financeiros saudáveis \n\nAqui vai o conteúdo do terceiro subcapítulo...",
        "Subcapítulo 4: Metas financeiras: como definir e alcançar seus objetivos \n\nAqui vai o conteúdo do quarto subcapítulo...",
        "Subcapítulo 5: O poder dos juros compostos: como o dinheiro trabalha para você \n\nAqui vai o conteúdo do quinto subcapítulo...",
        "Subcapítulo 6: Quiz \n\nAqui vai o conteúdo do quiz...",
        "Subcapítulo 7: Desafio \n\nAqui vai o conteúdo do desafio...",
    ]
    
    cabecalho = ft.Container(
        content=ft.Row(
            [
                ft.IconButton(
                    icon=ft.icons.ARROW_BACK,
                    icon_color="#0C0473",
                    icon_size=24,
                    on_click=lambda _: page.go("/capitulo1"),
                ),
                ft.Text(
                    "EduCash",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#0C0473",
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(horizontal=20, vertical=10),
        bgcolor="#F5E4B4",
        height=60, 
    )
    
    titulo_subcapitulo = ft.Text(
        f"Subcapítulo {subcapitulo_index + 1}: {conteudos[subcapitulo_index].split(' ')[0]}",
        size=18,
        weight=ft.FontWeight.BOLD,
        color="white",
        text_align=ft.TextAlign.CENTER,
    )

    conteudo_texto = ft.Text(
        conteudos[subcapitulo_index],
        size=16,
        weight=ft.FontWeight.NORMAL,
        color="white",
        text_align=ft.TextAlign.LEFT,
    )

    layout_principal = ft.Column(
        [
            cabecalho,
            titulo_subcapitulo,
            ft.Container(height=20),  
            ft.SingleChildScrollView(
                content=ft.Column([conteudo_texto], expand=True),
                scroll=ft.ScrollMode.ALWAYS,  
            ),
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )

    page.controls.clear()
    page.add(layout_principal)

