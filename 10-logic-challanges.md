# 10 desafios de raciocínio lógico em planilhas para iniciantes

**Aprender Excel ou Google Sheets através de desafios práticos que exercitam o raciocínio lógico é a forma mais eficaz de dominar planilhas.** Pesquisas acadêmicas confirmam que a metodologia "aprender fazendo" com progressão gradual de dificuldade (scaffolding) gera retenção significativamente maior do que tutoriais passivos. O segredo não está em decorar fórmulas, mas em desenvolver o pensamento computacional: decompor problemas complexos em etapas menores, reconhecer padrões nos dados e construir soluções lógicas passo a passo. Os 10 desafios a seguir foram desenhados para que cada um ensine **uma técnica diferente** de resolução de problemas, cobrindo desde classificação condicional até reconciliação de dados entre tabelas.

> **Nota importante sobre idiomas:** No Excel em português, os argumentos das funções são separados por ponto e vírgula (`;`) em vez de vírgula (`,`). No Google Sheets, as funções podem ser usadas em inglês independentemente do idioma da interface. Cada desafio apresenta as fórmulas nas duas versões.

---

## Desafio 1 — Classificar candidatos com lógica booleana (SE + E/OU)

### Técnica ensinada: Funções condicionais com lógica AND/OR

**Cenário:** Você trabalha no RH de uma empresa e precisa avaliar candidatos para um programa de estágio. Cada candidato tem duas informações: nota na prova (0 a 100) e se já concluiu um curso técnico (Sim/Não). O candidato é **"Aprovado"** se tiver nota ≥ 70 **E** curso técnico concluído. É **"Lista de espera"** se tiver nota ≥ 70 **OU** curso técnico concluído (mas não ambos). Caso contrário, é **"Reprovado"**.

**Dados de exemplo:**

| Candidato | Nota | Curso Técnico |
|-----------|------|---------------|
| Ana       | 85   | Sim           |
| Bruno     | 60   | Sim           |
| Carla     | 75   | Não           |
| Diego     | 50   | Não           |
| Eva       | 90   | Sim           |

**Sua missão:** Criar na coluna D uma fórmula que classifique automaticamente cada candidato nas três categorias.

**Fórmula-solução:**
```
Excel PT: =SE(E(B2>=70;C2="Sim");"Aprovado";SE(OU(B2>=70;C2="Sim");"Lista de espera";"Reprovado"))
Excel EN: =IF(AND(B2>=70,C2="Yes"),"Approved",IF(OR(B2>=70,C2="Yes"),"Waitlist","Rejected"))
```

**O que exercita:** Este desafio treina o **raciocínio dedutivo** — avaliar múltiplas condições simultaneamente e entender a diferença crucial entre E (todas as condições verdadeiras) e OU (pelo menos uma condição verdadeira). É a base da lógica booleana, presente em programação, banco de dados e análise de dados. O iniciante aprende que a **ordem das condições importa**: a condição mais restritiva (E) deve vir antes da mais permissiva (OU).

**Dica pedagógica:** Antes de escrever qualquer fórmula, peça ao aluno para desenhar uma árvore de decisão no papel. Isso transforma o raciocínio abstrato em algo visual e ajuda a entender a sequência lógica.

---

## Desafio 2 — Caçar dados duplicados em uma lista de clientes (CONT.SE)

### Técnica ensinada: Análise de frequência para detectar duplicatas

**Cenário:** Uma loja online exportou sua base de e-mails de clientes, mas suspeita que há cadastros duplicados que estão gerando cupons de desconto em dobro. Você recebeu uma lista com **50 endereços de e-mail** e precisa identificar quais estão repetidos.

**Dados de exemplo (primeiras linhas):**

| ID | Email                  |
|----|------------------------|
| 1  | maria@email.com        |
| 2  | joao.silva@email.com   |
| 3  | ana.costa@email.com    |
| 4  | maria@email.com        |
| 5  | pedro.lima@email.com   |
| 6  | joao.silva@email.com   |

