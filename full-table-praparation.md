# Guia acelerado de Excel e Google Sheets para entrevistas corporativas

**Se você tem poucas semanas para se preparar, concentre-se primeiro em três competências que aparecem em praticamente toda avaliação técnica corporativa: PROCV/VLOOKUP, Tabelas Dinâmicas (Pivot Tables) e SOMASES/SUMIFS.** Essas três habilidades, combinadas com formatação condicional e gráficos básicos, cobrem cerca de 80% do que é testado em processos seletivos de nível júnior a pleno. Dados do mercado mostram que **44% de todas as vagas publicadas em job boards listam Excel como requisito**, e 82% das posições de nível médio exigem ao menos proficiência básica em planilhas. Empresas de tecnologia e startups tendem a testar Google Sheets, enquanto bancos, consultorias e indústrias tradicionais focam em Excel — mas a lógica das fórmulas é transferível entre ambas. Este guia mapeia exatamente o que estudar, em que ordem, e com quais recursos gratuitos, para levar você do nível básico ao intermediário-avançado no menor tempo possível.

---

## 1. Resumo executivo: o que priorizar com tempo limitado

Com uma janela de 4 a 8 semanas, a estratégia mais eficiente é atacar os tópicos por camadas de impacto. **A primeira camada (semanas 1–2) deve cobrir PROCV, SE/IF, SOMASES/CONT.SES e Tabelas Dinâmicas** — essas competências aparecem em virtualmente 100% dos testes práticos, desde posições administrativas até analistas financeiros. A segunda camada (semanas 3–4) adiciona ÍNDICE/CORRESP (INDEX/MATCH), formatação condicional, validação de dados e gráficos profissionais, diferenciando você de candidatos que ficam apenas no básico. A terceira camada (semanas 5–6) é o salto para o nível avançado: dashboards interativos, Power Query no Excel, e funções QUERY e ARRAYFORMULA no Google Sheets. A quarta camada (semanas 7–8) é dedicada à preparação específica para entrevistas: testes simulados, construção de portfólio e prática de verbalização técnica. Candidatos que dominam as três primeiras camadas já se posicionam no **top 20% dos entrevistados** segundo recrutadores de plataformas como Toggl Hire e TestGorilla. A chave é praticar com dados reais, não apenas memorizar sintaxe.

---

## 2. Mapa de competências cobradas em entrevistas

A tabela abaixo organiza as habilidades por nível de prioridade, comparando como cada uma se aplica no Excel e no Google Sheets. O nível de prioridade reflete a frequência com que cada competência aparece em avaliações técnicas de processos seletivos corporativos.

