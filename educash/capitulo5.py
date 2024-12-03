import flet as ft

def Capitulo5Page(page: ft.Page):
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
                "pergunta": "Qual das opções abaixo apresenta o tipo de crédito com menor risco para a instituição financeira?",
                "alternativas": [
                    {"texto": "Empréstimo consignado", "correta": True},
                    {"texto": "Cartão de crédito", "correta": False},
                    {"texto": "Financiamento", "correta": False},
                    {"texto": "Cheque especial", "correta": False},
                ],
            },
                {
                "pergunta": "Qual é o principal fator a ser considerado ao escolher um cartão de crédito, de acordo com o texto?",
                "alternativas": [
                    {"texto": "O programa de fidelidade mais vantajoso.", "correta": False},
                    {"texto": "A anuidade mais baixa.", "correta": False},
                    {"texto": "A bandeira do cartão.", "correta": False},
                    {"texto": "O perfil de uso do consumidor.", "correta": True},
                ],
            },
                {
                "pergunta": "Qual a importância do score de crédito na hora de solicitar um cartão de crédito?",
                "alternativas": [
                    {"texto": "O score não influencia na aprovação do cartão.", "correta": False},
                    {"texto": "Um score baixo garante a aprovação em qualquer cartão.", "correta": False},
                    {"texto": "Um bom score aumenta as chances de aprovação em cartões com melhores benefícios.", "correta": True},
                    {"texto": "O score só é importante para cartões com anuidade.", "correta": False},
                ],
            },
               {
                "pergunta": "Qual a principal diferença entre um financiamento e um crédito pessoal?",
                "alternativas": [
                    {"texto": "O financiamento tem juros mais baixos, mas somente para empresas e o crédito tem juros mais altos.", "correta": False},
                    {"texto": "O financiamento é mais fácil de conseguir e é somente para quem tem CNPJ, o crédito pessoal é mais difícil mas é para todos.", "correta": False},
                    {"texto": "O financiamento é utilizado para bens específicos, enquanto o crédito pessoal pode ser utilizado para qualquer finalidade.", "correta": True},
                    {"texto": "O financiamento não exige análise de crédito.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a principal diferença entre poupar e investir, e por que ambas as ações são importantes para a saúde financeira de longo prazo?",
                "alternativas": [
                    {"texto": "Poupar é guardar dinheiro em conta corrente, enquanto investir é aplicar em ações. A principal diferença é a rentabilidade.", "correta": False},
                    {"texto": "Poupar é guardar dinheiro para despesas futuras, enquanto investir é aplicar esse dinheiro para que ele gere mais dinheiro. Ambas são importantes para alcançar a liberdade financeira.", "correta": True},
                    {"texto": "Poupar e investir são sinônimos. Ambos visam aumentar o patrimônio.", "correta": False},
                    {"texto": "Poupar é para pessoas com baixa renda, e investir é para pessoas com alta renda.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a importância do orçamento pessoal no processo de planejamento financeiro, e como ele pode ajudar a alcançar as metas financeiras?",
                "alternativas": [
                    {"texto": "O orçamento pessoal serve apenas para controlar os gastos, não sendo relevante para o planejamento de longo prazo.", "correta": False},
                    {"texto": "O orçamento pessoal é um instrumento fundamental para controlar os gastos, identificar prioridades e alcançar metas financeiras.", "correta": True},
                    {"texto": "O orçamento pessoal é importante apenas para pessoas com dívidas.", "correta": False},
                    {"texto": "O orçamento pessoal é uma ferramenta complexa e difícil de ser utilizada por pessoas que não possuem conhecimento em finanças.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual das seguintes estratégias NÃO é recomendada para alguém que busca sair das dívidas e construir um futuro financeiro mais sólido?",
                "alternativas": [
                    {"texto": "Utilizar o cartão de crédito para compras do dia a dia, pagando apenas o valor mínimo da fatura.", "correta": True},
                    {"texto": "Aumentar a renda familiar através de trabalhos extras.", "correta": False},
                    {"texto": "Priorizar o pagamento das dívidas com juros mais altos.", "correta": False},
                    {"texto": "Consolidar todas as dívidas em um único crédito com juros menores.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a importância de criar um fundo de emergência, mesmo durante o processo de pagamento de dívidas?",
                "alternativas": [
                    {"texto": "Um fundo de emergência não é necessário enquanto houver dívidas a serem pagas.", "correta": False},
                    {"texto": "Um fundo de emergência evita que novas dívidas sejam contraídas ao lidar com imprevistos.", "correta": True},
                    {"texto": "Um fundo de emergência serve apenas para realizar grandes compras, como um carro novo.", "correta": False},
                    {"texto": "Um fundo de emergência é apenas para pessoas com alta renda.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual das alternativas abaixo melhor explica a relação entre o score de crédito e as taxas de juros cobradas em um empréstimo?",
                "alternativas": [
                    {"texto": "Um score alto garante taxas de juros zero em qualquer tipo de empréstimo.", "correta": False},
                    {"texto": "O score de crédito não influencia nas taxas de juros, pois estas são definidas pela taxa Selic.", "correta": False},
                    {"texto": "Somente pessoas com score acima de 800 têm acesso a taxas de juros competitivas.", "correta": False},
                    {"texto": "Um score baixo indica um perfil de risco maior para as instituições financeiras, o que pode resultar em taxas de juros mais altas.", "correta": True},
                ],
            },
                {
                "pergunta": "Qual das seguintes ações NÃO contribui para a melhoria do score de crédito?",
                "alternativas": [
                    {"texto": "Pagar todas as contas em dia.", "correta": False},
                    {"texto": "Solicitar diversos cartões de crédito ao mesmo tempo.", "correta": True},
                    {"texto": "Manter um bom histórico de pagamentos de cartão de crédito.", "correta": False},
                    {"texto": "Regularizar dívidas negativadas.", "correta": False},
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

    def subcapitulo5_1():
        criar_subcapitulo(
            "Tipos de crédito\ne suas\ncaracterísticas",
            """
Os 6 principais tipos de crédito:

1. Cartão de crédito: 
O cartão de crédito é uma forma de empréstimo fixo. O cliente possui um limite liberado para usar da forma que quiser. Ao final de cada mês, ele paga a fatura com o valor que usou desse limite.
Apesar de trazer facilidade para os usuários, especialmente pela possibilidade de parcelar as compras, o cartão de crédito precisa ser usado com responsabilidade. 

2. Financiamento
O financiamento é um tipo de crédito de longo prazo e alto valor. Sua principal característica é que o dinheiro tem um objetivo de uso, como comprar um carro ou um imóvel. Nesse caso, o usuário paga em parcelas mensais e, costuma, ficar mais de 1 ano com essa dívida. O bem comprado é usado como garantia caso a dívida não seja quitada. O pagamento de um financiamento envolve o acréscimo de juros. Portanto, antes de fechar um contrato, lembre-se de calcular o valor total da dívida.

3. Cheque especial
O cheque especial é um tipo de crédito liberado automaticamente na conta do usuário. Assim como existe um limite no cartão de crédito, a conta também pode ser usada “além” do saldo disponível. Só que ao usar o cheque especial, você paga juros mais caros do mercado!Por isso, só use quando não tiver opção.

4. Crédito pessoal
Também chamado de empréstimo, o crédito pessoal é o tipo mais comum. Ao contrário do financiamento, que o dinheiro já tem um objetivo de uso, nesse caso, é possível pegar qualquer valor. A instituição financeira que vai emprestar o dinheiro, normalmente, faz uma análise de crédito da pessoa. Dessa forma, ela procura ter certeza que o compromisso do pagamento será honrado. Essa análise considera diferentes fatores, entre eles o score do Serasa.

5. Consórcio
O consórcio é a reunião de pessoas interessadas em comprar um bem de alto valor. Os participantes pagam parcelas mensais e esse dinheiro é colocado em um fundo comum.
Eventualmente, há um sorteio e um dos integrantes do consórcio recebe o valor necessário para comprar o bem pretendido. O sorteado terá uma carta de crédito para comprar o item.

6. Empréstimo consignado
O empréstimo consignado é um tipo de crédito com taxas de juros mais baixas e de pouco risco. Isso acontece porque o pagamento é descontado, automaticamente, do pagamento ou benefício do INSS.
            """
        )

    def subcapitulo5_2():
        criar_subcapitulo(
            "Como escolher\no melhor cartão\nde crédito",
            """
Com tantos cartões disponíveis no mercado, pode ser difícil escolher o que mais atenda às nossas necessidades.

Reunimos aqui algumas dicas que podem lhe ajudar na hora de escolher o cartão certo para o seu perfil:

1. Como você pretende usar o cartão de crédito?
É importante saber qual uso você pretende fazer do cartão. Se será apenas para compras de alto valor, se para todas as compras cotidianas ou se para apenas situações em que você não dispõe de dinheiro em espécie. Independente da resposta, o cartão de crédito é sempre uma ótima forma de pagamento. No entanto, é importante que você pague o total da fatura todos os meses até a data de vencimento. 

2. Qual programa de fidelidade é mais interessante para você?
A maioria dos cartões de crédito oferece algum tipo de incentivo para que o cliente gaste o máximo possível. Como recompensa, você pode ganhar milhas ou pontos para viajar, descontos em postos de combustível, desconto na compra de eletrodomésticos, créditos na fatura (cashback) e muitos outros. É interessante saber qual prêmio você mais e lhe será útil. 

3. Como fugir da anuidade do cartão de crédito? 
A maioria dos cartões vem com a cobrança da tarifa de anuidade. Alguns cartões oferecem anuidade grátis para sempre, outros estabelecem condições para que você não seja cobrado. Se você tem interesse em um cartão que ofereça benefícios como os mencionados no item anterior, é bem provável que esse cartão cobre anuidade. É importante que, ao solicitar o cartão, você esteja ciente do valor da anuidade. Caso contrário, é melhor optar por um cartão com anuidade mais acessível ou que ofereça anuidade grátis independente sem nenhuma exigência.

4. Qual bandeira de cartão escolher? 
Hoje temos diversas bandeiras disponíveis no mercado. As principais são Mastercard, Visa, American Express e Elo. Embora as maquinetas de cartões aceitem mais de uma bandeira, pode acontecer de uma bandeira não ser aceita em algum estabelecimento específico. Algumas bandeiras são globalmente reconhecidas e aceitas em quase todos os lugares ao redor do mundo. Já outras têm aceitação somente no Brasil ou dependem de acordos com bandeiras internacionais para terem aceitação no exterior. 
Com exceção da aceitação, as bandeiras funcionam de forma bem similar. Todas permitem realizar compras online e presencial, permitem realizar compras parceladas oferecem função crédito e débito em um só cartão.

5. Considere o banco em que você já é cliente 
Se você já é cliente de algum banco, seja com uma conta corrente ou poupança, verifique as opções de cartões que ele oferece. É provável que o seu cartão de débito possa se tornar um cartão múltiplo com funções de crédito e débito e você não saiba disso.
Mesmo que o seu banco não lhe ofereça um bom cartão de crédito de imediato, ele pode servir de porta de entrada para que você comece a utilizar o produto. Mantendo um bom relacionamento com o cartão, ele irá gerar pontos positivos para o seu score de crédito que facilitará o pedido de outros cartões no futuro.

6. Considere o seu score de crédito 
Ao consultar os seus dados, os bancos certamente irão ter acesso ao seu score de crédito. Ele é uma das informações analisadas para aprovar a sua proposta e tem muita importância por se basear em como o mercado financeiro classifica o risco de emprestar dinheiro para você. Se o seu score estiver baixo, pode ser difícil ser aprovado para os melhores cartões, então para ter mais chances de aprovação, opte por um mais básico até que a sua pontuação melhore. 

7. Escolha o cartão de crédito certo para a sua renda 
Por mais que os cartões de crédito mais exclusivos sejam cheios de benefícios, é importante que você escolha um cartão que seja compatível com a sua renda mensal. Pode não valer a pena você ter um cartão com anuidade alta se o seu e o seu consumo mensal for baixo ou se você não conseguir tirar aproveito dos benefícios. Na medida em que a sua renda aumentar, você pode preencher propostas para cartões melhores ou pedir upgrade do cartão que você já tem.
            """
        )

    def subcapitulo5_3():
        criar_subcapitulo(
            "O impacto das\ndívidas no seu\nfuturo financeiro",
            """
Como você já deve imaginar, cuidar das finanças pessoais no presente tem relação direta com a sua vida financeira no futuro. De forma geral, os cuidados com gastos, dívidas, recebimentos e investimentos são essenciais para evitar surpresas e garantir qualidade de vida.
Para equilibrar as finanças ao padrão de vida, é preciso ter disciplina. Mas os brasileiros ainda têm dificuldades em relação ao planejamento financeiro. Isso pode ocorrer por diversos motivos, como endividamento ou falta de conhecimento sobre o tema.

A da ANBIMA mostrou que apenas 36% dos brasileiros economizou dinheiro em 2020. Esse dado é muito importante, pois economizar permite investir. E quem investe consegue pensar no futuro e estar mais preparado para ele.
O fato de que a maior parte das pessoas não consegue economizar indica que elas estão gastando toda a renda ao longo do mês. Se elas não estão se organizando financeiramente, fica ainda mais difícil poupar para fazer o dinheiro render e realizar sonhos, não é mesmo?

A desorganização financeira tem um impacto direto na saúde financeira das pessoas, na medida em que torna mais difícil controlar problemas e lidar com imprevistos. De acordo com o Bureau de Proteção Financeira ao Consumidor dos Estados Unidos, a saúde financeira pode ser definida como um estado no qual a pessoa:
Tem controle sobre suas finanças do dia-a-dia e mensais;
É capaz de absorver um evento que a impacte financeiramente;
Está no caminho certo para alcançar suas metas financeiras;
Tem a liberdade financeira para tomar decisões que permitirão que ela aproveite melhor a vida.
Na contramão desses aspectos, os sintomas da desorganização financeirasão:
Não conseguir controlar seu orçamento de forma a não contrair dívidas;
Não conseguir poupar qualquer valor no final do mês;
Pagar uma grande quantidade de juros em função dos parcelamentos realizados.
Isso significa que não se trata apenas de uma questão de renda, porque mesmo pessoas muito ricas podem ter uma alta desorganização financeira.

Se alguém que ganha um alto salário chega ao final do ano sem ter poupado praticamente nada, só isso já demonstra que essa pessoa não está organizando suas finanças de forma adequada e que está vivendo no limite da sua renda.
Caso se depare com uma emergência, provavelmente terá dificuldades.

Além disso, se a pessoa vive focando apenas no agora, terá problemas no futuro, quando for se aposentar e não tiver os fundos para manter o mesmo padrão de vida (ou mesmo um padrão de vida minimamente digno).
            """
        )

    def subcapitulo5_4():
        criar_subcapitulo(
            "Estratégias para\nsair do\nendividamento",
            """
Com planejamento e disciplina, é possível recuperar o controle das suas finanças e sair das dívidas. Essa é uma jornada que possui algumas etapas importantes e você pode contar com a gente em todas elas. Confira o passo a passo que preparamos:
1. Registre os gastos
O primeiro passo para sair das dívidas é entender exatamente para onde o seu dinheiro está indo. Anote todas as suas despesas, desde as maiores até as menores, isso inclui contas fixas como aluguel e água, e gastos variáveis, como compras no supermercado e pequenas despesas diárias. Você pode usar um caderno, uma planilha ou aplicativos de controle financeiro para fazer esse registro. 
            
2. Organize as finanças
Depois de registrar os gastos, é hora de organizar e classificar tudo. Para isso, separe suas despesas em categorias:
• Fixas: aquelas que não mudam todo mês;
• Variáveis: que podem mudar de um mês para o outro;
• Extraordinárias: gastos esporádicos e emergenciais.
Com isso, você terá uma visão ainda mais clara de qual categoria está consumindo mais do seu orçamento e qual delas precisa ser revisitada .
            
3. Crie metas
Defina objetivos claros e mensuráveis, como pagar uma dívida específica primeiro, poupar uma quantia determinada por mês para quitar uma dívida à vista ou reduzir determinados gastos por um período. As metas devem ser realistas e detalhadas, para que você possa acompanhar seu progresso, recalcular rota e fazer ajustes necessários para que elas se cumpram.
            
4. Corte gastos desnecessários
Analise seus registros de gastos e identifique despesas que podem ser reduzidas ou eliminadas, gerando recursos para o seu plano de pagamento de dívidas.
No momento em que o seu foco é sair do endividamento, algumas prioridades devem ser revistas. Considere então substituir atividades de lazer mais caras por alternativas gratuitas ou mais baratas e revise suas assinaturas de serviços e veja se alguma pode ser cancelada ou renegociada.
            
5. Converse com os familiares
Sair das dívidas é um esforço coletivo, especialmente se você vive com outras pessoas. É importante conversar com os familiares sobre a situação financeira e a necessidade de economizar para o bem de todos. Explique as metas e peça a colaboração de todos para reduzir despesas. Quando todos estão alinhados e comprometidos, fica mais fácil alcançar os objetivos e evitar novos gastos desnecessários. 
            
6. Renegocie as dívidas
Muitas vezes, é possível conseguir condições melhores para pagar as dívidas entrando em contato com os credores. Além disso, renegociar as dívidas pode facilitar o pagamento ao aliviar o peso das parcelas mensais ou até mesmo o valor total da dívida. Explique sua situação e peça um novo plano de pagamento, com parcelas menores ou prazos maiores. 
            
7. Priorize as dívidas com os juros mais altos
Dívidas com juros altos, como as de cartão de crédito e cheque especial, crescem rapidamente e podem se tornar uma bola de neve se não forem controladas. Então, priorize o pagamento dessas dívidas primeiro.
            
8. Busque fontes de renda extra
Além de cortar gastos, buscar fontes de renda extra pode acelerar o processo de sair das dívidas. Considere fazer trabalhos freelancer, vender produtos que você não usa mais ou oferecer serviços na sua comunidade. A renda extra pode ser utilizada diretamente para o pagamento das dívidas, aliviando o impacto causado no orçamento mensal.
            
9. Crie o hábito de poupar
Mesmo enquanto está pagando dívidas, é importante começar ou continuar a poupar. Estabeleça um valor mensal, por menor que seja, para ser guardado inclusive durante esse período. Isso ajuda a criar um fundo de emergência, que pode evitar novas dívidas no futuro.
            
10. Consulte o seu CPF regularmente
Verificar regularmente a situação do seu CPF é essencial para acompanhar com agilidade qualquer nova pendência registrada no documento, evitando falhas ou fatores surpresa no plano que você definiu para regularizar suas dívidas.
            """
        )

    def subcapitulo5_5():
        criar_subcapitulo(
            "A importância de\num bom score\nde crédito",
            """
Buscar empréstimos pode acontecer por diversos motivos, desde para a quitação de dívidas de cheque especial ou cartão de crédito, até para financiar projetos como a compra da casa própria, a aquisição de um carro ou a realização de um curso de extensão. O fato é que, uma hora ou outra, essa busca acontece. E, muitas vezes, a taxa de juros assusta e pode comprometer os planos de muitas pessoas. Nesse cenário entra o score de crédito – que pode te ajudar a conseguir juros mais baixos. Mas, para isso, você precisa estar com a sua vida financeira em ordem.
Score trata-se de um indicador do seu perfil financeiro. Isso quer dizer, na prática, que ele mostra se você é um bom pagador ou não. Ele é calculado pelos chamados birôs de crédito, empresas que fazem a gestão de uma série de dados relacionados ao histórico de pagamentos das pessoas, como Serasa, Serviço de Proteção de Crédito (SPC), Boa Vista e Quod.
As informações têm base nos dados presentes no cadastro positivo. Diferentemente do cadastro negativo, que lista quem está com o nome sujo e leva em consideração as contas não pagas, o score sinaliza, por meio de uma nota, quem consegue quitar em dia todas as dívidas e contas.
O score leva em consideração pagamentos de contas, boletos e crediários, nome negativado e relacionamento financeiro com as empresas nas quais você adquiriu produtos e serviços. A soma dos três fatores gera a “nota de crédito” de uma pessoa. Outras informações também são utilizadas, como estado civil, emprego formalizado em carteira e hábitos de consumo – isso pode variar de empresa para empresa.
Qual a importância do Score
Segundo dados do Banco Mundial, o uso do cadastro positivo podem:
Aumentar em até 88% a aprovação de crédito;
Reduzir a inadimplência em até 45%;
Aumentar do saldo de crédito de 47% para até 66% do PIB.
            
O que é um score bom?
A pontuação vai de 0 a 1.000 e indica a probabilidade daquele consumidor honrar com seus compromissos financeiros. Quanto mais próxima de mil, maiores são as chances daquele perfil ter um crédito aprovado. Pontuações acima de 700 significam um score bom. Nesse caso, existe um baixo risco de inadimplência.Aqueles que têm um bom score também garantem credibilidade no mercado financeiro e acesso a financiamentos e empréstimos com condições melhores.
            
O que é um score regular?
O score regular está entre 301 e 700 pontos. Nesse caso, existe um risco médio de inadimplência. Funciona como uma luz amarela indicando que o consumidor pode não fazer o pagamento de uma conta em dia. As pessoas que estão nessa faixa podem conseguir boas taxas ou cartões de crédito mais básicos, mas também podem encontrar dificuldades em aumentar o limite ou acessar produtos financeiros mais robustos.
            
O que é um score baixo?
O score baixo está em pontuações de 0 a 300. O risco de inadimplência é alto e as instituições te reconhecem como um mau pagador, dificilmente liberando algum crédito.

            """
        )

    def subcapitulo5_quiz():
            criar_quiz()

    def subcapitulo5_desafio():
        criar_subcapitulo(
            "Desafio",
            """
Parabéns por avançar em sua jornada de educação financeira! Você aprendeu sobre os diferentes tipos de crédito e suas características. Agora é hora de aplicar esse conhecimento em um desafio prático.
 
Desafio: Análise de Opções de Crédito
Imagine que você está planejando financiar um carro, reformar sua casa ou resolver uma emergência financeira. Escolha um dos cenários abaixo e faça uma pesquisa detalhada:

Financiamento de Carro:
Pesquise três instituições financeiras que oferecem financiamento de veículos. Compare as taxas de juros, prazos e condições de pagamento. Calcule o custo total do financiamento e analise se o valor cabe no seu orçamento mensal.

Cartão de Crédito:
Selecione dois cartões de crédito diferentes que atendam às suas necessidades. Compare os benefícios, como cashback ou milhas, além de taxas como anuidade e juros. Determine qual cartão é mais vantajoso para o seu perfil.

Crédito Pessoal ou Consignado:
Considere uma necessidade urgente, como quitar dívidas ou realizar uma compra importante. Pesquise instituições que oferecem empréstimos pessoais ou consignados. Compare as condições e escolha a melhor opção com base nas taxas e impacto financeiro.

Reflexão Final:

Qual tipo de crédito pareceu mais vantajoso para o cenário escolhido?
O que você aprendeu sobre o impacto das taxas de juros no custo total?
Você se sente mais preparado para tomar decisões financeiras relacionadas a crédito no futuro?
Lembre-se: o conhecimento é uma das ferramentas mais poderosas para conquistar sua liberdade financeira!
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
            criar_bloco("Tipos de crédito e suas características", lambda _: subcapitulo5_1()),
            criar_bloco("Como escolher o melhor cartão de crédito", lambda _: subcapitulo5_2()),
            criar_bloco("O impacto das dívidas no seu futuro financeiro", lambda _: subcapitulo5_3()),
            criar_bloco("Estratégias para sair do endividamento", lambda _: subcapitulo5_4()),
            criar_bloco("A importância de um bom score de crédito", lambda _: subcapitulo5_5()),
            criar_bloco("Quiz", lambda _: subcapitulo5_quiz()),
            criar_bloco("Desafio", lambda _: subcapitulo5_desafio()),
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
