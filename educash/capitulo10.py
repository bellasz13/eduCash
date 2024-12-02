import flet as ft

def Capitulo10Page(page: ft.Page):
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

    def subcapitulo10_1():
        criar_subcapitulo(
            "Criptomoedas e investimentos em tecnologia",
            """
            Com a adoção crescente por instituições financeiras e bancos centrais pelo mundo, o Bitcoin e outros criptoativos já são uma realidade em meio às tantas opções para a diversificação de investimentos.
            Trata-se de um investimento que tem seus riscos, afinal existe a volatilidade intrínseca a este ativo, mas a tecnologia de criptografia por trás do universo cripto garante a segurança das transações e o avanço da regulamentação dos criptoativos no Brasil estabelece um ambiente de garantias para se comprar e vender criptomoedas e Tokens. 
            Bitcoin é praticamente sinônimo de criptomoeda. Não é a única, muito pelo contrário, pois há milhares de opções, mas o Bitcoin foi o primeiro criptoativo do mercado. Trata-se de uma moeda digital, que existe apenas na internet e não depende de sistema bancário nem de soberania nacional.
            A base tecnológica é um sistema de criptografia - daí o prefixo cripto - que torna cada transação única, com um código numérico de segurança que não pode ser adulterado. 
            As criptomoedas mais populares são Bitcoin, a pioneira, e Ethereum. Diferentemente do Bitcoin que é um ativo por si próprio, o Ethereum é um ecossistema, tecnicamente falando, ou uma plataforma de contratos inteligentes (smart contracts).
            Como o Ethereum é um ativo com externalidade de rede encadeada, ele se valoriza junto com as aplicações que rodam na sua blockchain própria. Em outras palavras, o ETH como moeda vai sendo alavancado pela valorização de seus ativos subjacentes, com milhares de aplicações na sua blockchain própria. 
            De modo geral, as outras criptomoedas são classificadas como altcoins, moedas alternativas ao Bitcoin, como Ethereum, Solana, Cardano e tantas outras; e stablecoins, que usam algum valor fiduciário como referência, por exemplo uma moeda física, como dólar e euro, ou cotação de algum ativo real, como ouro ou petróleo. As stablecoins mais populares são as atreladas ao dólar americano, como USD Tether (USDT) e USD Coin (USDC). 
            Existem ainda criptomoedas oficiais de países, lançadas por bancos centrais, as chamadas CBDCs - do inglês "Central Bank Digital Currency" - ou Moeda Digital Emitida por Banco Central. E nesse assunto, o Brasil é um dos pioneiros, com o Drex, uma espécie de real digital, que está já em fase piloto pelo Banco Central.
            Comprar e vender criptomoedas é fácil, bastam alguns cliques. Além das criptomoedas mais conhecidas e de maior liquidez, o mercado institucional também oferece opções de fundos de investimento com cestas de criptoativos variados e ETFs de Bitcoin e Ethereum. Consulte seu assessor de investimentos para escolher a melhor estratégia conforme seus objetivos. 
            É preciso aprender um pouco sobre esse mundo para ter mais segurança nos investimentos cripto, que apresentam grande volatilidade. O perfil de investidor costuma ser mais arrojado, para aguentar os solavancos desse mercado, considerado mais arriscado do que outros tipos de aplicação em renda variável. Via de regra, especialistas recomendam para os interessados colocar um percentual pequeno da carteira em cripto, como estratégia de diversificação de portfólio. 
            O que é NFT? E o que é token?
            Toda criptomoeda é um token, mas nem todo token é uma criptomoeda. Vamos lá. Os tokens são títulos digitais que representam virtualmente a posse de ativos ou uma fração deles. A tecnologia blockchain permite que os tokens sejam registrados e negociados. 
            Qualquer ativo real, na forma física ou digital, pode ser negociado na forma de token. No mercado financeiro, a tokenização é tendência mundial, pois permite criar produtos diferenciados e seguros para ampliar as possibilidades de captação de investimentos. A lógica é parecida com a da bolsa de valores, em que uma empresa divide seu patrimônio em ações.
            Na essência, os tokens são fungíveis ou não fungíveis, os famosos NFTs (Non-Fungible Tokens). Os fungíveis podem ser substituídos por outros da mesma espécie, qualidade e quantidade. Já o conceito de não fungíveis é usado para ativos com características únicas, como uma obra de arte, por exemplo, ou benefícios exclusivos para torcedores de um determinado time de futebol, os chamados fan-tokens.
            """
        )

    def subcapitulo10_2():
        criar_subcapitulo(
            "Inflação e seus impactos no seu poder de compra",
            """
            Inflação é um termo da economia usado para designar o aumento generalizado de preços de bens e serviços. Com isso, a inflação representa o aumento do custo de vida e a consequente redução no poder de compra da moeda.
            Esse aumento de preços não é necessariamente ruim ou prejudicial ao consumidor, principalmente quando é controlado, espaçado ao longo do tempo e vem acompanhado de reajustes nos salários-mínimos. Mas pode causar transtornos para consumidores – e para a economia de um país – quando aumenta em uma velocidade maior do que pode ser absorvida. 
            Um aumento nos índices de inflação pode ser influenciado por diferentes causas, que podem ser agrupadas em quatro grandes grupos: 1) aumento na demanda; 2) aumento, ou pressões, nos custos de produção; 3) inércia inflacionária e expectativas de inflação; e 4) aumento de emissão de moeda.
            As causas também podem ser divididas em de curto prazo ou um prazo maior, que aumentam de forma contínua durante meses ou até anos.  Dificilmente, no entanto, a causa da inflação será única.
            A inflação tem um impacto direto em diferentes aspectos da vida dos consumidores: da alimentação básica até o preço de imóveis. Por isso, a inflação não é medida por um índice único.
            No Brasil, entre os muitos índices que medem a inflação, o principal para calcular o seu valor oficial é o IPCA ( Índice de Preços ao Consumidor Amplo). Este indicador é chamado de amplo porque tem o objetivo de abranger 90% da população urbana no país e é calculado mensalmente pelo Instituto Brasileiro de Geografia e Estatística (IBGE).
            O IPCA determina a inflação de produtos e serviços do varejo consumidos por famílias que recebem de 1 a 40 salários mínimos e leva em conta os valores de uma cesta de produtos e serviços consumidos pela população.
            Os pesquisadores do instituto entrevistam famílias para saber onde e o que compram. A partir dessa lista, são estipulados quais itens vão entrar na cesta de produtos mais consumidos pela população e o peso que cada um deles terá para o cálculo da inflação. O preço do arroz, por exemplo, alimente presente em quase todas as mesas brasileiras, terá um peso maior no cálculo do IPCA do que o preço do macarrão.
            Feita a determinação de itens mais consumidos, os pesquisadores organizam outro relatório, desta vez com os comércios onde será feita a checagem de preços dos produtos mais consumidos. Com todos os dados reunidos, os técnicos do IBGE chegam aos valores dos índices para um determinado período.
            Na prática, se os preços da habitação subiram 2%, os valores do setor elétrico aumentaram 2%, e os preços do setor de alimentação caíram 3,5%, o valor mensal da inflação será a soma dessas variações, considerando o peso que cada item possui.
            Além do IPCA, existem outros índices que ajudam a medir a inflação em diferentes setores do comércio de bens e serviços. Esses índices medem os preços de bens e serviços de formas distintas, cada um com seu método.
            Na cesta do IPCA é calculada a variação dos preços dos bens e serviços consumidos na rotina das famílias brasileiras com renda mensal entre um e 40 salários mínimos. Cada item e serviço presente nessa cesta terá um determinado peso, de acordo com o consumo médio dele pela população.
            Dessa forma, a função do IPCA é medir o valor do dinheiro com o passar do tempo. Mas essa cesta de produtos e serviços também mudou. A versão recente de cesta de produtos e serviços do IPCA, por exemplo, inclui itens básicos e tradicionais como arroz e feijão, mas também produtos e serviços que foram criados há pouco tempo, como serviços de streaming e transporte por aplicativo.
            Já o INPC (Índice Nacional de Preços ao Consumidor), mede a variação dos valores dos produtos de bens e serviços para famílias com renda de até cinco salários mínimos, uma faixa da população de renda mais baixa e, portanto, mais sensível aos movimentos de preços de itens básicos. Como está focado em famílias de até cinco salários mínimos, o INPC serve como um termômetro para o reajuste do salário mínimo.
            O IGP (Índice Geral de Preços), que é medido pela Fundação Getulio Vargas (FGV), tem outro objetivo muito específico: serve para registrar a alta dos preços que vão desde a matéria-prima usada em produção agrícola e industrial, até elas virarem bens e serviços, a serem adquiridos pelos consumidores finais.
            O IGP dá origem a outros índices, como o IGP-DI, o IGP-10 e o IGP-M. O IGP-DI, Índice Geral de Preços – Disponibilidade Interna. 
            Já o IGP-10 (Índice Geral de Preços - 10) faz a medição da evolução dos preços entre o período que vai do dia 11 do mês anterior e o dia 10 do mês corrente.
            O IGP-M (Índice Geral de Preços - Mercado), por sua vez, faz a coleta de dados do dia 21 do mês anterior ao dia 20 do mês atual e, além de fornecer um panorama da economia, pode ter um impacto direto no bolso dos consumidores que moram de aluguel. Isso porque o índice do IGP-M é, normalmente, usado como base para o reajuste de tarifas e contratos como os alugueis comerciais e residenciais.
            O IPA (Índice de Preços no Atacado), também medido pela FGV, estima o ritmo dos preços que são trabalhados no comércio atacadista, nas transações entre empresas, que são feitas antes das vendas no varejo. Esse índice também reflete o valor adicionado na produção de bens agropecuários, industriais, bens finais dos setores da alimentação, máquinas e equipamentos, matérias-brutas agropecuárias e minerais. 
            Já o IPC-S (Índice de Preços ao Consumidor Semanal) é bem parecido com o INPC, mas mensura os preços da alimentação, produtos de limpeza, higiene e serviços, a cada 10 dias.
            Há ainda o IPC-Fipe (Índice de Preços ao Consumidor), calculado pela Fundação Instituto de Pesquisas Econômicas (Fipe). Esse índice mede a variação dos preços dos produtos consumidos na cidade de São Paulo e mostra a variação do custo de vida médio de famílias que têm renda entre 1 e 10 salários mínimos.
            A principal consequência da inflação é a perda do poder de compra ao longo do tempo, com o aumento dos preços das mercadorias e a desvalorização da moeda.
            Outra consequência está associada ao rendimento real em investimentos. O rendimento real ou a rentabilidade real é aquela conseguida em uma aplicação, descontada a inflação. Se um investimento teve um retorno de 10% ao ano e a inflação no período foi de 2% ao ano, sua rentabilidade real foi de 8%. Mas se um investimento teve esse mesmo rendimento, de 10% ao ano, em um período em que a inflação foi 11%, a rentabilidade real foi negativa: isto é, mesmo rendendo alguma coisa, o investidor “perdeu” dinheiro.
            É isso que pode acontecer com aplicações como a poupança, cuja rentabilidade está atrelada à Selic, a taxa básica de juros da economia. Se a Selic ficar abaixo da inflação, a rentabilidade real da poupança será negativa.
            A inflação não é uma vilã da economia. O Banco Central procura trabalhar para que a inflação se mantenha controlada e dentro de uma meta estabelecida, mas não para que os preços dos produtos comecem a cair ao ponto de ficarem mais baratos ao longo do tempo.
            A ideia é que os preços cobrados se mantenham razoavelmente estáveis ao longo do tempo, com um crescimento que acompanhe, também, o crescimento do país.
            Dessa forma, uma queda generalizada de preços, poderia gerar uma série de problemas para a economia. As causas que podem levar à deflação são relacionadas com aquelas que podem levar à inflação. Um aumento inesperado de oferta, por exemplo, pode fazer com que o preço de produtos caia e levar a uma série de efeitos em cascata. Maior oferta de produtos na prateleira leva a uma queda de preços, que leva a um prejuízo do fabricante que precisaria reduzir seus custos, reduzindo a produção ou demitindo funcionários, por exemplo.
            """
        )

    def subcapitulo10_3():
        criar_subcapitulo(
            "Planejamento financeiro para aposentadoria",
            """
           Existem várias estratégias de investimento que podem garantir uma boa renda na aposentadoria, como planos de previdência privada, Tesouro Direto RendA+, dividendos de ações e fundos imobiliários. A escolha da estratégia de investimento ideal depende das suas metas financeiras.

           Importante dizer que, independente de suas metas, alguns passos são inevitáveis em seu planejamento para a aposentadoria:
           1. Avalie suas finanças pessoais
           Faça um balanço completo de sua vida financeira: renda, custos fixos e variáveis, investimentos atuais, bens e dívidas. A diferença entre o que você possui (ativos) e suas despesas recorrentes (passivo) é o seu patrimônio líquido. Ter clareza sobre esse número e revisá-lo anualmente ajudará você a manter-se dentro do plano de metas traçado.
           2. Defina sua meta de aposentadoria
           Investir com o objetivo de se aposentar é muito vago. Para montar uma carteira estruturada, você precisa detalhar essa meta: qual idade você quer se aposentar? Qual será sua renda mensal quando parar de trabalhar? Quanto você precisa acumular até a data definida para se aposentar?
           Lembre-se de incluir nessa conta, a projeção de inflação, do contrário, seu poder de compra será comprometido.
           3. Conheça as opções de previdência privada
           No Brasil, existem dois tipos de previdência privada: VGBL (Vida Gerador de Benefício Livre) e PGBL (Plano Gerador de Benefício Livre). Ambos permitem que você defina o valor e a periodicidade das suas contribuições, além do tipo de alíquota do Imposto de Renda.
           Considere conversar com um especialista que possa orientar qual o tipo de plano de previdência mais adequado ao seu caso.
           4. Pesquise modalidades de investimentos
           Investir em ações e fundos imobiliários é uma ótima opção para quem deseja uma renda complementar à aposentadoria. Apesar da volatilidade desses ativos, eles oferecem maior valorização do patrimônio no longo prazo.
           Além disso, ações e fundos imobiliários asseguram uma renda perpétua, pois enquanto você mantiver os ativos sob sua custódia, irá receber os dividendos correspondentes isentos de Imposto de Renda.
           5. Comece a investir cedo
           Quanto mais cedo você começar a investir para a aposentadoria, mais benefícios terá. Isso inclui criar o hábito de destinar uma parte da sua renda para esse fim todos os meses.
           Além disso, há uma série de outras vantagens em começar cedo:
           quanto mais tempo para que os juros compostos trabalhem para você, maior a acumulação de patrimônio;
           será possível destinar uma parcela maior de seu aporte para ativos com maior risco/retorno, pois haverá tempo hábil para recuperar eventuais perdas;
           você terá mais tempo para aprimorar sua estratégia, adquirindo conhecimento em um número maior de modalidades de investimento;
           a maior parte de seus aportes acontecerá na fase da vida adulta em que você está mais produtivo e com disposição para gerar várias alternativas de renda.
           6. Cuidado com as emoções
           Por mais que as decisões sobre investimentos pareçam algo matemático e meramente racional, não subestime a influência que as emoções exercem sobre elas, pois isso acontecerá em algum momento, portanto, esteja atento.
           O mercado se movimenta em ciclos de alta e baixa, impactando o resultado dos investimentos. Assim, quando os investimentos estão apresentando alta performance, temos a tendência a ficar excessivamente confiantes, subestimando os riscos.
           Por outro lado, quando os investimentos vão mal, a aversão à perda pode dominar e, eventualmente, nos levar a vender ativos com prejuízo e migrar para investimentos considerados de baixo risco.
           Em ambos os casos, decisões tomadas sob influência das emoções podem causar perdas substanciais, além de privá-lo da oportunidade de ganhar dinheiro com cada um dos ciclos de mercado.
           Manter uma carteira diversificada, com classes de ativos com diferentes graus de risco irá funcionar como proteção e dará mais tranquilidade para tomar decisões com calma e baseadas em fundamentos, em vez de reagir ao calor dos acontecimentos.
           7. Priorize seu planejamento financeiro
           Assumir responsabilidade pelas suas finanças pessoais é uma das melhores decisões que você pode tomar na vida. Se você não tem tempo ou disposição para cuidar dos seus investimentos sozinho, considere contratar um especialista em mercado.
           Há excelentes profissionais que podem auxiliar no planejamento financeiro de forma independente e totalmente customizada, portanto, contratar um planejador financeiro certificado, ou um consultor CVM credenciado, pode ser uma excelente forma de ganhar tempo e otimizar seus investimentos.
           Fazer o quanto antes o plano de aposentadoria é algo que nenhum de nós pode se dar ao luxo de negligenciar, portanto, coloque-se como prioridade em sua própria vida e comece já.
            """
        )

    def subcapitulo10_4():
        criar_subcapitulo(
            "Como se preparar para uma crise financeira",
            """
            A reserva de emergência é um dos elementos mais importantes para ter uma vida financeira saudável. Ela consiste em uma quantia que deve ficar disponível e segura para o uso em situações de imprevistos ou dificuldades, como em uma crise econômica.
            Entre as situações que podem levar à necessidade de usar esse dinheiro estão acidentes, problemas de saúde, dificuldades com o negócio e mais. Nesses e em outros momentos semelhantes, a reserva é bastante útil, pois você cobrirá essas situações sem precisar recorrer a empréstimos, por exemplo.
            O ideal, portanto, é deixar para usar a reserva como última alternativa antes do endividamento. Em períodos de crise econômica, entretanto, esse momento pode chegar mais cedo, então é preciso avaliar se esse é o momento certo de utilizar os recursos.
            Outra dica relevante para a sua gestão financeira pessoal é elaborar um planejamento das finanças. Por meio dele, você saberá como lidar melhor com seu dinheiro e usá-lo para alcançar seus objetivos.
            Nesse contexto, é bastante válido reunir a família e identificar as prioridades. Ao conhecer as necessidades mais relevantes, o planejamento fica mais fácil, pois ele se baseará nas demandas de cada membro.
            Além de ter um planejamento financeiro é essencial avaliar o orçamento, pois isso o ajudará a conhecer a sua realidade financeira e da sua família. Ainda, será possível entender quais são as fontes de receita e as despesas.
            Para criar o orçamento, é necessário considerar a renda disponível e dividi-la entre as prioridades e necessidades da família.
            Após finalizar a montagem do orçamento, analisá-lo permite identificar áreas que possam estar gastando demais ou que exijam mais atenção. Assim, você consegue encontrar oportunidades de melhorar o uso do dinheiro, pensando também em períodos de crise econômica.
            Depois de definir e analisar o orçamento familiar, ficará mais fácil encontrar estratégias para reduzir os custos de maneira eficiente e sem prejudicar a sua qualidade de vida. Nesse momento, é válido verificar quais são as despesas supérfluas que podem ser reduzidas ou até cortadas.
            Com mudanças que ajudem a gerar economia, é possível cuidar melhor da gestão financeira pessoal. Afinal, a medida pode ajudar a manter os custos menores que as receitas. Em períodos de redução nos ganhos, como costuma acontecer em crises econômicas, essa estratégia se torna essencial.
            As dívidas comprometem a saúde financeira de milhões de famílias brasileiras, por isso, evite-as. Caso você não quite os compromissos financeiros, incidirão multas e juros. Ainda, há o risco de ficar com o nome sujo e ter dificuldades para conseguir crédito no futuro.
            Em vez de fazer compras por impulso, por exemplo, foque naquilo que é realmente necessário e que você pode pagar sem contrair dívidas. Também é interessante repensar o uso excessivo do cartão de crédito, já que ele pode levar ao endividamento.
            Ao adotar a gestão financeira pessoal de modo adequado, é esperado que você consiga gastar menos do que ganha, certo? Vale utilizar esse valor extra para começar a investir. Dessa forma, é possível fazer o dinheiro trabalhar para você e fortalecer seu patrimônio.
            Nesse caso, considere também os impactos da crise sobre o mercado financeiro e avalie quais são as principais oportunidades. Ainda, é preciso avaliar sua capacidade de investimento, seus objetivos e seu apetite ao risco.
            No geral, os investimentos o ajudarão a melhorar a sua saúde financeira e a alcançar seus diversos objetivos. Após os momentos turbulentos, o bom hábito de investir será essencial para manter a disciplina com o uso do dinheiro e conquistar mais tranquilidade em relação ao orçamento.
            Como você aprendeu, a gestão financeira pessoal o ajuda a organizar melhor o dinheiro e se preparar para lidar com os efeitos das crises econômicas. Ao adotar as práticas apresentadas, você poderá ter mais segurança em relação aos recursos familiares — mesmo diante de cenários desafiadores.
            """
        )

    def subcapitulo10_5():
        criar_subcapitulo(
            "Inteligência artificial e o futuro das finanças",
            """
            A Inteligência Artificial (IA) está mudando a maneira como as empresas operam no setor financeiro. Com a capacidade de processar grandes quantidades de dados, a IA está sendo usada para automatizar muitas tarefas e aprimorar processos de tomada de decisão. 
            5 aplicações atuais da Inteligência Artificial no setor das Finanças
            Análise de dados
            A Inteligência Artificial é usada para analisar grandes quantidades de dados e ajudar a identificar tendências e outras informações importantes que podem ajudar os investidores a tomar decisões mais informadas. 
            Previsão de mercado
            As ferramentas financeiras de IA podem ser usadas para analisar dados passados e prever como os mercados devem se comportar no futuro, permitindo que os investidores obtenham uma vantagem competitiva.
            Robôs de negociação
            Robôs de negociação são programas que usam algoritmos de Inteligência Artificial para negociar ativos financeiros em nome de seus usuários.
            Eles automatizam tarefas como a execução de ordens de compra e venda, monitoramento de mercados e análise de dados, para ajudar a tomar decisões informadas sobre quais ativos comprar e vender.
            Os robôs de negociação são usados ​​por investidores, bancos, fundos de hedge e outros profissionais do mercado financeiro para automatizar suas tarefas de negociação e gerenciamento de portfólio, ajudando-os a reduzir custos, tempo e erros.
            Análise de risco
            A Inteligência Artificial nas Finanças também pode ser usada para identificar riscos de investimento e ajudar os investidores a tomar decisões mais seguras.
            Uma instituição financeira pode usar a IA para ajudar a analisar o risco de empréstimos, por exemplo. Para isso, o banco pode usar algoritmos de aprendizado de máquina para analisar grandes quantidades de dados históricos relacionados a empréstimos, como crédito dos candidatos, informações sobre histórico de pagamentos e outros fatores de risco.
            O algoritmo de IA então pode usar esses dados para prever quais candidatos a empréstimo têm maior probabilidade de não pagar de volta suas dívidas, ajudando assim o banco a tomar decisões informadas sobre quais empréstimos conceder e quais não.
            Gestão de portfólio
            A Inteligência Artificial nas Finanças ajuda na gestão de um portfólio de investimentos neste mercado ao automatizar algumas tarefas essenciais. Por exemplo, ela pode realizar análises de mercado para acompanhar tendências e identificar oportunidades.
            Também pode ajudar na análise de riscos, monitorando as condições do mercado e avaliando a volatilidade no mercado, além de ajudar a gerir e a monitorar as carteiras de investimento, avaliando os resultados e gerando relatórios.Isso permite que os investidores tomem decisões de investimento mais informadas e de forma mais eficiente.
            """
        )

    def subcapitulo10_quiz():
            criar_quiz()

    def subcapitulo10_desafio():
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
            criar_bloco("Criptomoedas e investimentos em tecnologia", lambda _: subcapitulo10_1()),
            criar_bloco("Inflação e seus impactos no seu poder de compra", lambda _: subcapitulo10_2()),
            criar_bloco("Planejamento financeiro para aposentadoria", lambda _: subcapitulo10_3()),
            criar_bloco("Como se preparar para uma crise financeira", lambda _: subcapitulo10_4()),
            criar_bloco("Inteligência artificial e o futuro das finanças", lambda _: subcapitulo10_5()),
            criar_bloco("Quiz", lambda _: subcapitulo10_quiz()),
            criar_bloco("Desafio", lambda _: subcapitulo10_desafio()),
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