| Competência | Prioridade | Excel | Google Sheets | Cenário típico de teste |
|---|---|---|---|---|
| PROCV / VLOOKUP | 🔴 Crítico | `=PROCV(valor; tabela; coluna; FALSO)` | Mesma sintaxe: `=VLOOKUP(...)` | "Cruze estas duas tabelas pelo código do produto" |
| PROCX / XLOOKUP | 🟡 Importante | `=PROCX(valor; busca; retorno)` (Excel 365+) | Disponível desde 2023 | "Qual a vantagem sobre o PROCV?" |
| ÍNDICE+CORRESP / INDEX+MATCH | 🔴 Crítico | `=ÍNDICE(faixa; CORRESP(valor; busca; 0))` | Mesma lógica | "Busque um valor à esquerda da coluna-chave" |
| SE / IF (incluindo aninhados) | 🔴 Crítico | `=SE(condição; verdadeiro; falso)` | `=IF(condition, true, false)` | "Classifique vendedores por faixa de desempenho" |
| SOMASES / SUMIFS | 🔴 Crítico | `=SOMASES(soma; critério1_faixa; critério1)` | Mesma estrutura | "Some vendas da região Norte acima de R$1.000" |
| CONT.SES / COUNTIFS | 🔴 Crítico | `=CONT.SES(faixa1; critério1; faixa2; critério2)` | Mesma estrutura | "Conte quantos pedidos atrasados existem por região" |
| Tabela Dinâmica / Pivot Table | 🔴 Crítico | Inserir → Tabela Dinâmica | Inserir → Tabela Dinâmica | "Resuma vendas por trimestre e região" |
| Formatação Condicional | 🟡 Importante | Home → Formatação Condicional | Formatar → Formatação Condicional | "Destaque valores acima da meta em verde" |
| Gráficos e Visualização | 🟡 Importante | Inserir → Gráfico | Inserir → Gráfico | "Crie um gráfico de barras comparando regiões" |
| Validação de Dados | 🟡 Importante | Dados → Validação | Dados → Validação de dados | "Crie um menu suspenso para seleção de departamento" |
| SEERRO / IFERROR | 🟡 Importante | `=SEERRO(fórmula; "N/D")` | `=IFERROR(formula, "N/A")` | "Trate os erros #N/D nesta planilha" |
| Power Query | 🟢 Diferencial | Dados → Obter Dados | ❌ Não existe | "Importe e transforme dados de 5 arquivos CSV" |
| QUERY (Google Sheets) | 🟢 Diferencial | ❌ Não existe | `=QUERY(dados; "SELECT A, SUM(C) GROUP BY A")` | "Filtre e agregue dados sem tabela dinâmica" |
| ARRAYFORMULA | 🟢 Diferencial | ❌ (Excel usa arrays dinâmicos) | `=ARRAYFORMULA(A2:A*B2:B)` | "Aplique uma fórmula a toda a coluna de uma vez" |
| VBA / Macros | 🟢 Diferencial | Alt+F11, linguagem VBA | ❌ (usa Apps Script) | "Automatize a formatação deste relatório mensal" |
| Apps Script | 🟢 Diferencial | ❌ Não existe | Extensões → Apps Script (JavaScript) | "Crie um script para enviar e-mails automáticos" |
| Dashboard Interativo | 🟢 Diferencial | Segmentações + Tabelas Dinâmicas + Gráficos | Gráficos + filtros + formatação | "Monte um painel de KPIs para a diretoria" |
| Funções IMPORT* | 🟢 Diferencial | ❌ Não existe | IMPORTRANGE, IMPORTHTML, IMPORTDATA | "Puxe dados de outra planilha/site automaticamente" |

**Legenda de prioridade:** 🔴 Crítico = estudar primeiro, aparece em quase toda entrevista; 🟡 Importante = segunda camada de estudo, diferencia candidatos; 🟢 Diferencial = nível avançado, impressiona entrevistadores.

---

## 3. Guia de estudo acelerado para Excel

### Semanas 1–2: a base que todo teste cobra

Comece pela tríade essencial: **PROCV, SE e SOMASES**. O PROCV (VLOOKUP) é a função de busca mais testada em entrevistas corporativas segundo múltiplas fontes de recrutamento. Sua sintaxe em português é `=PROCV(valor_procurado; matriz_tabela; núm_índice_coluna; FALSO)` — note que o Excel em português usa ponto-e-vírgula como separador, não vírgula. Pratique cenários de cruzamento de tabelas: receber duas listas (uma com códigos de produto e outra com preços) e uni-las é o exercício mais clássico.

Em paralelo, domine `=SE(teste; verdadeiro; falso)` e seus aninhamentos. Entrevistadores frequentemente pedem para classificar dados em faixas ("se vendas > 100.000, classificar como 'Ouro', senão..."). Combine com `E()` e `OU()` para condições múltiplas. O terceiro pilar são as funções condicionais de agregação: **SOMASES** para somar com múltiplos critérios e **CONT.SES** para contar. A diferença de sintaxe entre SOMASE (critério único) e SOMASES (múltiplos critérios) é uma pegadinha recorrente em provas.

Dedique pelo menos 3 horas à criação de **Tabelas Dinâmicas**. Elas são consideradas a "linha divisória" entre usuários básicos e intermediários. O fluxo padrão é: selecionar dados tabulares → Inserir → Tabela Dinâmica → arrastar campos para Linhas, Colunas, Valores e Filtros. Pratique agrupar datas por mês/trimestre e alterar a função de resumo (SOMA vs. CONTAGEM vs. MÉDIA).

### Semanas 3–4: subindo para intermediário