**Sua missão em 3 etapas:**
1. Na coluna C, contar quantas vezes cada e-mail aparece na lista inteira
2. Na coluna D, marcar "Duplicado" ou "Único" com base na contagem
3. Responder: quantos e-mails únicos existem na lista?

**Fórmulas-solução:**
```
Contagem:
Excel PT: =CONT.SE($B$2:$B$51;B2)
Excel EN: =COUNTIF($B$2:$B$51,B2)

Classificação:
Excel PT: =SE(C2>1;"Duplicado";"Único")
Excel EN: =IF(C2>1,"Duplicate","Unique")

Total de únicos (Google Sheets):
=COUNTA(UNIQUE(B2:B51))
```

**O que exercita:** O raciocínio por trás desse desafio é a **análise de frequência** — uma das técnicas mais fundamentais em análise de dados. O aluno aprende que contar ocorrências revela anomalias invisíveis a olho nu. A função CONT.SE transforma uma pergunta qualitativa ("tem duplicata?") em uma resposta quantitativa (contagem). O uso de referências absolutas (`$B$2:$B$51`) é um conceito essencial: a faixa de busca precisa ficar "travada" para não se mover quando a fórmula é copiada para baixo.

**Erro comum de iniciante:** Esquecer o símbolo `$` nas referências. Sem ele, ao arrastar a fórmula para baixo, o intervalo de busca se desloca e os resultados ficam incorretos.

---

## Desafio 3 — Montar um pedido automático com PROCV/VLOOKUP

### Técnica ensinada: Mapeamento relacional entre tabelas

**Cenário:** Você é assistente administrativo de um restaurante. Na **Aba 1** há um catálogo com 20 produtos, seus códigos e preços. Na **Aba 2** há um formulário de pedido onde o garçom digita apenas o código do produto e a quantidade. O sistema precisa buscar automaticamente o nome e o preço do produto e calcular o subtotal.

**Tabela de Produtos (Aba 1):**

| Código | Produto          | Preço   |
|--------|------------------|---------|
| P001   | Hambúrguer       | R$ 25,90|
| P002   | Pizza Margherita | R$ 39,90|
| P003   | Suco Natural     | R$ 12,00|
| P004   | Salada Caesar    | R$ 22,50|

**Formulário de Pedido (Aba 2):**

| Código | Produto (automático) | Preço (automático) | Qtd | Subtotal |
|--------|---------------------|--------------------|-----|----------|
| P002   | ?                   | ?                  | 2   | ?        |
| P003   | ?                   | ?                  | 3   | ?        |

**Sua missão:** Preencher automaticamente as colunas "Produto", "Preço" e "Subtotal" usando PROCV.

**Fórmulas-solução:**
```
Produto:
Excel PT: =PROCV(A2;Produtos!$A$2:$C$21;2;FALSO)
Excel EN: =VLOOKUP(A2,Products!$A$2:$C$21,2,FALSE)

Preço:
Excel PT: =PROCV(A2;Produtos!$A$2:$C$21;3;FALSO)
Excel EN: =VLOOKUP(A2,Products!$A$2:$C$21,3,FALSE)

Subtotal: =C2*D2
```

**O que exercita:** O PROCV ensina **pensamento relacional** — conectar informações entre tabelas usando uma chave identificadora, exatamente como funcionam bancos de dados. O aluno desenvolve a lógica de "dado X, encontre Y": o código é a ponte que liga o pedido ao catálogo. Esse conceito é transferível para qualquer sistema que trabalhe com tabelas relacionadas, de ERPs corporativos a bancos de dados SQL.

**Armadilha clássica:** O parâmetro FALSO (correspondência exata) é obrigatório. Sem ele, o PROCV assume correspondência aproximada e pode retornar o produto errado — um bug silencioso que é difícil de detectar.

---

## Desafio 4 — Decifrar códigos de produto usando funções de texto

### Técnica ensinada: Decomposição e extração de informações de strings

