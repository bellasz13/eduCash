import flet as ft

def Capitulo8Page(page: ft.Page):
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

    def subcapitulo8_1():
        criar_subcapitulo(
            "Mercado imobiliário",
            """
            Frequentemente, as mudanças sociais, ambientais, culturais, bem como as inovações tecnológicas transformam o cenário e influenciam nas nossas decisões. Por isso, antes de se decidir sobre comprar ou não um imóvel, é fundamental saber quais são as tendências do momento.
Nesse sentido, o setor imobiliário atua fortemente, move o país e dita o comportamento desse mercado, que impactam outros movimentos da economia. Mas, quais serão as tendências para 2024? Para saber mais, continue acompanhando o artigo.

Para 2024, então, as projeções são otimistas, considerando o saldo positivo apresentado no mercado imobiliário em 2023. Com uma oferta maior de linhas de crédito e um incremento nas vendas, o cenário tende a ser promissor.
Além disso, o orçamento destinado ao programa Minha Casa, Minha Vida teve um acréscimo de 41% para famílias enquadradas na Faixa 1 do programa, conforme anunciado no final de 2023 pelo Governo Federal.
Essas boas novas, portanto, sinalizam um novo fôlego para a aquisição da casa própria ainda em 2024 e nos próximos anos. Mas, afinal, quais são as 10 tendências do mercado imobiliário para este ano?

1. Sustentabilidade e construções ecológicas

A crescente preocupação com as práticas de ESG (Environmental, social and governance — traduzido para o português: ambiental, social e governança) faz com que, a cada ano, aumente a demanda por construções ecológicas e sustentáveis no mercado imobiliário. Esta, aliás, é uma das maiores tendências deste mercado para os próximos anos.

Tecnologia e casas inteligentes

Casas inteligentes são ecológicas e a sociedade tem se conscientizado sobre a limitação dos recursos naturais, que devem ser explorados racionalmente. Essa responsabilidade tem o objetivo de garantir que as futuras gerações não herdem um planeta totalmente degradado.
Hoje, já dispomos de diversas técnicas que favorecem o uso otimizado de materiais para a construção civil. Com isso, é possível reduzir os desperdícios e reutilizar peças que normalmente seriam destinadas ao descarte.

3. Plantas flexíveis

Os projetos dos ambientes das casas já são mais adaptáveis, eficientes e multifuncionais. Sua flexibilidade e versatilidade permitem que apenas um ambiente atenda a diversas necessidades.
Essa multifuncionalidade é usada também em locais de entretenimento, escritórios e espaços públicos. Dessa maneira, é possível transformar o ambiente de acordo com a necessidade, tanto para trabalho, reuniões ou para relaxar.

4. Condomínios multifuncionais

Para 2024 os condomínios multifuncionais também exercem um forte apelo na escolha de investidores do ramo imobiliário e de compradores, uma vez que significam conveniência e versatilidade.
A ideia é oferecer uma estrutura completa aos moradores, com o intuito de melhorar sua qualidade de vida. São espaços com área de lazer e convivência entre os condôminos, como: academia, piscina, churrasqueira, playground, salão de festas e outros.
Contudo, esse tipo de condomínio já existe há bastante tempo. O diferencial, hoje, é a acessibilidade para os mais diversos perfis de compradores e não apenas exclusividade de projetos luxuosos ao alcance de poucos.

Investimento em segurança residencial
Em 2024, o aumento do investimento em sistemas de segurança avançados em residência deverá permanecer no centro das prioridades dos novos compradores de imóveis.
Essas tecnologias, compostas por controle de acesso, câmeras e outros equipamentos tenderão a ser incorporadas aos projetos imobiliários como forma de garantir mais segurança e tranquilidade aos moradores.

            """
        )

    def subcapitulo8_2():
        criar_subcapitulo(
            "Tipos de investimento em imóveis",
            """
            Aluguel de imóveis: os FIIs que possuem imóveis utilizam-os para gerar renda através do aluguel. Com isso, o fundo capta recursos através de contratos de aluguéis e essa renda se converte em rendimento;
Arrendamento de imóveis: o arrendamento de um imóvel é o contrato pelo qual o contratado se obriga a ceder o ativo, por tempo determinado ou não, com o objetivo de nele ser exercida atividade de exploração;
Construção de imóveis: nesse caso, o fundo utiliza seus recursos para incorporação e construção de imóveis para futura venda, e assim, lucrar com o negócio;
Aquisição de títulos de renda fixa: essa é uma prática comum principalmente nos fundos de papel, em que são adquiridos recebíveis e títulos atrelados ao mercado imobiliário, como LCIs e CRIs, que geram um retorno mensal na forma de juros;
Aquisição de cotas de outros fundos imobiliários: essa prática é adotada de forma comum pelos fundos de fundos (FOFs), que adquirem cotas de outros fundos imobiliários.
É preciso dizer que, por lei, os FIIs são obrigados a distribuir pelo menos 95% dos seus rendimentos aos cotistas.
Pronto, você já entendeu como os FIIs ganham, mas como você pode ganhar dinheiro com esse investimento? De duas formas principais:
Valorização da cota: as cotas dos fundos imobiliários são negociadas no mercado e estão sujeitas às forças de oferta e demanda; caso a demanda seja maior que a oferta, o preço da sua cota vai valorizar; e
Recebimento de proventos: o lucro que o fundo obtém em suas operações é distribuído aos cotistas na forma de rendimentos mensalmente; esses rendimentos funcionam como uma renda passiva.
Contudo, existe uma terceira forma de ser remunerado, que é alugando suas cotas no mercado.
Na verdade, esse método é muito usado por investidores que têm um horizonte de investimento de longo prazo e que, por isso, não querem negociar suas cotas no curto prazo.
Dessa forma, eles podem emprestar suas cotas para especuladores que apostam na desvalorização do fundo e ser remunerado pelo tempo que o ativo ficou emprestado.Risco Os FIIs são ativos de renda variável, então seu maior risco é o de mercado.
O risco de mercado acontece pela possibilidade de termos prejuízo por causa de uma variação negativa no preço dos ativos. Na maioria dos ativos do mercado financeiro, existe um mercado em que atuam as forças de oferta e demanda. Se a demanda for maior que a oferta, o preço sobe e vice-versa.
Como dissemos, as cotas dos FIIs são negociadas em bolsa. Desse modo, podemos acompanhar constantemente a oscilação do preço das cotas dos fundos.
Naturalmente, a demanda e a oferta da cota vão variar por algum motivo.
Os motivos principais são variações na taxa de juros, ritmo da economia e o desempenho das próprias operações do fundo.
Então, é importante que o investidor fique atento a esses indicadores. Liquidez Liquidez é a velocidade e a facilidade em que um ativo pode se converter em dinheiro sem que haja perda significativa do valor. Em síntese, a falta de liquidez acontece pelo baixo volume de negociação em um mercado.
Veja o exemplo dos imóveis tradicionais. É comum vermos pessoas que estão há muito tempo tentando vender uma casa, mas não conseguem por falta de comprador. Caso elas queiram vender rápido, elas teriam que abaixar muito o valor do imóvel. Logo, esse ativo não tem liquidez.
Dessa forma, se quiser vender um ativo, não vai conseguir rapidamente ou terá que baixar o preço para atrair compradores. Em ambos os casos, a liquidez é baixa.
Nesse sentido, também existe o risco de liquidez, que é o risco de perder dinheiro caso você não consiga resgatar seus investimentos quando precisa.
No caso dos fundos imobiliários, grande parte deles tem uma boa liquidez na maior parte, pois o volume de negociação é alto. Como investir em fundos imobiliários
O processo de como investir em fundos imobiliários é semelhante ao de qualquer ativo que se negocia no ambiente de bolsa.
Como todo ativo negociado na bolsa, os FIIs têm um código próprio, chamado de ticker, que indica o fundo correspondente.
Em sites especializados, você pode achar os códigos de vários fundos através de um filtro por segmento, por exemplo.
De todo modo, é preciso ter uma conta em uma corretora de valores, acessar o home broker e digitar o código do fundo correspondente.
Dentre as melhores corretoras do Brasil, uma excelente opção para investir em fundos imobiliários é a XP Investimentos. É importante que você saiba também que o preço da cota de cada fundo varia de fundo para fundo. Existem aqueles que são negociados por cerca de R$ 10,00 a cota, enquanto outros custam mais de R$ 1.000,00.
Por fim, para otimizar seu processo de como investir em fundos imobiliários, recomenda-se que você saiba qual parcela da sua carteira de investimentos estará alocada nesse tipo de ativo.
Dessa forma, você só vai investir aquele valor que esteja de acordo com a alocação ideal. Tipos de fundos imobiliários Existem duas formas de classificar os fundos imobiliários: uma mais ampla e outra mais específica.
Na classificação mais ampla, os fundos são divididos em:
Fundos de Tijolo: investem em ativos físicos;
Fundos de Papel: investem em ativos de renda fixa vinculados ao setor imobiliário;
Fundos Híbridos: investem em ativos físicos e em ativos de renda fixa.
Em uma classificação mais específica, existem os:
Fundos de Desenvolvimento Imobiliário;
Fundos de Shoppings;
Fundos de Lajes Corporativas;
Fundos de Galpões Industriais;
Fundos de Hotéis;
Fundos Educacionais;
Fundos de Hospitais;
Fundos de Fundos;
Fundo de Agências Bancárias;
Fundos de Varejo;
Entre outros.
Meu objetivo não é apresentar uma definição completa de cada uma dessas categorias, mas apenas mostrar que existem diversas classificações que suprem as necessidades e se enquadram nas estratégias dos mais diversos tipos de investidores.  Tributação dos fundos imobiliários  Os fundos imobiliários são isentos de imposto de renda em seus rendimentos, o que é uma vantagem para o investidor.
Contudo, no que diz respeito à valorização da cota, você terá que pagar 20% sobre o ganho de capital, sem nenhum tipo de isenção.
Ou seja, se você investiu R$ 10.000,00 em um fundo específico, e este valorizou transformando seu investimento em R$ 15.000,00, você terá que pagar 20% sobre R$ 5.000,00 caso decida fazer o resgate.  Além disso, o recolhimento desse imposto é responsabilidade do investidor, que terá que emitir uma DARF no site da Receita Federal e realizar o pagamento.
E até quando você deverá pagar? Até o último dia útil do mês posterior ao mês que você teve lucro. Por que investir em fundos imobiliários?
Mas, afinal, quais são as vantagens de se investir em fundos imobiliários?
Fácil compreensão: é muito simples de entender a dinâmica dos FIIs, pois é algo comum na vida do brasileiro comprar imóveis, colocar para alugar e viver com a renda dos aluguéis;
Risco menor: como ativo de renda variável, os FIIs têm riscos inerentes que vêm da oscilação dos preços; contudo, se compararmos com outros ativos de RV, eles têm um risco menor, até porque o modelo de negócio é menos dinâmico;
Isenção de IR: se tiver um imóvel, tem que pagar IPTU, mas quando se tem um FII, só paga Imposto de Renda se vender a cota com lucro (os proventos são isentos); isso significa que eu posso ser cotista de um fundo durante décadas, receber os proventos dele e não paga um centavo de imposto;
Diversificação: apesar de haver FII com um imóvel só, a maioria detém vários ativos na carteira, ou seja, você vai adquirir muitos imóveis/títulos por um preço baixo;
Liquidez: vender um imóvel nem sempre é fácil, mas vender um FII (a maioria tem uma boa liquidez) é como vender uma ação, bem rápido;
Gestão profissional: como o FII é um fundo de investimento, existe um gestor profissional que é pago para gerenciar os ativos do fundo, ou seja, você vai pagar para alguém capacitado gerenciar uma carteira de ativos ligados ao setor imobiliário;
Reinvestimento: se eu ganho aluguel de um imóvel que eu tenho, eu não posso investir ele na casa e ganhar mais alguns centavos do inquilino; a única forma de eu ganhar é aumentando o aluguel ou comprando outro imóvel; no caso dos FIIs, o reinvestimento é fácil e simples, então eu posso só comprar outras cotas com o valor dos proventos que eu já recebo;
Investimento inicial baixo: enquanto um imóvel mais simples é pelo menos 60.000 reais, eu consigo investir em FIIs a partir de 10 reais;
Proteção contra a inflação: como todo imóvel, os dos FIIs têm seus aluguéis corrigidos por um índice de preços, ou seja, seus proventos sempre vão crescer de acordo com a inflação;
Facilidade de investimento: investir em imóveis demanda tempo e burocracia, mas escolher um bom FII demanda apenas algumas horas de estudo e pode ser feito da própria casa pela internet, através de sites especializados; e
Previsibilidade da renda: existem vários ativos de renda variável que são fontes de renda passiva, contudo o diferencial dos fundos imobiliários é que a distribuição de seus proventos é mensal, ou seja, essa frequência auxilia muito no planejamento financeiro.
            """
        )

    def subcapitulo8_3():
        criar_subcapitulo(
            "Financiamento imobiliário",
            """
            De forma resumida, trata-se de pegar dinheiro emprestado com um banco para comprar um imóvel.
O método mais comum é o comprador pagar um valor de entrada e solicitar o restante ao banco. Esse montante será pago em prestações acrescidas de juros por um prazo que, dependendo do banco, pode se estender por até 35 anos.
Caso você seja um investidor de imóveis, vale lembrar que, durante o período de financiamento, o imóvel fica ligado a você, mas não pode ser negociado. Ou seja, uma revenda será impossível enquanto a dívida com o banco não for paga.
Tipos de financiamento
No dinâmico cenário de financiamento imobiliário, os consumidores têm à disposição diversas opções, cada uma com suas características e requisitos específicos. Neste tópico, exploraremos os principais tipos de financiamento imobiliário disponíveis no Brasil, destacando as vantagens e particularidades de cada um. Desde o Sistema Financeiro de Habitação (SFH) até o Sistema Financeiro Imobiliário (SFI), passando pelo programa governamental Casa Verde e Amarela e o financiamento direto com construtoras, examinaremos como essas modalidades podem influenciar a aquisição da casa própria e as considerações que os compradores devem levar em conta ao escolher a opção mais adequada às suas necessidades e metas financeiras.
Sistema Financeiro de Habitação (SFH)
O SFH é o principal programa de financiamento imobiliário do país, regulamentado pelo governo federal. Suas principais características incluem:
Financiamento de imóveis de até R$ 1,5 milhão.
Taxas de juros máximas de 12% ao ano.
Disponível apenas para pessoas físicas.
Utilização de recursos do Fundo de Garantia do Tempo de Serviço (FGTS) e do Sistema Brasileiro de Poupança e Empréstimo (SBPE).
Valor máximo financiado correspondendo a 80% do valor total do imóvel.
Restrição de que a parcela mensal não pode comprometer mais de 30% da renda mensal do mutuário.
Proibição de ter outra linha de crédito semelhante em aberto.
Possibilidade de utilizar o FGTS para compor a entrada ou amortizar o financiamento.
Sistema Financeiro Imobiliário (SFI)
O SFI abriga diversas modalidades de financiamento imobiliário e não é regulamentado pelo governo federal. Suas principais características incluem:
Disponível para pessoas físicas e jurídicas.
Regras menos rígidas, com condições estabelecidas pelos agentes financeiros.
Não há um valor máximo para imóveis financiados.
As taxas de juros podem ser mais elevadas, frequentemente acima de 12% ao ano.
Pode financiar de 80% a 90% do preço do imóvel.
Prazo de pagamento pode chegar a 35 anos (420 meses).
Permite o uso do FGTS para abatimentos desde 2021.
Programa Minha Casa, Minha Vida
Este programa governamental é voltado para famílias de baixa renda e tem como objetivo facilitar a aquisição da casa própria. Criado em 2009, oferece subsídios e taxas de juros reduzidas para tornar acessível a aquisição de moradias populares.
Após um período de interrupção, o MCMV foi retomado em 2023 trazendo algumas mudanças, como especificações aprimoradas e isenção de prestações para beneficiários do Bolsa Família e BPC. O programa atende famílias com renda bruta de até R$ 8 mil em áreas urbanas e R$ 96 mil em áreas rurais, divididas em três faixas de renda:
Faixa 1:
Renda Familiar (Bruta) Mensal até R$ 2.640,00.
Renda Familiar (Bruta) Anual em Áreas Rurais até R$ 31.680,00.
Faixa 2:
Renda Familiar (Bruta) Mensal de R$ 2.640,01 a R$ 4.400,00.
Renda Familiar (Bruta) Anual em Áreas Rurais de R$ 31.608,01 a R$ 52.800,00.
Faixa 3:
Renda Familiar (Bruta) Mensal de R$ 4.400,01 a R$ 8.000,00.
Renda Familiar (Bruta) Anual em Áreas Rurais de R$ 52.800,01 a R$ 96.000,00.
As famílias devem satisfazer requisitos de renda e não podem possuir qualquer imóvel registrado em seus nomes.
Financiamento direto com a construtora
Esta modalidade é menos burocrática, mas as condições de crédito podem ser menos favoráveis:
Não há regulamentação específica.
Prazos de pagamento geralmente mais curtos, até 20 anos.
Taxas de juros podem ser mais altas em comparação às instituições financeiras.
Adequado para quem deseja adquirir imóveis prontos com rapidez.
Necessário quando o imóvel está na planta, parte financiada diretamente com a construtora e parte com o banco.
Financiamento pelo FGTS
O financiamento com o FGTS pode ser feito no âmbito do Sistema Financeiro de Habitação (SFH). Só podem participar pessoas com uma determinada renda familiar máxima, que varia de acordo com a região do país, e os valores máximos do imóvel e do financiamento são definidos periodicamente.
Optando por usar o FGTS para habitação, você poderá:
Dar entrada no financiamento, constituindo parte do pagamento ou do valor total;
Quitar totalmente  ou parcialmente sua dívida;
Diminuir em até 80% o valor das prestações em 12 meses.
Confira as condições no site da Caixa Econômica Federal.
Financiamento com construtoras
A negociação do imóvel direto com a construtora é a melhor opção para quem busca flexibilidade, uma vez que há imposição de limites sobre os valores financiados, renda ou taxas de juros. Normalmente, o cliente precisa dar uma entrada e negocia o restante do valor com a empresa.
Como o processo não tem a mediação dos bancos, os custos acabam ficando menores. No entanto, não se pode descartar o risco de a construtora falir e deixar a pessoa que iniciou o financiamento sem imóvel.
Por isso, é importante visitar outros empreendimentos da construtora e checar se ela não tem problemas judiciários. Além disso, as condições variam de uma construtora para a outra e é fundamental ler o contrato com muita atenção.
Como fazer financiamento pelo banco?
Depois de escolher o melhor banco para pedir o financiamento, a primeira etapa será comprovar sua identidade, estado civil e renda. Confira nesse post a lista dos documentos necessários para compra de imóvel.
A comprovação de renda indicará sua capacidade de pagamento, uma vez que o valor das parcelas não pode ser maior que 30% da renda familiar bruta. Além disso, também é feita uma verificação em cadastros de inadimplentes antes de liberar o crédito.
Após essa análise, o banco fará a avaliação do imóvel para confirmar o seu valor. Se tudo estiver correto, a instituição financeira elabora o contrato para que comprador e vendedor o assinem.
Após o registro do contrato em cartório, o crédito será liberado para o pagamento do vendedor. A partir de então, o comprador passará a pagar as prestações mensais para quitar a dívida com o banco.
Etapas do financiamento imobiliário
Comprar uma casa envolve um planejamento cuidadoso e a consideração de diversos fatores importantes. Aqui estão os passos essenciais.
1. Planejamento Financeiro
Adquirir uma casa é um compromisso de longo prazo que envolve um financiamento imobiliário. É crucial avaliar seu orçamento e determinar quanto da sua renda mensal pode ser alocada para o pagamento da parcela do financiamento.
Certifique-se de que o comprometimento da renda não exceda 30% da sua renda bruta.
2. Escolha do Imóvel
Defina o tipo de imóvel que atenda às necessidades da sua família. Pesquise a região desejada, conheça a vizinhança e verifique se o local está de acordo com suas expectativas.
3. Pesquisa de Taxas em Vários Bancos:
Compare as condições oferecidas por diferentes instituições bancárias e fique atento às taxas de juros, pois elas afetam o custo total do financiamento.
Considere o relacionamento com o banco, pois isso pode influenciar a cota e as taxas de juros.
4. Documentação Necessária:
Prepare toda a documentação necessária, incluindo identificação, comprovante de endereço, holerites, declaração de Imposto de Renda, extrato do FGTS, entre outros.
5. Análise da Renda:
Comprove sua renda para o financiamento, lembrando que o valor da parcela não deve exceder 30% da renda familiar. Idade, renda, histórico de pagamento (score bancário) e restrições ao crédito são considerados pelos bancos.
6. Avaliação do Imóvel:
Uma empresa especializada avaliará o imóvel para determinar seu valor.
7. Assinatura do Contrato e Registro:
Após a análise dos documentos, ocorre a assinatura do contrato entre compradores e vendedores. O contrato é registrado no cartório de imóveis competente.
8. Liberação do Dinheiro:
Após o registro do imóvel, o dinheiro é liberado para o vendedor em até cinco dias.
Seguir esses passos e planejar cuidadosamente ajudará a tornar esse processo mais suave e bem-sucedido. Certifique-se de consultar um consultor financeiro ou um corretor imobiliário para orientação adicional.
            """
        )

    def subcapitulo8_4():
        criar_subcapitulo(
            "Impostos e custos envolvidos na compra e venda de imóveis",
            """
            O Imposto de Transmissão de Bens Imóveis — mais conhecido pela sigla ITBI — é um tributo municipal que deve ser pago quando ocorre uma transferência imobiliária.
Dessa forma, a oficialização do processo de compra e venda só será feita após o seu acerto, sendo que, sem a confirmação de pagamento do tributo, o imóvel não pode ser transferido e a documentação não é liberada.
Previsto na Constituição Federal, esse imposto é cobrado apenas quando ocorre a transmissão de posse de um imóvel envolvendo pessoas vivas.
Quando há sucessão por meio do falecimento ou doação, é cobrado o Imposto sobre Transmissão “Causa Mortis” e Doação (ITCMD).
Em geral, é necessário que se reúna uma série de documentos para emitir a guia de recolhimento do imposto, como contratos, comprovantes de pagamento e formulários próprios de cada município.
Por que deve se pagar o ITBI?
É preciso que o comprador quite esse tributo para que ocorra a transferência de propriedade do bem adquirido para o seu nome.
Sendo assim, esse imposto é importante para regularizar o imóvel nos registros públicos e garantir o acesso a serviços como asfaltamento das ruas, coleta de lixo, instalação e abastecimento de água e luz, entre outros.
Além disso, é importante lembrar que, por se tratar de uma taxa cobrada pela Prefeitura Municipal, os recursos arrecadados pela cobrança do ITBI são utilizados para o benefício dos próprios munícipes, assim como o IPTU.
Quando se deve pagá-lo?
O ITBI deve ser recolhido pelo município sempre que houver a transmissão da propriedade de um imóvel envolvendo uma pessoa física, exceto em casos de sucessão por falecimento ou doação.
Alguns municípios instituem que o ITBI deve ser pago após a lavratura da escritura pública, enquanto outros estabelecem que o recolhimento precisa ser efetuado depois do registro da escritura. Portanto, fique atento a isso e procure saber como funciona na cidade onde a transação imobiliária foi realizada. 
Os prazos de pagamento também podem variar de acordo com a cidade onde a venda é feita. No entanto, é comum que os vencimentos para a quitação do imposto sejam próximos à efetuação da transmissão do imóvel, mais ou menos após um mês da conclusão da compra.
Quem deve pagar esse imposto?
A Legislação Federal não deixa claro quem é responsável por quitar o ITBI. Portanto, é comum que essa questão seja regulamentada por uma lei municipal.
Na maioria dos casos, ficou estabelecido que o comprador seria o responsável pelo pagamento do ITBI.
Mesmo que não haja uma regra clara sobre essa questão, é uma prática comum do mercado que o consumidor se responsabilize por esse imposto, que comumente é pago no início do processo de financiamento imobiliário.
Entretanto, nada impede que as partes envolvidas na negociação façam um acordo no qual o vendedor assuma, parcial ou totalmente, esse compromisso.
Desse forma, para evitar maiores problemas, o ideal é consultar a legislação da sua cidade — o que se tornou uma tarefa bem mais simples com a Internet.
Por que pagar esse imposto?
O motivo pelo qual esse imposto não deve ser negligenciado é o fato dele ser o responsável pela transferência do imóvel para o nome do novo proprietário no Cartório de Registro de Imóveis.
Além disso, ele garantirá que o proprietário tenha acesso a serviços públicos essenciais oferecidos pelo município, como o asfaltamento das ruas, coleta de lixo, a instalação e o abastecimento de água e luz, entre outros.
Ademais, é preciso ressaltar que arcar com impostos é uma obrigação de qualquer cidadão. Lembrando que os valores recolhidos são direcionados para melhorias nas cidades e bairros, em benefício dos contribuintes.
Qual é o valor do ITBI e quem o define? 
Uma das principais características do ITBI é que não é cobrado um valor fixo por esse tributo.
Para definir o montante a ser pago é necessário considerar o valor venal (valor de venda) constado na guia de recolhimento do Imposto Predial e Territorial Urbano (IPTU), que se altera de acordo com a cidade, assim como a alíquota do imposto, que também é variável conforme a cidade.
Também é possível definir o custo por meio do preço registrado no contrato de compra e venda — a escritura também poderá ser utilizada.
No entanto, devido às cobranças indevidas de algumas prefeituras, o Superior Tribunal de Justiça (STJ) teve um entendimento de que o ITBI deve ser calculado sobre o valor de compra do imóvel, mesmo que ele seja superior ao valor venal informado no IPTU. Assim, a cobrança desse imposto estaria coerente com o valor real do bem.
Todavia, isso não ocorre na prática, uma vez que, ao ficar constatado que o valor venal é superior ao montante da negociação, a maioria das prefeituras utiliza o maior preço como base de cálculo desse tributo.
Como essa prática é ilegal, o contribuinte que se sentir prejudicado poderá entrar com um recurso, administrativo ou judicial, para que o ITBI seja calculado de acordo com o entendimento do STJ.
Como o ITBI é calculado?
Para determinar o montante a ser pago de ITBI não é necessário a realização de operações matemáticas complexas. Com o auxílio de uma calculadora, basta multiplicar a alíquota do imposto com o valor venal do imóvel. O resultado dessa conta é a quantia a ser quitada.
Suponhamos que você deseja comprar um apartamento que custa R$ 200 mil. Caso a alíquota seja de 2%, a quantia a ser paga de imposto será de R$ 4 mil, ou seja:
200.000 (valor do imóvel) x 2% (alíquota do imposto, conforme município) = 4.000.
Quais são as alíquotas cobradas?
Pelo fato de o ITBI ser um tributo municipal, a Constituição Federal estabelece que cada prefeitura tem a autonomia para definir as regras sobre a cobrança desse imposto.
Sendo assim, cada cidade pode determinar o valor da alíquota que será usada como base de cálculo.
Nos grandes centros urbanos, por exemplo, as taxas variam entre 2% e 3%.
Quais as alíquotas nas principais cidades do País?
Nas principais cidades do País a alíquota do ITBIé a seguinte:
São Paulo (SP): 3%;
Rio de Janeiro (RJ): 3%;
Belo Horizonte (MG): 3%;
Recife (PE): 3%;
Porto Alegre (RS): 3%;
Salvador (BA): 1% para imóveis populares e 3% para os demais;
Curitiba (PR): 2,7%.
Os valores e taxas adicionais podem ser consultados diretamente na Secretaria da Fazenda ou Finanças do Município.
Em algumas cidades, as alíquotas podem variar de acordo com o valor e tipo de financiamento imobiliário ou compra do imóvel.
Geralmente, moradias populares ou que estejam vinculadas a algum programa do Governo Federal ganham descontos para pagar o ITBI.
É possível conseguir desconto?
Assim como acontece com as isenções, cada município tem autonomia para definir as regras que estabelecem a existência ou não de desconto no pagamento do ITBI.
É preciso consultar a legislação municipal para descobrir em quais condições ocorrem a diminuição na cobrança do imposto.
É comum algumas prefeituras, como a de São Paulo, conceder desconto para os beneficiários de programas habitacionais que adquirirem o primeiro imóvel.
De forma semelhante, existem legislações municipais que favorecem os contribuintes que quitarem o ITBI antes da lavratura da escritura.
Qual o prazo para pagamento do ITBI?
O pagamento do Imposto sobre Transmissão de Bens Imóveis, em geral, deve ser feito de 30 a 60 dias após a solicitação das guias de recolhimento. No entanto, como o pagamento desse imposto é pré-requisito para registrar o imóvel, é de interesse do comprador quitá-lo o mais rapidamente possível. 
Vale ressaltar que, em alguns municípios, é permitido o parcelamento desse imposto. Daí a importância de entrar em contato com a prefeitura para saber as condições de pagamento do ITBI. Se for o caso, é exigido pelo órgão recolhedor o pagamento da primeira parcela para seguir com o processo.
Quanto à isenção, por ser uma taxação em nível municipal, cada prefeitura tem suas próprias regras para isentar (ou não) o pagamento. No entanto, em caso de falecimento, a propriedade é transferida para seus sucessores com isenção de taxa.
Quando não é necessário pagar o ITBI?
Conforme consta na Constituição Federal, o ITBI é um tributo que incide em uma transação imobiliária entre pessoas vivas. Portanto, caso ocorra o falecimento do proprietário, não ocorre a incidência do imposto na transmissão de propriedade por herança. O mesmo acontece quando o bem é doado a um terceiro — em ambas as situações é cobrado o ITCMD (Imposto sobre Transmissão “Causa Mortis” e Doação). 
O tributo também não é cobrado quando a propriedade for adquirida por uma pessoa jurídica que pretenda utilizá-lo. No entanto, o ITBI é normalmente incidido quando a empresa adquire o imóvel com o objetivo de vendê-lo ou locá-lo. Também não há cobrança nas devoluções de imóveis.
Dependendo da legislação municipal, existem situações em que ocorre isenção do imposto para determinadas faixas de valores.
O mesmo acontece quando o comprador é beneficiário de algum programa habitacional do Governo Federal.
O que fazer em caso de atraso?
Caso o comprador perca o prazo de pagamento do ITBI, em geral, ele não sofrerá nenhuma penalidade. Mas em algumas cidades pode haver multa.
Entretanto, não será possível realizar a transmissão de propriedade do bem adquirido naquele momento.
Se essa situação vier a acontecer, será preciso reiniciar o processo de solicitação de cálculo do imposto na prefeitura para gerar um novo boleto.
Preciso pagar ITBI mesmo se comprar o imóvel na planta?
Mesmo que você compre um apartamento ou casa ainda na planta, o pagamento do ITBI é obrigatório assim que as condições citadas nos tópicos acima forem concretizadas.
No caso desse tipo de compra, é utilizado o valor do imóvel quando estiver pronto para calcular o montante a ser pago de imposto.
É preciso muita atenção para as ofertas que prometem valores menores do ITBI para apartamentos comprados na planta.
Como planejar o pagamento do ITBI?
É recomendado sempre reservar um valor aproximado para pagar os impostos e documentação na hora de receber o imóvel. Isso é importante, pois algumas prefeituras não permitem o parcelamento do imposto.
As transações imobiliárias podem parecer muito complicadas mas, no final, é tudo uma questão de pesquisar pela informação certa. Agora que você já sabe o que é ITBI e sua importância na negociação, pois é ele que garante que o imóvel seja transferido para o seu nome no Cartório de Registro de Imóveis, não deixe de se informar sobre o seu valor ao negociar a tão sonhada casa própria.
            """
        )

    def subcapitulo8_5():
        criar_subcapitulo(
            "Gestão de um imóvel alugado",
            """
            Estratégias para fixar um valor de locação adequado

Fixar um valor de locação adequado para o seu imóvel é fundamental para atrair inquilinos e garantir um retorno financeiro satisfatório. Para determinar um preço justo, é essencial realizar uma análise de mercado, considerando os valores de imóveis similares na mesma área. 
Fatores como localização, tamanho, condições do imóvel e comodidades oferecidas desempenham um papel crucial na definição do preço. É importante também estar atento às tendências do mercado imobiliário da sua região, ajustando o valor de acordo com a demanda e a oferta. 
Uma precificação adequada não só aumenta as chances de locação rápida, mas também ajuda a manter uma boa relação com os futuros inquilinos, equilibrando rentabilidade e competitividade no mercado.

Divulgação

A divulgação eficaz do seu imóvel para locação é um processo muitas vezes negligenciado, mas que exige muita atenção para que você alcance o público certo e garanta uma locação satisfatória. 
Utilizar plataformas online, como sites de imóveis e redes sociais, é uma maneira eficiente de atingir um vasto público que estão buscando por imóveis. 
Fotos de alta qualidade e descrições detalhadas do imóvel podem aumentar significativamente o interesse das pessoas. 
Incluir informações sobre a localização, proximidade com serviços essenciais e infraestrutura do bairro ajuda a destacar o imóvel. 
Além do marketing digital, métodos tradicionais como placas de “aluga-se” e anúncios em jornais locais ainda têm seu valor, especialmente para alcançar um público local específico. 
Estratégias de divulgação bem planejadas e executadas, que utilizam tanto canais digitais quanto tradicionais, são fundamentais para aumentar a visibilidade do seu imóvel e atrair inquilinos potenciais.

Contrato de locação

Elaborar um contrato de locação sólido é crucial para a administração efetiva de imóveis. O contrato deve detalhar claramente os termos e condições da locação, incluindo o valor do aluguel, duração do contrato, regras sobre manutenção e quem arcará com as despesas pertinentes. 
É importante assegurar que o contrato esteja em conformidade com a legislação vigente, protegendo os direitos tanto do locador quanto do locatário.
Incluir cláusulas específicas sobre o uso da propriedade, políticas, e condições para rescisão ou renovação do contrato também é essencial. 
Uma redação clara e sem ambiguidades ajuda a prevenir mal-entendidos e possíveis disputas legais no futuro. Para proprietários iniciantes, pode ser aconselhável buscar a assistência de uma imobiliária ou de um advogado especializado para garantir que todos os aspectos legais e práticos estejam adequadamente cobertos no contrato de locação.


Seleção e gestão de inquilinos

A seleção e gestão cuidadosa de inquilinos são componentes chave na administração bem-sucedida de locações. Iniciar com uma seleção rigorosa é fundamental. Isso inclui verificar antecedentes financeiros, histórico de locações anteriores e, em alguns casos, referências pessoais ou profissionais. Esta abordagem ajuda a garantir que os inquilinos sejam confiáveis e capazes de cumprir com as obrigações do contrato.
Uma vez selecionados, manter uma boa relação com os inquilinos é essencial para a gestão tranquila do imóvel. Isso envolve comunicação clara e regular, sendo responsivo às suas necessidades e garantindo que quaisquer problemas com o imóvel sejam resolvidos prontamente. 
Estabelecer expectativas claras desde o início e ser consistente na aplicação das políticas do contrato pode prevenir muitos problemas na locação.
Além disso, implementar sistemas eficazes para a cobrança de aluguéis e manutenção ajuda a manter a organização e a eficiência na gestão dos inquilinos, contribuindo para uma experiência positiva para ambas as partes.

Vistoria de imóvel para locação

A vistoria de locação deve ocorrer em dois momentos: Na entrada de um novo inquilino, e em sua saída do imóvel. A vistoria de entrada tem como objetivo descrever o estado do imóvel antes da entrada do inquilino, como guia para a entrega do imóvel. Ao final da locação, o inquilino deve restaurá-lo para a forma como recebeu. Na vistoria de saída, é verificado se isto foi feito. 
As duas vistorias devem ser transformadas em laudos, que são anexados no contrato de locação e no distrato ao final.
A vistoria de entrada funciona da seguinte forma: O vistoriador, geralmente algum técnico ou até mesmo o corretor, vai até o imóvel, e faz um levantamento descrevendo o estado do imóvel e de tudo que faz parte dele. Depois, o inquilino tem um tempo para contestar o descrito pelo técnico/corretor. Esse tempo pode ser, em média, 5 a 10 dias. O inquilino precisa deste tempo para avaliar a situação – principalmente – hidráulica e elétrica, que só podem ser avaliadas com o uso.
A vistoria de saída ocorre após a retirada dos bens do inquilino e entrega das chaves. O responsável pela parte do proprietário (corretor, imobiliária ou técnico) vai até o imóvel e faz o levantamento dos mesmos quesitos apontados na entrada, averiguando se o estado é o mesmo. Caso haja alguma divergência, o inquilino deve pagar pelo dano ou restituir o estado em um curto período.
 
Para a realização da vistoria as partes podem contratar técnicos, para averiguar questões que nós, leigos, não somos capazes (como a hidráulica e a elétrica). Fica a critério dos envolvidos e não é uma regra. Mas, lembrando que, quanto mais completa a vistoria, mais garantias você terá.

Manutenção regular no imóvel

A manutenção regular do imóvel é crucial para preservar seu valor e assegurar a satisfação do inquilino. A manutenção preventiva sempre que há a troca de inquilinos pode ser essencial para evitar reparos dispendiosos no futuro e manter o imóvel em ótimas condições. Isso inclui verificar sistemas essenciais, como elétrica, hidráulica, além de cuidar da pintura, limpeza e paisagismo.
É importante responder prontamente a qualquer solicitação de reparo por parte dos inquilinos. Resolver problemas rapidamente não apenas melhora a relação locatário-locador, mas também evita que pequenos problemas se tornem grandes preocupações. 
Ter uma lista de contatos de confiança, como eletricistas, encanadores e outros profissionais de manutenção, pode facilitar esse processo.
Manter registros detalhados de todas as manutenções e reparos realizados também é essencial, pois oferece um histórico útil do cuidado e melhorias feitas no imóvel ao longo do tempo. Uma manutenção regular e eficaz assegura que o imóvel permaneça atraente e funcional, protegendo seu investimento e mantendo a satisfação dos inquilinos.

Lidando com problemas comuns na locação

Lidar com problemas comuns na locação de imóveis exige preparação e uma abordagem proativa por parte do proprietário. Questões frequentes incluem atrasos no pagamento do aluguel, danos à propriedade causados pelo inquilino, e desacordos sobre responsabilidades de manutenção.
Manter uma boa relação com os inquilinos pode facilitar a resolução de problemas. Por isso, invista tempo em responder o locatário sempre que este acionar você, dedique-se a uma resolução rápida e efetiva dos problemas.
Em situações mais desafiadoras, pode ser necessário buscar aconselhamento legal ou a intervenção de uma imobiliária especializada. Eles podem oferecer suporte na mediação de conflitos e garantir que as questões sejam resolvidas de forma justa e conforme as leis locais. Lidar com esses problemas de forma eficiente e justa é crucial para manter uma relação saudável com os inquilinos e a integridade do seu investimento imobiliário.

O que fazer quando o inquilino não paga o aluguel?

Quando um inquilino não paga o aluguel, a primeira etapa é tentar uma abordagem comunicativa e compreensiva. Entre em contato para entender as razões do atraso e discutir possíveis soluções, como um plano de pagamento. 
Se a inadimplência persistir, é importante revisar o contrato de locação para verificar as cláusulas relacionadas a atrasos e possíveis penalidades. 
Em última instância, pode ser necessário iniciar procedimentos legais para cobrança ou despejo, conforme as leis locais. Para estas situações, contar com o apoio de uma imobiliária ou assessoria jurídica especializada pode ser crucial para resolver o problema de maneira eficaz e legal.

O que fazer quando o inquilino não paga alguma taxa?

Se um inquilino não pagar alguma taxa associada ao aluguel, como taxas de condomínio, água, luz e outras, a primeira ação é entender se é de sua responsabilidade a cobrança do débito.
Por exemplo, para o pagamento do condomínio ou IPTU você pode fazer a cobrança. Já no caso de inadimplência de água ou luz, são as empresas de fornecimento as responsáveis pela cobrança, visto que o inquilino deve assumir a titularidade da matrícula do imóvel assim que a locação inicia. 
Leia tudo sobre o assunto em: Contas pendentes de água e luz em imóveis locados, o que fazer?
Para as taxas que são de sua responsabilidade de pagamento, e por consequência é você quem deve cobrar do inquilino e repassar ao recebedor (como no caso do IPTU e muitas vezes do condomínio), é importante sempre esclarecer a responsabilidade pelo pagamento dessas taxas, conforme estabelecido no contrato de locação. 
Uma conversa amigável pode resolver mal-entendidos ou questões de esquecimento. Se o não pagamento persistir, deve-se rever o contrato para determinar as consequências contratuais e legais. 
Em casos de não-resolução, pode ser necessário buscar aconselhamento jurídico ou apoio de uma imobiliária para mediar a situação e tomar as medidas apropriadas, respeitando sempre a legislação vigente.

Rescisão ou quebra de contrato

No caso de rescisão ou quebra de contrato de locação, é crucial agir de acordo com as cláusulas estabelecidas no contrato e a legislação local. Se o inquilino desejar rescindir o contrato antes do prazo, deve-se verificar as condições previstas, como a necessidade de aviso prévio ou penalidades. 
Por outro lado, se o locador identifica uma quebra de contrato por parte do inquilino, como danos ao imóvel ou uso indevido da propriedade, é importante documentar as infrações e buscar uma resolução conforme as diretrizes contratuais. 
Em ambas as situações, a comunicação clara e a busca por uma solução amigável são sempre recomendadas. Contudo, se não for possível uma resolução consensual, pode ser necessário recorrer a medidas legais, com o suporte de profissionais especializados para garantir que os direitos e deveres de ambas as partes sejam respeitados.

Entendendo os aspectos legais e fiscais da locação

Compreender os aspectos legais e fiscais da locação de imóveis é fundamental para qualquer proprietário. Legalmente, é essencial estar em conformidade com a legislação vigente, incluindo as regras da Lei do Inquilinato e as normativas municipais específicas. 
Isso envolve compreender os direitos e deveres tanto do locador quanto do locatário, além de estar atento às regras de reajuste de aluguel e procedimentos para rescisão de contrato.
Do ponto de vista fiscal, os proprietários devem se informar sobre os impostos aplicáveis aos rendimentos de aluguel. É necessário declarar os ganhos de aluguel no Imposto de Renda e entender as possíveis deduções fiscais relacionadas à propriedade alugada. 
Manter registros financeiros detalhados e precisos é crucial para facilitar a declaração e evitar problemas. Para lidar adequadamente com esses aspectos legais e fiscais, muitos proprietários optam por contar com o auxílio de contadores e advogados especializados, ou uma imobiliária experiente, que pode oferecer orientação e gestão especializada nesses assuntos.

O papel de uma imobiliária na administração da locação

O papel de uma imobiliária na administração da locação de imóveis é vital, oferecendo suporte abrangente e profissional aos proprietários. Uma imobiliária experiente cuida de todos os aspectos do processo de locação, desde a divulgação do imóvel e seleção de inquilinos confiáveis até a gestão de contratos e o recebimento dos aluguéis. 
Ela também desempenha um papel muito importante na manutenção regular do imóvel, garantindo que esteja sempre em ótimas condições e atendendo às demandas dos inquilinos de maneira eficaz.
Além disso, a imobiliária oferece orientação valiosa sobre aspectos legais e fiscais, ajudando os proprietários a navegar pelas complexidades e a garantir a conformidade com a legislação local. 
Em casos de desacordos ou problemas com inquilinos, a imobiliária atua como mediadora, buscando soluções justas e eficazes para todas as partes envolvidas. Assim, contar com os serviços de uma imobiliária pode significar uma administração de locação mais tranquila, eficiente e rentável para os proprietários.
            """
        )

    def subcapitulo8_quiz():
            criar_quiz()

    def subcapitulo8_desafio():
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
            criar_bloco("Mercado imobiliário", lambda _: subcapitulo8_1()),
            criar_bloco("Tipos de investimento em imóveis", lambda _: subcapitulo8_2()),
            criar_bloco("Financiamento imobiliário: Como funciona, taxas de juros, condições e prazos", lambda _: subcapitulo8_3()),
            criar_bloco("Impostos e custos envolvidos na compra e venda de imóveis", lambda _: subcapitulo8_4()),
            criar_bloco("Gestão de um imóvel alugado: Contratos, manutenção, inadimplência", lambda _: subcapitulo8_5()),
            criar_bloco("Quiz", lambda _: subcapitulo8_quiz()),
            criar_bloco("Desafio", lambda _: subcapitulo8_desafio()),
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
