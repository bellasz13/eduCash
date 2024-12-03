import flet as ft

def Capitulo6Page(page: ft.Page):
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
                "pergunta": "Qual das seguintes opções NÃO representa uma vantagem do investimento em imóveis, de acordo com o texto?",
                "alternativas": [
                    {"texto": "Diversificação do portfólio de investimentos.", "correta": False},
                    {"texto": "Potencial de valorização do imóvel ao longo do tempo.", "correta": False},
                    {"texto": "Segurança patrimonial e possibilidade de gerar renda através do aluguel.", "correta": False},
                    {"texto": "Alta liquidez, permitindo a venda rápida do imóvel quando necessário.", "correta": True},
                ],
            },
            {
                "pergunta": "Qual das seguintes afirmações sobre o Sistema Financeiro de Habitação (SFH) é INCORRETA?",
                "alternativas": [
                    {"texto": "O SFH utiliza recursos da caderneta de poupança e do FGTS.", "correta": False},
                    {"texto": "O valor máximo do imóvel financiado pelo SFH é de R$ 1,5 milhão.", "correta": False},
                    {"texto": "As taxas de juros do SFH são geralmente mais baixas do que as do SFI.", "correta": False},
                    {"texto": "O SFH permite financiar imóveis comerciais e industriais.", "correta": True},
                ],
            },
                {
                "pergunta": "Qual das seguintes opções NÃO representa um benefício do planejamento sucessório?",
                "alternativas": [
                    {"texto": "Eliminação completa da possibilidade de conflitos familiares.", "correta": True},
                    {"texto": "Garantia de que os bens serão distribuídos de acordo com a vontade do falecido.", "correta": False},
                    {"texto": "Redução de custos e tempo no processo de inventário.", "correta": False},
                    {"texto": "Proteção dos beneficiários contra imprevistos legais e financeiros.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a principal função do inventário no processo de sucessão?",
                "alternativas": [
                    {"texto": "Definir a forma como os bens serão distribuídos entre os herdeiros.", "correta": False},
                    {"texto": "Identificar os bens e dívidas do falecido e determinar os herdeiros.", "correta": True},
                    {"texto": "Calcular o valor dos bens para fins de pagamento de impostos.", "correta": False},
                    {"texto": "Garantir que todos os herdeiros tenham acesso aos bens do falecido.", "correta": False},
                ],
            },
                {
                "pergunta": "Considerando as opções de financiamento imobiliário, qual a principal diferença entre o financiamento direto com a construtora e o financiamento através de uma instituição financeira?",
                "alternativas": [
                    {"texto": "O financiamento direto com a construtora não exige análise de crédito.", "correta": False},
                    {"texto": "O financiamento através de uma instituição financeira oferece taxas de juros mais baixas.", "correta": False},
                    {"texto": "O prazo para quitação do financiamento é sempre menor no financiamento direto com a construtora.", "correta": True},
                    {"texto": "O financiamento direto com a construtora permite a utilização do FGTS, enquanto o financiamento através de uma instituição financeira não.", "correta": False},
                ],
            },
                {
                "pergunta": "Considerando as desvantagens, qual o maior desafio enfrentado por um investidor que deseja alugar seu imóvel?",
                "alternativas": [
                    {"texto": "A dificuldade em encontrar um inquilino rapidamente.", "correta": False},
                    {"texto": "Os custos associados à administração do imóvel, como taxas e impostos.", "correta": True},
                    {"texto": "A necessidade de realizar reformas constantes no imóvel.", "correta": False},
                    {"texto": "A impossibilidade de vender o imóvel enquanto ele estiver alugado.", "correta": False},
                ],
            },
            {
                "pergunta": "Qual das seguintes afirmações sobre o seguro de vida é INCORRETA?",
                "alternativas": [
                    {"texto": "O seguro de vida garante o pagamento de uma indenização aos beneficiários em caso de morte do segurado.", "correta": False},
                    {"texto": "O seguro de vida pode incluir coberturas adicionais, como invalidez permanente por acidente.", "correta": False},
                    {"texto": "O valor da indenização em um seguro de vida é definido no momento da contratação da apólice.", "correta": False},
                    {"texto": "O seguro de vida é obrigatório para todos os cidadãos brasileiros.", "correta": True},
                ],
            },
                {
                "pergunta": "Qual a principal diferença entre o seguro de vida e o seguro de acidentes pessoais?",
                "alternativas": [
                    {"texto": "O seguro de vida cobre apenas o falecimento por causas naturais, enquanto o seguro de acidentes pessoais cobre apenas o falecimento por acidentes.", "correta": False},
                    {"texto": "O seguro de vida é mais caro que o seguro de acidentes pessoais.", "correta": False},
                    {"texto": "O seguro de vida é destinado a pessoas físicas, enquanto o seguro de acidentes pessoais é destinado a pessoas jurídicas.", "correta": False},
                    {"texto": "O seguro de vida pode incluir coberturas adicionais, como invalidez permanente por acidente, enquanto o seguro de acidentes pessoais se limita à cobertura por morte acidental.", "correta": True},
                ],
            },
                {
                "pergunta": "Qual das seguintes afirmações sobre a decisão de comprar ou alugar um imóvel é INCORRETA?",
                "alternativas": [
                    {"texto": "Alugar um imóvel é mais indicado para pessoas que desejam ter mais flexibilidade para mudar de cidade.", "correta": False},
                    {"texto": "O custo de manutenção de um imóvel alugado é sempre menor do que o custo de manutenção de um imóvel próprio.", "correta": True},
                    {"texto": "Comprar um imóvel é um investimento a longo prazo que pode gerar valorização e renda futura.", "correta": False},
                    {"texto": "A decisão de comprar ou alugar um imóvel deve levar em consideração o planejamento de vida a médio e longo prazo.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual é o principal fator que deve ser considerado ao decidir entre comprar ou alugar um imóvel?",
                "alternativas": [
                    {"texto": "O valor do imóvel.", "correta": False},
                    {"texto": "O planejamento de vida a longo prazo.", "correta": True},
                    {"texto": "A taxa de juros do financiamento.", "correta": False},
                    {"texto": "A localização do imóvel.", "correta": False},
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

    def subcapitulo6_1():
        criar_subcapitulo(
            "Imóveis como\ninvestimento:\nvantagens e desvantagens",
            """
Investir em imóvel é considerado vantajoso pelos especialistas. Afinal, raramente ele será revendido pelo valor abaixo do que foi comprado.

Sair do aluguel e ter a segurança de adquirir seu próprio imóvel promove mais conforto para aos moradores. Pois, morando em uma casa ou apartamento alugados a qualquer momento, o proprietário pode pedir as chaves do imóvel e de repente você terá que mudar toda a sua vida. Outra segurança é saber que seu imóvel será valorizado com o passar dos anos.

A rentabilidade com o serviço de aluguel pode ser algo bastante vantajoso. Uma boa iniciativa é comprar imóvel e alugá-lo, caso você não tenha interesse em morar nele. Na verdade, seu bem parado dá prejuízo, pois existem custos com taxas e condomínio. Por outro lado, se você alugar, ele trará lucros, rentabilizando ainda mais seu investimento inicial.
O investimento em imóveis é muito usado para diversificar o portfólio, o seu cardápio de investimentos, e reduzir os riscos do investidor. Mesmo aqueles que preferem investir na bolsa de valores possuem ao menos parte de seu dinheiro alocado em imóveis, seja de forma direta, adquirindo um imóvel, ou indireto, através de fundos imobiliários.

Milhares de famílias brasileiras procuram melhorar sua qualidade de vida. E a aquisição de uma nova casa ou apartamento cumpre essa necessidade da melhor forma possível.

Algumas desvantagens podem ocorrer, principalmente se o investidor tiver dificuldades na revenda.
Uma das desvantagens de comprar um imóvel para investir e não conseguir alugar ou vender rápido é em relação às contas com as quais o proprietário deverá arcar. Condomínio, taxas e impostos são custos que ficarão por conta do proprietário enquanto o imóvel não for vendido ou locado.
Com o passar do tempo os imóveis necessitam de reformas e sempre haverá gastos com novos reparos. Se a mudança também for estética, isso gerará ainda mais custos.
Se você quiser alugar ou vender seu imóvel, ou vai fazer isso através de uma imobiliária, ou por conta própria. Se você optar por uma imobiliária, terá que arcar com os custos exigidos. Caso for fazer por conta própria, terá que lidar com outras questões que tomam tempo e que podem trazer dores de cabeça.
Os custos de compra de imóveis ou terrenos são muito altos, principalmente quando comparados a outros tipos de investimento. Isso pode representar alguns perigos à sua renda, ainda mais quando não há planejamento ou quando você precisa financiar parte do valor do imóvel. Além disso, existem ainda custos com pagamento do Imposto sobre Transmissão de Bens (ITBI), dentre outros impostos e gastos com corretagem.

            """
        )

    def subcapitulo6_2():
        criar_subcapitulo(
            "Financiamento\nimobiliário:\ncomo funciona?",
            """
O financiamento imobiliário é um modelo de empréstimo voltado exclusivamente para a compra de uma casa ou apartamento, tanto novo quanto usado, a construção ou a reforma de um imóvel residencial, assim como de um espaço comercial, uma sala ou um galpão.
O consumidor que não tem o montante todo para a aquisição, recorre a uma instituição financeira a fim de conseguir esse crédito e, em seguida, paga o valor por meio de parcelas acrescidas de juros e correção monetária. Esse é o tipo de financiamento com as taxas mais baixas no mercado e tem um prazo bem longo para quitação, de até 35 anos.
Em linhas gerais, para conseguir um financiamento imobiliário é preciso ter 18 anos ou mais, demonstrar ter renda suficiente para pagar as parcelas e estar com o cadastro de pessoa física (CPF) regularizado. O CPF pode estar negativado sem que o consumidor saiba. Por isso, é importante consultar se o nome não foi incluído em órgãos de proteção ao crédito como Serasa, SPC, entre outros.
O prazo médio para a liberação de um financiamento imobiliário é de cerca de 40 dias, de acordo com a Abecip. Por isso, juntamente com a busca pelo imóvel, ou até mesmo antes, vale pesquisar as instituições financeiras. Isso garante tempo para encontrar aquelas que têm as melhores taxas e condições.
Se a instituição escolhida for a mesma onde já se tem conta, o cliente pode encontrar facilidades na hora de negociar. Como o banco já conhece o perfil do cliente, fica mais ágil a análise para a concessão do montante. Há ainda instituições que oferecem condições mais vantajosas para clientes de longo prazo.
Existem 3 tipos de financiamento imobiliário no Brasil: 
            
SFH
Os recursos do SFH vêm da caderneta de poupança e do FGTS e ele possui características e limites bem definidos:
o valor do imóvel é de até R$ 1,5 milhão
o crédito concedido cobre no máximo 80% do valor do imóvel
as prestações não devem ultrapassar 30% da renda do consumidor
a taxa máxima de juros é de 12%
o imóvel deve constar no cartório de registro, ser residencial e urbano, novo ou usado, mas deve situar-se na mesma região em que o consumidor mora ou trabalha há pelo menos um ano
o imóvel escolhido não pode ter sido comprado com a utilização do FGTS nos três anos anteriores
o consumidor tem a opção de utilizar seu saldo do FGTS para pagar parte do imóvel, desde que seja residencial e o primeiro a ser adquirido
o prazo para quitação é de até 35 anos.
            
SFI
Sistema Financeiro Imobiliário (SFI) que foi criado para suprir as carências do SFH. Ou seja, o SFI flexibilizou as regras.
essa modalidade utiliza recursos direcionados por grandes instituições e investidores
o imóvel deve custar acima do teto permitido pelo SFH, isto é, mais de R$ 1,5 milhão e o financiamento pode chegar a 90% do valor total
a taxa de juros é variável
o comprador pode ser tanto pessoa física quanto jurídica
o valor mensal não é limitado por um percentual da renda
ao contrário do SFH, o SFI permite financiar imóvel não residencial e, mesmo quem já tem um em seu nome, pode pleitear crédito para comprar outro
desde agosto do ano passado tornou-se possível utilizar o FGTS para reduzir o saldo devedor do imóvel (também do primeiro a ser adquirido) ou para abater até 80% da prestação em 12 meses
o tempo para pagar o crédito também é de até 35 anos.
            
Financiamento direto com a construtora
Existe ainda a possibilidade de financiar o imóvel com a própria construtora ou incorporadora. Geralmente, ocorre com casas ou apartamentos comercializados quando estão na planta ou em construção.
A construtora entrega as chaves quando o consumidor já pagou entre 30% e 40% do valor do imóvel. O restante pode ser financiado pelos modelos apresentados anteriormente, com uma instituição financeira, ou com a própria empresa que está fazendo a obra.
Neste caso, os prazos para quitação costumam ser menores e, por isso, as prestações mais altas.
            
Para conseguir um financiamento imobiliário, o cliente passa por algumas etapas:
1- Análise do crédito
A primeira delas é quando a pessoa já tem em mente quanto quer gastar num imóvel e sabe detalhes sobre quanto precisa conseguir no banco e qual o valor das prestações cabem no bolso. Com os dados do cliente em mãos, a instituição financeira avalia renda, perfil, prazo etc para saber se é seguro liberar aquele montante.
            
2- Batendo o martelo sobre o imóvel
Geralmente, o consumidor que sai em busca do financiamento já começou também a pesquisa pelo imóvel. No momento em que ele tiver o crédito pré-aprovado, ele já pode tomar a decisão sobre qual imóvel quer adquirir. O ideal é ter mais de uma opção para o caso de algum problema com a documentação ou o valor liberado, por exemplo.
            
3- Inspeção do imóvel
Logo que o cliente faz sua escolha, a instituição financeira envia um engenheiro para fazer a vistoria e checar se o imóvel está dentro da qualidade esperada e se o preço condiz com o valor de mercado.A avaliação é um serviço cobrado. Um avaliador verifica o imóvel in loco. Atualmente, porém, parte das avaliações pode ser feita online.
            
4- Questões jurídicas
Em seguida, o banco faz também uma minuciosa análise de toda a documentação, que inclui as informações do vendedor. Nessa fase, outros documentos podem ser solicitados.
            
5- Contrato
Se tudo estiver correto, o banco dá sequência na elaboração do contrato. Depois, é só assinar.
            
6- Registro
O último passo é fazer o registro do imóvel em um cartório. Nessa etapa há taxas envolvidas e o cartório pede ainda a apresentação do pagamento do Imposto sobre Transmissão de Bens Imóveis. Com o registro em mãos, o cliente o apresenta ao banco, que finaliza a análise e libera o valor para o pagamento. Nesse momento, já é possível comemorar a compra da casa própria.
            
Se o financiamento for aprovado, a instituição desembolsa o valor e o consumidor começa a pagar as parcelas.
Em geral, é cobrada uma entrada de 20% do imóvel no financiamento. O tomador do empréstimo pode oferecer mais. Especialistas no tema recomendam pagar o máximo possível de entrada. Como os juros são calculados sobre o saldo devedor, quanto menor a dívida, menos juros você irá pagar.
O próprio imóvel objeto do financiamento é a garantia da operação. Isso pode ocorrer por meio de hipoteca ou alienação fiduciária. A última modalidade é de longe a mais utilizada pelas instituições financeiras, pois o bem fica alienado a quem empresta até a quitação, o que torna mais fácil sua retomada em caso de inadimplência.
Lembrando que é possível amortizar as parcelas que tem como consequência diminuir o prazo originalmente acertado com a instituição financeira. Há bancos que apresentam essa opção online, na página onde o consumidora companha a evolução da sua amortização. É preciso lembrar que existe a possibilidade de abater do valor das parcelas ou diminuir o número de parcelas (nesse caso, a prestação não diminui, e sim, o tempo).
            """
        )

    def subcapitulo6_3():
        criar_subcapitulo(
            "Planejamento sucessório:\nprotegendo seu patrimônio",
            """
O planejamento sucessório é o processo de avaliação e programação da sucessão familiar. Podemos dizer que é onde desenhamos a trajetória dos recursos não usados pela família em vida, garantindo que eles cheguem aonde essas famílias queriam que chegassem da forma mais rápida, eficiente e barata possível. 
Após falecermos, o patrimônio que construímos e não usamos em vida (o nosso legado financeiro) forma o que chamamos de espólio (que inclui todo o patrimônio líquido e imobilizado, assim como as dívidas deixadas para trás). Antes que esse espólio seja transferido, é necessária a realização do inventário, no qual são identificados os sucessores e as distribuições desenhadas a cada um deles.
O processo de inventário é normalmente demorado e caro. Além de demandar a presença de um advogado, ele pode se tornar judicial caso haja discussões em relação à partilha adequada dos bens ou dívidas pendentes que precisem ser quitadas. Um inventário fluido costuma levar no mínimo dois meses, enquanto inventários complexos e repletos de brigas judiciais podem levar anos. Sem dúvidas, em um caso como esse, um planejamento sucessório mais robusto e bem estruturado teria poupado todo o stress e divergências que foram causadas entre os membros da família.
Feito o inventário, há o recolhimento do ITCMD (Imposto de Transmissão Causa Mortis e Doação), que varia de 4 a 8% a depender do estado. Após os trâmites legais, os bens são destravados e devidamente partilhados.
Custo de advogado, imposto de transmissão, desgaste familiar, inacessibilidade aos bens durante o processo... sim, é um processo chato e repleto de riscos. 
Um planejamento sucessório bem estruturado é crucial para evitar problemas e garantir que seu patrimônio seja transmitido conforme sua vontade. Aqui estão os principais benefícios de realizar um planejamento sucessório:
            
1. Evitar conflitos familiares
Redução de disputas: Um plano claro e bem definido diminui as chances de desentendimentos e disputas judiciais entre herdeiros.
Harmonia familiar: Mantém a harmonia entre os familiares, evitando brigas que podem surgir devido à falta de clareza na distribuição dos bens.
            
2. Redução de custos e impostos
Menor carga tributária: Planejar a sucessão permite utilizar estratégias que minimizem os impostos incidentes, como o ITCMD.
Economia de tempo e dinheiro: Um planejamento sucessório pode reduzir os custos com advogados e outros profissionais, além de acelerar o processo de inventário.
            
3. Garantia da vontade do titular
Cumprimento dos desejos: Assegura que os desejos do titular do patrimônio sejam respeitados, garantindo que os bens sejam distribuídos conforme sua vontade.
Proteção de beneficiários: Permite a escolha de beneficiários específicos e a definição de condições para o recebimento dos bens.
            
4. Continuidade dos negócios familiares
Sustentabilidade dos negócios: Evita a fragmentação de empresas familiares, garantindo sua continuidade e prosperidade.
Planejamento de gestão: Facilita a transição de gestão e propriedade, mantendo a estabilidade dos negócios.
            
5. Tranquilidade e segurança
Previsibilidade: Proporciona previsibilidade e segurança financeira para os herdeiros, que sabem o que esperar e podem se planejar adequadamente.
Proteção contra imprevistos: Protege os herdeiros de imprevistos legais e financeiros, evitando que fiquem desamparados.
            """
        )

    def subcapitulo6_4():
        criar_subcapitulo(
            "Seguro de vida\ne outros seguros\nimportantes",
            """
Quais são os principais tipos de seguro no Brasil?
Confira algumas das principais alternativas disponíveis e suas características:
            
1. Seguro de vida
Em geral, o seguro de vida possui cobertura para morte, o que faz com que as pessoas escolhidas por você recebam os recursos diante do seu falecimento.

2. Seguro de morte acidental
Nesse contexto, ele prevê o pagamento de indenização no caso de ocorrer o falecimento do titular em decorrência de um acidente. É importante compreender que o acidente deve estar previsto na apólice. Assim, a situação deve atender aos critérios definidos pela seguradora para garantir o direito ao recebimento de indenização por parte dos beneficiários.
            
3. Seguro contra acidentes pessoais
O seguro de acidentes pessoais também é uma modalidade de seguro de vida e pode ser de dois tipos diferentes. O primeiro é o seguro por morte acidental. Além disso, existe o seguro de invalidez permanente total por acidente. Nesse caso, existe o direito de receber o capital segurado se uma eventualidade resultar em condição de invalidez permanente em decorrência de um acidente. 
            
4. Seguro patrimonial
O seguro patrimonial é uma solução financeira voltada para quem deseja proteger parte do patrimônio. Ele pode servir para pessoas físicas que desejam proteger um item ou propriedade de valor, por exemplo. Porém, é mais comum que essa alternativa seja voltada para empresas que desejam proteger bens que integram seu patrimônio.
            
5. Seguro automotivo
O seguro automotivo, também conhecido apenas como seguro auto, é outra possibilidade popular no mercado brasileiro. Como o nome sugere, ele é voltado para proteger veículos automotores. Além de carros, essa alternativa pode servir para proteger motos e caminhões, por exemplo.
Em geral, existe a cobrança de uma franquia, que exige o pagamento de um valor por parte do segurado, em caso de sinistro. Já as coberturas variam entre cada apólice. 
            
6. Seguro residencial
O seguro residencial tem como principal objetivo proteger um imóvel nas condições previstas em contrato. Ele é aplicável tanto a casas quanto a apartamentos e atende às necessidades variadas de proprietários e locatários.
            
7. Seguro viagem
O seguro viagem é uma modalidade voltada aos viajantes nacionais e internacionais que desejem ter assistência diante de eventualidades. Aqui, o segurado tem a proteção da empresa contratada durante o período de viagem para o destino escolhido, conforme as condições previstas na apólice. Vale notar que, para entrar em alguns países, é obrigatória a apresentação de um seguro viagem. Isso é especialmente verdadeiro no caso de destinos internacionais, com destaque para as nações que fazem parte da União Europeia.
            
8. Seguro empresarial
O seguro empresarial é uma das modalidades que pode ser contratada apenas por pessoas jurídicas. Com ele, a empresa pode proteger tanto o patrimônio corporativo quanto determinadas operações realizadas pelo negócio. Como cada setor e empresa tem necessidades específicas, é comum que as coberturas variem bastante entre cada seguradora.
            
9. Seguro celular
O seguro celular é um tipo de apólice mais simples e acessível, voltada para smartphones e dispositivos móveis que sejam de valor para você. Suas coberturas permitem ter uma proteção mais completa no caso de sinistros, além de suporte financeiro especializado se o pior acontecer.
            """
        )

    def subcapitulo6_5():
        criar_subcapitulo(
            "Aluguel x compra\nde imóvel: qual\na melhor opção?",
            """
Vantagens de comprar um imóvel
Seus custos são mais previsíveis, porque há apenas a manutenção e o financiamento (se existir);
Sua vida tem mais segurança, porque sempre terá um teto para morar;
Você começa a formar ou aumenta seu patrimônio;
O imóvel tende a se valorizar com o tempo — e isso pode levar a uma negociação melhor depois;
Você pode ficar na sua casa pelo tempo que quiser — e se preferir sair, pode ter uma renda passiva.
Desvantagens de comprar um imóvel
É provável que você precise fazer algum tipo de financiamento imobiliário e isso gera uma dívida alta e de longo prazo;
Você pode ter dificuldade de pagar as parcelas do financiamento, caso sua condição de renda mude;
Você se torna responsável pela manutenção, administração e pagamento de impostos da propriedade.
            
Vale a pena alugar um imóvel?
Vale a pena alugar um imóvel quando você não quer ter raízes fixadas em nenhum lugar e deseja ter mais liberdade. Essa também é a melhor opção para quem não tem condições financeiras de comprar uma propriedade ou ainda não decidiu qual é seu objetivo de vida.
            
Vantagens de alugar um imóvel
Você tem liberdade para mudar de bairro, cidade e até de país;
Você não precisa pagar manutenção, exceto em situações específicas;
A tendência é que o gasto seja menor do que o de um financiamento;
A burocracia do aluguel de imóveis é menor;
A sua mudança é mais rápida, porque o contrato de locação é assinado com rapidez.
            
Desvantagens de alugar um imóvel
Você pode precisar se mudar a qualquer momento;
Não há liberdade para fazer todas as mudanças e reformas desejadas.
O valor do aluguel de imóveis é reajustado anualmente.
Você pode precisar de um fiador ou seguro fiança.
É feito um pagamento mensal, mas você não constroi um patrimônio.
            
O que é mais vantajoso: comprar ou alugar?
Comprar ou alugar imóvel pode ser vantajoso, mas isso depende do seu momento e estilo de vida, e condições financeiras. Ainda é necessário verificar como está o mercado imobiliário. Por isso, é importante considerar várias questões antes de decidir.
Vale a pena alugar em vez de comprar se você pretender se mudar, não tiver condições financeiras para fazer uma negociação ou se tiver dúvidas sobre a sua decisão.
            
Analise seus planos de vida
Segundo especialistas, no geral, ter uma casa compensa financeiramente se você tiver planos de morar, no mínimo, por seis anos nela. Caso o seu momento de vida demande um lugar para viver por um período menor, alugar pode ser uma boa opção para você. 
E há também as questões que, não necessariamente, estão ligadas à parte financeira. Vale a pena, por exemplo, você se questionar sobre seus planos de vida a médio e longo prazo. 
Será que você tem vontade de morar para o resto da vida naquele bairro ou gostaria, no futuro, de estar numa outra região? Você tem planos de se mudar para o exterior em algum momento? Ou mesmo para outra cidade? Dentro do seu planejamento familiar, por exemplo, o imóvel que você pretende comprar comporta a chegada dos filhos, caso planeje ter?
            
Considere o retorno financeiro de alugar ou comprar imóvel
Por mais que algumas perguntas sobre o seu momento de vida possam te desencorajar por um momento, saiba que nenhum plano para o futuro é excludente para quem tem o sonho de comprar um imóvel.
Até porque, caso você não tenha planos de viver toda sua vida na mesma casa ou apartamento, o simples fato de ter um imóvel torna-se um fator de segurança e também uma fonte de renda com aluguel ou, caso necessário, uma revenda.
Por isso, na hora de comprar um imóvel, leve em consideração, também, as possibilidades de valorização do seu bem e pense na liquidez. Ou seja, se um dia você precisar alugar ou mesmo vender, terá mais facilidade e maior rentabilidade se o imóvel tiver características entre as mais buscadas, como ter pelo menos dois quartos em um bairro com boas oportunidades de transporte, por exemplo.
            """
        )

    def subcapitulo6_quiz():
            criar_quiz()

    def subcapitulo6_desafio():
        criar_subcapitulo(
            "Desafio",
            """
Chegou o momento de aplicar o que aprendeu sobre "Imóveis como investimento" e "Financiamento imobiliário". Este desafio vai testar sua capacidade de planejamento e análise financeira para garantir que suas decisões sejam embasadas e seguras.

Tarefa 1: Decidindo entre comprar ou alugar
Analise sua situação atual e escolha se prefere investir em um imóvel ou optar pelo aluguel. Considere fatores como:
Estabilidade financeira.
Planos de médio e longo prazo.
Mercado imobiliário na sua região.
Escreva os prós e contras da sua escolha e justifique sua decisão.
Tarefa 2: Simulação de um financiamento imobiliário
Escolha um imóvel fictício com base em valores reais na sua cidade.
Simule um financiamento considerando:
O modelo de financiamento (SFH, SFI ou construtora).
Taxa de juros média.
Percentual de entrada que você está disposto a oferecer.
Tempo de parcelamento.
Use uma ferramenta online de simulação para calcular o valor total a ser pago, incluindo juros.
Tarefa 3: Planejamento de manutenção
Imagine que adquiriu o imóvel. Faça um planejamento anual estimando os custos com:
Reformas.
Impostos (ITBI e IPTU).
Condomínio (se aplicável).
Pergunta Reflexiva
Com base no seu desafio, responda:

O investimento em imóvel, para você, é viável e alinhado aos seus objetivos financeiros?
Como a decisão de comprar ou alugar impactaria sua estabilidade e segurança financeira no futuro?
Boa sorte! 
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
            criar_bloco("Imóveis como investimento: vantagens e desvantagens", lambda _: subcapitulo6_1()),
            criar_bloco("Financiamento imobiliário: como funciona?", lambda _: subcapitulo6_2()),
            criar_bloco("Planejamento sucessório: protegendo seu patrimônio", lambda _: subcapitulo6_3()),
            criar_bloco("Seguro de vida e outros seguros importantes", lambda _: subcapitulo6_4()),
            criar_bloco("Aluguel x compra de imóvel: qual a melhor opção?", lambda _: subcapitulo6_5()),
            criar_bloco("Quiz", lambda _: subcapitulo6_quiz()),
            criar_bloco("Desafio", lambda _: subcapitulo6_desafio()),
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