**Cenário:** Uma empresa usa códigos de produto com uma estrutura fixa: `CAT-CID-0000`, onde os 3 primeiros caracteres indicam a **categoria** (ELE = Eletrônicos, ROU = Roupas, ALI = Alimentos), os caracteres 5-7 indicam a **cidade** do armazém (SPO = São Paulo, RJO = Rio de Janeiro, BHZ = Belo Horizonte), e os 4 últimos dígitos são o número sequencial. Você recebeu 30 códigos e precisa extrair cada parte.

**Dados de exemplo:**

| Código Completo | Categoria | Cidade | Número |
|-----------------|-----------|--------|--------|
| ELE-SPO-0042    | ?         | ?      | ?      |
| ROU-RJO-0187    | ?         | ?      | ?      |
| ALI-BHZ-0003    | ?         | ?      | ?      |

**Sua missão:**
1. Extrair a categoria (3 primeiros caracteres)
2. Extrair a cidade (caracteres 5 a 7)
3. Extrair o número sequencial (4 últimos caracteres)
4. **Bônus:** Criar uma coluna que traduza as siglas para nomes completos

**Fórmulas-solução:**
```
Categoria:
Excel PT: =ESQUERDA(A2;3)
Excel EN: =LEFT(A2,3)

Cidade:
Excel PT: =EXT.TEXTO(A2;5;3)
Excel EN: =MID(A2,5,3)

Número:
Excel PT: =DIREITA(A2;4)
Excel EN: =RIGHT(A2,4)

Tradução (bônus):
Excel PT: =SE(B2="ELE";"Eletrônicos";SE(B2="ROU";"Roupas";"Alimentos"))
Excel EN: =IF(B2="ELE","Electronics",IF(B2="ROU","Clothing","Food"))
```

**O que exercita:** Funções de texto ensinam **decomposição algorítmica** — quebrar uma informação complexa em partes menores e manipuláveis. É o mesmo raciocínio usado em programação quando se faz "parsing" de dados. O aluno precisa pensar em posições e comprimentos de caracteres, desenvolvendo precisão lógica. O bônus combina extração de texto com lógica condicional, mostrando como técnicas se encadeiam.

**Atenção:** A posição inicial no EXT.TEXTO/MID começa em **1**, não em 0 (diferente de muitas linguagens de programação). É o erro "off-by-one" mais comum entre iniciantes.

---

## Desafio 5 — Calcular comissões escalonadas para vendedores

### Técnica ensinada: Cálculos condicionais encadeados (SE aninhado / IFS)

**Cenário:** Uma empresa de tecnologia paga comissões progressivas aos vendedores com base no valor total de vendas no mês. As faixas são:

| Faixa de Vendas          | Comissão |
|--------------------------|----------|
| Até R$ 5.000             | 5%       |
| De R$ 5.001 a R$ 15.000  | 8%       |
| De R$ 15.001 a R$ 30.000 | 12%      |
| Acima de R$ 30.000       | 15%      |

**Dados dos vendedores:**

| Vendedor | Vendas Mês  |
|----------|-------------|
| Lucas    | R$ 3.200    |
| Marina   | R$ 12.500   |
| Rafael   | R$ 28.000   |
| Sofia    | R$ 45.000   |
| Thiago   | R$ 5.000    |

**Sua missão:** Calcular a comissão de cada vendedor e o valor em reais que cada um receberá.

**Fórmulas-solução:**
```
SE aninhado (ordem decrescente — do maior para o menor):
Excel PT: =SE(B2>30000;B2*15%;SE(B2>15000;B2*12%;SE(B2>5000;B2*8%;B2*5%)))
Excel EN: =IF(B2>30000,B2*15%,IF(B2>15000,B2*12%,IF(B2>5000,B2*8%,B2*5%)))

Alternativa com SES/IFS (Excel 2016+):
Excel PT: =SES(B2>30000;B2*15%;B2>15000;B2*12%;B2>5000;B2*8%;VERDADEIRO;B2*5%)
Excel EN: =IFS(B2>30000,B2*15%,B2>15000,B2*12%,B2>5000,B2*8%,TRUE,B2*5%)
```

