Guia completo de planilhas do zero absoluto
Se você nunca abriu uma planilha na vida, este é o seu ponto de partida. Este tutorial vai transformar você de alguém que não sabe o que é uma célula em alguém pronto para usar VLOOKUP, Tabelas Dinâmicas e criar dashboards profissionais. O guia cobre tudo — desde “o que é isso?” até exercícios práticos — em Google Sheets e Microsoft Excel, as duas plataformas que dominam o mercado e aparecem em praticamente toda entrevista de emprego. Ao final, você terá a base necessária para encarar um plano de estudo de 3 horas focado em funções avançadas.
--------------------------------------------------------------------------------
PARTE 1 — O que é uma planilha e por que ela existe
Uma planilha eletrônica é uma grade organizada em linhas (horizontais, numeradas: 1, 2, 3…) e colunas (verticais, identificadas por letras: A, B, C… Z, AA, AB…). O cruzamento de uma linha com uma coluna forma uma célula — o bloco fundamental de toda planilha. Cada célula tem um endereço único baseado na combinação da letra da coluna com o número da linha: a célula no canto superior esquerdo é A1, a célula ao lado direito é B1, a célula logo abaixo é A2, e assim por diante. Esse sistema de coordenadas funciona como uma grade de batalha naval.
Um arquivo de planilha pode conter várias abas (também chamadas de “sheets” ou “planilhas”), visíveis como guias na parte inferior da tela. Isso permite organizar dados relacionados em páginas separadas — por exemplo, uma aba por mês num controle financeiro.
Os três tipos de conteúdo que uma célula aceita
Toda célula pode conter apenas um destes três tipos de conteúdo:
Texto — qualquer combinação de letras, números e símbolos tratada como informação descritiva. O texto se alinha à esquerda automaticamente. Exemplos: “João Silva”, “Departamento de Vendas”, “SKU-1234”. Texto não pode ser usado em cálculos matemáticos.
Número — valores numéricos como 42, 3.14, R$ 500,00 ou 75%. Números se alinham à direita automaticamente. Datas também são números internamente — o computador armazena cada data como um número sequencial (1º de janeiro de 1900 = 1, e cada dia seguinte soma 1). É por isso que é possível subtrair datas para calcular intervalos.
Fórmula — uma instrução de cálculo que sempre começa com o sinal de igual (=). A célula mostra o resultado da fórmula, mas a barra de fórmulas mostra a fórmula em si. Exemplo: se você digitar =50+50 em uma célula, ela mostrará 100, mas ao clicar na célula, a barra de fórmulas exibirá =50+50.
Dica visual para identificar tipos: se um valor está alinhado à esquerda, provavelmente é texto; se está à direita, é um número ou data. Essa é a maneira mais rápida de detectar problemas como “números armazenados como texto” — um erro muito comum que faz fórmulas de soma darem zero.
Referências de célula — o conceito mais importante
Uma referência de célula é quando você menciona o endereço de uma célula dentro de uma fórmula em vez de digitar o valor diretamente. Em vez de escrever =1200*12, você escreve =B2*12, onde B2 contém o valor 1200. A vantagem? Se o valor de B2 mudar para 1500, a fórmula recalcula automaticamente. Toda planilha profissional funciona com referências, não com valores digitados diretamente.
Referências relativas, absolutas e mistas
Este conceito é absolutamente crítico para entrevistas de emprego e uso profissional:
Referência relativa (A1) — é o padrão. Quando você copia ou arrasta uma fórmula para outra célula, a referência se ajusta automaticamente. Se a célula C1 contém =A1+B1 e você copia para C2, ela se torna =A2+B2. O Excel e o Sheets “entendem” que você quer repetir a mesma lógica na linha seguinte.
Referência absoluta (A1) — os cifrões ()travamarefer 
e
^
 ncia.N 
a
~
 oimportaparaondevoc 
e
^
 copieaf 
