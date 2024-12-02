import flet as ft

def Capitulo4Page(page: ft.Page):
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
                "pergunta": "",
                "alternativas": [
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": True},
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": False},
                ],
            },
            {
                "pergunta": "",
                "alternativas": [
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": True},
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": False},
                ],
            },
                {
                "pergunta": "",
                "alternativas": [
                    {"texto": "", "correta": True},
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": False},
                ],
            },
                {
                "pergunta": "",
                "alternativas": [
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": True},
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": False},
                ],
            },
                {
                "pergunta": "",
                "alternativas": [
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": True},
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": False},
                ],
            },
                {
                "pergunta": "",
                "alternativas": [
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": True},
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": False},
                ],
            },
            {
                "pergunta": "",
                "alternativas": [
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": True},
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": False},
                ],
            },
                {
                "pergunta": "",
                "alternativas": [
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": True},
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": False},
                ],
            },
                {
                "pergunta": "",
                "alternativas": [
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": True},
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": False},
                ],
            },
                {
                "pergunta": "",
                "alternativas": [
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": True},
                    {"texto": "", "correta": False},
                    {"texto": "", "correta": False},
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

    def subcapitulo4_1():
        criar_subcapitulo(
            "A importância de construir uma reserva de emergência",
            """
            A reserva de emergência é um valor que você mantém separado exclusivamente para lidar com imprevistos.
Esse dinheiro é destinado para cobrir despesas inesperadas que podem surgir a qualquer momento — como um problema de saúde, reparos urgentes na casa, conserto do carro ou até mesmo a perda de um emprego.

A principal função da reserva para emergência é proporcionar segurança financeira, evitando que você precise recorrer a empréstimos ou créditos em situações de crise.

Ao ter essa quantia guardada, você pode enfrentar os desafios financeiros com mais tranquilidade, sabendo que tem um suporte para situações que fogem do seu controle.

Para começar a calcular sua reserva de emergência, você precisa saber exatamente quais são suas despesas mensais essenciais.

Faça uma lista detalhada de todas as suas despesas fixas e variáveis e inclua tudo o que é necessário para a sua manutenção e da sua família.

Após listar, some os valores para descobrir o total das suas despesas mensais e multiplique esse valor pelos meses desejados.

O ideal é que a reserva cubra de três a seis meses de despesas, pois assim você terá dinheiro para se manter sem nenhuma entrada nesse período.

Então, por exemplo, se suas despesas mensais são de R$3.000 e você deseja criar uma reserva para seis meses, deve ter R$18.000 guardados.

A importância de uma reserva de emergência vai além das finanças. De acordo com uma pesquisa realizada em março de 2024 pelo SPC Brasil e a Confederação Nacional de Dirigentes Lojistas (CNDL), 82% dos inadimplentes sofreram impacto na saúde física ou mental devido às dívidas em atraso.

Alterações no sono (66%) e no apetite (51%), além da ansiedade descontada em vícios como cigarro e álcool (37%), são algumas das consequências relatadas.

A inadimplência não afeta apenas a saúde, mas também o padrão de vida. O levantamento aponta que 88% dos inadimplentes relataram mudanças significativas em seus estilos de vida devido às dívidas.

Além disso, 66% dos entrevistados indicaram um nível de preocupação alto ou muito alto com suas dívidas, refletindo um estado constante de ansiedade e estresse.
Com uma reserva, você tem mais liberdade e tranquilidade para tomar decisões financeiras sem pressa. Você pode, por exemplo, recusar uma oferta de emprego inadequada e esperar por uma melhor — já que não está pressionado pela falta de dinheiro.

Saber que você tem um fundo para emergências proporciona paz de espírito e tranquilidade, o que reduz o estresse e a ansiedade em relação às finanças, permitindo que você se concentre melhor em suas atividades diárias e planejamento de longo prazo.
O estudo também mostrou que as dívidas em atraso também podem impactar a produtividade no trabalho e as relações sociais.

Mais da metade dos inadimplentes (56%) relataram que as dívidas afetaram suas relações sociais, e 57% indicaram que a inadimplência influenciou negativamente sua produtividade no trabalho.
Portanto, construir e manter uma reserva de emergência não só fortalece sua saúde financeira, mas também contribui para seu bem-estar geral, evitando os impactos negativos que a falta de uma rede de segurança pode causar.
            """
        )

    def subcapitulo4_2():
        criar_subcapitulo(
            "Diferentes tipos de investimentos: qual o melhor para você?",
            """
            Ações:
Para investir com visão, você precisa de uma perspectiva de mercado de alta convicção. Desenvolvemos a nossa com informações filtradas por nossa equipe de estrategistas, economistas e profissionais de trade e de derivativos do mundo todo. E com isso, trabalhamos com você para decidir quais ideias são indicadas para você.

Investimentos alternativos:
Investir em fundos hedge, capital privado (private equity), crédito privado e fundos imobiliários pode ser um complemento de longo prazo atraente para uma alocação em ações/títulos de renda fixa públicos tradicionais.

Renda fixa:
Nossos estrategistas de mercados de títulos de renda fixa, profissionais de trade e analistas de crédito trabalham com vários mercados para encontrar a combinação perfeita para você. O objetivo pode ser identificar as melhores escolhas para o seu portfólio de longo prazo, buscando renda ou estabilidade.

Investimentos sustentáveis:
Acreditamos no poder do investimento sustentável para gerar crescimento de longo prazo e impacto positivo. O investimento sustentável é uma forma de ajudar você a investir com intenção para atingir seus objetivos e o futuro que você vislumbra.
            """
        )

    def subcapitulo4_3():
        criar_subcapitulo(
            "Entendendo os riscos e retornos dos investimentos",
            """
            O que é a relação risco e retorno?

A relação entre risco e retorno é um conceito central no mercado financeiro. Ele representa a correlação direta entre a exposição frente às incertezas do mercado e a possibilidade de ganhos mais elevados.

Nesse relação, de um lado há o risco, definido pela volatilidade e a probabilidade de perda do capital investido. Já do outro lado, observa-se o potencial ganho de capital que se espera obter.

Em um investimento, quanto maior o risco existente, mais elevada tende a ser a remuneração proposta. Isso acontece para que o ativo seja atrativo, compensando a possibilidade de perdas que o investidor precisará suportar ao se expor àquela alternativa.

Afinal, se todos os ativos do mercado oferecessem a mesma remuneração, não haveria razões para escolher aqueles mais arriscados. Nesse contexto, se estabelece a ideia de relacionar os dois fatores para que o investidor possa verificar se o retorno esperado é compatível com o nível de risco assumido.

É comum investidores inexperientes cometerem o erro de considerar apenas o potencial de retorno ao escolher uma alternativa. Por exemplo, investir em ações de empresas traz a possibilidade de multiplicar o seu capital, caso os papéis escolhidos valorizem.

No entanto, uma das principais características do mercado acionário é a sua volatilidade — embasada, entre outros fatores, na lei da oferta e demanda. Então, de fato, há chances de ter ganhos expressivos com as ações, mas as chances de enfrentar prejuízos também são mais elevadas.

Ao analisar as possibilidades de perdas e o potencial de ganhos da alternativa, você identifica os fatores que podem impactar negativamente sua carteira. Da mesma forma, a avaliação permite determinar as chances de um investimento gerar lucros e até mesmo superar um índice de referência (benchmark).
Investidores que dominam essa relação conseguem gerenciar melhor suas expectativas quanto ao investimento. 

Adicionalmente, eles conseguem escolher alternativas que se alinham não só com suas metas financeiras, mas também com sua tolerância ao risco. 

Isso evita escolhas que podem levar a perdas expressivas, inclusive de custo de oportunidade — no caso de uma alocação que não traz os resultados esperados ao investidor, por exemplo

O indicador financeiro costuma calcular quanto o investidor ganhou ou perdeu em relação ao montante alocado — mas pode ser adaptado a partir de projeções de retorno.

O seu cálculo envolve subtrair do ganho obtido o valor investido. Em seguida, divide-se o resultado pelo valor investido, multiplicando por 100 para se obter um resultado em porcentagem.

A fórmula fica assim:
ROI = [(Ganho obtido – Valor investido) / Valor investido] x 100
Suponha que você está comparando dois fundos de investimento. As cotas do fundo A foram compradas por R$ 10.000 e, após um ano, estão valendo R$ 12.000. Já as cotas do fundo B foram adquiridas por R$ 5.000 e atualmente estão precificadas a R$ 6.500. 

Calculando o ROI de cada um, você encontrará um retorno de 20% para as cotas do fundo A e de 30% para as cotas do fundo B. Dessa forma, é possível avaliar qual delas teve o melhor desempenho e comparar os resultados considerando o nível de risco oferecido em cada veículo.

Vale dizer que o ROI também pode ser negativo, o que revelaria que o investimento gerou prejuízo no período. Logo, a análise do indicador ajuda a tomar decisões informadas, comparar diferentes alternativas e otimizar estratégias para maximizar os retornos.

Outra prática relevante para essa análise é o uso do índice de Sharpe. Ele é um pouco mais complexo, considerando o retorno do investimento analisado, a taxa livre de risco (como a Selic) e a volatilidade do ativo avaliado para compreender se a relação entre risco e retorno é atrativa.
            """
        )

    def subcapitulo4_4():
        criar_subcapitulo(
            "Planejamento financeiro a longo prazo: aposentadoria e outros objetivos",
            """
            É crucial para garantir uma velhice tranquila e confortável, colocar a aposentadoria como prioridade. Muitas vezes, as pessoas adiam o planejamento financeiro para a aposentadoria, priorizando outras despesas e objetivos de curto prazo. 
No entanto, reservar tempo e recursos para planejar o futuro financeiro é essencial. Isso pode envolver cortar gastos supérfluos, reduzir despesas fixas, aumentar a receita por meio de atividades complementares, como trabalhos freelancer, negociar dívidas para reduzir os encargos financeiros e fazer investimentos inteligentes que garantam retornos satisfatórios a longo prazo.
 
Ao tornar a aposentadoria uma prioridade e adotar medidas concretas para alcançar os objetivos financeiros estabelecidos, os indivíduos podem estar mais preparados para enfrentar os desafios e as incertezas do futuro, assegurando uma aposentadoria mais confortável e estável.

Um passo fundamental no planejamento financeiro: Definir o estilo de vida desejado na aposentadoria. Ter clareza sobre as metas e os objetivos para essa fase da vida ajuda a direcionar os esforços e os recursos financeiros de forma mais eficaz. 
Seja viver em uma praia tranquila desfrutando da natureza e do sossego ou viajar pelo mundo explorando novas culturas e paisagens, entender essas preferências e aspirações é essencial para criar um plano financeiro que assegure a realização desses sonhos. 

Ao definir o estilo de vida desejado, os indivíduos podem tomar decisões mais conscientes em relação aos gastos, investimentos e estratégias de poupança, alinhando suas escolhas financeiras com suas expectativas e prioridades para a aposentadoria.

Poupar regularmente e diversificar os investimentos são práticas essenciais para garantir uma aposentadoria confortável e segura. Além de contribuir para o INSS, reservar uma parte do orçamento mensal para poupança e investimento é fundamental para acumular recursos ao longo do tempo. 

Ao diversificar os investimentos, distribuindo os recursos entre diferentes classes de ativos, como ações, títulos, fundos de investimento e imóveis, os indivíduos podem reduzir os riscos e maximizar os retornos de seus investimentos. 

É importante também considerar o perfil de investidor de cada um ao escolher as aplicações financeiras mais adequadas, buscando opções alinhadas com seus objetivos, tolerância ao risco e horizonte de investimento. 
Essa abordagem ajuda a proteger o patrimônio contra flutuações do mercado e a construir uma base sólida para uma aposentadoria tranquila e confortável.
            """
        )

    def subcapitulo4_5():
        criar_subcapitulo(
            "Impostos sobre investimentos: o que você precisa saber",
            """
            Os investimentos no mercado financeiro têm dois grandes custos principais:

 impostos e taxas.

 Os impostos são cobrados pelo governo e variam de investimento para investimento. Já no caso das taxas, elas são cobradas pelas instituições (bancos, corretoras e distribuidoras de títulos e valores mobiliários) e variam de uma para a outra.
Em ambos os casos, é importante saber quais são as cobranças que podem existir, até para comparar os custos e fazer uma escolha que ajude seu dinheiro a render mais. 

Conheça a seguir os principais impostos e taxas:

Principais impostos
O Imposto Sobre Operação Financeira (IOF) e o Imposto de Renda (IR) são os principais impostos que incidem sobre os investimentos financeiros. Em ambos os casos, a cobrança do imposto se dá sempre sobre o rendimento e não sobre o capital investido. Ou seja, caso você não tenha rendimento na sua aplicação, não haverá cobrança nem de IR, nem de IOF. 

Confira a seguir como funciona a tributação em cada caso.

Imposto de renda (IR)

A cobrança do IR varia conforme o investimento que você fizer. No site do Ministério da Fazenda, você pode encontrar mais informações sobre a tributação do IR para pessoa física. A seguir, temos um resumo das regras gerais para esse tributo.
 
REGRAS GERAIS
Tipo de produto e Tributação no resgate:

 Renda Fixa:
22,5% para aplicações com prazo de até 180 dias;
20% para aplicações com prazo de 181 até 360 dias;
17,5% para aplicações com prazo de 361 até 720 dias;
15% para aplicações com prazo acima de 720 dias;

Fundos de Renda Fixa, Cambial e MultimercadoFundos classificados como de Longo Prazo pela CVM:
22,5% para aplicações com prazo de até 180 dias;
20% para aplicações com prazo de 181 até 360 dias;
17,5% para aplicações com prazo de 361 até 720 dias;
15% para aplicações com prazo acima de 720 dias;
 
Fundos de classificados como de Curto Prazo pela CVM:
22,5% para aplicações com prazo de até 180 dias;
20% para aplicações com prazo de mais de 180 dias;

TRIBUTAÇÃO SEMESTRAL: a cada seis meses (maio e novembro), uma tributação antecipada é cobrada, a conhecida “come-cotas”.  O valor incide em 15% para fundos de longo prazo e 20% para aqueles de curto prazo. No resgate, você pagará apenas a diferença do valor do imposto devido, ainda não cobrado.

Fundos de Ações
15%

Renda VariávelOperações de Day Trade (resgate no mesmo dia da compra):
20% sobre ganhos.
 
Outras operações:
15% sobre ganhos.
 
Imposto sobre operação financeira (IOF):
A cobrança do imposto segue a tabela regressiva de 96% a 3%, em caso de resgate em menos de 30 dias de aplicação. E a cobrança se dá dessa forma mesmo. Se sacar seu investimento no primeiro dia, paga 96% do rendimento de IOF; se sacar no segundo dia, 93%; no terceiro dia, 90%; e assim sucessivamente ate o 29º dia, quando você paga 3% de IOF sobre o rendimento e depois disso não há mais a cobrança de IOF.

Principais taxas:

Na hora de decidir qual instituição escolher, um fator decisivo pode ser o valor das taxas cobradas. Este é um ponto que você deve pesquisar com atenção, pois, ao longo do tempo, a economia em taxas pode fazer seu dinheiro render muito mais. Confira a seguir as principais taxas que podem ser cobradas pelas instituições financeiras:
Taxa de administração: cobrada pelo serviço de administração do seu investimento.
Taxa de custódia: cobrada pelo serviço de guarda do seu dinheiro.
Taxa de corretagem: cobrada pelo serviço de compra e venda de ações.
Comissões: uma proporção do seu rendimento, cobrada pelo serviço de gestão do seu investimento.
Taxa de carregamento: cobrada sobre o valor de cada depósito realizado no investimento.

Pesquise e compare as taxas cobradas! Escolha sempre aquela instituição que te oferecer o melhor serviço, pelo melhor preço.
            """
        )

    def subcapitulo4_quiz():
            criar_quiz()

    def subcapitulo4_desafio():
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
            criar_bloco("A importância de construir uma reserva de emergência", lambda _: subcapitulo4_1()),
            criar_bloco("Diferentes tipos de investimentos: qual o melhor para você?", lambda _: subcapitulo4_2()),
            criar_bloco("Entendendo os riscos e retornos dos investimentos", lambda _: subcapitulo4_3()),
            criar_bloco("Planejamento financeiro a longo prazo: aposentadoria e outros objetivos", lambda _: subcapitulo4_4()),
            criar_bloco("Impostos sobre investimentos: o que você precisa saber", lambda _: subcapitulo4_5()),
            criar_bloco("Quiz", lambda _: subcapitulo4_quiz()),
            criar_bloco("Desafio", lambda _: subcapitulo4_desafio()),
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