**O que exercita:** Este desafio treina a **lógica de árvore de decisão sequencial** — o mesmo raciocínio por trás de tabelas de imposto de renda e precificação variável. A armadilha pedagógica central é a **ordem das condições**: o SE aninhado avalia de cima para baixo e para na primeira condição verdadeira. Se o aluno testar `>5000` antes de `>30000`, todo vendedor acima de R$ 5.000 recebe apenas 8%. Essa lição sobre prioridade de condições é transferível para programação e qualquer sistema baseado em regras.

**Extensão avançada:** Para alunos que terminarem rápido, proponha o cálculo por faixas acumulativas (como o IRPF real), onde os primeiros R$ 5.000 rendem 5%, os próximos R$ 10.000 rendem 8%, e assim por diante. Isso eleva significativamente a complexidade lógica.

---

## Desafio 6 — Planejar entregas com cálculos de dias úteis

### Técnica ensinada: Raciocínio temporal com funções de data

**Cenário:** Você gerencia a logística de uma editora. Cada pedido de livro tem um prazo de entrega que depende da região: **Sul/Sudeste = 5 dias úteis**, **Nordeste/Centro-Oeste = 8 dias úteis**, **Norte = 12 dias úteis**. Há uma lista de feriados nacionais que devem ser excluídos. Você precisa calcular a data de entrega prevista e verificar se algum pedido está atrasado.

**Dados de exemplo:**

| Pedido | Data do Pedido | Região    | Feriados (lista à parte) |
|--------|---------------|-----------|--------------------------|
| #101   | 10/03/2026    | Sudeste   | 21/04/2026               |
| #102   | 12/03/2026    | Nordeste  | 01/05/2026               |
| #103   | 05/03/2026    | Norte     | 07/09/2026               |

**Sua missão:**
1. Determinar o prazo em dias úteis com base na região (usando SE)
2. Calcular a data prevista de entrega (usando DIATRABALHO)
3. Calcular quantos dias úteis faltam entre hoje e a data prevista (usando DIATRABALHOTOTAL)
4. Marcar como "Atrasado" ou "No prazo" comparando a data prevista com a data atual

**Fórmulas-solução:**
```
Prazo por região:
Excel PT: =SE(C2="Sudeste";5;SE(C2="Sul";5;SE(C2="Nordeste";8;SE(C2="Centro-Oeste";8;12))))
Excel EN: =IF(C2="Southeast",5,IF(C2="South",5,IF(C2="Northeast",8,IF(C2="Midwest",8,12))))

Data de entrega:
Excel PT: =DIATRABALHO(B2;D2;Feriados!$A$2:$A$20)
Excel EN: =WORKDAY(B2,D2,Holidays!$A$2:$A$20)

Dias úteis restantes:
Excel PT: =DIATRABALHOTOTAL(HOJE();E2;Feriados!$A$2:$A$20)
Excel EN: =NETWORKDAYS(TODAY(),E2,Holidays!$A$2:$A$20)

Status:
Excel PT: =SE(HOJE()>E2;"Atrasado";"No prazo")
Excel EN: =IF(TODAY()>E2,"Late","On time")
```

**O que exercita:** O raciocínio temporal é surpreendentemente complexo para iniciantes. O aluno precisa entender que **dias úteis ≠ dias corridos**, que feriados são exceções à regra, e que a função DIATRABALHO não conta o dia inicial. Esse desafio combina lógica condicional (classificar regiões) com cálculo de datas (projetar prazos) e comparação temporal (avaliar atrasos), integrando três camadas de raciocínio em um cenário realista.

**Cuidado com formatação:** O resultado de DIATRABALHO pode aparecer como número serial (ex.: 46105). Formate a célula como "Data" para exibir corretamente.

---