Avance para **ÍNDICE+CORRESP** (INDEX+MATCH), que resolve a principal limitação do PROCV: a impossibilidade de buscar à esquerda. A fórmula combinada `=ÍNDICE(faixa_retorno; CORRESP(valor; faixa_busca; 0))` é mais flexível e não quebra quando colunas são inseridas ou removidas. Entrevistadores frequentemente perguntam: *"Qual a diferença entre PROCV e ÍNDICE/CORRESP?"* — saiba responder que ÍNDICE/CORRESP busca em qualquer direção e é mais robusto.

Estude também o **PROCX (XLOOKUP)**, disponível no Excel 365 e 2021+, que substituiu ambas as abordagens com sintaxe mais limpa: `=PROCX(valor; faixa_busca; faixa_retorno; "não encontrado")`. Inclua tratamento de erros com `=SEERRO(fórmula; valor_alternativo)`.

Nesta fase, incorpore **formatação condicional** (escalas de cores, barras de dados, ícones de semáforo para KPIs) e **validação de dados** (menus suspensos, restrição de valores). Ambas são cobradas em cenários do tipo "crie um formulário de entrada de dados profissional".

### Semanas 5–6: recursos avançados que impressionam

**Power Query** é o maior diferencial no Excel moderno. Acessado via Dados → Obter Dados, ele permite importar, limpar e transformar dados de múltiplas fontes (CSV, bancos de dados, web, pastas de arquivos) sem uma única fórmula. Cada transformação fica gravada como um "passo aplicado" que pode ser atualizado com um clique. Uma pesquisa indica que usuários de Power Query economizam em média **76 dias de trabalho por ano** em tarefas repetitivas de dados. Para entrevistas, saiba explicar quando usar Power Query em vez de PROCV: datasets grandes (100K+ linhas), dados recorrentes que precisam de atualização, ou quando é necessário combinar múltiplas fontes.

Construa pelo menos um **dashboard** seguindo a arquitetura de 3 abas: (1) aba de dados brutos, (2) aba de cálculos intermediários, (3) aba visual com gráficos, KPIs e segmentações de dados (slicers). Aprenda a conectar segmentações a múltiplas Tabelas Dinâmicas para criar interatividade.

Para quem mira em vagas de analista financeiro, estude as funções financeiras **VPL (NPV)**, **TIR (IRR)** e **PGTO (PMT)**, além da Análise de Hipóteses (Atingir Meta e Gerenciador de Cenários). Noções de **VBA** (gravar macros simples, entender Sub vs. Function, automatizar formatação) colocam o candidato em um patamar ainda mais alto — mas priorize Power Query se o tempo for limitado.

### Atalhos essenciais para demonstrar fluência