o
ˊ
 rmula,‘A$1` sempre apontará para A1. Use quando uma célula contém um valor fixo que todos os cálculos precisam consultar, como uma taxa de imposto ou câmbio.
Referência mista (A1ouA1) — trava apenas a coluna ou apenas a linha. $A1 mantém a coluna A fixa mas permite que a linha mude; A$1 mantém a linha 1 fixa mas permite que a coluna mude. Útil para tabelas de multiplicação e matrizes.
Atalho essencial: ao editar uma fórmula, clique sobre a referência da célula e pressione F4 para alternar entre os quatro modos: A1 → A1 → A$1 → $A1 → A1. Funciona tanto no Excel quanto no Google Sheets.
Exemplo prático — Cálculo de imposto sobre vendas:
A (Produto)
B (Preço)
C (Taxa)
D (Imposto)
1
Produto
Preço
Taxa
Imposto
2
Notebook
R$ 4.999
7,5%
=B2*C2
3
Mouse
R$ 89
7,5%
=B3*C2
4
Teclado
R$ 250
7,5%
=B4*C2
Na coluna D, B2 é relativa (muda para B3, B4 ao copiar para baixo), mas C2 é absoluta (sempre aponta para a célula da taxa). Se você arrastar a fórmula de D2 até D4, tudo funciona automaticamente.
O que é um intervalo (range)
Um intervalo é um grupo retangular de células, expresso com dois-pontos entre o primeiro e o último endereço: A1:C10 significa “todas as células de A1 até C10” (3 colunas × 10 linhas = 30 células). Intervalos são usados em praticamente todas as funções: =SUM(A1:A10), =AVERAGE(B2:B20), =VLOOKUP(D2, A1:C100, 2, FALSE).
Também é possível referenciar intervalos não contíguos usando vírgula: =SUM(A1:A5, C1:C5) soma dois intervalos separados.
Navegação e interface — elementos comuns às duas plataformas
Antes de mergulhar em cada plataforma, saiba que ambas compartilham elementos essenciais:
Barra de fórmulas — localizada acima da grade de células, mostra o conteúdo real da célula selecionada. Se a célula contém uma fórmula, aqui você vê a fórmula (não o resultado). Clique na barra de fórmulas para editar diretamente. Para ver todas as fórmulas de uma vez, pressione Ctrl+` (acento grave).
Caixa de Nome — à esquerda da barra de fórmulas, mostra o endereço da célula ativa (ex.: “A1”). Você pode clicar nela, digitar qualquer endereço (ex.: “Z100”) e pressionar Enter para navegar instantaneamente.
Abas de planilha — na parte inferior da tela, cada aba representa uma planilha dentro do arquivo. Clique no + para criar nova aba. Clique com o botão direito sobre uma aba para renomear, excluir, duplicar ou mover.
Atalhos universais essenciais (funcionam em ambas as plataformas):
Ação
Atalho (Windows)
Copiar
Ctrl+C
Colar
Ctrl+V
Recortar
Ctrl+X
Desfazer
Ctrl+Z
Refazer
Ctrl+Y
Negrito
Ctrl+B
Itálico
Ctrl+I
Localizar
Ctrl+F
Editar célula ativa
F2
Alternar referência
F4
Selecionar tudo
Ctrl+A
Ir para célula A1
Ctrl+Home
Pular entre abas
Ctrl+Page Down / Page Up
--------------------------------------------------------------------------------
PARTE 2 — Google Sheets do zero absoluto
Como acessar e criar sua primeira planilha
Requisitos: apenas uma conta Google gratuita (Gmail). Funciona em qualquer navegador moderno — Chrome, Firefox, Edge, Safari. Nenhuma instalação é necessária.
Três formas de abrir o Google Sheets:
Atalho instantâneo: digite sheets.new na barra de endereço do navegador e pressione Enter. Uma planilha em branco é criada imediatamente.
Página inicial do Sheets: acesse sheets.google.com para ver seus arquivos recentes e modelos prontos.
Pelo Google Drive: acesse drive.google.com → clique no botão + Novo → Google Planilhas → Planilha em branco.
A interface do Google Sheets, de cima para baixo:
Barra de título (canto superior esquerdo): mostra o nome da planilha (“Planilha sem título” por padrão). Clique diretamente sobre o texto para renomear.
Barra de menus: Arquivo, Editar, Ver, Inserir, Formatar, Dados, Ferramentas, Extensões, Ajuda.
Barra de ferramentas (ícones abaixo do menu): botões rápidos para Desfazer/Refazer, Imprimir, Copiar Formatação (ícone de rolo de pintura), Zoom, Formato de moeda/porcentagem, Fonte, Tamanho, Negrito, Itálico, Cor do texto, Cor de preenchimento, Bordas, Alinhamento, Filtro (funil), Funções (Σ).
Barra de fórmulas (fx): à esquerda mostra o endereço da célula; à direita mostra o conteúdo/fórmula.
Cabeçalhos de coluna: letras A, B, C… no topo.
Cabeçalhos de linha: números 1, 2, 3… na lateral esquerda.
Grade de células: a área principal de trabalho. Uma planilha nova tem 1.000 linhas e 26 colunas (expandíveis).
Abas de planilha (parte inferior): mostra as abas existentes (padrão: “Página1”) e o botão + para criar novas.
Salvamento: o Google Sheets salva automaticamente e continuamente no Google Drive. Não existe botão “Salvar” — toda edição é salva em tempo real. A mensagem “Todas as alterações foram salvas no Drive” aparece próximo ao menu.
Compartilhamento — passo a passo:
Clique no botão azul “Compartilhar” no canto superior direito.
Digite o e-mail da pessoa no campo indicado.
À direita do campo de e-mail, clique no menu suspenso para escolher o nível de permissão:
Leitor — só pode ver, não pode editar nem comentar
Comentador — pode ver e comentar, mas não edita dados
Editor — pode ver, editar e adicionar dados livremente
Clique em “Enviar”.
Para compartilhar via link: na mesma janela, em “Acesso geral”, altere de “Restrito” para “Qualquer pessoa com o link” e defina se será Leitor, Comentador ou Editor.
Primeiros passos práticos no Google Sheets
Digitando dados: clique em qualquer célula e comece a digitar. Pressione Enter para confirmar e descer uma célula, Tab para confirmar e mover para a direita, ou Esc para cancelar. Para editar uma célula existente, dê dois cliques sobre ela ou selecione e pressione F2.
Formatação de células — caminhos exatos:
Negrito: Ctrl+B ou clique no B na barra de ferramentas
Itálico: Ctrl+I
Sublinhado: Ctrl+U
Cor do texto: clique no ícone “A” com barra colorida na barra de ferramentas → escolha a cor
Cor de preenchimento (fundo): clique no ícone de balde de tinta → escolha a cor
Bordas: clique no ícone de grade na barra de ferramentas → escolha o tipo (todas, externas, internas)
Formato numérico: Formatar → Número → escolha entre Número, Moeda, Porcentagem, Data, etc.
Atalhos de formato numérico: Ctrl+Shift+1 (número), Ctrl+Shift+4 (moeda), Ctrl+Shift+5 (porcentagem), Ctrl+Shift+3 (data)
Limpar toda formatação: Ctrl+\
Redimensionar colunas e linhas:
Arrastar: posicione o cursor na borda entre duas letras de coluna (ex.: entre A e B) até ele virar uma seta dupla ↔. Clique e arraste.
Ajuste automático ao conteúdo: dê dois cliques na borda da coluna/linha — ela se ajusta ao conteúdo mais largo/alto.
Valor exato: clique com o botão direito na letra da coluna → “Redimensionar coluna” → digite o valor em pixels → OK.
Preenchimento automático (Auto-fill) — o quadradinho azul mágico:
Selecione uma célula com um valor e observe o pequeno quadrado azul no canto inferior direito. Posicione o cursor sobre ele até virar uma cruz (+), clique e arraste para baixo ou para o lado.
O comportamento muda conforme o conteúdo:
Um número sozinho (ex.: “5”): copia o mesmo valor (5, 5, 5, 5…)
Dois números em sequência (ex.: “1” na célula A1 e “2” na A2): selecione ambos e arraste → continua a sequência (3, 4, 5, 6…)
Dois números com intervalo (ex.: “2” e “4”): selecione ambos e arraste → incrementa de 2 em 2 (6, 8, 10…)
Uma data (ex.: “01/01/2025”): arrastar gera dias consecutivos (02/01, 03/01…)
Texto com número (ex.: “Item 1”): gera Item 2, Item 3, Item 4…
Dias da semana (ex.: “Segunda”): gera Terça, Quarta, Quinta…
Meses (ex.: “Janeiro”): gera Fevereiro, Março, Abril…
Fórmulas: copia a fórmula ajustando as referências relativas automaticamente
Dica avançada: dê dois cliques no quadradinho azul para preencher automaticamente até a última linha de dados adjacentes, sem precisar arrastar manualmente.
Classificação e filtro:
Para classificar (ordenar) dados: clique em qualquer célula da coluna desejada → menu Dados → “Classificar página por coluna X, de A a Z” (ou de Z a A).
Para filtrar dados: selecione qualquer célula nos seus dados → Dados → Criar um filtro (ou clique no ícone de funil na barra de ferramentas). Setas de menu suspenso (▼) aparecem em cada cabeçalho de coluna. Clique na seta para filtrar por valores específicos, condições (“maior que”, “contém”, etc.) ou cor.
Congelar linhas/colunas (manter cabeçalhos visíveis ao rolar):
Vá em Ver → Congelar
Escolha: 1 linha (congela apenas o cabeçalho) ou 2 linhas, 1 coluna ou 2 colunas
Uma linha cinza grossa aparece indicando o limite congelado
Para descongelar: Ver → Congelar → Nenhuma linha / Nenhuma coluna.
Suas primeiras fórmulas no Google Sheets
Toda fórmula começa com = (sinal de igual). Digite = em qualquer célula, escreva a fórmula e pressione Enter.
Fórmulas básicas essenciais:
Fórmula
O que faz
Exemplo
=A1+B1
Soma duas células
=A1+B1
=A1-B1
Subtrai
=A1-B1
=A1*B1
Multiplica
=A1*B1
=A1/B1
Divide
=A1/B1
=SUM(A1:A10)
Soma um intervalo inteiro
=SUM(A1:A10)
=AVERAGE(A1:A10)
Calcula a média
=AVERAGE(A1:A10)
=COUNT(A1:A10)
Conta células com números
=COUNT(A1:A10)
=COUNTA(A1:A10)
Conta células não vazias
=COUNTA(A1:A10)
=MAX(A1:A10)
Valor máximo
=MAX(A1:A10)
=MIN(A1:A10)
Valor mínimo
=MIN(A1:A10)
Como copiar/arrastar fórmulas: digite a fórmula na primeira célula, pressione Enter, selecione a célula novamente e use o quadradinho azul (fill handle) para arrastar. As referências relativas se ajustam automaticamente — =A1+B1 copiada uma linha para baixo vira =A2+B2.
⚠️ PONTO CRÍTICO — Idioma das funções no Google Sheets:
O Google Sheets usa nomes de funções em inglês por padrão, independentemente do idioma da interface. Mesmo que seus menus apareçam em português, as fórmulas usam SUM (não SOMA), AVERAGE (não MÉDIA), IF (não SE). Isso é controlado por uma configuração em Arquivo → Configurações, onde existe a opção “Sempre usar nomes de funções em inglês” — que vem ativada por padrão.
Se você desmarcar essa opção, pode usar nomes em português. Porém, a recomendação para iniciantes é: aprenda os nomes em inglês primeiro, pois são o padrão do Google Sheets e aparecem em tutoriais internacionais. Mais adiante neste guia, há uma tabela completa de tradução.
Separador de argumentos: no Google Sheets com a configuração padrão (inglês), use vírgula para separar argumentos: =SUM(A1, B1, C1). Se mudar para funções em português e o locale for Brasil, o separador passa a ser ponto e vírgula: =SOMA(A1; B1; C1).
Configurações importantes do Google Sheets
Localidade da planilha (afeta formato de números, datas e moeda):
Vá em Arquivo → Configurações → aba “Geral”. No campo “Localidade”, selecione “Brasil”. Isso define:
Formato de data: DD/MM/AAAA (ex.: 15/03/2025)
Separador decimal: vírgula (ex.: 1.234,56)
Separador de milhar: ponto
Símbolo de moeda: R$
Fuso horário: ajuste conforme sua região
Recurso “Explorar” — descontinuado: o Google descontinuou o botão “Explorar” em janeiro de 2024. Ele foi parcialmente substituído pelo Gemini (IA do Google) para assinantes do Workspace, e pelo Localizador de ferramentas (Alt+/ no Windows ou Option+/ no Mac), que permite buscar qualquer ação do menu por nome.
--------------------------------------------------------------------------------
PARTE 3 — Microsoft Excel do zero absoluto
Como acessar o Excel (três opções)
Opção 1 — Excel Online (GRATUITO):
Acesse office.com e faça login com uma conta Microsoft gratuita, ou digite excel.new na barra do navegador para criar uma planilha instantaneamente
Funciona em qualquer navegador. Arquivos salvam automaticamente no OneDrive (5 GB gratuitos)
Inclui a maioria dos recursos que um iniciante precisa
Opção 2 — Excel Desktop (PAGO, com opções gratuitas):
Assinatura Microsoft 365: aproximadamente R36/m 
e
^
 s(Pessoal)ouR 45/mês (Família)