## Desafio 7 — Criar um mapa de calor de vendas com formatação condicional

### Técnica ensinada: Análise visual de padrões usando formatação condicional

**Cenário:** Uma rede de cafeterias tem 6 filiais e registrou vendas diárias durante uma semana. O gerente regional quer identificar rapidamente: quais filiais vendem mais, quais dias são mais fracos e se há alguma filial com desempenho muito abaixo da média.

**Dados de exemplo (vendas em R$):**

| Filial       | Seg   | Ter   | Qua   | Qui   | Sex   | Sáb   | Dom   |
|-------------|-------|-------|-------|-------|-------|-------|-------|
| Centro      | 2.800 | 2.650 | 2.900 | 3.100 | 3.500 | 4.200 | 3.800 |
| Shopping    | 3.200 | 3.100 | 3.000 | 3.300 | 4.000 | 5.500 | 5.200 |
| Bairro Sul  | 1.200 | 1.100 | 1.300 | 1.250 | 1.800 | 2.100 | 1.900 |
| Aeroporto   | 4.100 | 4.000 | 3.800 | 4.200 | 4.500 | 3.900 | 3.700 |
| Universidade| 2.500 | 2.400 | 2.600 | 2.700 | 2.200 | 800   | 600   |
| Praia       | 1.500 | 1.400 | 1.600 | 1.500 | 2.800 | 4.800 | 5.000 |

**Sua missão em 4 etapas:**
1. Aplicar uma **escala de cores** (verde = alto, vermelho = baixo) em toda a matriz de vendas
2. Usar **barras de dados** em uma coluna de totais semanais
3. Criar uma regra que destaque em **negrito com fundo amarelo** qualquer valor abaixo de R$ 1.000
4. Responder: qual padrão você identifica ao olhar o mapa de calor? Quais filiais têm comportamento diferente nos fins de semana?

**Como fazer:**
```
Escala de cores: Selecionar B2:H7 → Formatação Condicional → Escalas de Cor → Verde-Amarelo-Vermelho
Barras de dados: Selecionar coluna de totais → Formatação Condicional → Barras de Dados
Regra personalizada: Formatação Condicional → Nova Regra → "Formatar apenas células que contêm" → Valor da célula < 1000 → Fundo amarelo, negrito
```

**O que exercita:** A formatação condicional transforma o cérebro do aluno em um **detector de padrões visuais**. Sem ela, uma tabela 6×7 é apenas uma massa de números. Com ela, padrões saltam aos olhos: a filial "Universidade" despenca nos fins de semana (público estudantil ausente), enquanto "Praia" dispara (turismo). O aluno aprende que **visualização é análise** — não é decoração. Essa habilidade de transformar dados brutos em insights visuais é uma das mais valorizadas em entrevistas de emprego para analistas.

---

## Desafio 8 — Analisar a distribuição do orçamento familiar

### Técnica ensinada: Percentuais, proporções e análise parte-todo

**Cenário:** Uma família quer entender para onde vai o dinheiro. Registraram todas as despesas do mês e querem calcular: qual porcentagem do salário vai para cada categoria, como isso se compara com a regra 50/30/20 (necessidades/desejos/investimentos), e qual foi a variação em relação ao mês anterior.

**Dados de exemplo:**

| Categoria        | Mês Atual  | Mês Anterior | Tipo          |
|-----------------|------------|--------------|---------------|
| Aluguel          | R$ 1.800   | R$ 1.800     | Necessidade   |
| Supermercado     | R$ 1.200   | R$ 1.050     | Necessidade   |
| Transporte       | R$ 450     | R$ 400       | Necessidade   |
| Saúde            | R$ 300     | R$ 280       | Necessidade   |
| Lazer            | R$ 600     | R$ 750       | Desejo        |
| Restaurantes     | R$ 400     | R$ 520       | Desejo        |
| Roupas           | R$ 250     | R$ 180       | Desejo        |
| Streaming        | R$ 80      | R$ 80        | Desejo        |
| Investimentos    | R$ 500     | R$ 500       | Investimento  |
| **Salário líquido** | **R$ 6.500** | **R$ 6.500** | — |

