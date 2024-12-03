import flet as ft

def Capitulo9Page(page: ft.Page):
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
                "pergunta": "Qual dos modelos de negócios digitais abaixo se destaca por permitir que profissionais liberais atendam seus clientes de forma mais ágil e prática, sem a necessidade de um espaço físico?",
                "alternativas": [
                    {"texto": "E-commerce", "correta": False},
                    {"texto": "Marketplace", "correta": False},
                    {"texto": "Prestação de serviços online", "correta": True},
                    {"texto": "Soluções SaaS", "correta": False},
                ],
            },
            {
                "pergunta": "Qual das seguintes afirmações sobre o Marketing de Conteúdo é FALSA?",
                "alternativas": [
                    {"texto": "É uma estratégia antiga que ganhou força com o surgimento das redes sociais.", "correta": False},
                    {"texto": "Engloba diversos profissionais, como infoprodutores e influenciadores digitais.", "correta": False},
                    {"texto": "Tem como objetivo principal gerar leads qualificados e aumentar as vendas a curto prazo.", "correta": True},
                    {"texto": "É uma forma de construir relacionamento com o público e posicionar a marca como autoridade em um determinado assunto.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual das alternativas abaixo representa o maior erro cometido por empreendedores digitais em relação à gestão financeira?",
                "alternativas": [
                    {"texto": "Não ter um plano de negócio detalhado.", "correta": False},
                    {"texto": "Não investir em marketing digital.", "correta": False},
                    {"texto": "Misturar as finanças pessoais com as da empresa.", "correta": True},
                    {"texto": "Não utilizar softwares de gestão financeira.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a importância de projetar o fluxo de caixa para empresas que vendem infoprodutos em lançamentos?",
                "alternativas": [
                    {"texto": "Permite identificar novas oportunidades de mercado.", "correta": False},
                    {"texto": "Garante que a empresa tenha dinheiro para cobrir os custos em períodos de menor faturamento.", "correta": True},
                    {"texto": "Aumenta a credibilidade da empresa perante os investidores.", "correta": False},
                    {"texto": "Diminui a necessidade de contratar funcionários.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual das seguintes opções NÃO é uma tendência do mercado digital mencionada no texto?",
                "alternativas": [
                    {"texto": "Mobile Marketing", "correta": False},
                    {"texto": "Realidade Virtual", "correta": False},
                    {"texto": "E-mail Marketing", "correta": True},
                    {"texto": "Web Analytics", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a principal vantagem do geomarketing para as empresas?",
                "alternativas": [
                    {"texto": "Aumentar o alcance global da marca.", "correta": False},
                    {"texto": "Reduzir custos com produção de conteúdo.", "correta": False},
                    {"texto": "Personalizar as ações de marketing para regiões específicas.", "correta": True},
                    {"texto": "Melhorar a experiência do usuário em sites e aplicativos.", "correta": False},
                ],
            },
            {
                "pergunta": "Qual das seguintes opções NÃO é um método de pagamento online comum no Brasil?",
                "alternativas": [
                    {"texto": "Cartões de crédito e débito", "correta": False},
                    {"texto": "Pix", "correta": False},
                    {"texto": "Dinheiro em espécie", "correta": True},
                    {"texto": "Carteiras digitais", "correta": False},
                ],
            },
                {
                "pergunta": "Considerando os diferentes métodos de pagamento online apresentados, qual deles é mais indicado para empresas que buscam reduzir custos operacionais e aumentar a agilidade nas transações?",
                "alternativas": [
                    {"texto": "Cartões de crédito e débito", "correta": False},
                    {"texto": "Pix", "correta": True},
                    {"texto": "Boletos", "correta": False},
                    {"texto": "Link de pagamento", "correta": False},
                ],
            },
                {
                "pergunta": "Qual a principal diferença entre o Simples Nacional e o Lucro Presumido em relação à forma de cálculo dos impostos?",
                "alternativas": [
                    {"texto": "O Simples Nacional calcula os impostos com base na receita bruta, enquanto o Lucro Presumido considera uma estimativa de lucro.", "correta": True},
                    {"texto": "O Simples Nacional possui alíquotas fixas, enquanto o Lucro Presumido permite a personalização das alíquotas.", "correta": False},
                    {"texto": "O Simples Nacional é mais complexo que o Lucro Presumido em termos de cálculo.", "correta": False},
                    {"texto": "O Lucro Presumido é mais indicado para empresas de grande porte, enquanto o Simples Nacional é exclusivo para pequenas empresas.", "correta": False},
                ],
            },
                {
                "pergunta": "Qual regime tributário é mais indicado para um negócio digital com faturamento anual de R$ 3.000.000,00 e uma folha de pagamento que representa 30% do faturamento?",
                "alternativas": [
                    {"texto": "Simples Nacional, Anexo III", "correta": True},
                    {"texto": "Simples Nacional, Anexo V", "correta": False},
                    {"texto": "Lucro Presumido", "correta": False},
                    {"texto": "Lucro Real", "correta": False},
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

    def subcapitulo9_1():
        criar_subcapitulo(
            "Modelos de\nnegócios digitais",
            """
O crescimento do e-commerce e a popularização das estratégias de Marketing de Conteúdo são alguns dos fatores responsáveis pela demanda cada vez maior de serviços relacionados à tecnologia.
Os principais modelos de negócios digitais
1. E-commerce
As lojas virtuais são um símbolo do empreendedorismo digital, pois permitem uma comparação certeira entre os modelos de comércio.
O empreendedor que pretende divulgar e vender seus produtos em um e-commerce não se livra das negociações com fornecedores, da administração de estoque e da distribuição de mercadorias, mas consegue concentrar toda a sua vitrine e sua comunicação em um canal facilmente gerenciável.
É importante, porém, se manter atento às inovações do setor em termos de tecnologia e resoluções legais.
2. Marketplace
Para quem deseja vender seus produtos pela internet, mas não dispõe de muitos recursos para criação e divulgação de uma marca, os marketplaces são uma excelente solução.
Essas plataformas concentram diversas lojas diferentes dentro de um mesmo espaço, que geralmente já é consolidado e muito acessado. A vantagem é que, além de disponibilizarem tráfego e público qualificado, os marketplaces ainda oferecem diversas ferramentas de promoção e divulgação para seus parceiros.
3. Prestação de serviços online
A internet também dá espaço para profissionais oferecerem seus serviços, ou parte deles, de maneira online. Advogados, contadores e consultores de marketing, por exemplo, já começaram a explorar os benefícios de atender seus clientes por email, chats e videoconferências.
Observe que os benefícios não são apenas para o prestador de serviços, mas também para o consumidor, que consegue ser atendido com mais agilidade e praticidade, sem a necessidade de se deslocar até uma agência ou escritório.
4. Marketing de Conteúdo
O Marketing de Conteúdo é uma estratégia antiga que ganhou uma nova roupagem após a ascensão dos blogs corporativos e das redes sociais. É um mercado muito amplo que engloba infoprodutores, afiliados, influenciadores, produtores de conteúdo e muitos outros.
Não importa a categoria ou o nicho do seu negócio, a única maneira de ganhar notoriedade na internet é produzindo e divulgando informações que atendam os interesses do seu público.
5. Soluções SaaS
Indo um pouco mais longe, temos as empresas SaaS, sigla que significa Software as a Service, ou “software como serviço”. Essas organizações são o corpo empresarial por trás dos aplicativos, plataformas de serviços e até das redes sociais.
É um modelo de negócio complexo, que requer investimentos significativos em desenvolvimento e gestão, mas é uma área de enorme sucesso no mercado que ainda tem muito a crescer. Afinal, são esses empreendimentos que garantem a evolução e o pleno funcionando de boa parte das aplicações online em nossos desktops e smartphones.
            """
        )

    def subcapitulo9_2():
        criar_subcapitulo(
            "Finanças de um\nnegócio digital",
            """
As empresas digitais e os infoprodutores estão em um mercado promissor. Afinal, com o crescimento do comércio online, as oportunidades se ampliaram para o empreendedor que deseja aproveitá-las. Mas é fundamental ter uma gestão financeira eficiente para que seu negócio alcance sucesso.
Assim, é possível manter a boa saúde financeira da organização, crescer e ter resultados positivos. No entanto, o controle das finanças é uma das maiores dificuldades enfrentadas pelos empreendedores. Por isso, é importante obter conhecimento sobre gestão financeira.
Com o crescimento desse nicho, surgem mais profissionais e organizações interessados em aproveitar as oportunidades.
Entretanto, parte dos empreendedores não se preocupa em ter uma gestão financeira eficaz — pelo menos, até sofrerem as consequências da falta dessa prática. Assim, não ter o controle sobre as finanças é um dos maiores erros no empreendedorismo.
Ao retirar dinheiro além do que o caixa suporta, por exemplo, a empresa pode gerar dívidas que se acumulam, prejudicando o seu crescimento. Dessa maneira, a organização que não tem uma gestão financeira eficiente está sujeita ao fracasso. 
Afinal, uma boa saúde financeira é fundamental para a longevidade de qualquer negócio — inclusive digital.
Não é incomum encontrar empresas digitais mais enxutas, com poucos funcionários e a presença do empreendedor em funções mais ativas. Essa estrutura simples pode trazer vantagens e riscos. Um deles é levar o proprietário a misturar as finanças de pessoa física e pessoa jurídica.
Esse equívoco compromete muito a saúde financeira do seu negócio — e, consequentemente, as suas finanças pessoais. Isso porque misturar as contas não dá clareza sobre o caixa necessário para o negócio. Assim, a empresa pode não ter capital para seguir suas operações, por exemplo. 
Por isso, vale a pena ter mais de uma conta bancária. Também é válido determinar o seu salário e viver com esse dinheiro. O restante será o dinheiro da empresa.
Após entender a importância de separar as finanças da empresa e da pessoa física, é o momento de analisar a situação atual do seu negócio. Para isso, saiba qual é o valor em caixa, a média de vendas mensais, se há dívidas vencidas e a vencer etc.
Desse modo, você tem informações relevantes para elaborar um plano de ação para a gestão financeira.
Os indicadores são ferramentas que mensuram o desempenho de determinado processo ou setor. No caso dos indicadores financeiros, eles quantificam a performance das finanças da empresa. Assim, eles funcionam como um guia para entender a situação real do negócio e tomar decisões.
O lucro líquido, por exemplo, é o dinheiro que sobra no caixa após pagar todas as despesas da empresa.
Além de entender a situação atual da empresa e analisar indicadores, é interessante projetar o fluxo de caixa para os próximos meses. Isso é especialmente relevante para quem vende infoprodutos em lançamento. 
Afinal, nessa modalidade de vendas, a entrada de receita é sazonal. Assim, ao fazer a projeção do faturamento, você garante que a organização terá dinheiro para cobrir os custos nas épocas em que não há entradas no caixa.
Como foi possível acompanhar, fazer a gestão financeira de uma empresa digital não é uma tarefa fácil, principalmente para quem não está habituado a essa atividade. Ao mesmo tempo, o gerenciamento deve ser feito regularmente e sem erros.
Felizmente, há como contar com software especializado para obter ajuda em todos os processos
Além disso, você pode automatizar as tarefas burocráticas, como emissão de boletos e notas fiscais, e aproveitar outras funcionalidades. Assim, será viável ter mais tempo para se dedicar a outras atividades do seu negócio e buscar aumento de lucros.
            """
        )

    def subcapitulo9_3():
        criar_subcapitulo(
            "Pagamento online",
            """
Para uma transação digital acontecer sem fraudes ou problemas, principalmente em um e-commerce, gestores precisam utilizar meios de garantir a segurança em pagamentos online, a exemplo da criptografia e da autenticação em dois fatores, dentre outros que você confere neste artigo.
O primeiro passo para qualquer empreendedor saber como evitar golpes online, inclusive colocando-se no lugar de quem compra, é saber detalhes sobre o processo de pagamento digital e quais os meios mais usados.
Para que um pagamento online aconteça, é fundamental que tanto as empresas quanto os consumidores tenham acesso a ferramentas digitais. Quem fornece um produto ou serviço precisa contar com um e-commerce, uma plataforma de vendas na web, e o cliente precisa usufruir do máximo de flexibilidade em termos de opções de pagamentos.
Destaque para cartões de crédito e débito, Pix, boletos, links de pagamento e carteiras digitais.
Pagamentos online são, de forma resumida, todas as transações que ocorrem de maneira virtual e não ficam restritos só ao celular e ao computador.
Atualmente, o pagamento online acontece com mais frequência através dos cinco diferentes formatos listados a seguir:
Cartões de crédito e débito: unindo compras online e offline, os brasileiros movimentaram mais de R$ 330 trilhões só em 2022 apenas no cartão de crédito. Tanto esse formato quanto o débito são amplamente utilizados.
Pix: o meio de pagamento que está dominando o mercado garante o envio instantâneo e sem custos de dinheiro para quem precisa receber um pagamento. Ele é o segundo formato mais usado no Brasil, se você considerar as compras como um todo e não só em ambientes digitais, perdendo apenas para o dinheiro físico.
Carteiras digitais: aos poucos, as chamadas “e-wallets” estão caindo no gosto dos consumidores. Destaque para as das marcas PayPal, Google Pay, Apple Pay, PagSeguro e MercadoPago.
Boletos: este ainda entra como um dos formatos mais utilizados do mercado, mesmo sem ser impresso. Com certeza, você paga boletos através do aplicativo do seu banco pela internet ou pelo celular de vez em quando, não é mesmo?
Link de pagamento: por meio dele, o cliente recebe a cobrança de uma conta através do WhatsApp ou do endereço de e-mail e consegue acertar o valor em apenas alguns cliques.
Enfim, a verdade é que, a cada dia que passa, a população no geral toca menos em papel moeda e usa mais os apps e sites para pagar ou receber, e tudo isso gera uma janela de oportunidades para golpistas à espreita, logo, fique atento(a).
            """
        )

    def subcapitulo9_4():
        criar_subcapitulo(
            "Impostos para\nnegócios digitais",
            """
Dentre as opções mais comuns para negócios online, destacam-se o Simples Nacional, mencionado anteriormente, e o Lucro Presumido. Para aqueles cuja receita ultrapassa a impressionante marca de 78 milhões ao ano, o Lucro Real se torna a única opção. 

Simples Nacional
O Simples Nacional é um regime tributário que se destaca por consolidar o pagamento de até oito diferentes impostos em uma única guia. Essa simplificação facilita enormemente o processo de recolhimento tributário mensal para pequenos e médios negócios digitais.
O limite de receita anual permitido para enquadramento neste regime é de até R$ 4,8 milhões, o que corresponde a uma média de R$ 400 mil por mês. Dentro desse regime, os impostos são calculados com base na receita bruta acumulada, levando em conta também o tipo de atividade exercida pela empresa. É uma opção atrativa para quem busca simplicidade e eficiência na gestão dos impostos para negócios online.

Lucro Presumido
Por outro lado, o regime de Lucro Presumido funciona através de uma estimativa prévia feita pela Receita Federal sobre a margem de lucro do negócio. Esta base de cálculo simplificada serve para determinar os impostos devidos pela empresa.
O Lucro Presumido é uma escolha vantajosa para empresas digitais que possuem uma margem de lucro bem definida e que buscam flexibilidade na gestão fiscal.

Impostos para negócios online: Como calcular no Simples Nacional?
O Simples Nacional é um regime tributário que oferece um método simplificado de recolhimento de impostos para negócios online, incluindo uma variedade de atividades comerciais.
Este regime é dividido em cinco tabelas de tributação, que variam conforme o tipo de atividade exercida. Para os empreendimentos digitais, a tributação pode ser realizada sob o Anexo III ou Anexo V, com alíquotas iniciando em 6% e 15,5%, respectivamente. A escolha do anexo adequado é fundamental, pois influencia diretamente a carga tributária do negócio.

Anexo V do Simples Nacional
Negócios digitais, em geral, se encaixam no Anexo V do Simples Nacional, conforme determinado pela Classificação Nacional de Atividades Econômicas (CNAEs). Este anexo é indicado para atividades com maior lucratividade, mas também com alíquotas iniciais mais altas, começando em 15,5%. É essencial que empreendedores digitais compreendam como essa classificação afeta os impostos de seus negócios online.

Anexo III do Simples Nacional
Felizmente negócios online classificados inicialmente sob o Anexo V têm a possibilidade de migrar para o Anexo III, que oferece alíquotas mais favoráveis, a partir de 6%. Para tal, é necessário que o fator R — que é a razão entre a folha de pagamento dos últimos 12 meses e o faturamento bruto no mesmo período — seja igual ou superior a 28%.

Quais são os negócios online tributáveis pelo Anexo III?
Diversos tipos de negócios online são diretamente tributáveis pelo Anexo III, incluindo:
Copywriters;
Co-produtores;
Influenciadores digitais;
Produtores de conteúdo digital (Infoprodutores);
Profissionais de mentorias;
Especialistas em mídias sociais (Social Media);
Streamers;
Youtubers.
Essas atividades se destacam no cenário digital e são diretamente beneficiadas pelas alíquotas mais vantajosas do Anexo III, ressaltando a importância de possuir conhecimentos técnicos atualizados e um planejamento tributário eficaz.

Quais são os negócios online tributáveis pelo Anexo V?
Certas atividades digitais são inicialmente classificadas sob o Anexo V, contudo, possuem a oportunidade de transição para o Anexo III. Entre elas, encontramos:
Afiliados;
Agências de lançamento;
Agências de marketing digital;
Empresas de dropshipping;
Gestores de tráfego.
Para efetivar essa mudança, é essencial a consultoria de uma contabilidade especializada. Esse apoio profissional garante que a transição seja realizada de forma legal e otimizada, assegurando que os negócios online aproveitem ao máximo as possibilidades tributárias disponíveis, potencializando suas operações e contribuindo para uma gestão fiscal mais eficiente.

Impostos para negócios online: Como calcular no lucro presumido?
Quando se trata do regime de Lucro Presumido, os impostos para negócios online adotam uma abordagem um pouco diferente daquela do Simples Nacional. Ao invés de um recolhimento unificado, os tributos são pagos de maneira separada, com alguns impostos sendo apurados mensalmente e outros, trimestralmente.
Para negócios digitais, as alíquotas variam de 11,33% a 16,33%, influenciadas pelo ISS (Imposto Sobre Serviços) que flutua entre 2% e 5%, a depender do município onde a empresa opera.
Adicionalmente, empresas que registram um faturamento superior a R$187.500,00 por trimestre no Lucro Presumido estão sujeitas ao pagamento de um Imposto de Renda adicional de 10% sobre a parcela que excede este limite.
Este detalhe é fundamental para negócios online que apresentam uma receita elevada, destacando a importância de uma gestão tributária atenta e estratégica.
            """
        )

    def subcapitulo9_5():
        criar_subcapitulo(
            "Tendências do\nmercado digital\ne \nde investimento",
            """
O mercado digital é uma expressão abrangente para cobrir todas as atividades comerciais que se estabelecem na internet, desde as atividades de compra, venda, anúncio, atendimento e demais interações que ocorrem, acontece por meio de interações entre os consumidores e as empresas no ambiente online. Isso significa que é essencial ter acesso à internet para conseguir aproveitar o crescimento que ele vem apresentando, além de entender o comportamento do consumidor.
Existem vários aspectos que tornam o mercado digital e suas plataformas um ambiente atrativo. O melhor é que isso acontece por um custo bem baixo, além de existirem ferramentas que podem potencializar os resultados, oferecendo escalabilidade para o seu empreendimento. Há vários modelos de negócios que podem ser iniciados nesse ambiente.
Por fim, vale ressaltar a possibilidade de acompanhar métricas para encontrar pontos de melhorias, sendo essa uma característica muito forte desse ambiente.

O mercado digital é um oceano azul, cheio de oportunidades para as empresas. Porém, para aproveitá-las da melhor forma possível, é importante entender as tendências para aplicá-las em seu negócio. 

1 - Mobile Marketing
O uso de smartphones é muito elevado no Brasil e no mundo. Segundo dados, já são mais de 190 milhões de aparelhos. Por isso, o mobile marketing é uma tendência que merece atenção. Para aproveitá-la, é preciso ajustar as suas páginas, tornando-as mobile friendly. Ou seja, elas devem se adaptar às telas dos dispositivos móveis para oferecer uma experiência incrível para os consumidores.

2 - Lives
Outra estratégia de marketing digital de sucesso, que pode ser aproveitada nesse mercado, são as transmissões ao vivo. Elas representam uma ótima maneira de criar vínculo com a audiência da empresa. E isso é essencial, afinal, as pessoas compram de quem elas confiam. 

3 - Conteúdos visuais
Os conteúdos visuais também ganharam campo e hoje são uma das tendências do mercado digital. Principalmente os desenvolvidos em vídeo, que prendem a atenção das pessoas.

4 - Realidade virtual
A transformação digital também está ganhando espaço e se tornando cada vez mais real no mundo. Com isso, recursos de realidade virtual também obtém destaque no mundo online.

5 - Geomarketing
O geomarketing não é uma novidade, porém, entra na lista porque é eficaz e pode agregar muito nas estratégias e transformação digital em vendas da sua empresa. Isso porque ele foca em ações específicas para uma região. Por exemplo, você consegue limitar os anúncios realizados por meio das redes sociais apenas para a sua cidade. 

6 - Web Analytics
O uso de dados é cada vez mais primordial para acompanhar a performance das campanhas de marketing e vendas e adotar melhorias. Para isso é preciso realizar análises detalhadas a fim de encontrar possíveis erros. É aí que entra o Web Analytics. Ele vai ajudar a encontrar ideias do que pode ser feito no seu negócio e identificar os pontos fracos e fortes das ações que estão sendo implementadas.

7 - Inteligência artificial
Por fim, a tendência da moda é a inteligência artificial. Ferramentas como o ChatGPT tem conquistado espaço no cotidiano das pessoas. Inclusive, conforme dados levantados, esse foi o aplicativo com crescimento mais rápido da história. Recursos que usam a IA podem ajudar no atendimento ao público, nas estratégias de marketing, edição de imagens e com muitas outras tarefas.
            """
        )

    def subcapitulo9_quiz():
            criar_quiz()

    def subcapitulo9_desafio():
        criar_subcapitulo(
            "Desafio",
            """
Parabéns por chegar até aqui, futuro empreendedor digital!
Você explorou conceitos fundamentais sobre Modelos de Negócios Digitais, Finanças, Pagamentos Online, Impostos e Tendências do Mercado Digital. Agora é a hora de colocar seus conhecimentos em prática e dar o primeiro passo na jornada rumo ao sucesso no mercado online.

Sua missão:
Escolha um modelo de negócio digital que você gostaria de implementar (e-commerce, marketplace, SaaS, etc.).
Elabore um plano financeiro básico para os primeiros 6 meses, respondendo às seguintes perguntas:
Qual será seu investimento inicial?
Quais são os principais custos fixos e variáveis?
Quanto você espera faturar mensalmente?
Utilize um indicador financeiro (como lucro líquido ou margem de contribuição) para projetar o desempenho do seu negócio.
Planeje sua estratégia de pagamento online:
Quais métodos de pagamento você oferecerá?
Como garantirá segurança nas transações?
Estude o regime tributário mais adequado para o seu negócio (Simples Nacional ou Lucro Presumido) e calcule o impacto dos impostos no seu faturamento.
Reflexão final:
Após concluir este desafio, reflita:

Sua estratégia financeira é realista e sustentável?
Quais ajustes você faria no seu planejamento?
A pergunta que fica é: você está pronto para transformar sua ideia em um negócio digital de sucesso?
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
            criar_bloco("Modelos de negócios digitais", lambda _: subcapitulo9_1()),
            criar_bloco("Finanças de um negócio digital", lambda _: subcapitulo9_2()),
            criar_bloco("Pagamento online", lambda _: subcapitulo9_3()),
            criar_bloco("Impostos para negócios digitais", lambda _: subcapitulo9_4()),
            criar_bloco("Tendências do mercado digital e oportunidades de investimento", lambda _: subcapitulo9_5()),
            criar_bloco("Quiz", lambda _: subcapitulo9_quiz()),
            criar_bloco("Desafio", lambda _: subcapitulo9_desafio()),
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