Estudantes e professores: acesse microsoft.com/education com e-mail institucional (.edu) para verificar se sua instituição oferece acesso gratuito
Teste grátis de 1 mês disponível em microsoft.com/microsoft-365/try
Possui todas as funcionalidades: macros/VBA, Power Query, Power Pivot, gráficos avançados, trabalho offline
Opção 3 — Excel no celular:
App gratuito disponível na App Store (iOS) e Google Play (Android)
Bom para visualização e edições simples
Como criar uma conta Microsoft gratuita:
Acesse outlook.live.com e clique em “Criar conta gratuita”
Escolha um endereço de e-mail (terminará em @outlook.com)
Crie uma senha
Preencha nome e sobrenome
Complete a verificação de segurança
Pronto — agora acesse office.com com este e-mail
Se você já tem e-mail @outlook.com, @hotmail.com, @msn.com ou @live.com, já possui uma conta Microsoft.
A interface do Excel — o Ribbon (Faixa de Opções)
A maior diferença visual entre Excel e Google Sheets é a Faixa de Opções (Ribbon) — uma barra de ferramentas organizada em Guias (Tabs), cada uma contendo Grupos de comandos relacionados.
Guias principais em português (PT-BR):
Guia PT-BR
Guia em Inglês
Para que serve
Arquivo
File
Abrir, salvar, imprimir, compartilhar
Página Inicial
Home
Formatação, fonte, alinhamento, números, clipboard
Inserir
Insert
Gráficos, tabelas, imagens, links
Layout da Página
Page Layout
Margens, orientação, impressão
Fórmulas
Formulas
Inserir funções, gerenciar nomes
Dados
Data
Classificar, filtrar, importar dados
Revisão
Review
Ortografia, comentários, proteção
Exibir
View
Zoom, congelar painéis, modos de visualização
Dentro da guia “Página Inicial”, os grupos mais importantes são:
Área de Transferência — Recortar, Copiar, Colar, Pincel de Formatação
Fonte — Nome da fonte, tamanho, Negrito, Itálico, bordas, cor de preenchimento, cor da fonte
Alinhamento — Alinhar esquerda/centro/direita, Quebrar Texto, Mesclar e Centralizar
Número — Formato numérico (Geral, Número, Moeda, Data, Porcentagem), botões de casas decimais
Estilos — Formatação Condicional, Formatar como Tabela, Estilos de Célula
Células — Inserir, Excluir, Formatar (largura/altura)
Edição — AutoSoma, Preencher, Classificar e Filtrar, Localizar
Barra de Ferramentas de Acesso Rápido: localizada acima (ou abaixo) do Ribbon, contém por padrão Salvar, Desfazer e Refazer. Personalize clicando com o botão direito.
Barra de Status (parte inferior da janela): quando você seleciona duas ou mais células com números, a barra de status mostra instantaneamente a Soma, Média e Contagem — sem precisar escrever fórmulas. É uma maneira ultra-rápida de verificar dados.
Diferenças entre Excel Online e Excel Desktop
O Excel Online é excelente para iniciantes, mas tem limitações em relação à versão Desktop:
Macros/VBA: não funciona no Online
Power Query e Power Pivot: não disponíveis
Gráficos: limitados a tipos básicos 2D
Guia Fórmulas: aparece quase vazia (mas as fórmulas funcionam normalmente digitando na célula)
Trabalho offline: não é possível
Funcionalidades avançadas de dados: Flash Fill, Texto para Colunas e filtros avançados são limitados
Para os exercícios do plano de 3 horas, o Excel Online é suficiente para a maioria dos tópicos, exceto possivelmente macros. Tabelas Dinâmicas básicas, VLOOKUP, IF, SUMIFS, INDEX+MATCH e gráficos funcionam no Online.
Primeiros passos práticos no Excel
Digitando dados: clique na célula, digite e pressione Enter (desce) ou Tab (move para a direita). Nas configurações regionais PT-BR, use vírgula como separador decimal (ex.: 1234,56) e datas no formato DD/MM/AAAA (ex.: 15/03/2025).
Formatação — caminhos exatos no Ribbon:
Negrito: Página Inicial → grupo Fonte → botão N (ou Ctrl+B)
Bordas: Página Inicial → grupo Fonte → ícone de bordas (quadrado com grade) → escolha o tipo
Cor de preenchimento: Página Inicial → grupo Fonte → ícone de balde de tinta
Formato numérico: Página Inicial → grupo Número → menu suspenso (Geral, Número, Moeda, etc.)
Diálogo completo de formatação: selecione células → Ctrl+1 → abre “Formatar Células” com abas Número, Alinhamento, Fonte, Borda, Preenchimento, Proteção
Redimensionar colunas e linhas:
Arrastar: posicione o cursor na borda entre letras de coluna e arraste
Ajuste automático: dê dois cliques na borda da coluna — ajusta ao conteúdo mais largo
Via Ribbon: Página Inicial → grupo Células → Formatar → AutoAjustar Largura da Coluna
Preenchimento automático (Alça de Preenchimento):
Funciona igual ao Google Sheets, mas o quadradinho é verde (não azul). Selecione a célula, posicione o cursor no canto inferior direito até virar uma cruz preta fina (+), clique e arraste. No Excel PT-BR, meses e dias da semana funcionam em português: “Jan” gera Fev, Mar, Abr… e “Segunda” gera Terça, Quarta…
Após arrastar, um pequeno ícone de Opções de Preenchimento Automático aparece, permitindo escolher entre: Copiar Células, Preencher Série, Preencher somente Formatação ou Preencher sem Formatação.
Classificar e filtrar:
Classificar: selecione uma célula na coluna desejada → guia Dados → Classificar de A a Z ou Classificar de Z a A
Filtro: selecione qualquer célula nos dados → guia Dados → Filtrar (ou Ctrl+Shift+L). Setas de filtro aparecem nos cabeçalhos.
Congelar painéis:
Clique na célula abaixo da(s) linha(s) e à direita da(s) coluna(s) que deseja congelar. Exemplo: para congelar a linha 1, clique em A2; para congelar linhas 1-2 e coluna A, clique em B3.
Vá em guia Exibir → Congelar Painéis → Congelar Painéis
Para congelar apenas a primeira linha: Exibir → Congelar Painéis → Congelar Linha Superior
Para descongelar: Exibir → Congelar Painéis → Descongelar Painéis
Suas primeiras fórmulas no Excel PT-BR
⚠️ DIFERENÇA FUNDAMENTAL: enquanto o Google Sheets usa nomes de funções em inglês, o Excel em português brasileiro usa nomes de funções em português com ponto e vírgula (;) como separador de argumentos.
Fórmulas básicas essenciais no Excel PT-BR:
Fórmula Excel PT-BR
Equivalente em Inglês
O que faz
=SOMA(A1:A10)
=SUM(A1:A10)
Soma um intervalo
=MÉDIA(A1:A10)
=AVERAGE(A1:A10)
Calcula a média
=CONT.NÚM(A1:A10)
=COUNT(A1:A10)
Conta células com números
=CONT.VALORES(A1:A10)
=COUNTA(A1:A10)
Conta células não vazias
=MÁXIMO(A1:A10)
=MAX(A1:A10)
Maior valor
=MÍNIMO(A1:A10)
=MIN(A1:A10)
Menor valor
Exemplo prático: no Google Sheets você digita =SUM(A1:A10), no Excel PT-BR você digita =SOMA(A1:A10). No Google Sheets: =IF(A1>10,"Sim","Não"). No Excel PT-BR: =SE(A1>10;"Sim";"Não") — note o ponto e vírgula.
AutoSoma — o atalho mais útil do Excel:
Clique na célula logo abaixo de uma coluna de números
Pressione Alt + =
O Excel insere automaticamente =SOMA() com o intervalo detectado
Pressione Enter para confirmar
Também acessível via: Página Inicial → grupo Edição → botão AutoSoma (Σ) → clique na seta ao lado para escolher Soma, Média, Contar Números, Máximo ou Mínimo.
Inserir Função (Shift+F3): abre um diálogo onde você pode buscar qualquer função por nome ou categoria. Útil quando não lembra o nome exato.
Tabela de tradução completa das funções que você vai usar
Esta tabela é essencial para quem vai trabalhar nas duas plataformas ou seguir tutoriais em inglês:
Inglês (Google Sheets)
PT-BR (Excel)
Descrição
SUM
SOMA
Soma valores
AVERAGE
MÉDIA
Média aritmética
COUNT
CONT.NÚM
Conta células numéricas
COUNTA
CONT.VALORES
Conta células não vazias
MAX
MÁXIMO
Valor máximo
MIN
MÍNIMO
Valor mínimo
IF
SE
Condição lógica
IFERROR
SEERRO
Trata erros em fórmulas
VLOOKUP
PROCV
Procura vertical
INDEX
ÍNDICE
Retorna valor por posição
MATCH
CORRESP
Encontra posição de um valor
SUMIF
SOMASE
Soma condicional
SUMIFS
SOMASES
Soma com múltiplas condições
COUNTIF
CONT.SE
Conta com condição
COUNTIFS
CONT.SES
Conta com múltiplas condições
AND
E
Operador lógico E
OR
OU
Operador lógico OU
TODAY
HOJE
Data de hoje
NOW
AGORA
Data e hora atuais
LEFT
ESQUERDA
Extrai caracteres da esquerda
RIGHT
DIREITA
Extrai caracteres da direita
LEN
NÚM.CARACT
Conta caracteres
TRIM
ARRUMAR
Remove espaços extras
TEXT
TEXTO
Formata número como texto
ROUND
ARRED
Arredonda número
CONCATENATE
CONCATENAR
Junta textos
TRUE
VERDADEIRO
Valor lógico verdadeiro
FALSE
FALSO
Valor lógico falso
Dica profissional: a Microsoft oferece um suplemento gratuito chamado “Functions Translator” que traduz nomes de funções entre idiomas. Instale via: Inserir → Suplementos → procure “Functions Translator”.
--------------------------------------------------------------------------------
PARTE 4 — Convertendo entre plataformas
Abrindo arquivo Excel (.xlsx) no Google Sheets
Método 1 — Upload pelo Drive:
Acesse drive.google.com
Clique em + Novo → Upload de arquivo → selecione o arquivo .xlsx
Após o upload, clique com o botão direito no arquivo → Abrir com → Google Planilhas
Para converter permanentemente: Arquivo → Salvar como Google Planilhas
Método 2 — Direto no Sheets:
Abra sheets.google.com
Clique no ícone de pasta → aba Upload → arraste o arquivo ou clique em “Procurar”
Baixando Google Sheets como Excel
No Google Sheets: Arquivo → Fazer download → Microsoft Excel (.xlsx). O arquivo é baixado no formato padrão do Excel.
Problemas de compatibilidade que você deve conhecer
Macros/VBA são a maior barreira — simplesmente não funcionam no Google Sheets (que usa uma linguagem diferente, Google Apps Script). Tabelas Dinâmicas básicas transferem bem, mas Tabelas Dinâmicas avançadas (com Data Model ou Power Pivot) podem não converter corretamente. Gráficos padrão (barras, linhas, pizza) transferem sem problemas; gráficos 3D ou muito customizados podem perder formatação. Formatação condicional básica funciona; regras complexas com fórmulas ou conjuntos de ícones podem falhar.
Regra geral: para trabalho colaborativo simples, use Google Sheets. Para análise avançada com macros e Power Query, use Excel Desktop.
--------------------------------------------------------------------------------
PARTE 5 — Boas práticas para dados limpos
Antes de aprender VLOOKUP, Tabelas Dinâmicas ou qualquer função avançada, você precisa organizar seus dados corretamente. Dados mal organizados são a causa número um de erros em planilhas. Siga estas cinco regras sagradas:
Regra 1 — Uma linha de cabeçalho, dados a partir da linha 2. A linha 1 contém títulos descritivos de cada coluna (ex.: “Nome”, “Departamento”, “Salário”). Os dados reais começam na linha 2. Formate os cabeçalhos em negrito para diferenciá-los visualmente. Nunca use múltiplas linhas de cabeçalho.
Regra 2 — Nunca mescle células dentro de uma tabela de dados. Células mescladas causam erros graves em classificação, filtros, Tabelas Dinâmicas e VLOOKUP. O Excel sequer permite mesclar dentro de uma Tabela formatada (Ctrl+T). Se precisa de aparência visual centralizada, use “Centralizar na Seleção” (Formatar Células → Alinhamento → Horizontal → Centralizar na Seleção).
Regra 3 — Sem linhas ou colunas vazias no meio dos dados. O Excel e o Sheets detectam os limites dos dados pela primeira célula vazia. Uma linha vazia no meio “corta” seus dados e faz com que funções como VLOOKUP, filtros e Tabelas Dinâmicas ignorem tudo que está abaixo.
Regra 4 — Tipos de dados consistentes por coluna. Se uma coluna é de preços, todas as células devem conter números. Nunca misture texto como “Pendente” ou “N/A” numa coluna numérica — crie uma coluna separada de “Observações”.
Regra 5 — Cabeçalhos curtos, únicos e sem caracteres especiais. Use “Valor_Venda” em vez de “O Valor Total da Venda do Período (R$)”. Evite acentos e espaços nos cabeçalhos se possível — embora planilhas modernas aceitem, cabeçalhos simples causam menos problemas em integrações.
Formatar como Tabela no Excel (Ctrl+T) — esta funcionalidade transforma um intervalo de dados em um objeto especial com superpoderes:
Selecione qualquer célula nos seus dados
Pressione Ctrl+T
Confirme o intervalo e marque “Minha tabela tem cabeçalhos”
Clique em OK
Benefícios imediatos: a tabela se expande automaticamente quando você adiciona dados, fórmulas se copiam automaticamente para novas linhas, filtros já vêm ativados, linhas alternadas coloridas facilitam a leitura, e qualquer gráfico ou Tabela Dinâmica baseado nessa tabela se atualiza sozinho. No Google Sheets não existe equivalente exato, mas você pode usar Formatar → Cores alternadas + Dados → Criar um filtro para obter resultado similar.
--------------------------------------------------------------------------------
PARTE 6 — O que vem a seguir: prévia das funções avançadas
Após dominar tudo acima, você está pronto para o plano de 3 horas focado em entrevistas de emprego. Aqui está uma prévia do que cada função faz, para que você já saiba o que esperar:
VLOOKUP / PROCV — procura um valor na primeira coluna de uma tabela e retorna um dado correspondente de outra coluna na mesma linha. Pense como procurar o nome de alguém numa lista telefônica para encontrar o número. Exemplo: você tem um código de produto e quer encontrar automaticamente o nome e preço desse produto.
IF / SE — toma uma decisão baseada em uma condição. Se algo é verdadeiro, retorna um valor; se falso, retorna outro. Exemplo: se a nota de um aluno é ≥ 7, mostra “Aprovado”; caso contrário, mostra “Reprovado”.
SUMIFS / SOMASES — soma valores que atendem a múltiplas condições simultaneamente. É como o SUM, mas com filtros embutidos. Exemplo: somar todas as vendas da região “Norte” que aconteceram no mês de “Janeiro”.
Tabelas Dinâmicas (Pivot Tables) — resumem, contam e analisam grandes volumes de dados automaticamente. Sem fórmulas — você simplesmente arrasta e solta campos. A partir de milhares de linhas de vendas, você vê instantaneamente o total por região, por mês ou por vendedor.
INDEX+MATCH / ÍNDICE+CORRESP — dupla poderosa que funciona como VLOOKUP, porém com mais flexibilidade. MATCH encontra a posição de um valor; INDEX busca o dado nessa posição. Diferente do VLOOKUP, pode procurar em qualquer direção, inclusive para a esquerda.
IFERROR / SEERRO — captura erros em fórmulas e substitui por uma mensagem amigável ou valor alternativo, em vez de exibir códigos como #N/D ou #DIV/0!. Exemplo: envolver um VLOOKUP com IFERROR para que, se o item não for encontrado, apareça “Não encontrado” em vez de erro.
Gráficos e Dashboards — gráficos são representações visuais dos dados (barras, linhas, pizza). Dashboards combinam vários gráficos, tabelas e resumos numa única tela para visão panorâmica. Transformam números em histórias visuais.
--------------------------------------------------------------------------------
PARTE 7 — Configuração para praticar e exercícios recomendados
Como se preparar para começar agora
Para Google Sheets: basta ter uma conta Google. Acesse sheets.new e comece. Zero custo, zero instalação.
Para Excel Online (gratuito): crie uma conta Microsoft gratuita em outlook.live.com, depois acesse office.com e clique em Excel. Ou digite excel.new no navegador.
Para Excel Desktop: verifique se sua instituição de ensino oferece acesso gratuito em microsoft.com/education. Caso contrário, use o teste grátis de 1 mês ou trabalhe com o Excel Online, que é suficiente para a maioria dos exercícios.
Alternativa offline gratuita: LibreOffice Calc (download em libreoffice.org) — software gratuito e de código aberto, compatível com arquivos .xlsx, com interface similar ao Excel.
Cinco exercícios práticos para consolidar tudo que você aprendeu
Exercício 1 — Orçamento pessoal mensal (pratica: digitação, formatação, SUM/SOMA, referências) Crie colunas: Categoria, Valor Planejado, Valor Real, Diferença. Adicione categorias como Aluguel, Alimentação, Transporte, Lazer, Contas. Use SUM para totalizar cada coluna e uma fórmula de subtração para a coluna Diferença. Formate como moeda (R$).
Exercício 2 — Controle de notas de alunos (pratica: AVERAGE/MÉDIA, IF/SE, formatação condicional) Crie colunas: Nome do Aluno, Prova 1, Prova 2, Prova 3, Média, Situação. Use AVERAGE para calcular a média e IF para mostrar “Aprovado” (≥7) ou “Reprovado” (<7). Aplique formatação condicional para destacar reprovados em vermelho.
Exercício 3 — Lista de produtos com inventário (pratica: preenchimento automático, classificação, filtros, formatação de tabela) Crie colunas: Código (Item 001, Item 002…), Produto, Categoria, Preço Unitário, Quantidade em Estoque, Valor Total. Use auto-fill para gerar os códigos, fórmula de multiplicação para Valor Total, classifique por categoria e aplique filtros. No Excel, formate como Tabela (Ctrl+T).
Exercício 4 — Lista de tarefas com datas (pratica: datas, TODAY/HOJE, congelar painéis) Crie colunas: Tarefa, Prioridade, Data Limite, Status, Dias Restantes. Use a fórmula =Data Limite - TODAY() para calcular dias restantes. Congele a primeira linha. Classifique por data limite.
Exercício 5 — Preparação para VLOOKUP (pratica: duas abas, referências entre planilhas) Na Aba 1, crie uma tabela de vendas: Data, Código do Produto, Quantidade. Na Aba 2, crie um catálogo: Código do Produto, Nome, Preço. Por enquanto, apenas organize os dados seguindo todas as boas práticas — este será o dataset perfeito para praticar VLOOKUP e INDEX+MATCH no plano de 3 horas.
Recursos de aprendizado recomendados
Canais do YouTube em português:
Ninja do Excel — treinamento completo do básico ao avançado
Guru do Excel — parte do projeto “Academia do Excel”, conteúdo estruturado
Planilheiros — dois vídeos novos por semana, cobre também Power BI
Curso de Excel com Johnny Lopes — passo a passo do zero
Canais do YouTube em inglês:
ExcelIsFun (Mike Girvin) — mais de 3.000 vídeos, cursos completos gratuitos
Leila Gharani — dicas práticas com cenários do mundo real
Kevin Stratvert — tutoriais claros para iniciantes
Sites de referência rápida:
ExcelJet (exceljet.net) — mais de 350 guias de funções com exemplos
Chandoo (chandoo.org) — mais de 1.000 artigos, forte em dashboards
Ben Collins (benlcollins.com) — especialista em Google Sheets
Caminhos oficiais:
Google: support.google.com/docs (documentação oficial do Sheets)
Microsoft Learn: learn.microsoft.com (módulos gratuitos e autoguiados)
Microsoft Support: support.microsoft.com/excel (treinamento em vídeo)
--------------------------------------------------------------------------------
Conclusão: da célula A1 ao dashboard profissional
O caminho de “nunca abri uma planilha” até “construo dashboards em entrevistas de emprego” é mais curto do que parece — mas exige que a fundação esteja sólida. Os conceitos que parecem simples neste guia — referências absolutas, tipos de dados, dados limpos sem células mescladas — são exatamente os que separam quem passa na entrevista de quem trava no meio de um exercício.
Três insights que vale levar consigo: primeiro, a maior armadilha para brasileiros que trabalham com ambas as plataformas é a diferença nos nomes das funções — domine a tabela de tradução e você transita entre Excel e Google Sheets sem atrito. Segundo, o hábito de formatar dados como Tabela (Ctrl+T no Excel) elimina a maior parte dos problemas que iniciantes encontram com Tabelas Dinâmicas e VLOOKUP. Terceiro, pratique os cinco exercícios acima antes de iniciar o plano de 3 horas — eles foram desenhados para que cada função avançada faça sentido imediato quando você encontrá-la pela primeira vez.
Agora abra sheets.new ou excel.new, crie sua primeira planilha e comece pelo Exercício 1. A melhor forma de aprender planilhas é fazendo.