**Sua missão:**
1. Calcular o % de cada categoria sobre o salário
2. Calcular a variação percentual mês a mês de cada categoria
3. Somar os totais por tipo (Necessidade/Desejo/Investimento) e calcular suas proporções
4. Comparar com a regra 50/30/20 e apontar desvios

**Fórmulas-solução:**
```
% do salário:
=B2/$B$11 (formatar como %)
PT: =B2/$B$11

Variação mês a mês:
=(B2-C2)/C2 (formatar como %)

Total por tipo:
Excel PT: =SOMASE($D$2:$D$10;F2;$B$2:$B$10)
Excel EN: =SUMIF($D$2:$D$10,F2,$B$2:$B$10)

Proporção por tipo:
=E2/$B$11
```

**O que exercita:** Raciocínio proporcional — entender relações **parte-todo** — é uma das habilidades analíticas mais importantes e frequentemente avaliada em entrevistas. O aluno aprende a diferença entre valor absoluto e relativo (R$ 600 em lazer parece pouco, mas é **9,2% do salário**). A variação percentual ensina comparação temporal. O uso de SOMASE para agrupar por categoria exercita a lógica de **agregação condicional**. O erro mais comum é esquecer de travar a referência do total com `$`, fazendo o denominador mudar ao copiar a fórmula.

---

## Desafio 9 — Encontrar erros em uma folha de pagamento usando filtros e ordenação

### Técnica ensinada: Detecção de anomalias por exploração sistemática de dados

**Cenário:** Você é auditor interno e recebeu a folha de pagamento de uma empresa com **40 funcionários**. Há 5 erros escondidos nos dados — e seu trabalho é encontrá-los. Os erros possíveis incluem: salário fora da faixa do cargo, CPF duplicado, data de admissão no futuro, departamento inexistente e nome em branco.

**Dados de exemplo (amostra):**

| ID  | Nome           | CPF           | Departamento | Cargo       | Salário   | Data Admissão |
|-----|---------------|---------------|-------------|-------------|-----------|---------------|
| 001 | Maria Santos  | 123.456.789-00| Vendas      | Analista Jr | R$ 3.500  | 15/03/2022    |
| 002 | João Silva    | 987.654.321-00| Financeiro  | Gerente     | R$ 12.000 | 01/06/2019    |
| 003 |               | 111.222.333-00| TI          | Estagiário  | R$ 1.800  | 10/01/2024    |
| 004 | Ana Costa     | 123.456.789-00| Marketing   | Analista Pl | R$ 5.500  | 22/08/2021    |
| 005 | Pedro Lima    | 555.666.777-00| Logísticaa  | Analista Jr | R$ 15.000 | 01/12/2027    |

**Erros plantados:**
- Linha 3: nome em branco
- Linha 4: CPF duplicado (igual ao da linha 1)
- Linha 5: departamento com erro de digitação ("Logísticaa"), salário incompatível com cargo Jr (R$ 15.000), data de admissão no futuro (2027)

**Sua missão (usando apenas ordenação, filtros e CONT.SE):**
1. Ordenar por Nome (A-Z) para encontrar células em branco (ficam no topo ou no fim)
2. Usar CONT.SE na coluna CPF para encontrar duplicados
3. Filtrar a coluna Data de Admissão por valores maiores que HOJE()
4. Ordenar por Salário (maior para menor) dentro de cada cargo para identificar outliers
5. Filtrar por Departamento e verificar se todos os nomes de departamento são válidos

**Fórmulas auxiliares:**
```
CPF duplicado:
Excel PT: =SE(CONT.SE($C$2:$C$41;C2)>1;"⚠ DUPLICADO";"OK")
Excel EN: =IF(COUNTIF($C$2:$C$41,C2)>1,"⚠ DUPLICATE","OK")

Data futura:
Excel PT: =SE(G2>HOJE();"⚠ DATA FUTURA";"OK")
Excel EN: =IF(G2>TODAY(),"⚠ FUTURE DATE","OK")
```