Memorize pelo menos estes atalhos, que demonstram proficiência durante testes ao vivo: **Ctrl+T** (converter em Tabela), **Alt+N+V** (inserir Tabela Dinâmica), **Ctrl+Shift+L** (ativar filtros), **F4** (alternar referência absoluta/relativa), **Ctrl+`** (mostrar fórmulas), **F2** (editar célula) e **Ctrl+;** (inserir data atual).

---

## 4. Guia de estudo acelerado para Google Sheets

### Semanas 1–2: fundamentos compartilhados com Excel

As fórmulas básicas do Google Sheets são funcionalmente idênticas ao Excel em inglês: `=VLOOKUP()`, `=IF()`, `=SUMIFS()`, `=COUNTIFS()`, `=INDEX()+MATCH()`. A diferença é que o Google Sheets **sempre usa nomes de funções em inglês**, independentemente do idioma da interface. Isso simplifica o aprendizado se você já sabe os nomes em inglês. Pivot Tables são criadas via Inserir → Tabela Dinâmica e funcionam de forma similar, com a vantagem de que o Sheets sugere automaticamente análises baseadas nos seus dados.

Foque nos mesmos cenários práticos do Excel: cruzamento de tabelas com VLOOKUP, classificação com IF aninhados, agregação condicional com SUMIFS. A prática transfere diretamente entre as plataformas.

### Semanas 3–4: funções exclusivas que entrevistadores valorizam

Aqui o Google Sheets se diferencia radicalmente. A **função QUERY** é considerada a ferramenta mais poderosa e exclusiva do Sheets — ela usa uma linguagem similar a SQL para filtrar, ordenar, agrupar e agregar dados diretamente em uma célula. A sintaxe é `=QUERY(dados; "SELECT A, SUM(C) WHERE B='Norte' GROUP BY A ORDER BY SUM(C) DESC")`. Com uma única fórmula, a QUERY substitui o que no Excel exigiria PROCV + SOMASES + classificação manual + Tabela Dinâmica.

As cláusulas seguem ordem fixa: **SELECT → WHERE → GROUP BY → PIVOT → ORDER BY → LIMIT → OFFSET → LABEL → FORMAT**. Valores de texto no WHERE usam aspas simples; referências de coluna usam letras (A, B, C). Não suporta subconsultas nem JOINs, mas para a maioria dos cenários corporativos é extremamente eficiente.

A segunda função exclusiva essencial é **ARRAYFORMULA**: `=ARRAYFORMULA(A2:A*B2:B)` aplica uma fórmula a uma coluna inteira de uma só vez, eliminando a necessidade de arrastar fórmulas. Isso é especialmente útil em planilhas colaborativas onde novos dados são adicionados constantemente — a fórmula se expande automaticamente.

### Semanas 5–6: importação de dados e automação

As **funções IMPORT** são exclusivas do Google Sheets e não existem no Excel:

- **IMPORTRANGE**: puxa dados de outra planilha Google Sheets → `=IMPORTRANGE("url_planilha"; "Aba1!A1:C100")`
- **IMPORTHTML**: importa tabelas ou listas de qualquer página web → `=IMPORTHTML("url"; "table"; 2)`
- **IMPORTDATA**: importa arquivos CSV/TSV de uma URL → `=IMPORTDATA("url_do_csv")`
- **IMPORTXML**: extrai dados estruturados via XPath → `=IMPORTXML("url"; "//h2")`

Para automação, o **Google Apps Script** (acessado via Extensões → Apps Script) usa JavaScript e permite criar funções personalizadas, automatizar tarefas com gatilhos temporais, integrar com Gmail, Calendar e Drive, e até construir web apps. A vantagem sobre o VBA do Excel é a integração nativa com todo o ecossistema Google e a capacidade de fazer requisições HTTP a APIs externas.

Funções únicas adicionais que vale conhecer: **GOOGLEFINANCE** (cotações de ações e câmbio em tempo real), **GOOGLETRANSLATE** (tradução automática de textos), **SPLIT** (divide texto por delimitador, substituindo "Texto para Colunas"), **IMAGE** (exibe imagens de URLs em células) e **SPARKLINE** (minigráficos via fórmula).

---

## 5. Diferenças-chave que entrevistadores testam

### Capacidade e performance definem o contexto de uso

O Google Sheets suporta aproximadamente **10 milhões de células** por planilha, enquanto o Excel desktop lida com **mais de 17 milhões** (1.048.576 linhas × 16.384 colunas). Para datasets grandes, o Excel desktop processa localmente e é significativamente mais rápido. O Sheets depende de conexão com a internet e pode ficar lento acima de 50.000 linhas com fórmulas complexas. Essa distinção importa em entrevistas: se o cenário envolve análise de grandes volumes de dados, mencione que o Excel (ou Power Query) seria mais adequado.

### Colaboração é o trunfo do Google Sheets

O Sheets permite **até 100 editores simultâneos** com cursores coloridos, histórico de versões completo, comentários com @menções, e salvamento automático. O Excel Online oferece colaboração, mas com funcionalidades reduzidas em relação ao desktop. Em entrevistas para empresas que usam Google Workspace, saber falar sobre **Filter Views** (visualizações de filtro pessoais que não afetam outros usuários) e controle de permissões (Visualizador/Comentador/Editor) demonstra familiaridade real com trabalho colaborativo.

### Automação segue caminhos distintos

No Excel, a automação passa por **VBA (Visual Basic for Applications)** — uma linguagem madura, com décadas de uso corporativo, ideal para automatizar tarefas complexas dentro do ambiente Office. No Google Sheets, o equivalente é o **Apps Script (JavaScript)** — mais moderno, baseado em nuvem, com integração nativa ao ecossistema Google e capacidade de conectar a APIs externas. A pergunta "Qual a diferença entre VBA e Apps Script?" aparece em entrevistas que testam versatilidade entre plataformas.

### O que cada plataforma tem de exclusivo

O Excel se destaca com **Power Query** (ETL sem código), **Power Pivot** (modelagem de dados com DAX), **Análise de Hipóteses** (Atingir Meta, Cenários, Tabela de Dados), mais tipos de gráficos (Sunburst, Waterfall, Treemap) e **Segmentações de Dados** avançadas em Tabelas Dinâmicas. O Google Sheets se destaca com **QUERY**, **ARRAYFORMULA**, funções **IMPORT***, **GOOGLEFINANCE**, **GOOGLETRANSLATE**, colaboração em tempo real superior e **Connected Sheets** (integração direta com BigQuery para big data).

---

## 6. Recursos gratuitos recomendados

### Cursos estruturados gratuitos

O melhor ponto de partida para Excel é o **curso gratuito de 4 horas do Chandoo** (chandoo.org/wp/complete-excel-course-free), que cobre Power Query, fórmulas, Tabelas Dinâmicas, formatação condicional e dashboards com arquivos para download. Para uma abordagem mais formal, a **Great Learning** oferece um curso gratuito com certificado (mygreatlearning.com/academy/learn-for-free/courses/excel-for-beginners). A própria **Microsoft** disponibiliza treinamento oficial gratuito em vídeo (support.microsoft.com/en-gb/office/excel-video-training-9bc05390-e94c-46af-a5b3-d7c22f6990bb).

Para Google Sheets, a **Coursera** oferece três cursos oficiais do Google Cloud que podem ser auditados gratuitamente: nível básico (coursera.org/learn/google-sheets), intermediário (coursera.org/learn/getting-started-with-google-sheets) e avançado (coursera.org/learn/google-sheets---advanced-topics). O **Google Skillshop** (skillshop.withgoogle.com) oferece treinamentos gratuitos com certificados para ferramentas Google Workspace.

### Blogs e sites de referência

**ExcelJet** (exceljet.net) mantém mais de 1.000 fórmulas explicadas com vídeos curtos e mais de 350 funções documentadas — ideal para consulta rápida durante o estudo. **Chandoo.org** oferece mais de 500 tutoriais gratuitos e um roadmap de 3 meses para Excel avançado (chandoo.org/wp/advanced-excel-roadmap). Para Google Sheets, **Ben L. Collins** (benlcollins.com) é reconhecido como Google Developer Expert e publica mais de 100 tutoriais aprofundados, além de uma newsletter semanal com 50.000+ assinantes.

### Canais do YouTube essenciais

Para Excel, os três canais mais recomendados são: **ExcelIsFun** (Mike Girvin, 1M+ inscritos, 3.700+ vídeos estruturados do básico ao avançado), **Leila Gharani** (1,6M+ inscritos, foco em técnicas avançadas e produtividade) e **Chandoo** (825K+ inscritos, dashboards e análise de dados com sessões mensais ao vivo). Para Google Sheets, o canal **Learn Google Spreadsheets** (100K+ inscritos) é o mais completo e dedicado exclusivamente à plataforma.

### Plataformas de exercícios práticos e testes simulados

Para prática hands-on sem instalar nada, o **Spreadsheet Center** (spreadsheetcenter.com/excel-exercises) oferece 50+ exercícios com simulador no navegador e feedback instantâneo. O **Excel Practice Online** (excel-practice-online.com) e o **W3Schools** (w3schools.com/excel/excel_exercises.php) complementam com exercícios estruturados por tema. Para simular provas reais de entrevista, o teste gratuito do **Corporate Finance Institute** (corporatefinanceinstitute.com/resources/excel/excel-test) tem 20 questões focadas em finanças com nota de corte de 80%.

---

## 7. Como demonstrar competência em entrevistas

### Construa um mini portfólio de 3 a 5 projetos

Um portfólio tangível separa candidatos que "sabem Excel" daqueles que **provam que sabem**. Monte pelo menos três projetos: (1) um **dashboard interativo** com Tabelas Dinâmicas, gráficos e segmentações mostrando KPIs de vendas ou RH; (2) um **projeto de limpeza e análise de dados** usando PROCV/ÍNDICE+CORRESP e SOMASES sobre um dataset real (dados públicos do IBGE, Kaggle ou dados de exemplo); (3) um **relatório automatizado** demonstrando Power Query no Excel ou QUERY+ARRAYFORMULA no Google Sheets. Documente cada projeto com: problema resolvido, ferramentas utilizadas e resultado alcançado. Hospede no GitHub com arquivos .xlsx/.gsheet e README explicativo, ou crie links compartilháveis do Google Sheets em modo visualização.

### Domine o vocabulário técnico bilíngue

Em entrevistas para empresas multinacionais ou que usam software em inglês, você precisa navegar entre os termos. As equivalências mais cobradas: Planilha = Spreadsheet, Pasta de trabalho = Workbook, Célula = Cell, Tabela Dinâmica = Pivot Table, Formatação condicional = Conditional Formatting, Referência absoluta = Absolute reference ($A$1), Validação de dados = Data Validation, Fórmula matricial = Array formula, Painel = Dashboard. No Excel em português, as funções têm nomes traduzidos (PROCV, SE, SOMASES), mas no Google Sheets todas as funções usam nomes em inglês independentemente do idioma da interface.

### Estratégia para testes práticos ao vivo

Antes do teste, pergunte qual versão do software será usada e se será Windows ou Mac. Durante a prova, **leia todas as instruções antes de começar** para dimensionar o tempo. Verbalize seu raciocínio enquanto trabalha — entrevistadores avaliam o processo, não apenas o resultado. Comece pelos itens que você domina para acumular confiança. Use Tabelas Dinâmicas sempre que a tarefa envolver sumarização (são mais rápidas e menos propensas a erro que fórmulas manuais). Formate sua saída profissionalmente: cabeçalhos claros, formato numérico consistente, alinhamento correto. Se não souber algo, explique como resolveria ("eu buscaria na documentação a função X" demonstra maturidade técnica).

### Os erros que eliminam candidatos

Os cinco erros mais frequentes que entrevistadores relatam são: **(1)** superestimar o próprio nível — pesquisas indicam que a maioria dos candidatos infla suas habilidades em planilhas, e os testes práticos expõem isso imediatamente; **(2)** não usar atalhos de teclado, sinalizando pouca prática real; **(3)** ignorar tratamento de erros — deixar `#N/D` ou `#DIV/0!` visíveis em vez de usar SEERRO/IFERROR; **(4)** construir planilhas frágeis com valores fixos digitados diretamente nas fórmulas em vez de referências a células; **(5)** não conseguir explicar o raciocínio por trás das escolhas técnicas — saber *fazer* sem saber *explicar por quê* reduz drasticamente a avaliação.

