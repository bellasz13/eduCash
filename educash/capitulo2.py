import flet as ft

def Capitulo2Page(page: ft.Page):
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
                "pergunta": "Por que é importante ensinar crianças sobre o valor do dinheiro desde cedo?",
                "alternativas": [
                    {"texto": "Para que elas possam comprar tudo o que desejarem.", "correta": False},
                    {"texto": "Para que elas possam trabalhar e ganhar dinheiro.", "correta": False},
                    {"texto": "Para estabelecer uma base para decisões financeiras sólidas no futuro.", "correta": True},
                    {"texto": "Para que elas possam ensinar seus pais sobre finanças.", "correta": False},
                ],
            },
            {
                "pergunta": "Qual é o benefício de ter uma educação financeira sólida na vida adulta?",
                "alternativas": [
                    {"texto": "Evitar dívidas e ter uma vida financeira mais equilibrada.", "correta": True},
                    {"texto": "Tornar-se rico rapidamente.", "correta": False},
                    {"texto": "Ter mais tempo livre para gastar dinheiro.", "correta": False},
                    {"texto": "Não precisar trabalhar.", "correta": False},
                ],
            },
                {
                "pergunta": "Por que é importante usar um cofrinho para ensinar as crianças sobre finanças?",
                "alternativas": [
                    {"texto": "Para que elas tenham um lugar bonito para guardar moedas.", "correta": False},
                    {"texto": "Para ensinar o valor da paciência e da poupança.", "correta": True},
                    {"texto": "Para que elas possam comprar tudo o que quiserem.", "correta": False},
                    {"texto": "Apenas para decorar o quarto.", "correta": False},
                ],
            },
                {
                "pergunta": "Por que é importante explicar às crianças como o dinheiro é ganho?",
                "alternativas": [
                    {"texto": "Para que elas valorizem mais o dinheiro e evitem desperdícios.", "correta": True},
                    {"texto": "Para que elas peçam dinheiro aos pais com mais frequência.", "correta": False},
                    {"texto": "Para que elas possam trabalhar desde pequenas.", "correta": False},
                    {"texto": "Apenas para que elas entendam o valor das coisas.", "correta": False},
                ],
            },
                {
                "pergunta": "Por que definir objetivos financeiros comuns é importante para a família?",
                "alternativas": [
                    {"texto": "Ajuda a motivar todos os membros a participarem dos investimentos.", "correta": True},
                    {"texto": "Impede que cada membro tenha suas próprias metas financeiras.", "correta": False},
                    {"texto": "Torna a gestão financeira familiar mais complicada.", "correta": False},
                    {"texto": "Desmotiva os membros da família a investirem.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a importância de poupar em conjunto como família?",
                "alternativas": [
                    {"texto": "Ensina o valor da disciplina e da paciência, além de ajudar a alcançar metas financeiras.", "correta": True},
                    {"texto": "Obriga todos os membros da família a economizar a mesma quantia.", "correta": False},
                    {"texto": "Impede que cada membro da família gaste seu próprio dinheiro.", "correta": False},
                    {"texto": "Torna a vida financeira da família mais difícil.", "correta": False},
                ],
            },
            {
                "pergunta": "Qual o principal objetivo de dar mesada às crianças?",
                "alternativas": [
                    {"texto": "Agradar as crianças com dinheiro.", "correta": False},
                    {"texto": "Ensinar sobre o trabalho, o valor do dinheiro e a gestão financeira.", "correta": True},
                    {"texto": "Fazer com que as crianças trabalhem mais em casa.", "correta": False},
                    {"texto": "Aumentar o consumo das crianças.", "correta": False},
                ],
            },
                {
                "pergunta": "O que acontece se os pais sempre completarem a mesada das crianças quando elas gastam tudo?",
                "alternativas": [
                    {"texto": "As crianças aprendem a importância de economizar.", "correta": False},
                    {"texto": "As crianças aprendem a valorizar o dinheiro.", "correta": False},
                    {"texto": "As crianças aprendem a ganhar mais dinheiro.", "correta": False},
                    {"texto": "As crianças aprendem que podem gastar o dinheiro como quiserem.", "correta": True},
                ],
            },
                {
                "pergunta": "O que significa empreendedorismo infantil?",
                "alternativas": [
                    {"texto": "Forçar as crianças a trabalharem desde pequenas.", "correta": False},
                    {"texto": "Encorajar as crianças a terem ideias criativas e inovadoras.", "correta": True},
                    {"texto": "Obrigar as crianças a participarem de concursos de empreendedorismo.", "correta": False},
                    {"texto": "Fazer com que as crianças abram empresas.", "correta": False},
                ],
            },
                {
                "pergunta": "Por que o trabalho em equipe é importante no empreendedorismo infantil?",
                "alternativas": [
                    {"texto": "Para que as crianças aprendam a competir umas com as outras.", "correta": False},
                    {"texto": "Para que as crianças possam criar ideias mais inovadoras e executar projetos com mais facilidade.", "correta": True},
                    {"texto": "Para que as crianças obedeçam aos seus colegas.", "correta": False},
                    {"texto": "Para que as crianças se tornem líderes.", "correta": False},
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

    def subcapitulo2_1():
        criar_subcapitulo(
            "A importância de\nensinar educação\nfinanceira desde cedo",
            """
A educação financeira infantil é essencial para criar adultos conscientes e responsáveis financeiramente, capazes de gerenciar suas próprias finanças com sabedoria e eficiência.

Ensinar crianças sobre o valor do dinheiro e a importância de planejar gastos e poupanças desde cedo ajuda a estabelecer uma base para decisões financeiras sólidas, além de uma vida adulta mais segura e estável.

A familiaridade com conceitos financeiros básicos pode proteger esses futuros adultos contra as armadilhas do endividamento e da gestão financeira inadequada.

Este tipo de educação inclui lições sobre como o dinheiro é ganho, gasto, poupado e investido, além de conceitos sobre orçamento e o valor do trabalho.

O objetivo é equipar as crianças com o conhecimento e as habilidades necessárias para tomar decisões financeiras sábias desde cedo, preparando-as para uma vida adulta mais equilibrada e financeiramente saudável.
            """
        )

    def subcapitulo2_2():
        criar_subcapitulo(
            "Como conversar\ncom crianças sobre\ndinheiro",
            """
Aqui estão seis dicas valiosas para introduzir lições financeiras essenciais para as crianças:

1. Incentive brincadeiras que envolvam finanças

Transforme jogos de faz-de-conta em oportunidades de aprendizado financeiro.
Por exemplo, criar uma lojinha ou um mercado onde as crianças possam comprar e vender itens usando dinheiro de mentirinha. Isso pode ajudá-las a entender o conceito de troca e o valor das coisas.
Essas atividades incentivam as crianças a fazerem escolhas e priorizarem o que compram, introduzindo a ideia de alocação de recursos de maneira lúdica.            
Crie atividades que simulem experiências de compra reais, como montar um pequeno café ou uma loja em casa onde as crianças possam praticar o papel de cliente e comerciante.
Elas podem aprender a fazer troco, negociar preços e entender o custo das coisas de forma interativa e envolvente.

2. Use cofrinho para juntar moedas

Um cofrinho é uma ferramenta clássica para ensinar crianças sobre a importância de economizar. Encoraje-as a guardar uma pequena quantia regularmente.
Explique que o dinheiro acumulado poderá ser usado para comprar algo especial que elas desejem. Isso não só ensina paciência e disciplina, mas também as recompensas de poupar a longo prazo.

3. Utilize jogos educativos

Aproveite a tecnologia e incorpore jogos educativos que focam em habilidades financeiras.
Jogos de computador ou aplicativos de smartphone que simulam situações econômicas podem ser extremamente úteis para explicar conceitos como investimento, poupança e despesas.

4. Ensine o valor do dinheiro

Muitas vezes, as crianças não conseguem diferenciar, por exemplo, o brinquedo de dez de reais do outro que custa mil. Cabe a você explicar melhor tudo isso, conversando e explicando à medida que as dúvidas e oportunidades aparecerem.
Explique sempre como o dinheiro é ganho e como cada item comprado é fruto de esforço e trabalho. Além disso, ensinar sobre caridade e a importância de ajudar os outros também pode ser uma forma valiosa de mostrar que o dinheiro tem também um papel social significativo.
            """
        )

    def subcapitulo2_3():
        criar_subcapitulo(
            "Mesada: uma\nferramenta para ensinar\nsobre finanças",
            """
Dar às crianças uma pequena mesada em troca de tarefas cumpridas pode ser uma excelente maneira de ensinar sobre o trabalho e o valor do dinheiro.
A mesada permite que elas gerenciem seu próprio dinheiro e tomem decisões sobre gastar ou economizar.

Acompanhe suas decisões e oriente-as sobre como poderiam otimizar suas escolhas financeiras.
E lembre-se: os valores das mesadas devem ter um limite e não devem ser complementados caso a criança gaste tudo em pouco tempo. Isso porque o objetivo é que elas aprendam a enquadrar seus gastos dentro do que possuem.

Não adianta dar mais dinheiro toda vez que pedirem. Se não, você ensina que, quando adultos, entrar no cheque especial é uma solução, por exemplo.
            """
        )

    def subcapitulo2_4():
        criar_subcapitulo(
            "Estimulando o\nempreendedorismo\nnas crianças",
            """
O empreendedorismo infantil nada mais é do que encorajar positivamente as crianças, propondo atividades, seja na escola ou em casa, que ajudem elas a adquirirem ou a desenvolverem ainda mais as competências necessárias para ser um empreendedor.
Crianças estimuladas a pensarem de forma diferente, a serem inventivas, inovadoras, criativas, corajosas, resilientes, planejadas, têm as bases necessárias para conseguirem resolver situações e problemas cotidianos e já crescem com uma cultura empreendedora enraizada. 

Os principais benefícios do empreendedorismo infantil são:

Estimular a criatividade e a proatividade: a criança não tem medo de propor “ideias mirabolantes”, são ousadas por natureza, e possuem o ímpeto de executar o que idealizaram sem muitos grandes empecilhos. 

Ensinar sobre planejamento e custos: o empreendedorismo infantil pode auxiliar a mostrar para as crianças noções sobre planejamento, de que antes do resultado final existe um caminho a ser percorrido, no qual perguntas precisam ser respondidas.

Mostrar como executar projetos: a criança com pensamento empreendedor é guiada a compreender que os planos idealizados podem ser executados, já que o planejamento aconteceu previamente.

Revelar a importância do trabalho em equipe em todas as fases: a criança consegue perceber que ao ouvir outras ideias e ao se juntar com outras pessoas com um mesmo propósito é possível  criar inovações ainda melhores e executar as tarefas com mais facilidade. 
            """
        )

    def subcapitulo2_5():
        criar_subcapitulo(
            "Criando uma\ncultura de economia\nna família",
            """
Criar uma cultura de investimentos na família pode ser uma maneira poderosa de assegurar um futuro financeiro mais seguro para todos.

Além de promover a educação financeira, esse hábito pode aumentar o comprometimento de cada membro em buscar melhores rendimentos e, consequentemente, melhorar a qualidade de vida.

A seguir, apresentamos algumas dicas essenciais para ajudar você a criar e consolidar essa cultura dentro de sua família:

- Definir objetivos financeiros comuns: quando todos na família têm metas claras e alinhadas, é mais fácil motivar a todos a participar ativamente dos investimentos.

- Poupar é um hábito essencial para qualquer investidor de sucesso, e quando a família faz isso unida, a probabilidade de sucesso aumenta. Criar o hábito de poupar em conjunto não só ajuda a alcançar as metas financeiras, como também ensina o valor da disciplina e da paciência.

- Por último, mas não menos importante, acompanhar o progresso dos investimentos é fundamental para garantir que a família está no caminho certo.

Muitos investidores cometem o erro de não monitorar suas aplicações, o que pode levar a perdas e desvio de metas.
            """
        )

    def subcapitulo2_quiz():
            criar_quiz()

    def subcapitulo2_desafio():
        criar_subcapitulo(
            "Desafio",
            """
Parabéns por explorar um dos aspectos mais importantes da educação financeira: a introdução dos conceitos financeiros básicos na infância! Agora é hora de colocar esse aprendizado em prática.

Desafio: Crie um plano para ensinar educação financeira a uma criança.
Escolha a criança: Pode ser um sobrinho, primo, filho ou qualquer criança próxima a você.

Estabeleça uma atividade prática:
Monte uma "lojinha" ou "mercadinho" com itens simples (como brinquedos ou lanches) e use dinheiro fictício para simular trocas.
Utilize um cofrinho e defina com a criança uma meta de economia (por exemplo, comprar um brinquedo ou um passeio especial).

Explique os conceitos: Durante a atividade, ensine sobre o valor do dinheiro, como ele é ganho, economizado e utilizado. Mostre a importância do planejamento.

Documente o aprendizado: Peça para a criança contar o que aprendeu após a experiência.

Pergunta Reflexiva: Como você percebeu que essa abordagem lúdica influenciou o interesse da criança por aprender mais sobre dinheiro e economia?
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
            criar_bloco("A importância de ensinar educação financeira desde cedo", lambda _: subcapitulo2_1()),
            criar_bloco("Como conversar com crianças sobre dinheiro", lambda _: subcapitulo2_2()),
            criar_bloco("Mesada: uma ferramenta para ensinar sobre finanças", lambda _: subcapitulo2_3()),
            criar_bloco("Estimulando o empreendedorismo nas crianças", lambda _: subcapitulo2_4()),
            criar_bloco("Criando uma cultura de economia na família", lambda _: subcapitulo2_5()),
            criar_bloco("Quiz", lambda _: subcapitulo2_quiz()),
            criar_bloco("Desafio", lambda _: subcapitulo2_desafio()),
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
