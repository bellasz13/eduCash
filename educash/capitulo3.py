import flet as ft

def Capitulo3Page(page: ft.Page):
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
                "pergunta": "Por que o planejamento financeiro é importante para evitar compras por impulso?",
                "alternativas": [
                    {"texto": "Permite gastar mais dinheiro.", "correta": False},
                    {"texto": "Ajuda a identificar prioridades e evitar gastos desnecessários.", "correta": True},
                    {"texto": "Torna a vida mais chata.", "correta": False},
                    {"texto": "Impede que você compre o que deseja.", "correta": False},
                ],
            },
            {
                "pergunta": "Por que o uso excessivo de cartões de crédito pode aumentar as compras por impulso?",
                "alternativas": [
                    {"texto": "Porque os cartões de crédito são mais seguros que o dinheiro.", "correta": False},
                    {"texto": "Porque os cartões de crédito são mais práticos.", "correta": False},
                    {"texto": "Porque os cartões de crédito dão a sensação de que o dinheiro não é real.", "correta": True},
                    {"texto": "Porque os cartões de crédito oferecem mais descontos.", "correta": False},
                ],
            },
                {
                "pergunta": "O que acontece quando tratamos desejos como necessidades?",
                "alternativas": [
                    {"texto": "Podemos ter problemas financeiros.", "correta": True},
                    {"texto": "Temos uma vida mais feliz.", "correta": False},
                    {"texto": "Conseguimos realizar todos os nossos sonhos.", "correta": False},
                    {"texto": "Nada de ruim acontece.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a importância de planejar para realizar nossos desejos?",
                "alternativas": [
                    {"texto": "Para evitar qualquer tipo de frustração.", "correta": False},
                    {"texto": "Para ter mais tempo livre.", "correta": False},
                    {"texto": "Para gastar mais dinheiro.", "correta": False},
                    {"texto": "Para transformar nossos sonhos em realidade.", "correta": True},
                ],
            },
                {
                "pergunta": "Por que é importante registrar os gastos?",
                "alternativas": [
                    {"texto": "Para gastar mais dinheiro.", "correta": False},
                    {"texto": "Para saber para onde o dinheiro está indo e identificar oportunidades de economia.", "correta": True},
                    {"texto": "Para saber se é possível comprar algo que você deseja.", "correta": False},
                    {"texto": "Para impressionar os amigos.", "correta": False},
                ],
            },
                {
                "pergunta": "O que significa ter um superávit no fluxo de caixa?",
                "alternativas": [
                    {"texto": "Gastar mais do que ganha.", "correta": False},
                    {"texto": "Gastar exatamente o que ganha.", "correta": False},
                    {"texto": "Gastar menos do que ganha.", "correta": True},
                    {"texto": "Não ter nenhuma dívida.", "correta": False},
                ],
            },
            {
                "pergunta": "Qual a importância de se preparar antes de negociar uma dívida?",
                "alternativas": [
                    {"texto": "Não é necessário se preparar, basta ligar para o credor.", "correta": False},
                    {"texto": "É importante ter todos os documentos em mãos e um plano de pagamento.", "correta": True},
                    {"texto": "É suficiente saber o valor da dívida.", "correta": False},
                    {"texto": "Para saber se você precisa realmente pagar a dívida agora.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual o risco de não cumprir com as condições de um acordo de negociação?",
                "alternativas": [
                    {"texto": "Perder os benefícios obtidos na negociação.", "correta": True},
                    {"texto": "Não ter mais problemas financeiros.", "correta": False},
                    {"texto": "Aumentar o valor da dívida.", "correta": False},
                    {"texto": "Gerar juros aplicados na mesma dívida.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual o principal benefício de controlar suas despesas?",
                "alternativas": [
                    {"texto": "Evitar o endividamento e alcançar a estabilidade financeira.", "correta": True},
                    {"texto": "Ter mais dinheiro para comprar o que deseja", "correta": False},
                    {"texto": "Gastar menos com coisas bobas", "correta": False},
                    {"texto": "Não ter dívidas", "correta": False},
                ],
            },
                {
                "pergunta": "O que significa ter um orçamento?",
                "alternativas": [
                    {"texto": "Gastar todo o dinheiro disponível.", "correta": False},
                    {"texto": "Planejar seus gastos e receitas.", "correta": True},
                    {"texto": "Não se contentar em ter pouco dinheiro.", "correta": False},
                    {"texto": "Ter ações valorizadas.", "correta": False},
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

    def subcapitulo3_1():
        criar_subcapitulo(
            "Conhecendo seu\nperfil de gastos:\nonde seu dinheiro vai?",
            """
Nem chegou o fim do mês e já falta dinheiro para pagar as contas? Precisa se endividar para honrar os compromissos? Não tem recursos para quitar a fatura do cartão? Mais um mês sem conseguir poupar? 
 
Essas situações são mais comuns do que se imagina, e representam um cenário muito danoso para a vida financeira: gastar mais do que se ganha. O descontrole financeiro, além de causar diretamente estresse financeiro, mina a capacidade de construção de reservas financeiras, necessárias para a tranquilidade financeira e para o alcance dos objetivos de vida.  

Não há controle financeiro sem conhecimento. Quanto foram os gastos com as compras de mercado neste mês? Poucos têm a resposta exata. Alguns arriscam um número, mas ao comparar com a realidade, se surpreendem. E isso acontece com as outras categorias de despesas. Conhecer o destino do dinheiro é etapa fundamental para adquirir o controle financeiro.  

A sugestão aqui é registrar periodicamente os seus ganhos e despesas. Idealmente os registros devem ocorrer diariamente, e devem ser acompanhados pelo menos uma vez ao mês. Como? Tanto faz, seja um caderno, uma planilha ou aplicativo (caso queira, utilize esta planilha modelo). Essa ferramenta é conhecida como Fluxo de caixa pessoal ou familiar (FCF).  

O importante é definir as principais categorias de renda e despesas da família, como moradia, alimentação, transporte, saúde, educação, lazer e entretenimento, entre outros, e começar a anotar tudo. 

Ao final do primeiro período de apuração, normalmente um mês, os resultados podem identificar três diferentes perfis de gasto: 
Superavitário: gasta menos do que ganha. PARABÉNS! este é o cenário ideal. Quem está aqui, além de possivelmente não passar por estresse financeiro, ainda consegue poupar; 
Deficitário: gasta mais do que ganha. CUIDADO! Este é o pior cenário. Quem está aqui possivelmente passa por constantes situações de estresse financeiro, não poupa, e tende a se tornar endividado. 
Equilibrado: gasta exatamente o que ganha. ATENÇÃO! Apesar de aparentemente tranquilo, este não é o cenário ideal. Quem está aqui não consegue construir reservas financeiras e fica perto de se tornar deficitário, afinal qualquer despesa adicional pode desequilibrar as contas.  

A identificação dos perfis de gasto, no entanto, não é o único benefício do registro das despesas. Ao conhecer para onde o dinheiro está indo é possível apontar os principais vilões do FCF, e identificar as possíveis causas de um descontrole, por onde a mudança de comportamento poderia começar.   
            """
        )

    def subcapitulo3_2():
        criar_subcapitulo(
            "A importância de\nregistrar todas as\nsuas despesas para\nreduzir gastos",
            """
A importância do controle de despesas pessoais é fundamental para alcançar uma vida financeira saudável e equilibrada.

Quando se trata de gerenciar e controlar gastos pessoais, estabelecer um orçamento e registrar despesas de forma eficiente são práticas essenciais. Neste artigo, discutiremos a importância desses aspectos e forneceremos dicas úteis para ajudá-lo a administrar suas finanças de maneira eficaz.

Um controle efetivo de despesas pessoais é crucial por vários motivos. Em primeiro lugar, permite que você tenha uma visão clara de como está gastando seu dinheiro e ajuda a identificar áreas em que é possível economizar. Ao registrar todas as suas despesas, você terá uma noção precisa de para onde está indo seu dinheiro e poderá avaliar se está gastando de forma consciente ou se há espaço para reduzir gastos desnecessários.

Além disso, o controle de despesas pessoais é fundamental para evitar o endividamento e o acúmulo de dívidas. Quando você sabe exatamente quanto dinheiro tem disponível e para onde está indo, fica mais fácil tomar decisões financeiras responsáveis e evitar gastos impulsivos que possam comprometer sua estabilidade financeira. Ter um orçamento bem estruturado também permite que você planeje suas despesas futuras e esteja preparado para imprevistos, como emergências médicas ou reparos em casa.

Lembre-se de que o controle de despesas pessoais não se trata de privação, mas de tomar decisões conscientes e equilibradas sobre como usar seu dinheiro. Ao estabelecer um orçamento, registrar suas despesas e seguir as dicas mencionadas, você estará no caminho certo para uma vida financeira saudável e estável.

Ao longo do tempo, o controle de despesas pessoais pode trazer uma série de benefícios significativos para sua vida financeira. 

Lembre-se de que o controle de despesas pessoais é um processo contínuo. É importante revisar e ajustar seu orçamento regularmente à medida que suas circunstâncias e objetivos financeiros mudam. 

Com o tempo, você ganhará mais confiança e habilidade para administrar suas finanças de forma eficiente, o que o ajudará a alcançar uma vida financeira estável e próspera.
            """
        )

    def subcapitulo3_3():
        criar_subcapitulo(
            "Como lidar com gastos impulsivos",
            """
Desde promoções e descontos irresistíveis até apelos emocionais: quando percebemos, já estamos fazendo compras por impulso.

Esse hábito se caracteriza por compras feitas sem planejamento, motivadas por desejos momentâneos e emoções, em vez de uma real necessidade. Muitas vezes, é marcado pela tomada de decisão rápida, sem considerar consequências futuras.

Para alguns parece inofensivo, mas o alívio momentâneo obtido após a compra é seguido por arrependimento e culpa. Além disso, pode gerar sérios problemas financeiros.

Separamos algumas dicas para te lidas com esses gastos impulsivos: 
- O primeiro passo é ter um planejamento financeiro sólido. Essa visão geral de sua situação financeira ajudará a identificar oportunidades de corte de gastos e a definir prioridades.
- Antes de qualquer compra, faça uma pausa e reflita sobre a real necessidade do produto ou serviço. Essa prática de “espera” pode ajudar a evitar compras impulsivas.
- O uso excessivo de cartões de crédito facilita as compras por impulso, pois cria a ilusão de que não estamos gastando dinheiro, procure deixar o cartão em casa sempre que possível e acompanhar de perto as faturas e limitar o parcelamento.
            """
        )

    def subcapitulo3_4():
        criar_subcapitulo(
            "A diferença entre\nnecessidade e\nde comprar",
            """
Ao fazer escolhas, é importante saber distinguir DESEJO de NECESSIDADE.
Pode-se definir necessidade como tudo aquilo de que precisamos, independentemente de nossos anseios. São coisas indispensáveis para a vida. Por sua vez, os desejos podem ser definidos como tudo aquilo que queremos possuir ou usufruir, sendo essas coisas necessárias ou não.
Vamos exemplificar: a alimentação é indispensável para a vida e independe da nossa vontade. Logo, é uma NECESSIDADE. Agora, caso você queira fazer sua alimentação em um restaurante de luxo desfrutando de pratos finos, isso é um DESEJO. Sim, você está satisfazendo sua necessidade de alimento, mas a forma como almejou satisfazer tal necessidade foi um desejo.

Nossos recursos financeiros devem satisfazer nossas necessidades, mas, na medida do possível, podemos atender nossos desejos. Os desejos não são ruins. Eles nos dão prazer e determinam aquilo que queremos para o futuro.

O problema surge quando começamos a tratar os desejos como se fossem necessidades. Pensar assim pode nos colocar em uma situação de difícil controle, já que os desejos são ilimitados, mas os recursos são limitados. Ao tratarmos desejos como necessidades, podemos afetar nossa saúde financeira e dar início a um processo de endividamento excessivo.

Procure ter em mente que o dinheiro é um mero instrumento para atender a necessidades e desejos, realizando sonhos. Por isso, você deve administrá-lo bem.

Para transformar seus sonhos em realidade, não fique apenas no plano das ideias. Converta seus sonhos em projetos, planejando como alcançá-los. Procure basear suas escolhas equilibradamente nas emoções e na razão. Saiba identificar suas necessidades e desejos, pesando os custos e as recompensas da troca intertemporal.
Tendo esses ensinamentos em mente e colocando-os em prática, você estará criando uma sólida base para erguer uma vida financeira pessoal saudável.
            """
        )

    def subcapitulo3_5():
        criar_subcapitulo(
            "Negociando dívidas\ne obtendo\nmelhores condições",
            """
A negociação de dívidas pode ser bastante útil para quem de fato deseja quitá-las. Isso porque elas costumam proporcionar redução de juros, multas e até mesmo o perdão de parte da dívida.

Para saber como fazer a negociação de dívidas e limpar o nome do SPC e Serasa da melhor forma, confira abaixo o passo a passo e conheça as melhores dicas para conseguir um bom acordo:

1. A primeira dica é separar algum tempo para entender todos os detalhes e aspectos da respectiva dívida. Se organize, separe todos os documentos, reúna o seu orçamento pessoal e coloque no papel toda a situação.

2.Com a ajuda de uma calculadora, tente pensar na melhor saída para pagar a dívida, com base na sua capacidade financeira.
Formule pelo menos duas propostas diferentes para quitar o débito, e registre isso detalhadamente para usar durante a negociação.

3. Dependendo da dívida, ela só pode ser negociada pessoalmente. Ainda assim, nas opções onde é possível fazer este acordo por telefone, é preciso tempo e planejamento. Muitas vezes, até uma hora precisa ser empregada nesta missão.

4. Após entrar em contato e expor sua situação, provavelmente o credor irá fazer uma proposta para quitar a dívida. Porém, logo ouvir proposta do credor, vale fazer uma contraproposta — mesmo que a opção sugerida seja boa e caiba no seu orçamento.

5. Dificilmente será oferecida uma redução total de juros, multa e ainda um abate de 50% da dívida original, por exemplo.
Por isso, é preciso manter os pés no chão neste sentido. Afinal, trata-se da negociação de dívidas, não do seu perdão.

6. Pressupõe-se que, ao negociar sua dívida, o devedor tem a real intenção de pagá-la. Por isso, assumir parcelas de uma negociação e não quitá-las não é uma boa ideia. Isso porque, ao não arcar com o que foi acordado, perde-se todos os benefícios obtidos na negociação. Logo, só feche a negociação se tiver certeza que a dívida pode ser paga.
            """
        )

    def subcapitulo3_quiz():
            criar_quiz()

    def subcapitulo3_desafio():
        criar_subcapitulo(
            "Desafio",
            """
Parabéns por chegar até aqui, futuro mestre do controle financeiro! 

Chegou o momento de aplicar tudo o que você aprendeu no capítulo "Conhecendo seu perfil de gastos: onde seu dinheiro vai?". Vamos encarar a realidade dos números e trabalhar na construção de hábitos mais saudáveis para suas finanças.

Desafio: Registre e Analise Seus Gastos

Registre suas finanças por um mês:

Escolha uma ferramenta (caderno, planilha ou aplicativo) e anote diariamente todas as suas despesas e receitas, por menores que sejam.
Classifique os gastos em categorias como alimentação, transporte, lazer, contas fixas, etc.
            
Analise seus resultados:

Ao final do mês, identifique qual é o seu perfil de gasto:
Superavitário: Sobrou dinheiro? Parabéns! Avalie como investir esse excedente.
Equilibrado: Gasta exatamente o que ganha? Atenção! Pequenos imprevistos podem desestabilizar suas finanças.
Deficitário: Gastou mais do que ganhou? Cuidado! Hora de ajustar suas prioridades e cortar excessos.
            
Identifique os vilões:
Localize as categorias em que você gastou mais do que o esperado. São supérfluos? Gastos impulsivos? Necessidades?
            
Plano de ação:

Baseado em sua análise, defina uma estratégia para melhorar sua gestão financeira no próximo mês. Por exemplo:
Reduzir gastos não essenciais.
Estabelecer um valor fixo para poupar.
Pergunta Reflexiva: Depois de completar seu fluxo de caixa e analisar seus resultados, quais mudanças você acha que pode implementar para alcançar um perfil superavitário?

Lembre-se: o primeiro passo para controlar suas finanças é conhecer para onde vai seu dinheiro. Você está no caminho certo!
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
            criar_bloco("Conhecendo seu perfil de gastos: onde seu dinheiro vai?", lambda _: subcapitulo3_1()),
            criar_bloco("A importância de registrar todas as suas despesas para reduzir gastos", lambda _: subcapitulo3_2()),
            criar_bloco("Como lidar com gastos impulsivos", lambda _: subcapitulo3_3()),
            criar_bloco("A diferença entre necessidade e desejo de comprar", lambda _: subcapitulo3_4()),
            criar_bloco("Negociando dívidas e obtendo melhores condições", lambda _: subcapitulo3_5()),
            criar_bloco("Quiz", lambda _: subcapitulo3_quiz()),
            criar_bloco("Desafio", lambda _: subcapitulo3_desafio()),
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