### Como falar sobre planilhas usando o método STAR

Estruture suas respostas verbais no formato **Situação → Tarefa → Ação → Resultado**: "Na minha experiência anterior *(Situação)*, precisávamos consolidar relatórios de vendas de 12 filiais mensalmente *(Tarefa)*. Implementei um processo usando Power Query para importar e transformar os dados automaticamente, com um dashboard de Tabelas Dinâmicas e segmentações para a diretoria *(Ação)*. Isso reduziu o tempo de preparação do relatório de 8 horas para 30 minutos por mês *(Resultado)*." Quantifique sempre o impacto: horas economizadas, linhas de dados processadas, redução de erros percentual.

---

## Conclusão: o caminho mais curto para a proficiência que contrata

A preparação eficaz para entrevistas de planilhas não exige dominar centenas de funções — exige **profundidade nas 10-15 competências que realmente aparecem nos testes**. O investimento de maior retorno está em praticar com dados reais, construir projetos demonstráveis e desenvolver a capacidade de verbalizar decisões técnicas. A principal descoberta desta pesquisa é que o gap entre candidatos aprovados e reprovados raramente está no conhecimento de fórmulas obscuras; está na capacidade de usar Tabelas Dinâmicas com confiança, tratar erros sistematicamente e demonstrar uma mentalidade de automação — seja com Power Query no Excel ou QUERY+ARRAYFORMULA no Google Sheets. Empresas em 2025–2026 também valorizam cada vez mais candidatos que mencionam ferramentas modernas como PROCX/XLOOKUP, arrays dinâmicos e integração com IA (Copilot no Excel, Gemini no Sheets). Comece pelos recursos gratuitos do Chandoo e ExcelJet, faça o teste simulado do CFI na terceira semana, e construa seu portfólio antes da entrevista. A competência em planilhas é uma das poucas habilidades corporativas que pode ser desenvolvida de forma autodidata, gratuita e mensurável em poucas semanas.