**O que exercita:** Este é um exercício de **pensamento investigativo** — o aluno se torna um detetive de dados. Diferente dos outros desafios, aqui não há uma fórmula mágica que resolve tudo. O aluno precisa formular hipóteses ("que tipo de erro pode existir?"), escolher a ferramenta certa para cada investigação (ordenar para ver extremos, filtrar para isolar categorias, CONT.SE para verificar unicidade) e interpretar os resultados. Essa mentalidade de **auditoria e validação** é exatamente o que empresas testam em processos seletivos para analistas de dados.

---

## Desafio 10 — Reconciliar estoque físico com estoque do sistema

### Técnica ensinada: Validação cruzada entre duas fontes de dados

**Cenário:** Chegou o dia da contagem de estoque semestral. Na **Tabela A** está o estoque registrado no sistema (ERP) com 25 produtos. Na **Tabela B** está a contagem física feita pela equipe do armazém, também com 25 linhas. Mas os dados não batem perfeitamente: alguns produtos do sistema não foram encontrados no armazém, alguns itens do armazém não estão no sistema, e vários têm quantidades divergentes.

**Tabela A — Sistema (amostra):**

| Código | Produto         | Qtd Sistema |
|--------|-----------------|-------------|
| SKU001 | Caneta Azul     | 500         |
| SKU002 | Caderno 100fl   | 200         |
| SKU003 | Borracha Branca | 150         |
| SKU007 | Lápis HB        | 300         |

**Tabela B — Contagem Física (amostra):**

| Código | Produto         | Qtd Física |
|--------|-----------------|------------|
| SKU001 | Caneta Azul     | 485        |
| SKU002 | Caderno 100fl   | 200        |
| SKU003 | Borracha Branca | 160        |
| SKU005 | Clips Niquelado | 1.000      |

**Sua missão — Criar uma tabela de reconciliação:**
1. Buscar a quantidade física correspondente a cada item do sistema (PROCV)
2. Calcular a diferença (Sistema − Física)
3. Calcular a diferença percentual
4. Classificar cada item: "OK" (diferença = 0), "Divergente" (diferença ≠ 0), "Não encontrado" (sem correspondência)
5. Identificar itens que existem na contagem física mas não no sistema

**Fórmulas-solução:**
```
Buscar quantidade física:
Excel PT: =SEERRO(PROCV(A2;Física!$A$2:$C$26;3;FALSO);"NÃO ENCONTRADO")
Excel EN: =IFERROR(VLOOKUP(A2,Physical!$A$2:$C$26,3,FALSE),"NOT FOUND")

Diferença:
=SE(D2="NÃO ENCONTRADO";"—";C2-D2)

Diferença %:
=SE(D2="NÃO ENCONTRADO";"—";(C2-D2)/C2)

Classificação:
=SE(D2="NÃO ENCONTRADO";"⚠ Não encontrado";SE(E2=0;"✓ OK";"⚠ Divergente"))

Itens apenas na contagem física (usar na Tabela B):
Excel PT: =SE(ÉNÚM(CORRESP(A2;Sistema!$A$2:$A$26;0));"No sistema";"⚠ SOMENTE FÍSICO")
Excel EN: =IF(ISNUMBER(MATCH(A2,System!$A$2:$A$26,0)),"In system","⚠ PHYSICAL ONLY")
```

**O que exercita:** A reconciliação de dados é considerada uma das **habilidades mais testadas em entrevistas** para cargos de analista financeiro e de dados. Este desafio exercita o raciocínio de **validação bidirecional**: não basta verificar A contra B — é preciso também verificar B contra A, pois as diferenças podem estar em qualquer direção. O uso de SEERRO/IFERROR ensina tratamento de exceções (o que acontece quando um dado não é encontrado?), e a combinação ÉNÚM + CORRESP (ISNUMBER + MATCH) é uma técnica profissional para verificar a existência de um valor em outra tabela sem retornar dados, apenas "sim" ou "não".

