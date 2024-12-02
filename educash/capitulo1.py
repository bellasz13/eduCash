import flet as ft

def Capitulo1Page(page: ft.Page):
    def criar_cabecalho(titulo):
        def voltar_para_anterior(_):
            print("Voltando para o capítulo 1...")
            page.go("/continuar")
        
        return ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_size=24,
                        icon_color="#0C0473",
                        on_click=voltar_para_anterior,
                    ),
                    ft.Text(
                        titulo,
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color="#0C0473",
                        text_align=ft.TextAlign.CENTER,
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            padding=ft.padding.symmetric(horizontal=20, vertical=10),
            bgcolor="#F5E4B4",
            height=130,
        )

    def criar_subcapitulo(titulo, conteudo):
        page.controls.clear()
        page.add(
            ft.Column(
                [
                    criar_cabecalho(titulo),
                    ft.Container(
                        content=ft.ListView(
                            controls=[
                                ft.Text(
                                    conteudo,
                                    size=14,
                                    color="#FFFFFF",
                                    text_align=ft.TextAlign.LEFT,
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
    
    def criar_quiz():
        perguntas = [
            {
                "pergunta": "A educação financeira permite que as pessoas:",
                "alternativas": [
                    {"texto": "Gastem livremente, sem se preocupar com as consequências.", "correta": False},
                    {"texto": "Criem planos financeiros realistas para alcançar seus objetivos.", "correta": True},
                    {"texto": "Contratem qualquer tipo de crédito sem se informar sobre as condições.", "correta": False},
                    {"texto": "Evitem completamente qualquer tipo de investimento, por ser arriscado.", "correta": False},
                ],
            },
            {
                "pergunta": "O que é educação financeira?",
                "alternativas": [
                    {"texto": "A habilidade de ganhar muito dinheiro rapidamente.", "correta": False},
                    {"texto": "O conhecimento para gerenciar recursos financeiros e tomar decisões conscientes.", "correta": True},
                    {"texto": "A capacidade de evitar totalmente riscos financeiros.", "correta": False},
                    {"texto": "Um curso obrigatório para todos os cidadãos.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual é a importância de compreender os serviços financeiros como crédito, seguros e consórcios?",
                "alternativas": [
                    {"texto": "Para evitar cair em armadilhas e fazer escolhas mais conscientes. ", "correta": True},
                    {"texto": "Para conseguir os melhores produtos financeiros sem precisar comparar.", "correta": False},
                    {"texto": "Para ter acesso a crédito ilimitado e realizar todos os seus desejos.", "correta": False},
                    {"texto": "Para investir em produtos financeiros complexos e obter retornos altos.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a importância da educação financeira contínua no desenvolvimento de um mindset saudável?",
                "alternativas": [
                    {"texto": "Para aprender novas estratégias de investimento e se tornar um especialista.", "correta": False},
                    {"texto": "Para acompanhar as mudanças do mercado e tomar decisões mais informadas.", "correta": True},
                    {"texto": "Para poder dar conselhos financeiros aos amigos e familiares.", "correta": False},
                    {"texto": "Para se sentir superior aos outros que não se interessam por finanças.", "correta": False},
                ],
            },
                {
                "pergunta": "Considerando que o dinheiro não garante a felicidade, quais outros fatores podem contribuir para o bem-estar?",
                "alternativas": [
                    {"texto": "Relacionamentos saudáveis, saúde física e realização pessoal.", "correta": True},
                    {"texto": "Carros luxuosos, casas grandes e viagens internacionais.", "correta": False},
                    {"texto": "Poder e fama.", "correta": False},
                    {"texto": "Isolamento social e individualismo.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a principal conclusão que os estudos sobre dinheiro e felicidade apontam?",
                "alternativas": [
                    {"texto": "O dinheiro traz felicidade incondicionalmente.", "correta": False},
                    {"texto": "O dinheiro não tem nenhuma relação com a felicidade.", "correta": False},
                    {"texto": "O dinheiro pode contribuir para a felicidade, mas não é o único fator.", "correta": True},
                    {"texto": "A felicidade é determinada exclusivamente pela quantidade de dinheiro.", "correta": False},
                ],
            },
            {
                "pergunta": "O que é educação financeira?",
                "alternativas": [
                    {"texto": "A habilidade de ganhar muito dinheiro rapidamente.", "correta": False},
                    {"texto": "O conhecimento para gerenciar recursos financeiros e tomar decisões conscientes.", "correta": True},
                    {"texto": "A capacidade de evitar totalmente riscos financeiros.", "correta": False},
                    {"texto": "Um curso obrigatório para todos os cidadãos.", "correta": False},
                ],
            },
                {
                "pergunta": "O que você pode fazer para maximizar os benefícios dos juros compostos em sua previdência privada?",
                "alternativas": [
                    {"texto": "Investir grandes quantias de dinheiro de uma só vez.", "correta": False},
                    {"texto": "Mudar de fundo de investimento frequentemente em busca de melhores retornos.", "correta": False},
                    {"texto": "Escolher o fundo de investimento com a maior taxa de juros do mercado.", "correta": False},
                    {"texto": "Começar a investir o mais cedo possível e realizar contribuições regulares.", "correta": True},
                ],
            },
                {
                "pergunta": "Qual a importância da previdência privada para aproveitar o poder dos juros compostos?",
                "alternativas": [
                    {"texto": "A previdência privada é a única forma de investir e obter juros compostos.", "correta": False},
                    {"texto": "A previdência privada oferece as maiores taxas de juros do mercado.", "correta": False},
                    {"texto": "A previdência privada é um investimento de longo prazo, permitindo que os juros compostos atuem por mais tempo.", "correta": True},
                    {"texto": "A previdência privada é obrigatória para todos os trabalhadores.", "correta": False},
                ],
            },
                {
                "pergunta": "Por que é importante ter uma reserva de emergência?",
                "alternativas": [
                    {"texto": "Para evitar contrair novas dívidas em caso de imprevistos.", "correta": True},
                    {"texto": "Para poder fazer viagens.", "correta": False},
                    {"texto": "Para impressionar seus amigos com sua riqueza.", "correta": False},
                    {"texto": "Para investir em um negócio.", "correta": False},
                ],
            },
        ]
        
        def criar_pergunta(pergunta, alternativas):
            controles = [ft.Text(pergunta, size=16, weight=ft.FontWeight.BOLD, color="#FFFFFF")]

            for alternativa in alternativas:
                def on_click(e, correta=alternativa["correta"]):
                    if correta:
                        e.control.style = ft.ButtonStyle(bgcolor={"": "#4CAF50"})  # Verde
                    else:
                        e.control.style = ft.ButtonStyle(bgcolor={"": "#FF5252"})  # Vermelho
                    e.control.update()

                
                botao = ft.ElevatedButton(
                    text=alternativa["texto"],
                    width=300,
                    bgcolor="#D9C9F2",
                    color="#000000",
                    on_click=on_click
                )
                controles.append(botao)

            return ft.Container(
                content=ft.Column(controles, spacing=10),
                padding=ft.padding.all(20),
                border_radius=10,
                bgcolor="#0C0473",
                margin=ft.margin.only(bottom=20),
            )

        perguntas_controle = [criar_pergunta(p["pergunta"], p["alternativas"]) for p in perguntas]

        page.controls.clear()
        page.add(
            ft.Column(
                [
                    criar_cabecalho("Quiz"),
                    ft.ListView(
                        controls=perguntas_controle,
                        padding=ft.padding.all(10),
                        expand=True,
                    ),
                ],
                spacing=0,
                expand=True,
            )
        )
        page.update()

    criar_quiz()

    def subcapitulo1_1():
        criar_subcapitulo(
            "O que é educação\nfinanceira e por que\nela é importante?",
            """
            Educação financeira vai além de acumular recursos. É o processo de adquirir conhecimento e autoconfiança para gerenciar eficientemente seus recursos financeiros, compreendendo como tomar decisões financeiras, evitar endividamento e construir um futuro financeiro sustentável. 
            Investir tempo e esforço na educação financeira agrega conhecimento e proporciona vários benefícios que impactam positivamente a jornada de cada um. Dentre esses benefícios, destacam-se:
            Mais tranquilidade no dia a dia: pode-se tomar decisões mais informadas, reduzindo o estresse relacionado às finanças diárias.
            Prevenção de golpes e fraudes financeiras: maior capacidade de identificar e evitar ações fraudulentas, protegendo o patrimônio financeiro e os dados pessoais.
            Criação de planos de curto, médio e longo prazos: capacita a estabelecer metas financeiras realistas e a criar planos estratégicos para serem alcançados ao longo do tempo.
            Maior consciência de serviços financeiros: compreender o funcionamento e as implicações de créditos, seguros e consórcios, por exemplo, permite que esses recursos sejam usados de forma consciente, evitando endividamentos.
            Aumento da capacidade de investimento: proporciona oportunidades de investir com rentabilidade e segurança, potencializando o crescimento do patrimônio ao longo do tempo.
            Melhoria nas relações: ao compreender as finanças, as pessoas podem ter conversas mais abertas e construtivas sobre dinheiro, fortalecendo as relações familiares e sociais.
            """
        )

    def subcapitulo1_2():
        criar_subcapitulo(
            "A relação entre\ndinheiro e felicidade:\nmitos e verdades",
            """
            Afinal… dinheiro traz felicidade?
            Esta é uma pergunta complexa e cientistas do mundo todo já fizeram uma série de experimentos para respondê-la. Os estudos mostram que, se bem utilizado, o dinheiro pode trazer felicidade sim, mas claro que sozinho ele não é suficiente para tal. 
            Na realidade, o dinheiro ajuda mais as pessoas a saírem da pobreza e da miséria, facilitando suas vidas e diminuindo a possibilidade de tristeza. Porém, isso não significa que magnatas são mais felizes, muito pelo contrário, as estatísticas demonstram que a classe média é que conta com as pessoas mais felizes do mundo.
            De qualquer modo, embora o dinheiro não seja o único fator determinante para a felicidade, é inegável que ele desempenha um papel importante na qualidade de vida. Ter recursos financeiros adequados permite o acesso a necessidades básicas, como alimentação, moradia e saúde. Além disso, o dinheiro também pode proporcionar conforto, segurança e oportunidades de crescimento pessoal e profissional.
            Estudos têm mostrado que a falta de dinheiro pode levar a problemas de saúde, estresse e insatisfação geral. Por outro lado, ter uma situação financeira estável pode contribuir para o bem-estar emocional e a sensação de segurança. Portanto, é válido afirmar que o dinheiro pode sim influenciar positivamente a qualidade de vida e, consequentemente, a felicidade.
            """
        )

    def subcapitulo1_3():
        criar_subcapitulo(
            "Mentalidade de riqueza:\ncultivando hábitos\nfinanceiros saudáveis",
            """
            Um mindset financeiro saudável é a chave para ter uma vida financeira estável e tomar decisões inteligentes envolvendo dinheiro.
            Desenvolver essa mentalidade permitirá que você identifique e aproveite oportunidades de investimento e crescimento, adquira confiança e sabedoria para lidar com emergências e imprevistos, e também condições de alcançar uma aposentadoria confortável e segura.
            Como desenvolver um mindset financeiro saudável?
            Construir um mindset financeiro saudável exige muito mais do que apenas saber lidar com números - envolve uma mudança de mentalidade e a adoção de hábitos que promovem uma relação positiva com o dinheiro.
            Abaixo trouxemos algumas ideias para te ajudar nessa jornada. Confira:
            Autoconhecimento;
            Estabeleça metas financeiras claras;
            Desenvolva o hábito de guardar dinheiro;
            Educação financeira contínua;
            Se comprometer e manter a paciência;
            Cultive hábitos financeiros saudáveis;
            Mantenha um estilo de vida abaixo de suas possibilidades.
            """
        )

    def subcapitulo1_4():
        criar_subcapitulo(
            "Metas financeiras:\ncomo definir e\nalcançar seus objetivos",
            """
            1. Faça uma avaliação financeira:
            Antes de definir suas metas, faça uma análise profunda de sua situação financeira atual. Avalie suas receitas, despesas, dívidas e poupanças. Ter uma compreensão clara de sua posição financeira é fundamental para estabelecer metas realistas.
            2. Defina metas claras:
            Estabeleça metas financeiras específicas e mensuráveis. Tenha clareza sobre o que você deseja alcançar em 2024, seja pagar dívidas, criar um fundo de emergência, economizar para uma grande compra ou investir para o futuro.
            3. Elabore um orçamento realista:
            Crie um orçamento que esteja alinhado com suas metas. Aloque suas receitas de maneira eficiente, reservando fundos para suas prioridades financeiras. Considere cortar gastos desnecessários e direcionar recursos para o que realmente importa.
            4. Estude muito:
            Aprimore seus conhecimentos financeiros por meio de cursos online oferecidos por órgãos como o Banco Central do Brasil (Bacen), a Comissão de Valores Mobiliários (CVM) e a Associação Brasileira das Entidades dos Mercados Financeiro e de Capitais (Anbima) oferecem materiais educativos valiosos. Além dessas, outra sugestão é o Cooperação na Ponta do Lápis, programa gratuito de educação financeira.
            5. Diversifique suas fontes de renda:
            Considere diversas maneiras de aumentar suas receitas. Isso pode envolver explorar oportunidades de renda extra, investir em habilidades que valorizam seu perfil profissional ou procurar novas fontes de renda passiva.
            6. Crie uma reserva de emergência:
            Estabeleça uma reserva de emergência para lidar com situações inesperadas. Esse fundo deve cobrir de três a seis meses de despesas, proporcionando uma rede de segurança em caso de imprevistos financeiros.
            7. Acompanhe e ajuste regularmente:
            Mantenha um monitoramento constante de suas finanças. Avalie regularmente seu progresso em relação às metas estabelecidas e faça ajustes conforme necessário. A flexibilidade é chave para garantir o sucesso ao longo do ano.
            """
        )

    def subcapitulo1_5():
        criar_subcapitulo(
            "O poder dos juros\ncompostos: como o\ndinheiro trabalha\npara você",
            """
            Você já ouviu falar em juros compostos? Se você está pensando em garantir um futuro mais tranquilo, esse conceito pode ser seu grande aliado. Mas afinal, o que são esses juros e como eles podem te ajudar a construir um patrimônio sólido?
            Imagine uma bola de neve rolando ladeira abaixo. À medida que ela desce, vai coletando mais neve e ficando cada vez maior. Os juros compostos funcionam de forma similar. É como se você estivesse investindo e os juros gerados por esse investimento fossem reinvestidos, gerando ainda mais juros.
            Mas como isso funciona na prática?
            Quando você contribui para um plano de previdência privada, por exemplo, seu dinheiro começa a render juros. Os juros compostos fazem com que esses juros também rendam juros, criando um efeito multiplicador ao longo do tempo. É como se seu dinheiro estivesse trabalhando para você 24 horas por dia, 7 dias por semana.
            Confira mais vantagens:
            Crescimento exponencial: os juros compostos fazem com que seu dinheiro cresça de forma acelerada, te ajudando a alcançar seus objetivos financeiros mais rapidamente.
            Força para pequenos investimentos:mesmo pequenas quantias investidas regularmente podem gerar resultados expressivos ao longo de muitos anos.
            Tempo como aliado: quanto mais tempo seu dinheiro ficar investido, maior será o impacto dos juros compostos.
            Por isso, a previdência, por ser um investimento de longo prazo, é uma ótima opção.
            Em resumo, os juros compostos são uma força poderosa que pode transformar seus investimentos em um patrimônio significativo. Ao entender como eles funcionam e como se aplicam à previdência privada, você estará dando um passo importante para garantir um futuro mais tranquilo e próspero.
            """
        )

    def subcapitulo1_quiz():
            criar_quiz()

    def subcapitulo1_desafio():
        criar_subcapitulo(
            "Desafio",
            """
            Parabéns por ter chegado até 
            aqui futuro invetidor!\n
            Agora está na hora de colocar 
            em prática tudo que você aprendeu 
            no Capítulo 1 - O que é educação 
            financeira e por que ela é 
            importante?\n
            Crie um orçamento detalhado para 
            o próximo mês, estabeleça metas 
            financeiras e monitore seus 
            hábitos de consumo.\n
            A pergunta que fica agora é: ao 
            final do seu orçamento, você se 
            considera uma pessoa com bons hábitos 
            financeiros?
            """
        )

    def voltar_para_continuar(_):
        page.go("/continuar")
    
    def configurar_layout_principal():
        cabecalho = ft.Container(
            content=ft.Row(
                [
                    ft.IconButton(
                        icon=ft.icons.ARROW_BACK,
                        icon_size=24,
                        icon_color="#0C0473",
                        on_click=voltar_para_continuar,  
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
