import flet as ft

def Capitulo7Page(page: ft.Page):
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
                "pergunta": "Como o planejamento tributário pode auxiliar uma empresa a lidar com as mudanças constantes na legislação tributária?",
                "alternativas": [
                    {"texto": "O planejamento tributário não pode auxiliar nesse caso, pois as mudanças na legislação são imprevisíveis.", "correta": False},
                    {"texto": "O planejamento tributário é inútil em um ambiente de constante mudança legislativa.", "correta": False},
                    {"texto": "O planejamento tributário pode ajudar a identificar as mudanças e seus impactos na empresa, permitindo ajustes nas estratégias tributárias.", "correta": True},
                    {"texto": "O planejamento tributário pode ser utilizado para criar mecanismos de evasão fiscal e evitar o pagamento de novos impostos.", "correta": False},
                ],
            },
            {
                "pergunta": "Qual a principal diferença entre a COFINS e a CSLL?",
                "alternativas": [
                    {"texto": "A COFINS incide sobre a receita bruta, enquanto a CSLL incide sobre o lucro líquido.", "correta": True},
                    {"texto": "A COFINS é um imposto estadual, enquanto a CSLL é federal.", "correta": False},
                    {"texto": "A COFINS é paga apenas por pessoas físicas, enquanto a CSLL é paga apenas por pessoas jurídicas.", "correta": False},
                    {"texto": "Não há diferença entre os dois impostos.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual dos seguintes itens NÃO pode ser deduzido do Imposto de Renda?",
                "alternativas": [
                    {"texto": "Despesas com educação infantil.", "correta": False},
                    {"texto": "Despesas com tratamento médico.", "correta": False},
                    {"texto": "Contribuições para planos de previdência privada PGBL.", "correta": False},
                    {"texto": "Despesas com cursos de idiomas.", "correta": True},
                ],
            },
                {
                "pergunta": "Qual a principal diferença entre o ITBI e o IPTU?",
                "alternativas": [
                    {"texto": "O ITBI é um imposto federal, enquanto o IPTU é municipal.", "correta": False},
                    {"texto": "O ITBI incide sobre a transmissão de bens imóveis, enquanto o IPTU incide sobre a posse de bens imóveis.", "correta": True},
                    {"texto": "O ITBI é pago uma única vez, enquanto o IPTU é pago anualmente.", "correta": False},
                    {"texto": "Todas as alternativas estão corretas.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a principal diferença entre a sucessão legítima e a sucessão testamentária?",
                "alternativas": [
                    {"texto": "A sucessão legítima é sempre mais vantajosa para os herdeiros.", "correta": False},
                    {"texto": "A sucessão testamentária é mais comum do que a legítima.", "correta": False},
                    {"texto": "Não há diferença entre as duas, pois ambas resultam na transferência de bens após a morte.", "correta": False},
                    {"texto": "A sucessão legítima ocorre por determinação legal, enquanto a testamentária é definida pelo desejo do falecido em testamento.", "correta": True},
                ],
            },
                {
                "pergunta": "Qual a importância do planejamento sucessório para empresas familiares?",
                "alternativas": [
                    {"texto": "O planejamento sucessório é apenas para pessoas físicas com grande patrimônio.", "correta": False},
                    {"texto": "O planejamento sucessório garante que a empresa seja vendida para terceiros após a morte do fundador.", "correta": False},
                    {"texto": "O planejamento sucessório é obrigatório para todas as empresas familiares.", "correta": False},
                    {"texto": "O planejamento sucessório visa garantir a continuidade da empresa e proteger o patrimônio da família.", "correta": True},
                ],
            },
            {
                "pergunta": "Qual é o valor máximo permitido para dedução com despesas de educação por ano?",
                "alternativas": [
                    {"texto": "R$ 2.275,08", "correta": False},
                    {"texto": "12% da renda tributável", "correta": False},
                    {"texto": "R$ 3.561,50", "correta": True},
                    {"texto": "Não há limite", "correta": False},
                ],
            },
                {
                "pergunta": "Qual o principal objetivo dos incentivos fiscais oferecidos pelo governo às pequenas e médias empresas (PMEs)?",
                "alternativas": [
                    {"texto": "Aumentar a arrecadação de impostos para o governo.", "correta": False},
                    {"texto": "Estimular o crescimento econômico e a geração de empregos.", "correta": True},
                    {"texto": "Beneficiar apenas as grandes empresas que investem em tecnologia.", "correta": False},
                    {"texto": "Reduzir a burocracia para as empresas de todos os portes.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual das seguintes opções NÃO é um exemplo de incentivo fiscal para PMEs?",
                "alternativas": [
                    {"texto": "Redução da alíquota do Imposto de Renda.", "correta": False},
                    {"texto": "Aumento da carga tributária sobre produtos importados.", "correta": True},
                    {"texto": "Crédito fiscal para investimento em pesquisa e desenvolvimento.", "correta": False},
                    {"texto": "Isenção de impostos para empresas em zonas de incentivo.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a importância do planejamento tributário internacional para empresas que atuam no mercado global?",
                "alternativas": [
                    {"texto": "É obrigatório para todas as empresas que realizam operações internacionais.", "correta": False},
                    {"texto": "É irrelevante, pois as empresas brasileiras estão sujeitas apenas à legislação brasileira.", "correta": False},
                    {"texto": "Serve apenas para empresas de grande porte.", "correta": False},
                    {"texto": "É importante para evitar a dupla tributação e otimizar a carga tributária em operações internacionais.", "correta": True},
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

    def subcapitulo7_1():
        criar_subcapitulo(
            "Imposto de Renda\nPessoa Física\n(IRPF)",
            """
O contribuinte deverá manter os comprovantes de todos os rendimentos obtidos ao longo do ano passado. Isso inclui informe de rendimento das fontes pagadoras (empresas, governo, pessoas físicas etc.). Também é preciso guardar comprovantes de  rendimentos de aplicações financeiras em bancos e corretoras.
Comprovantes de despesas próprias ou de dependentes com médicos, hospitais e clínicas; com planos de saúde, dentistas e psicólogos. Também com gastos para instrução própria e de dependentes.
Quem paga pensão alimentícia homologada pela Justiça também deve manter os comprovantes de pagamento feitos ao beneficiário. Informações sobre dívidas contraídas no ano anterior, além de comprovantes de eventuais compra e venda de bens móveis e imóveis.
É fundamental manter comprovantes de todas as receitas e despesas dos dependentes, bem como os comprovantes dos seus respectivos bens e direitos. Amorim lembra que é obrigatório guardar por cinco anos todos os documentos referentes à Declaração. Por precaução, ele recomenda que se guarde por pelo menos seis anos.
            
Com tudo em mãos, o primeiro passo é baixar o Programa Gerador da Declaração (PGD IRPF 2023) no site da Receita Federal.
O programa está disponível a partir de 15 de março.
O contribuinte que quiser fazer a declaração por meio de smartphones ou tablets também pode baixar o aplicativo “Meu Imposto de Renda” no Google Play (para Android) ou na AppStore (iOS).
Quem possuir certificado digital ou conta gov.br, poderá acessar o novo portal de serviços da Receita, que no futuro substituirá o antigo Centro Virtual de Atendimento e-CAC. Nesse caso, encontrará a declaração pré-preenchida, bastando apenas validar as informações.
É importante conferir se está ou não obrigado a informar o número do recibo da declaração de ajuste do ano anterior. Segundo Valdir Amorim, consultor do IOB, o contribuinte está dispensado dessa exigência se a soma dos seus rendimentos e dos dependentes, sujeitos ao ajuste anual, for inferior a R$ 200 mil.O programa é autoexplicativo e auxilia no preenchimento, garante o analista. As instruções estão disponíveis a partir do menu “Ajuda” ou acionando a tecla “F1” no campo desejado. O contribuinte deve selecionar na “Tela de Entrada” “nova declaração”, “em preenchimento” ou “já transmitidas”.
A partir daí, o contribuinte deve preencher cada um dos quadros com as informações necessárias. Soares recomenda que, após a entrega, é importante não esquecer de conferir o “status” da declaração. Se tiver alguma pendência, basta regularizar.
            
Quem deve declarar Imposto de Renda
            
Pessoas físicas residentes no Brasil que tiveram, no ano passado, rendimentos tributáveis acima de R$ 30.639,90, como salários;
Quem recebeu rendimentos isentos, não-tributáveis ou tributados exclusivamente na fonte, superiores a R$ 200 mil, em 2023, como doações e herança;
Quem, no ano passado, teve receita bruta superior a R$ 153.199,50 em atividade rural;
Quem pretende compensar prejuízos com a atividade rural de anos-calendário anteriores ou do próprio ano-calendário de 2023.
Quem tinha, em 31 de dezembro de 2023, bens e direitos (como imóveis, veículos e investimentos) que, somados, superavam R$ 800 mil;
As pessoas que tiveram ganhos de capital na alienação de bens ou direitos;
Quem realizou operações de alienação (venda) em bolsas de valores, de mercadorias, de futuros e assemelhadas cuja soma foi superior a R$ 40 mil no ano; ou que teve lucro sujeito à incidência de imposto nas vendas;
Quem vendeu, no ano passado, imóvel residencial e usou o recurso para compra de outra residência para moradia, dentro do prazo de 180 dias da venda, e optou pela isenção do IR;
Pessoas que passaram a residir no Brasil em qualquer mês do ano passado;
Quem possuir investimentos em trust no exterior;
Quem deseja atualizar valor de mercado de bens no exterior;
Quem optou por detalhar bens do exterior da entidade controlada como se fossem da pessoa física.
Quem não se enquadra em nenhuma das hipóteses acima está automaticamente dispensado de apresentar a Declaração de Imposto de Renda.
            
Deduções
            
As deduções do Imposto de Renda são, basicamente, os valores que você pode abater da sua declaração. Entre as deduções estão os gastos feitos ao longo de 2023 que, se declarados, podem reduzir o quanto o contribuinte vai pagar de imposto ou mesmo aumentar a restituição.
Os gastos relacionados à saúde, educação, previdência privada, pensão e dependentes podem ser deduzidos na sua declaração.
No caso de saúde, gastos com consultas médicas particulares, cirurgias plásticas, hospitais, tratamentos odontológicos, fisioterapia, exames laboratoriais, serviços radiológicos, aparelhos ortopédicos, próteses dentárias, entre outros. As despesas médicas realizadas no exterior também podem ser deduzidas.
Em relação à educação, o contribuinte pode deduzir gastos próprios e também os gastos que teve com os seus dependentes. Somente podem ser deduzidas as despesas relacionadas à: educação infantil (creches e pré-escolas); ensino fundamental e ensino médio; educação superior (graduação, pós-graduação, mestrado, doutorado e especialização); e ensino técnico e tecnológico. Deduções de cursos de outros idiomas, como cursos de inglês, por exemplo, ou mesmo aulas de esportes e música, não são permitidas.Ainda, sobre deduções possíveis no âmbito da previdência privada: os contribuintes que têm planos de previdência PGBL (Plano Gerador de Benefício Livre) podem reduzir a base de cálculo do IR em até 12%. A dedução não vale os planos VGBL (Vida Gerador de Benefício Livre).
No caso de pensão alimentícia, o contribuinte que efetua o pagamento pode deduzir o gasto de sua declaração desde que a pensão tenha sido definida por decisão judicial ou por escritura pública (extrajudicial). Vale lembrar que o contribuinte que paga pensão não pode incluir o filho como dependente.
Também é possível deduzir doações feitas: a) aos fundos controlados pelos conselhos municipais, estaduais, distrital e nacional dos Direitos da Criança e do Adolescente, conforme o Estatuto da Criança e do Adolescente (ECA); b) aos fundos controlados pelos conselhos nacional, distrital, estaduais ou municipais do Idoso; e c) ao Fundo Nacional de Cultura (FNC), à produções audiovisuais, entre outros.
Quanto às deduções por dependente, são as mesmas que as do ano passado e a recomendação é verificar se foram incluídas todas as receitas recebidas pelos dependentes. Vale checar também se a renda que o dependente recebe já não o obriga a fazer a declaração sozinho.
Confira os limites das deduções:
Gastos com saúde (não há limites, dentro das regras da Receita)
R$ 3.561,50 por ano com despesas com educação do contribuinte, dependentes ou alimentandos;
Até 12% de rendimentos tributáveis por previdência complementar;
O somatório das deduções de doações feitas para as crianças e adolescentes, os idosos e a cultura está limitado a 6%;
R$ 2.275,08 por dependente, atendidas as regras da Receita.
            """
        )

    def subcapitulo7_2():
        criar_subcapitulo(
            "Impostos sobre\na propriedade",
            """
Qual a diferença entre impostos federais, estaduais e municipais?

Impostos Federais - São responsáveis por cerca de 60% das arrecadações do país. São eles: IOF, II, IPI, IRPF, IRPJ, Cofins, PIS / Pasep, CSLL, INSS.

Impostos Estaduais: São responsáveis por cerca de 28% das arrecadações do país, sendo eles: ICMS, IPVA, ITCMD.

Impostos Municipais: São responsáveis por cerca de 5,5% das arrecadações do país. São eles: IPTU, ISS, ITBI.

Entenda melhor:
Os impostos federais, estaduais e municipais são destinados a manter as suas respectivas máquinas públicas funcionando.
Impostos federais são responsáveis por cerca de 60% (sessenta por cento) do total das arrecadações de impostos no país, sendo os que existem em maior quantidade e também são os mais reconhecidos por suas siglas. Em geral seu destino é a manutenção do Governo Federal. 

São eles:
II: Imposto sobre importação, para mercadorias vindas de fora do país.
IOF: Imposto sobre operações financeiras, para empréstimos, ações e demais ações financeiras
IPI: Imposto sobre produtos industrializados, para a indústria
IRPF: Imposto de Renda Pessoa Física, sobre a renda do cidadão
IRPJ: Imposto de Renda Pessoa Jurídica, sobre a renda de CNPJs
Cofins: Contribuição de financiamento da seguridade social
PIS: Programa de Integração Social
CSLL: Contribuição social sobre lucro líquido
INSS: Instituto Nacional do Seguro Social
Já os impostos estaduais são destinados a manutenção da administração do Governo Estadual, bem como a financiamento de serviços públicos do estado e investimentos em infraestrutura a nível estadual (escolas e faculdades estaduais, rodovias estaduais, etc).
 São responsáveis por cerca de 28% (vinte e oito por cento) da arrecadação total.

São eles:

ICMS: Impostos sobre circulação de mercadorias e serviços
IPVA: Imposto sobre a propriedade de motores automotores
ITCMD: Imposto de transmissão causa mortis e doação

Os impostos municipais são de ordem do município e destinados a manutenção da administração pública local, serviços, investimentos e manutenções locais. São destinados para escolas municipais, unidades de pronto atendimento, etc. São responsáveis por cerca de 5,5% (cinco e meio por cento) da arrecadação total do país.

IPTU: Imposto sobre propriedade territorial urbana
ISS: Imposto sobre serviços
ITBI: Imposto de transmissão de bens imóveis 
            """
        )

    def subcapitulo7_3():
        criar_subcapitulo(
            "Planejamento tributário",
            """
            O planejamento tributário preventivo é uma estratégia adotada pelas empresas para reduzir a carga tributária de forma legal sem gerar inconformidades com a Receita Federal. 
Assim, para fazer um planejamento tributário preventivo é necessário que você analise a situação fiscal da empresa, identifique as oportunidades de economia de impostos com base nas operações do negócio e adote medidas para otimizar a gestão tributária. Se isso te parece complicado, conte com o apoio de um contador para auxiliá-lo. 

Além da possibilidade de redução da carga tributária, outra vantagem do planejamento tributário preventivo é a possibilidade de antecipar situações que podem gerar problemas fiscais no futuro.
Isso é, ao dar atenção para o planejamento preventivo, é possível identificar possíveis erros ou inconsistências nos registros contábeis e corrigi-los antes que se tornem um problema. Além disso, o planejamento tributário preventivo permite que a empresa esteja preparada para eventuais mudanças na legislação tributária. 
É importante ressaltar que o planejamento tributário preventivo deve ser realizado por profissionais especializados, como contadores e advogados tributaristas. Tais profissionais conseguem prestar uma consultoria assertiva para que o seu negócio esteja regularizado.

Todas as empresas podem se beneficiar de um planejamento tributário preventivo, independentemente do porte ou segmento de atuação. No entanto, é especialmente importante para empresas que possuem uma carga tributária elevada ou que estão sujeitas a uma complexidade tributária maior.
Empresas de médio e grande porte, que possuem um volume significativo de transações financeiras e operações comerciais, geralmente enfrentam uma carga tributária mais alta e têm mais oportunidades de otimização fiscal. Além disso, empresas que atuam em setores específicos, como indústria, comércio exterior, tecnologia, serviços financeiros, entre outros, podem se beneficiar de um planejamento tributário preventivo devido às particularidades e complexidades tributárias envolvidas em suas atividades.
            """
        )

    def subcapitulo7_4():
        criar_subcapitulo(
            "Impostos sobre\nheranças e doações",
            """
            O Imposto de transmissão causa mortis e doação (ITCMD) é um tributo que incide sobre transmissões gratuitas do patrimônio, ou seja, em situações em que há transferência da propriedade de bens e direitos sem pagamento de um valor em virtude da própria transmissão.
As transmissões gratuitas que geram incidência do ITCMD são:

Sucessão causa mortis: quando há transferência em razão do falecimento do proprietário aos seus herdeiros;
 Doação: quando há empobrecimento do doador e enriquecimento patrimonial do donatário devido ao fluxo patrimonial e liberalidade.

O tributo deve ser pago tanto em casos de sucessão legítima (aos herdeiros necessários) ou testamentária (aquela estabelecida por meio de testamento).

A transmissão gratuita objeto deste tributo diz respeito a bens e direitos com valor econômico, como imóveis, móveis, automóveis, obras de arte, ações, participações societárias, marcas, direitos minerários, entre outros.

É importante destacar que eventos aparentemente sem qualquer relação com os fatos geradores do ITCMD podem sim ser encarados como doação, como é o caso da renúncia à herança em favor de terceiro ou o excesso de meação no divórcio.

O Imposto sobre Transmissão Causa Mortis e Doação (ITCMD) é um tributo que incide sobre duas situações específicas: a transmissão gratuita de patrimônio em caso de morte (sucessão causa mortis) e a transmissão gratuita de bens em vida (doação). 
A contabilidade do imposto é feita por meio da multiplicação de uma alíquota por uma base de cálculo, que geralmente é o valor venal dos bens e direitos em questão.
Cada Estado tem sua própria legislação sobre o prazo para o pagamento do tributo, que pode variar dependendo do tipo de bem ou direito transmitido.

A alíquota do ITCMD depende do Estado em que a transmissão de bens ou direitos vai acontecer.
Cada Estado-membro tem a autonomia para definir sua alíquota, respeitando o limite máximo de 8% determinado pelo Senado Federal.
Existem algumas situações imunes ao ITCMD, como entidades religiosas, partidos políticos, instituições de educação e de assistência social sem fins lucrativos, entre outras, e também isenções que podem variar de acordo com a lei estadual e municipal.
É importante verificar na legislação pertinente a alíquota cabível e as condições para possíveis isenções.
O momento da ocorrência do fato gerador do ITCMD também é relevante para determinar a alíquota, que será vigente no momento da morte no caso de sucessão causa mortis ou no momento da celebração do ato ou contrato na doação.

O pagamento do imposto sobre herança, normalmente é responsabilidade dos herdeiros ou dos legatários arcar com esse custo.
A soma total de impostos é calculada sobre o valor dos bens deixados pelo falecido, no caso da sucessão causa mortis, ou sobre o valor dos bens doados, no caso de doação.
O prazo para o pagamento do imposto sobre herança pode variar de acordo com a legislação de cada país ou Estado, mas em geral, o pagamento deve ser feito após a avaliação dos bens do espólio ou da doação, e após o cálculo do tributo.
Algumas legislações estabelecem um prazo após a ocorrência da transmissão propriamente dita para efetuar o pagamento.
É importante ressaltar que, caso o imposto não seja pago no prazo estabelecido, podem ser cobrados juros e multas sobre o valor devido.
Por isso, é fundamental estar atento aos prazos e às obrigações fiscais relacionadas à herança ou doação de bens.

A doação em vida é um ato em que uma pessoa transfere a propriedade de um bem ou ativo financeiro para outra pessoa ainda em vida.
Esse tipo de doação tem implicações fiscais, pois antecipa o ITCMD sobre o bem ou ativo doado, portanto, é importante ter cuidado e analisar bem as alternativas antes de fazer uma doação em vida.
É recomendado que a doação seja feita apenas em situações muito bem pensadas e que não haja possibilidade de arrependimento.

Como facilitar a sucessão: veja algumas possibilidades

A sucessão empresarial é um processo importante e muitas vezes delicado, que envolve a transferência de uma empresa de uma geração para outra.
Para garantir que esse processo ocorra de forma tranquila e eficiente, é fundamental planejar a sucessão com antecedência.
Nesse sentido, existem diversas opções que podem ser adotadas para facilitar a sucessão. Confira a seguir as principais:

Holdings familiares:

Uma das alternativas mais comuns para a sucessão empresarial é a criação de holdings familiares, ou seja, de uma empresa que é controlada por uma família e que tem como objetivo gerenciar os negócios da família.
Nesse modelo, os membros da família podem transferir a propriedade da empresa para a holding, mantendo o controle da gestão e garantindo a continuidade dos negócios.
Além disso, a holding pode ser uma forma de proteger o patrimônio familiar e facilitar a transferência de bens entre gerações.

Seguro de vida:

Outra opção para facilitar a sucessão é o seguro de vida.
Ao contratar um seguro de vida, o empresário pode incluir uma cláusula de beneficiário indicando quem deve receber o valor do seguro em caso de falecimento.
Isso pode ser extremamente útil para garantir a transferência de bens e recursos para os herdeiros de forma rápida e eficiente.
Além disso, o seguro de vida é uma forma de reduzir o impacto financeiro da morte do empresário na empresa.

Previdência privada:

A previdência privada é uma alternativa interessante para garantir a segurança financeira dos herdeiros.
Com um plano de previdência privada, é possível garantir uma renda complementar para seus herdeiros, mesmo que não esteja mais presente.
Além disso, ela é uma forma de proteger o patrimônio e facilitar a transferência de recursos entre gerações.
Planejamento sucessório
Por fim, além das possibilidades mencionadas anteriormente, outra opção para facilitar a sucessão é o planejamento sucessório.
Trata-se de um conjunto de medidas que visam garantir a continuidade do patrimônio da família, bem como a proteção dos interesses dos herdeiros, após a morte do titular.
O planejamento sucessório pode ser feito através de estratégias como a criação de testamentos, a elaboração de acordos de sócios e a definição de regras para a transferência dos bens.



            """
        )

    def subcapitulo7_5():
        criar_subcapitulo(
            "Incentivos fiscais",
            """
            Os incentivos fiscais são mecanismos oferecidos pelo governo, em geral, como parte de sua política de desenvolvimento econômico, para estimular e apoiar determinados setores ou atividades econômicas, incluindo as pequenas e médias empresas (PMEs). 
Esses incentivos visam reduzir a carga tributária sobre empresas, para que aumentem o investimento em determinadas áreas, promover o crescimento econômico e gerar empregos. Eles podem assumir várias formas, como deduções fiscais, créditos tributários, isenções fiscais, entre outros benefícios fiscais.
Abaixo, compreenda mais sobre incentivos fiscais com os especialistas da Contabilizei e como eles podem auxiliar o crescimento da sua empresa. 

Exemplos de incentivos fiscais:

Para as micros, pequenas e médias empresas, esses incentivos fiscais podem ser particularmente importantes, pois podem ajudar a aliviar os custos tributários e fornecer capital adicional para reinvestimento nos negócios. 
Alguns exemplos de incentivos fiscais que podem beneficiar as PMEs incluem:

Redução de alíquotas de impostos
Em alguns casos, as pequenas empresas podem receber tratamento tributário preferencial, com alíquotas de imposto mais baixas em comparação com empresas maiores.

Créditos fiscais
As PMEs podem ser elegíveis para créditos fiscais que reduzem o valor do imposto devido. Isso pode incluir créditos para pesquisa e desenvolvimento, contratação de certos grupos de trabalhadores, como pessoas com deficiência, e investimentos em ativos qualificados.

Isenções fiscais
Algumas jurisdições oferecem isenções fiscais para empresas que atendem a critérios específicos, como startups, empresas em zonas de incentivos ou aquelas que promovem determinados objetivos econômicos, como a geração de empregos.

Deduções e benefícios fiscais específicos
Algumas regiões podem oferecer deduções fiscais ou outros benefícios específicos para empresas que investem em áreas como energia limpa, tecnologia, educação e treinamento de funcionários.
            """
        )

    def subcapitulo7_quiz():
            criar_quiz()

    def subcapitulo7_desafio():
        criar_subcapitulo(
            "Desafio",
            """
Parabéns por chegar até aqui, futuro especialista em finanças!
Agora, vamos colocar em prática o que você aprendeu no capítulo Imposto de Renda Pessoa Física (IRPF).

Desafio:
Organize-se para a próxima declaração de IRPF. Realize as seguintes etapas:

Reúna os documentos necessários:

Informe de rendimentos das fontes pagadoras (empresas, bancos, corretoras).
Comprovantes de despesas dedutíveis (saúde, educação, doações, entre outros).
Informações sobre bens e direitos, dívidas e receitas de dependentes.
Baixe o Programa Gerador da Declaração (PGD IRPF):

Simule o preenchimento de uma declaração com dados fictícios ou reais, dependendo de sua necessidade.
Identifique as deduções possíveis:

Liste os gastos que podem ser abatidos, como saúde e educação.
Pesquise sobre o tipo de declaração ideal:

Descubra se você se encaixa no modelo simplificado ou completo.
Reflexão final:
Após realizar essas etapas, avalie: você se sente preparado para declarar o imposto de renda? Identificou maneiras de reduzir sua carga tributária de forma legal?

Boa sorte! Lembre-se: entender o IRPF é o primeiro passo para garantir sua conformidade tributária e proteger seu patrimônio.
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
            criar_bloco("Imposto de Renda Pessoa Física (IRPF)", lambda _: subcapitulo7_1()),
            criar_bloco("Impostos sobre a propriedade", lambda _: subcapitulo7_2()),
            criar_bloco("Planejamento tributário", lambda _: subcapitulo7_3()),
            criar_bloco("Impostos sobre heranças e doações", lambda _: subcapitulo7_4()),
            criar_bloco("Incentivos fiscais", lambda _: subcapitulo7_5()),
            criar_bloco("Quiz", lambda _: subcapitulo7_quiz()),
            criar_bloco("Desafio", lambda _: subcapitulo7_desafio()),
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