---

## Como estruturar a progressão dos desafios

Os 10 desafios foram organizados em uma progressão pedagógica deliberada. Os três primeiros (SE/IF, CONT.SE, PROCV) introduzem as **funções-pilar** que serão reutilizadas em desafios posteriores. Os desafios 4 a 6 ampliam o repertório com texto, condicionais encadeados e datas. Os desafios 7 e 8 mudam o foco de fórmulas para **análise e interpretação**. Os desafios 9 e 10 simulam cenários reais de trabalho que combinam múltiplas técnicas.

Pesquisas publicadas no *Journal of Marketing Analytics* (Springer, 2024) confirmam que esse modelo de **scaffolding** — instruções detalhadas no primeiro contato com cada técnica, progressivamente reduzidas — gera resultados significativamente melhores do que tutoriais uniformes. O princípio-chave: o aluno deve receber **orientação máxima na primeira vez** que encontra uma função, e **autonomia crescente** nas aparições seguintes.

Cada desafio segue um padrão de 5 etapas validado pelos melhores recursos educacionais analisados (Chandoo, ExcelExercises.com, Spreadsheet Center, Coursera):

- **Contexto narrativo** — um cenário profissional realista que justifica o exercício
- **Dados prontos** — o aluno não perde tempo criando dados, foca na resolução
- **Missão clara** — tarefas numeradas e objetivas
- **Solução com explicação** — não apenas a fórmula, mas o raciocínio por trás dela
- **Reflexão sobre erros comuns** — antecipar onde o iniciante vai tropeçar

## Referência rápida de funções em português e inglês

| Técnica | Funções PT-BR | Funções EN | Desafio |
|---------|--------------|------------|---------|
| Lógica booleana | SE, E, OU | IF, AND, OR | 1 |
| Contagem condicional | CONT.SE | COUNTIF | 2 |
| Busca entre tabelas | PROCV | VLOOKUP | 3 |
| Manipulação de texto | ESQUERDA, EXT.TEXTO, DIREITA | LEFT, MID, RIGHT | 4 |
| Condicionais encadeados | SE aninhado, SES | Nested IF, IFS | 5 |
| Cálculos com datas | DIATRABALHO, DIATRABALHOTOTAL, HOJE | WORKDAY, NETWORKDAYS, TODAY | 6 |
| Formatação condicional | (recurso do menu) | (menu feature) | 7 |
| Percentuais e agregação | SOMASE | SUMIF | 8 |
| Ordenação e filtros | (recurso do menu) | (menu feature) | 9 |
| Validação cruzada | PROCV, SEERRO, CORRESP, ÉNÚM | VLOOKUP, IFERROR, MATCH, ISNUMBER | 10 |

**Lembrete de sintaxe:** No Excel em português, use ponto e vírgula (`;`) para separar argumentos. No Google Sheets, as funções funcionam em inglês mesmo com interface em português. Em ambos, DATEDIF mantém o nome em inglês.

## Conclusão

O fio condutor destes 10 desafios não são as fórmulas em si, mas o **raciocínio lógico subjacente**: classificar com base em critérios (desafios 1 e 5), verificar integridade de dados (desafios 2 e 9), conectar informações entre fontes (desafios 3 e 10), decompor informações complexas (desafio 4), projetar cenários no tempo (desafio 6), reconhecer padrões visuais (desafio 7) e quantificar proporções (desafio 8). Essas oito habilidades cognitivas — classificação, verificação, conexão, decomposição, projeção temporal, reconhecimento de padrões, quantificação e validação cruzada — formam a base do pensamento analítico que o mercado de trabalho mais valoriza. O aluno que completar os 10 desafios não terá apenas aprendido funções de planilha: terá desenvolvido um repertório de **estratégias de resolução de problemas** transferíveis para qualquer ferramenta de dados.