import flet as ft

def Capitulo1Page(page: ft.Page):
    
    def criar_cabecalho(titulo, voltar_acao):
        return ft.Container(
            content=ft.Stack(
                [
                    ft.Row(
                        [
                            ft.IconButton(
                                icon=ft.icons.ARROW_BACK,
                                icon_size=24,
                                icon_color="#0C0473",
                                on_click=voltar_acao,  
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.START,  
                    ),
                    ft.Container(
                        content=ft.Text(
                            titulo,
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color="#0C0473",
                            text_align=ft.TextAlign.CENTER,
                        ),
                        alignment=ft.alignment.center,  
                    ),
                ]
            ),
            padding=ft.padding.symmetric(horizontal=20, vertical=10),
            bgcolor="#F5E4B4",
            height=100,
        )

    def criar_subcapitulo(titulo, conteudo):
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    criar_cabecalho(titulo, lambda _: page.go("/continuar")), 
                    ft.Container(
                        content=ft.ListView(
                            controls=[
                                ft.Text(
                                    conteudo,
                                    size=16,
                                    color="#FFFFFF",
                                    text_align=ft.TextAlign.JUSTIFY,
                                )
                            ],
                            padding=ft.padding.all(20),
                            expand=True,
                        ),
                        bgcolor="#0C0473",
                        expand=True,
                    ),
                ],
                spacing=0,
                expand=True,
            )
        )
        page.update()
        
    def subcapitulo1_1():
        criar_subcapitulo(
            "O que é educação financeira e por que ela é importante?",
            """
            Educação financeira vai além de acumular recursos. 
            É o processo de adquirir conhecimento e autoconfiança 
            para gerenciar eficientemente seus recursos financeiros, 
            compreendendo como tomar decisões financeiras, evitar 
            endividamento e construir um futuro financeiro sustentável.

            Investir tempo e esforço na educação financeira agrega 
            conhecimento e proporciona vários benefícios que impactam 
            positivamente a jornada de cada um. Dentre esses benefícios, destacam-se:
            - Mais tranquilidade no dia a dia.
            - Prevenção de golpes e fraudes financeiras.
            - Criação de planos de curto, médio e longo prazo.
            - E muito mais!
            """
        )

    def subcapitulo1_2():
        criar_subcapitulo(
            "A relação entre dinheiro e felicidade: mitos e verdades",
            """
            Muitos acreditam que a felicidade está diretamente ligada à quantidade de dinheiro que possuem. 
            No entanto, pesquisas mostram que, após um certo ponto, o aumento da renda tem pouco impacto 
            na felicidade. O segredo está em como você administra e usa seus recursos financeiros.

            O dinheiro pode comprar conforto, segurança e experiências que trazem alegria. Contudo, 
            uma vida equilibrada e focada em valores, como família, saúde e amizades, é essencial para uma felicidade duradoura.
            """
        )

    def subcapitulo1_3():
        criar_subcapitulo(
            "Mentalidade de riqueza: cultivando hábitos financeiros saudáveis",
            """
            A mentalidade de riqueza não se trata apenas de ganhar mais dinheiro, mas sim de adotar hábitos saudáveis 
            que promovem a estabilidade financeira. Isso inclui viver abaixo das suas possibilidades, evitar dívidas desnecessárias 
            e investir regularmente.

            Cultivar essa mentalidade exige disciplina, paciência e o entendimento de que a riqueza é construída ao longo do tempo. 
            Pequenos passos consistentes podem levar a grandes resultados.
            """
        )

    def subcapitulo1_4():
        criar_subcapitulo(
            "Metas financeiras: como definir e alcançar seus objetivos",
            """
            Definir metas financeiras claras é o primeiro passo para alcançar seus objetivos. Divida suas metas em curto, médio e 
            longo prazo e crie um plano detalhado para atingi-las.

            Use ferramentas como orçamentos, investimentos e automatização de economias para facilitar esse processo. 
            Revise regularmente suas metas para se manter no caminho certo.
            """
        )

    def subcapitulo1_5():
        criar_subcapitulo(
            "O poder dos juros compostos: como o dinheiro trabalha para você",
            """
            Os juros compostos são uma ferramenta poderosa que permite que seu dinheiro cresça ao longo do tempo. 
            Quando você investe, os rendimentos gerados também começam a render, criando um efeito de "bola de neve".

            Quanto mais cedo você começar a investir, maior será o impacto dos juros compostos. Aproveite esse poder 
            e comece a fazer seu dinheiro trabalhar para você o quanto antes.
            """
        )

    def subcapitulo1_quiz():
        criar_subcapitulo(
            "Quiz",
            """
            Teste seus conhecimentos sobre educação financeira com nosso quiz interativo. 
            Responda perguntas para consolidar o aprendizado e entender melhor como aplicar os conceitos no seu dia a dia.
            """
        )

    def subcapitulo1_desafio():
        criar_subcapitulo(
            "Desafio",
            """
            Coloque em prática tudo o que aprendeu neste capítulo. Crie um orçamento detalhado para o próximo mês, 
            estabeleça metas financeiras e monitore seus hábitos de consumo.
            """
        )

    def configurar_layout_principal():
        cabecalho = ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_size=24,
                        icon_color="#0C0473",
                        on_click=lambda _: page.go("/continuar"),  
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

        def criar_bloco(titulo, acao):
            return ft.Container(
                width=200,
                height=200,
                bgcolor="#F5E4B4",
                border_radius=10,
                padding=ft.padding.all(10),
                alignment=ft.alignment.center,
                on_click=acao,
                content=ft.Text(
                    titulo,
                    size=16,
                    weight=ft.FontWeight.BOLD,
                    color="#0C0473",
                    text_align=ft.TextAlign.CENTER,
                ),
            )

        blocos = [
            criar_bloco("O que é educação financeira e por que ela é importante?", lambda _: subcapitulo1_1()),
            criar_bloco("A relação entre dinheiro e felicidade: mitos e verdades", lambda _: subcapitulo1_2()),
            criar_bloco("Mentalidade de riqueza: cultivando hábitos financeiros saudáveis", lambda _: subcapitulo1_3()),
            criar_bloco("Metas financeiras: como definir e alcançar seus objetivos", lambda _: subcapitulo1_4()),
            criar_bloco("O poder dos juros compostos: como o dinheiro trabalha para você", lambda _: subcapitulo1_5()),
            criar_bloco("Quiz", lambda _: subcapitulo1_quiz()),
            criar_bloco("Desafio", lambda _: subcapitulo1_desafio()),
        ]

        conteudo_scroll = ft.Container(
            content=ft.ListView(
                spacing=10,
                controls=blocos,
                padding=ft.padding.all(20),
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
        page.update()

    configurar_layout_principal()
