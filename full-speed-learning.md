# Plano de Emergência: 5 Horas Para Aprender Excel do Zero

> **Contexto:** Teste amanhã. Tempo: 5 horas. Nível atual: zero.
> **Filosofia:** Aprender fazendo. Cada minuto conta. Nada de teoria passiva.

---

## 📦 CHECKLIST DE PREPARAÇÃO (para quem está montando os arquivos)

Antes de a estudante começar, prepare dois arquivos Excel:

**Arquivo 1 — "TechStore_Desafios.xlsx"** (usado nos Desafios 1 a 5):
- [ ] Aba "Vendas" com 20 linhas de dados já preenchidas (ver tabela no Desafio 1)
- [ ] Aba "Catálogo" com 6 produtos, fornecedores e margens (ver tabela no Desafio 3)
- [ ] Ambas as tabelas convertidas com Ctrl+T
- [ ] Colunas de data formatadas como Data, valores como Moeda, margens como Porcentagem
- [ ] Deixar as colunas H em diante da aba Vendas vazias (ela vai criar)

**Arquivo 2 — "Teste_Entrevista.xlsx"** (usado no Desafio Final):
- [ ] Aba "Funcionários" com 10 funcionários (ver tabela no Desafio Final)
- [ ] Aba "Benefícios" com 3 cargos e valores (ver tabela no Desafio Final)
- [ ] Tabelas convertidas com Ctrl+T, salários como Moeda
- [ ] Colunas E–H da aba Funcionários vazias (ela vai criar)

> **Dica:** o Desafio 1 pede que ela crie a tabela do zero. Se quiser poupar tempo, ela pode pular o Desafio 1 e ir direto ao Desafio 2 usando o arquivo já preparado — mas criar do zero reforça as 5 Regras de Ouro.

---

## As 5 Regras de Ouro das Tabelas no Excel

Antes de qualquer coisa, grave estas 5 regras. Elas são o fundamento de tudo que você vai fazer. Entrevistadores não perguntam sobre elas diretamente, mas **toda resposta boa** segue essas regras.

### Regra 1: Uma linha = um registro, uma coluna = um tipo de dado
Cada linha da sua tabela representa UMA coisa (um produto, uma venda, um funcionário). Cada coluna guarda UM tipo de informação (nome, data, valor). **Nunca** misture tipos diferentes na mesma coluna. Nunca junte dois dados na mesma célula (ex: "São Paulo - 15/03" numa célula só).

### Regra 2: A primeira linha é SEMPRE o cabeçalho
A linha 1 da tabela deve conter os nomes das colunas, escritos de forma clara e sem repetição. Sem linhas em branco acima. Sem título da planilha ocupando a linha 1. O cabeçalho começa na A1 (ou na primeira célula da tabela).

### Regra 3: Zero linhas e colunas em branco dentro da tabela
Linhas ou colunas vazias "quebram" a tabela para o Excel. Filtros param de funcionar, Tabelas Dinâmicas não leem tudo, fórmulas de busca falham. Se precisa separar visualmente, use formatação (cor, borda) — nunca linhas vazias.

### Regra 4: Dados consistentes — mesmo formato do começo ao fim
Se uma coluna é de datas, TODAS as células devem ter datas reais (não texto). Se é de valores monetários, todos devem ser números (sem "R$" digitado à mão — use formatação de célula). Misturar texto com número numa coluna de valores é o erro mais destrutivo que existe.

### Regra 5: Converta seus dados em "Tabela" (Ctrl+T)
O Excel tem um recurso chamado "Tabela" (não é só uma grade de dados — é um objeto especial). Selecione seus dados e aperte Ctrl+T. A Tabela ganha: filtros automáticos, formatação alternada, expansão automática ao adicionar linhas, e referências estruturadas nas fórmulas. É o primeiro passo profissional em qualquer planilha.

---

## Distribuição das 5 Horas

| Bloco | Tempo | O que fazer | Objetivo |
|-------|-------|-------------|----------|
| **Bloco 1** | 0:00–0:45 (45min) | Navegação + 5 Regras de Ouro na prática | Ficar confortável no Excel, criar tabelas corretas |
| **Bloco 2** | 0:45–1:45 (60min) | Fórmulas essenciais: SE, SOMA, MÉDIA, CONT.SE | Saber calcular e classificar dados |
| **Bloco 3** | 1:45–2:45 (60min) | PROCV e SOMASES — as estrelas da entrevista | Cruzar tabelas e somar com critérios |
| **Bloco 4** | 2:45–3:45 (60min) | Tabelas Dinâmicas e Gráficos | Resumir dados em segundos |
| **Bloco 5** | 3:45–4:30 (45min) | Formatação condicional + Validação + Polimento | Fazer a planilha parecer profissional |
| **Bloco 6** | 4:30–5:00 (30min) | Desafio final integrado (simulação de teste) | Testar tudo junto sob pressão de tempo |

---

## BLOCO 1 — Navegação e as 5 Regras na Prática (45 min)

### O que aprender (15 min de exploração livre)

Abra o Excel (ou Google Sheets se não tiver Excel). Explore:

- **Selecionar:** clique numa célula, arraste para selecionar um bloco, Ctrl+Shift+Seta para selecionar até o fim dos dados
- **Mover:** Tab (próxima coluna), Enter (próxima linha), Ctrl+Seta (pular para o fim dos dados)
- **Desfazer:** Ctrl+Z (seu melhor amigo)
- **Copiar/Colar:** Ctrl+C, Ctrl+V — mas atenção: "Colar Especial" (Ctrl+Shift+V) cola só valores, sem arrastar fórmulas
- **Formatar número:** selecione células → clique direito → Formatar Células → Número/Moeda/Data

### Atalhos que DEVEM virar reflexo

| Ação | Atalho |
|------|--------|
| Criar Tabela | Ctrl+T |
| Filtrar | Ctrl+Shift+L |
| Selecionar tudo | Ctrl+A |
| Negrito | Ctrl+B |
| Desfazer | Ctrl+Z |
| Inserir data de hoje | Ctrl+; |
| Editar célula | F2 |
| Alternar referência ($) | F4 |
| Mostrar fórmulas | Ctrl+` |

---

### 🏋️ DESAFIO 1: "Monte a Base" (30 min)

**Descrição do desafio:**
Crie uma planilha de vendas de uma loja fictícia chamada "TechStore" seguindo rigorosamente as 5 Regras de Ouro.

**O que a planilha deve conter:**

A tabela deve ter 7 colunas: ID da Venda, Data, Vendedor, Produto, Categoria, Quantidade e Valor Unitário. Você deve preencher 20 linhas de dados fictícios com as seguintes restrições:

- **Vendedores:** use exatamente 4 nomes (Ana, Bruno, Carla, Diego) distribuídos entre as 20 vendas
- **Produtos:** use 6 produtos distribuídos em 3 categorias:
  - Eletrônicos: Fone Bluetooth (R$ 89,90), Carregador USB (R$ 45,50)
  - Acessórios: Capa de Celular (R$ 29,90), Película (R$ 15,00)
  - Informática: Mouse Wireless (R$ 79,90), Teclado Mecânico (R$ 249,90)
- **Datas:** distribua entre 01/01/2025 e 31/01/2025 (mês de janeiro)
- **Quantidades:** variem entre 1 e 10

**Instruções passo a passo:**
1. Abra uma planilha nova
2. Na célula A1, digite "ID_Venda". Em B1 "Data", C1 "Vendedor", D1 "Produto", E1 "Categoria", F1 "Quantidade", G1 "Valor_Unitario"
3. Preencha 20 linhas (linhas 2 a 21) com dados fictícios seguindo as restrições acima
4. Formate a coluna B como Data (dd/mm/aaaa)
5. Formate a coluna G como Moeda (R$)
6. Selecione toda a tabela (A1:G21) e aperte Ctrl+T para converter em Tabela
7. Renomeie a aba para "Vendas"

**Dicas:**
- Use IDs sequenciais (V001, V002... ou simplesmente 1, 2, 3...)
- Certifique-se de que as datas são DATAS reais (o Excel deve alinhar à direita automaticamente). Se alinhou à esquerda, o Excel interpretou como texto — delete e redigite
- Não digite "R$" na célula — use formatação de moeda
- Varie os dados: não coloque todas as vendas de Ana juntas. Misture

**Critérios de aceite:**
- [ ] A tabela tem exatamente 7 colunas com cabeçalhos na linha 1
- [ ] Há 20 linhas de dados sem nenhuma linha em branco
- [ ] Datas são reconhecidas como datas (alinhadas à direita, clicáveis no calendário)
- [ ] Valores são números formatados como moeda (não texto)
- [ ] Os 4 vendedores e 6 produtos aparecem distribuídos nos dados
- [ ] A tabela foi convertida com Ctrl+T (aparece com listras coloridas alternadas e setas de filtro)
- [ ] Ao clicar nas setas de filtro do cabeçalho, os filtros funcionam corretamente

### 📋 GABARITO DE DADOS — Tabela "Vendas" (20 linhas)

> **Para quem está preparando o material:** se a estudante travar no Desafio 1 ou para economizar tempo nos desafios seguintes, use exatamente estes dados. Copie linha por linha ou prepare o arquivo antes.

| ID_Venda | Data | Vendedor | Produto | Categoria | Quantidade | Valor_Unitario |
|---|---|---|---|---|---|---|
| 1 | 03/01/2025 | Ana | Fone Bluetooth | Eletrônicos | 3 | R$ 89,90 |
| 2 | 05/01/2025 | Bruno | Película | Acessórios | 8 | R$ 15,00 |
| 3 | 06/01/2025 | Carla | Teclado Mecânico | Informática | 1 | R$ 249,90 |
| 4 | 07/01/2025 | Diego | Capa de Celular | Acessórios | 5 | R$ 29,90 |
| 5 | 08/01/2025 | Ana | Mouse Wireless | Informática | 2 | R$ 79,90 |
| 6 | 09/01/2025 | Bruno | Fone Bluetooth | Eletrônicos | 4 | R$ 89,90 |
| 7 | 10/01/2025 | Carla | Carregador USB | Eletrônicos | 6 | R$ 45,50 |
| 8 | 11/01/2025 | Diego | Teclado Mecânico | Informática | 1 | R$ 249,90 |
| 9 | 13/01/2025 | Ana | Película | Acessórios | 10 | R$ 15,00 |
| 10 | 14/01/2025 | Bruno | Mouse Wireless | Informática | 3 | R$ 79,90 |
| 11 | 15/01/2025 | Carla | Capa de Celular | Acessórios | 7 | R$ 29,90 |
| 12 | 16/01/2025 | Diego | Fone Bluetooth | Eletrônicos | 2 | R$ 89,90 |
| 13 | 18/01/2025 | Ana | Carregador USB | Eletrônicos | 5 | R$ 45,50 |
| 14 | 19/01/2025 | Bruno | Teclado Mecânico | Informática | 2 | R$ 249,90 |
| 15 | 20/01/2025 | Carla | Fone Bluetooth | Eletrônicos | 3 | R$ 89,90 |
| 16 | 22/01/2025 | Diego | Película | Acessórios | 9 | R$ 15,00 |
| 17 | 24/01/2025 | Ana | Capa de Celular | Acessórios | 4 | R$ 29,90 |
| 18 | 26/01/2025 | Bruno | Carregador USB | Eletrônicos | 6 | R$ 45,50 |
| 19 | 28/01/2025 | Carla | Mouse Wireless | Informática | 2 | R$ 79,90 |
| 20 | 30/01/2025 | Diego | Capa de Celular | Acessórios | 3 | R$ 29,90 |

> **Verificação rápida:** 5 vendas por vendedor (Ana: 1,5,9,13,17 / Bruno: 2,6,10,14,18 / Carla: 3,7,11,15,19 / Diego: 4,8,12,16,20). Todos os 6 produtos e 3 categorias aparecem. Quantidades variam de 1 a 10. Após criar as colunas H (Total_Venda) e L (Lucro_Estimado), o faturamento total deve ser aproximadamente **R$ 3.365,50**.

---

## BLOCO 2 — Fórmulas Essenciais (60 min)

### O que aprender (20 min de estudo ativo)

Todas as fórmulas seguem a mesma lógica: `=NOME_DA_FUNÇÃO(argumentos)`. Comece sempre com `=`.

**Fórmulas deste bloco:**

| Fórmula | O que faz | Exemplo |
|---------|-----------|---------|
| `=SOMA(F2:F21)` | Soma um intervalo | Total de unidades vendidas |
| `=MÉDIA(G2:G21)` | Calcula a média | Preço médio unitário |
| `=MÁXIMO(F2:F21)` | Maior valor | Maior quantidade vendida |
| `=MÍNIMO(F2:F21)` | Menor valor | Menor quantidade vendida |
| `=CONT.VALORES(C2:C21)` | Conta células preenchidas | Total de vendas registradas |
| `=CONT.SE(C2:C21;"Ana")` | Conta com critério | Quantas vendas a Ana fez |
| `=SE(F2>5;"Alto";"Baixo")` | Condição lógica | Classificar quantidade |

**Conceito crucial — Referência absoluta ($):**
- `A1` → referência relativa (muda ao copiar)
- `$A$1` → referência absoluta (trava, não muda ao copiar)
- Atalho para alternar: **F4** enquanto edita a fórmula

---

### 🏋️ DESAFIO 2: "Analista de Vendas Júnior" (40 min)

**Descrição do desafio:**
Usando a planilha "Vendas" criada no Desafio 1, crie uma nova aba chamada "Análises" onde você vai extrair informações dos dados usando fórmulas.

**O que a aba "Análises" deve conter:**

**Seção 1 — Resumo Geral (células A1:B7):**
Monte uma mini-tabela com os seguintes indicadores na coluna A e os resultados com fórmulas na coluna B:

| A (Rótulo) | B (Fórmula esperada) |
|---|---|
| Total de Vendas | Contar quantas vendas existem |
| Quantidade Total Vendida | Somar todas as quantidades |
| Quantidade Média por Venda | Média das quantidades |
| Maior Quantidade numa Venda | Máximo da coluna quantidade |
| Menor Quantidade numa Venda | Mínimo da coluna quantidade |
| Valor Unitário Mais Alto | Máximo da coluna valor |
| Valor Unitário Mais Baixo | Mínimo da coluna valor |

**Seção 2 — Análise por Vendedor (células A10:C14):**
Monte uma tabela com uma linha por vendedor:

| Vendedor | Número de Vendas | Total de Itens Vendidos |
|---|---|---|
| Ana | (usar CONT.SE) | (usar SOMASE) |
| Bruno | ... | ... |
| Carla | ... | ... |
| Diego | ... | ... |

**Seção 3 — Coluna calculada na aba Vendas (voltar para a aba Vendas):**
- Na coluna H, cabeçalho "Total_Venda", calcule Quantidade × Valor Unitário para cada linha
- Na coluna I, cabeçalho "Classificação", use SE: se Total_Venda > R$ 200 → "ALTO", se > R$ 100 → "MÉDIO", senão → "BAIXO"

**Instruções passo a passo:**
1. Crie uma nova aba (clique no "+" na parte inferior) e renomeie para "Análises"
2. Para referenciar dados de outra aba, use: `=SOMA(Vendas!F2:F21)`
3. Para CONT.SE, a sintaxe é: `=CONT.SE(Vendas!C2:C21;"Ana")`
4. Para SOMASE, a sintaxe é: `=SOMASE(Vendas!C2:C21;"Ana";Vendas!F2:F21)` — lê-se: "some a coluna F onde a coluna C for igual a Ana"
5. Para o SE aninhado na coluna I: `=SE(H2>200;"ALTO";SE(H2>100;"MÉDIO";"BAIXO"))`
6. Formate a coluna H como Moeda

**Dicas:**
- Quando digitar a fórmula CONT.SE, o texto do critério vai entre aspas: "Ana"
- Se sua tabela foi convertida com Ctrl+T, o Excel pode usar nomes estruturados como `Tabela1[Quantidade]` em vez de `F2:F21` — ambos funcionam
- Para o SE aninhado, pense de "fora para dentro": primeiro teste a condição mais restritiva (>200), depois a intermediária (>100), e o último "senão" pega todo o resto
- A fórmula da coluna H é simplesmente `=F2*G2` — arraste para baixo para preencher as 20 linhas

**Critérios de aceite:**
- [ ] A aba "Análises" existe e tem as 3 seções organizadas
- [ ] Todas as 7 fórmulas do Resumo Geral retornam números (não erros, não texto)
- [ ] A tabela por vendedor mostra os 4 vendedores com CONT.SE e SOMASE corretos (a soma dos "Número de Vendas" deve ser 20)
- [ ] A coluna H na aba Vendas calcula corretamente Quantidade × Valor Unitário
- [ ] A coluna I classifica corretamente: valores acima de R$200 = ALTO, entre R$100 e R$200 = MÉDIO, abaixo = BAIXO
- [ ] Nenhuma célula mostra erro (#VALOR!, #REF!, #NOME?)

### 📋 RESPOSTAS ESPERADAS — Desafio 2 (para conferência)

> **Para quem está acompanhando:** use estes valores para verificar se as fórmulas estão corretas (baseado nos dados do gabarito do Desafio 1).

**Resumo Geral:**
- Total de Vendas: **20**
- Quantidade Total Vendida: **84**
- Quantidade Média por Venda: **4,2**
- Maior Quantidade numa Venda: **10**
- Menor Quantidade numa Venda: **1**
- Valor Unitário Mais Alto: **R$ 249,90**
- Valor Unitário Mais Baixo: **R$ 15,00**

**Por Vendedor (Nº de Vendas / Total de Itens):**
- Ana: 5 vendas / 24 itens
- Bruno: 5 vendas / 23 itens
- Carla: 5 vendas / 19 itens
- Diego: 5 vendas / 18 itens

**Coluna H (Total_Venda) — primeiras 5 linhas:**
- V1: 3 × R$ 89,90 = **R$ 269,70**
- V2: 8 × R$ 15,00 = **R$ 120,00**
- V3: 1 × R$ 249,90 = **R$ 249,90**
- V4: 5 × R$ 29,90 = **R$ 149,50**
- V5: 2 × R$ 79,90 = **R$ 159,80**

**Coluna I (Classificação) — primeiras 5 linhas:**
- V1: R$ 269,70 → **ALTO** (>200)
- V2: R$ 120,00 → **MÉDIO** (>100)
- V3: R$ 249,90 → **ALTO** (>200)
- V4: R$ 149,50 → **MÉDIO** (>100)
- V5: R$ 159,80 → **MÉDIO** (>100)

---

## BLOCO 3 — PROCV e SOMASES (60 min)

### O que aprender (15 min de estudo ativo)

**PROCV (VLOOKUP) — a função mais testada em entrevistas:**

Sintaxe: `=PROCV(o_que_buscar; onde_buscar; qual_coluna_retornar; FALSO)`

- **o_que_buscar:** o valor que você quer encontrar (ex: código do produto)
- **onde_buscar:** a tabela inteira onde o valor está (ex: A2:D100)
- **qual_coluna_retornar:** número da coluna na tabela que tem a informação desejada (1 = primeira coluna, 2 = segunda, etc.)
- **FALSO:** sempre use FALSO (busca exata). VERDADEIRO faz busca aproximada e quase nunca é o que você quer

Exemplo: `=PROCV("Fone Bluetooth";D2:G21;4;FALSO)` → busca "Fone Bluetooth" na coluna D e retorna o valor da 4ª coluna do intervalo.

**SOMASES (SUMIFS) — soma com múltiplos critérios:**

Sintaxe: `=SOMASES(coluna_que_soma; coluna_critério1; critério1; coluna_critério2; critério2)`

Exemplo: `=SOMASES(H2:H21;C2:C21;"Ana";E2:E21;"Eletrônicos")` → "Some os totais de venda onde o vendedor é Ana E a categoria é Eletrônicos"

**SEERRO (IFERROR) — tratamento de erros:**

Sintaxe: `=SEERRO(sua_fórmula; "valor se der erro")`

Exemplo: `=SEERRO(PROCV("XYZ";A2:G21;7;FALSO);"Não encontrado")` → se o PROCV não achar "XYZ", mostra "Não encontrado" em vez de #N/D

---

### 🏋️ DESAFIO 3: "Cruzando Tabelas" (45 min)

### 📋 PREPARAÇÃO — Tabela "Catálogo" (criar ANTES do desafio)

> **Para quem está preparando o material:** crie esta aba no mesmo arquivo da aba "Vendas". A estudante vai usar PROCV para buscar dados aqui.

No mesmo arquivo, crie uma nova aba chamada **"Catálogo"** com exatamente estes dados (6 linhas + cabeçalho):

| Produto | Categoria | Fornecedor | Margem_Lucro |
|---|---|---|---|
| Fone Bluetooth | Eletrônicos | FornecedorA | 35% |
| Carregador USB | Eletrônicos | FornecedorA | 40% |
| Capa de Celular | Acessórios | FornecedorB | 55% |
| Película | Acessórios | FornecedorB | 60% |
| Mouse Wireless | Informática | FornecedorC | 30% |
| Teclado Mecânico | Informática | FornecedorC | 25% |

**Atenção na preparação:**
- Os nomes dos produtos devem ser IDÊNTICOS aos da aba Vendas (sem espaços extras, sem acentos diferentes). O PROCV é sensível a isso
- A coluna Margem_Lucro deve ser formatada como **Porcentagem** (não digitar "35%", e sim digitar 0,35 ou digitar 35 e formatar como %)
- Converta esta tabela com Ctrl+T também
- A coluna A **deve** ser "Produto" porque o PROCV sempre busca na primeira coluna do intervalo

**Descrição do desafio:**
Crie uma nova aba chamada "Catálogo" com informações extras dos produtos, e depois use PROCV para puxar essas informações para a aba de Vendas. Também use SOMASES para criar um relatório cruzado.

**Parte A — Crie a aba "Catálogo":**

Monte a seguinte tabela de referência na nova aba:

| Produto | Categoria | Fornecedor | Margem_Lucro |
|---|---|---|---|
| Fone Bluetooth | Eletrônicos | FornecedorA | 35% |
| Carregador USB | Eletrônicos | FornecedorA | 40% |
| Capa de Celular | Acessórios | FornecedorB | 55% |
| Película | Acessórios | FornecedorB | 60% |
| Mouse Wireless | Informática | FornecedorC | 30% |
| Teclado Mecânico | Informática | FornecedorC | 25% |

**Parte B — Use PROCV na aba Vendas:**
- Na coluna J, cabeçalho "Fornecedor", use PROCV para buscar o fornecedor de cada produto a partir da aba Catálogo
- Na coluna K, cabeçalho "Margem", use PROCV para buscar a margem de lucro de cada produto
- Na coluna L, cabeçalho "Lucro_Estimado", calcule: Total_Venda (coluna H) × Margem (coluna K)
- Envolva cada PROCV com SEERRO para que, se o produto não for encontrado, apareça "N/D" em vez de erro

**Parte C — Relatório cruzado com SOMASES na aba "Análises":**
Adicione uma nova seção na aba Análises (abaixo do que já existe):

Monte uma tabela cruzada: linhas = Vendedores (Ana, Bruno, Carla, Diego), colunas = Categorias (Eletrônicos, Acessórios, Informática). Cada célula deve ter o total de vendas (em R$) daquele vendedor naquela categoria, usando SOMASES.

Adicione uma linha "TOTAL" embaixo e uma coluna "TOTAL" à direita usando SOMA.

**Instruções passo a passo:**
1. Para o PROCV da coluna J: `=SEERRO(PROCV(D2;Catálogo!A:D;3;FALSO);"N/D")`
   - D2 é o nome do produto na aba Vendas
   - Catálogo!A:D é a tabela na aba Catálogo (colunas A até D)
   - 3 significa "retorne a 3ª coluna" (Fornecedor)
   - FALSO = busca exata
2. Para a Margem (coluna K): mude o 3 para 4 (4ª coluna = Margem_Lucro)
3. A Margem virá como decimal (0,35 para 35%) — isso é correto. Formate como Porcentagem se quiser
4. Para SOMASES no relatório cruzado: `=SOMASES(Vendas!H:H;Vendas!C:C;"Ana";Vendas!E:E;"Eletrônicos")`

**Dicas:**
- O PROCV **sempre busca na primeira coluna** do intervalo fornecido. Por isso a coluna A do Catálogo deve ser "Produto" (é o que você está buscando)
- Ao copiar o PROCV para baixo, a referência D2 vai mudar para D3, D4... (isso é bom). Mas a referência Catálogo!A:D deve ficar fixa — como estamos usando colunas inteiras (A:D), ela já é fixa naturalmente
- Se aparecer #N/D, verifique se o nome do produto está escrito EXATAMENTE igual nas duas abas (espaços extras ou acentos diferentes quebram o PROCV)
- No relatório cruzado, comece com uma célula, teste se funciona, e só depois copie para as demais

**Critérios de aceite:**
- [ ] A aba "Catálogo" existe com 6 produtos e 4 colunas
- [ ] A coluna J (Fornecedor) mostra o fornecedor correto para cada produto via PROCV
- [ ] A coluna K (Margem) mostra porcentagens corretas via PROCV
- [ ] A coluna L (Lucro_Estimado) calcula Total_Venda × Margem corretamente
- [ ] Todas as fórmulas PROCV estão envolvidas em SEERRO
- [ ] O relatório cruzado na aba Análises mostra 4 vendedores × 3 categorias com SOMASES
- [ ] As linhas e colunas de TOTAL batem (Total da linha = soma das 3 categorias; Total da coluna = soma dos 4 vendedores)

---

## BLOCO 4 — Tabelas Dinâmicas e Gráficos (60 min)

### O que aprender (10 min de estudo ativo)

**Tabela Dinâmica (Pivot Table):** transforma centenas de linhas em resumos instantâneos arrastando campos. É o recurso mais poderoso do Excel para análise rápida.

**Como criar:**
1. Clique em qualquer célula da sua tabela de dados
2. Vá em Inserir → Tabela Dinâmica
3. Escolha "Nova Planilha" e clique OK
4. No painel lateral, arraste campos para as áreas:
   - **Linhas:** o que quer como rótulos laterais (ex: Vendedor)
   - **Colunas:** o que quer como rótulos superiores (ex: Categoria)
   - **Valores:** o que quer calcular (ex: Soma de Total_Venda)
   - **Filtros:** o que quer poder filtrar (ex: Mês)

**Gráficos:**
1. Selecione os dados que quer visualizar
2. Inserir → Gráfico → escolha o tipo
3. Tipos mais usados: Barras (comparação), Linhas (tendência), Pizza (proporção)

---

### 🏋️ DESAFIO 4: "O Painel do Gerente" (50 min)

**Descrição do desafio:**
Crie 3 Tabelas Dinâmicas diferentes a partir dos dados de Vendas, e para cada uma, crie um gráfico correspondente. Organize tudo numa aba chamada "Dashboard".

**Tabela Dinâmica 1 — Vendas por Vendedor:**
- Linhas: Vendedor
- Valores: Soma de Total_Venda (coluna H) E Contagem de ID_Venda
- Resultado esperado: uma tabela mostrando quanto cada vendedor faturou e quantas vendas fez
- Gráfico: Barras horizontais mostrando o faturamento por vendedor

**Tabela Dinâmica 2 — Vendas por Categoria e Vendedor:**
- Linhas: Categoria
- Colunas: Vendedor
- Valores: Soma de Total_Venda
- Resultado esperado: uma matriz cruzada mostrando quanto cada vendedor vendeu em cada categoria
- Gráfico: Barras empilhadas comparando categorias com cores por vendedor

**Tabela Dinâmica 3 — Top Produtos por Quantidade:**
- Linhas: Produto
- Valores: Soma de Quantidade
- Ordenar: do maior para o menor (clique com direito no campo → Classificar → Maior para Menor)
- Resultado esperado: ranking de produtos mais vendidos
- Gráfico: Barras verticais do produto mais vendido ao menos vendido

**Instruções passo a passo:**
1. Vá para a aba Vendas, clique em qualquer célula com dados
2. Inserir → Tabela Dinâmica → Nova Planilha → OK
3. No painel à direita, arraste os campos conforme indicado acima
4. Para adicionar dois campos em "Valores" (TD1), arraste Total_Venda e depois arraste ID_Venda para a mesma área — o Excel mostra ambos
5. Para mudar de Soma para Contagem: clique no campo em Valores → "Configurações do Campo de Valor" → escolha "Contagem"
6. Para criar o gráfico: selecione a Tabela Dinâmica → Inserir → Gráfico → escolha o tipo
7. Repita para as 3 Tabelas Dinâmicas
8. Para montar o Dashboard: crie uma aba nova, recorte (Ctrl+X) os gráficos e cole na aba Dashboard, organizando-os lado a lado

**Dicas:**
- Se a Tabela Dinâmica não mostrar "Total_Venda" como campo, volte na aba Vendas e verifique se a coluna H tem cabeçalho e dados
- Para formatar os valores como moeda na Tabela Dinâmica: clique com direito num valor → Formatar Números → Moeda
- Gráficos de Tabela Dinâmica são "vivos" — quando os dados mudam, clique com direito na TD → Atualizar, e o gráfico atualiza junto
- No Dashboard, redimensione os gráficos para ficarem organizados. Use o recurso "Alinhar" (Formatar → Alinhar) para deixar tudo alinhado

**Critérios de aceite:**
- [ ] Existem 3 Tabelas Dinâmicas funcionais, cada uma numa aba separada ou na mesma aba
- [ ] TD1 mostra vendedores com faturamento total E número de vendas
- [ ] TD2 mostra a matriz cruzada Categoria × Vendedor
- [ ] TD3 mostra o ranking de produtos ordenado do maior para menor
- [ ] Há 3 gráficos correspondentes às 3 TDs (barras horizontais, barras empilhadas, barras verticais)
- [ ] A aba "Dashboard" existe com os 3 gráficos organizados visualmente
- [ ] Os valores nos gráficos são consistentes com as Tabelas Dinâmicas

---

## BLOCO 5 — Formatação Condicional + Validação + Polimento (45 min)

### O que aprender (10 min de estudo ativo)

**Formatação Condicional:** muda a aparência da célula automaticamente com base no valor.
- Caminho: Selecione células → Página Inicial → Formatação Condicional
- Tipos mais usados: "Maior que", "Entre", "Escala de Cores", "Barras de Dados", "Conjunto de Ícones"

**Validação de Dados:** restringe o que pode ser digitado numa célula.
- Caminho: Selecione células → Dados → Validação de Dados
- Mais usado: criar Menu Suspenso (tipo "Lista") com opções pré-definidas

---

### 🏋️ DESAFIO 5: "Planilha Profissional" (35 min)

**Descrição do desafio:**
Aplique camadas de profissionalismo à sua planilha existente. Isso é o que separa uma planilha de iniciante de uma planilha de alguém que sabe o que faz.

**Parte A — Formatação Condicional na aba Vendas:**
1. Na coluna I (Classificação), aplique formatação condicional:
   - Células com "ALTO" → fundo verde claro, texto verde escuro
   - Células com "MÉDIO" → fundo amarelo claro, texto laranja
   - Células com "BAIXO" → fundo vermelho claro, texto vermelho escuro
2. Na coluna H (Total_Venda), aplique "Barras de Dados" (barras proporcionais dentro das células)
3. Na coluna F (Quantidade), aplique "Escala de Cores" (gradiente de branco a azul: quanto maior, mais escuro)

**Parte B — Validação de Dados:**
1. Crie uma nova aba chamada "Entrada_Dados"
2. Monte um formulário de entrada para novas vendas com as mesmas colunas da aba Vendas
3. Na coluna "Vendedor", crie uma validação de dados tipo Lista com as opções: Ana, Bruno, Carla, Diego
4. Na coluna "Produto", crie uma validação tipo Lista com os 6 produtos do catálogo
5. Na coluna "Quantidade", crie uma validação tipo Número Inteiro, entre 1 e 100
6. Para cada validação, configure uma "Mensagem de Erro" personalizada (ex: "Selecione um vendedor da lista")

**Parte C — Polimento visual do Dashboard:**
1. Volte à aba Dashboard
2. Adicione um título no topo: "Dashboard de Vendas — TechStore — Janeiro 2025" em fonte grande e negrito
3. Adicione 3 cartões de KPI (pequenas caixas com métricas-chave):
   - KPI 1: Faturamento Total (com fórmula referenciando a aba Vendas)
   - KPI 2: Número de Vendas
   - KPI 3: Ticket Médio (Faturamento Total ÷ Número de Vendas)
4. Formate os KPIs: fonte grande para o número, fonte menor para o rótulo, borda ao redor
5. Congele a linha do título: Exibir → Congelar Painéis → Congelar Linha Superior

**Instruções passo a passo:**
- Formatação condicional por texto: Selecione I2:I21 → Formatação Condicional → Nova Regra → "Formatar apenas células que contêm" → "Texto específico" → "contém" → "ALTO" → Formatar → aba Preenchimento → verde claro → OK. Repita para MÉDIO e BAIXO
- Barras de dados: Selecione H2:H21 → Formatação Condicional → Barras de Dados → escolha um estilo
- Validação tipo Lista: Selecione as células → Dados → Validação → Permitir: Lista → Origem: Ana,Bruno,Carla,Diego (separados por ponto-e-vírgula no Excel em português, ou vírgula no Sheets)
- Para os KPIs no Dashboard: crie células com fórmulas tipo `=SOMA(Vendas!H2:H21)` e formate com fonte tamanho 20+

**Dicas:**
- Formatação condicional é cumulativa — se você aplicar 3 regras, todas funcionam ao mesmo tempo
- Na validação, marque "Mostrar mensagem de entrada" para criar uma dica quando o usuário clicar na célula
- Os KPIs no dashboard são simplesmente células formatadas com fórmulas — não precisa de nada especial
- Se quiser que o dashboard pareça limpo, esconda as linhas de grade: Exibir → desmarque "Linhas de Grade"

**Critérios de aceite:**
- [ ] A coluna I tem 3 cores diferentes (verde/amarelo/vermelho) via formatação condicional
- [ ] A coluna H mostra barras de dados proporcionais
- [ ] A coluna F mostra escala de cores
- [ ] A aba "Entrada_Dados" tem validações funcionais (testar: digitar "Zé" no campo Vendedor deve dar erro)
- [ ] A mensagem de erro personalizada aparece ao tentar digitar valor inválido
- [ ] O Dashboard tem título, 3 KPIs e 3 gráficos organizados
- [ ] As linhas de grade estão ocultas no Dashboard

---

## BLOCO 6 — Desafio Final Integrado (30 min)

### 🏋️ DESAFIO FINAL: "O Teste da Entrevista" (30 min cronometrados)

### 📋 PREPARAÇÃO — Arquivo do Desafio Final (criar ANTES em arquivo separado)

> **Para quem está preparando o material:** crie um arquivo Excel novo e separado chamado **"Teste_Entrevista.xlsx"**. Este arquivo simula o que a estudante receberia numa prova real. Ela deve abrir este arquivo e completar as tarefas em 30 minutos cronometrados. Crie as duas abas abaixo já populadas.

#### Aba 1 — "Funcionários" (10 linhas + cabeçalho)

| Nome | Departamento | Cargo | Salario_Mensal |
|---|---|---|---|
| Mariana Silva | TI | Analista | R$ 4.500,00 |
| Pedro Santos | Marketing | Coordenador | R$ 8.200,00 |
| Juliana Costa | Financeiro | Gerente | R$ 14.000,00 |
| Rafael Oliveira | TI | Coordenador | R$ 7.800,00 |
| Camila Souza | RH | Analista | R$ 3.800,00 |
| Lucas Ferreira | Marketing | Analista | R$ 4.200,00 |
| Beatriz Lima | TI | Analista | R$ 5.100,00 |
| Thiago Rocha | Financeiro | Coordenador | R$ 9.500,00 |
| Amanda Alves | RH | Gerente | R$ 12.000,00 |
| Fernando Dias | TI | Gerente | R$ 15.000,00 |

**Atenção na preparação:**
- Salários devem ser números formatados como moeda (não texto)
- Departamentos devem ser escritos exatamente: TI, Marketing, Financeiro, RH
- Cargos devem ser exatamente: Analista, Coordenador, Gerente
- Converta com Ctrl+T
- Deixe as colunas E, F, G, H vazias (é onde ela vai criar as fórmulas)

#### Aba 2 — "Benefícios" (3 linhas + cabeçalho)

| Cargo | Valor_Beneficio |
|---|---|
| Analista | R$ 800,00 |
| Coordenador | R$ 1.200,00 |
| Gerente | R$ 2.000,00 |

**Atenção na preparação:**
- Os nomes dos cargos devem ser IDÊNTICOS aos da aba Funcionários
- Valores devem ser números formatados como moeda
- A coluna A deve ser "Cargo" (o PROCV busca na primeira coluna)

#### Respostas esperadas para conferência:

- **PROCV Benefício:** Mariana (Analista) → R$ 800 / Pedro (Coordenador) → R$ 1.200 / Juliana (Gerente) → R$ 2.000
- **Custo Total mais alto:** Fernando Dias → R$ 15.000 + R$ 2.000 = R$ 17.000
- **Faixa Salarial:** SÊNIOR (>10k): Juliana, Amanda, Fernando / PLENO (>6k): Pedro, Rafael, Thiago / JÚNIOR (resto): Mariana, Camila, Lucas, Beatriz
- **SOMASES (TI + Analista):** Mariana (R$ 5.300) + Beatriz (R$ 5.900) = **R$ 11.200** (Salário + Benefício de cada uma)

---

**Descrição do desafio:**
Simule um teste real de entrevista. Cronometre 30 minutos. Abra o arquivo **Teste_Entrevista.xlsx** já preparado (com as abas "Funcionários" e "Benefícios" preenchidas). Não consulte os desafios anteriores. Este é o teste de retenção.

**Cenário:**
Uma empresa de consultoria enviou uma planilha com dados de funcionários e uma tabela de benefícios por cargo. Sua tarefa é analisar, calcular e apresentar os dados profissionalmente.

**Tarefas obrigatórias (devem ser completadas em 30 min):**

1. **PROCV:** Na aba Funcionários, adicione uma coluna "Valor_Benefício" que busque automaticamente o benefício com base no Cargo, usando PROCV referenciando a aba Benefícios. Envolva em SEERRO.

2. **Coluna calculada:** Adicione uma coluna "Custo_Total" = Salário + Valor_Benefício.

3. **SE:** Adicione uma coluna "Faixa_Salarial" usando SE:
   - Salário > R$ 10.000 → "SÊNIOR"
   - Salário > R$ 6.000 → "PLENO"
   - Senão → "JÚNIOR"

4. **SOMASES:** Na aba "Resumo" (nova aba), calcule o custo total de todos os funcionários de TI que são Analistas.

5. **Tabela Dinâmica:** Crie uma TD mostrando a soma de Custo_Total por Departamento.

6. **Gráfico:** Crie um gráfico de barras a partir da Tabela Dinâmica.

7. **Formatação Condicional:** Na coluna Faixa_Salarial, aplique cores (SÊNIOR=azul, PLENO=verde, JÚNIOR=laranja).

8. **Validação:** Na coluna Departamento, aplique validação tipo Lista com os 4 departamentos.

**Critérios de aceite:**
- [ ] Tudo foi feito em 30 minutos ou menos
- [ ] A tabela de Funcionários segue as 5 Regras de Ouro
- [ ] O PROCV funciona corretamente (benefícios corretos por cargo)
- [ ] A fórmula SE classifica corretamente as 3 faixas
- [ ] O SOMASES retorna um valor numérico correto
- [ ] A Tabela Dinâmica mostra custo por departamento
- [ ] O gráfico existe e reflete os dados da TD
- [ ] A formatação condicional mostra 3 cores distintas
- [ ] A validação impede digitar departamentos inválidos

**Meta de tempo:**
- ⭐⭐⭐ Excelente: completou tudo em até 25 min
- ⭐⭐ Bom: completou tudo em até 30 min
- ⭐ Aceitável: completou pelo menos 6 de 8 tarefas em 30 min

---

## Checklist Final — O que Você Deve Saber ao Fim das 5 Horas

| # | Habilidade | Consigo fazer? |
|---|---|---|
| 1 | Criar uma tabela seguindo as 5 Regras de Ouro | ☐ |
| 2 | Converter dados em Tabela com Ctrl+T | ☐ |
| 3 | Usar SOMA, MÉDIA, MÁXIMO, MÍNIMO | ☐ |
| 4 | Usar CONT.SE para contar com critério | ☐ |
| 5 | Usar SE com condições aninhadas | ☐ |
| 6 | Usar PROCV para cruzar duas tabelas | ☐ |
| 7 | Envolver PROCV em SEERRO | ☐ |
| 8 | Usar SOMASES com dois critérios | ☐ |
| 9 | Criar uma Tabela Dinâmica arrastando campos | ☐ |
| 10 | Criar um gráfico a partir de dados | ☐ |
| 11 | Aplicar formatação condicional por texto e por escala | ☐ |
| 12 | Criar validação de dados com lista suspensa | ☐ |
| 13 | Navegar com atalhos básicos (Ctrl+T, Ctrl+Z, F4, F2) | ☐ |
| 14 | Saber a diferença entre referência relativa e absoluta ($) | ☐ |
| 15 | Explicar verbalmente o que cada fórmula faz | ☐ |

**Se você marcou 12+ itens, está pronto para o teste. Boa sorte amanhã!**
