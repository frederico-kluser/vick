# Guia do Desafio 9: Caça aos Erros na Folha de Pagamento

## 1. Apresentação do Desafio

Você acaba de assumir o papel de **Auditor Interno**. Sua primeira missão é analisar a folha de pagamento de uma empresa com 40 funcionários.

**O Problema:** A base de dados contém erros que podem custar caro para a empresa. Há 5 erros escondidos propositalmente nos dados e você precisa encontrá-los.

**Os erros podem ser do tipo:**
*   Salário incompatível com o cargo (muito alto ou baixo).
*   CPF duplicado (duas pessoas com o mesmo documento).
*   Data de admissão no futuro (impossível!).
*   Departamento inexistente (erro de digitação).
*   Nome do funcionário em branco.

Seu objetivo é identificar **quais linhas contêm erros** e **qual é o erro**.

---

## 2. Tutorial de Técnicas e Ferramentas

Para este desafio, você não precisará de fórmulas complexas, apenas de ferramentas de análise básica. Aqui está o que você vai usar:

### A. Ordenação (Sort)
Organiza os dados para facilitar a visualização de extremos (maior/menor) ou itens vazios.

*   **Excel:** Selecione a coluna desejada (clique na letra da coluna, ex: A) -> Vá na aba **Dados** -> Clique em **Classificar de A a Z** (crescente) ou **Z a A** (decrescente).
*   **Google Sheets:** Passe o mouse sobre a letra da coluna -> Clique na setinha que aparece -> Escolha **Classificar página A-Z**.

### B. Filtros (Filter)
Permite esconder dados que não interessam e mostrar apenas o que você quer ver. É ótimo para ver todos os valores únicos de uma coluna (ex: listar todos os departamentos para achar um escrito errado).

*   **Excel:** Selecione a linha de cabeçalho (a primeira linha com os nomes das colunas) -> Vá na aba **Dados** -> Clique no botão **Filtro** (ícone de funil). Agora cada coluna tem uma setinha para filtrar.
*   **Google Sheets:** Selecione a linha de cabeçalho -> Vá no menu **Dados** -> **Criar um filtro**.

### C. Contagem Condicional (CONT.SE / COUNTIF)
Útil para achar duplicatas. Conta quantas vezes um valor aparece numa lista.

*   **Fórmula:** `=CONT.SE(intervalo; critério)`
    *   *Excel (Português):* `=CONT.SE(C:C; C2)` -> Conta quantas vezes o CPF da linha 2 aparece na coluna C inteira. Se der mais de 1, é duplicado!
    *   *Google Sheets / Excel (Inglês):* `=COUNTIF(C:C, C2)`

### D. Data de Hoje (HOJE / TODAY)
Ajuda a verificar se uma data já passou ou é futura.

*   **Fórmula:** `=HOJE()`
    *   Retorna a data atual. Você pode comparar: `=G2 > HOJE()`. Se der VERDADEIRO, a data é futura.

---

## 3. O que é esperado ao final

Ao final deste exercício, você deve ter uma lista com 5 anotações, indicando o ID ou Nome do funcionário e qual o erro encontrado.

**Exemplo do formato de entrega (mental ou anotado):**
*   Erro 1: Linha X - Erro tal.
*   Erro 2: Linha Y - Erro tal.
...

Não se preocupe em corrigir os dados agora, o foco é **encontrar e reportar** as inconsistências.

---

## 4. Dicas Progressivas

Se estiver travado, use estas dicas uma por uma. Tente fazer sem elas primeiro!

### Dica 1: Nomes em branco
Use a **Ordenação** na coluna "Nome". Células vazias costumam ir para o topo ou para o final da lista quando ordenadas.

### Dica 2: CPFs Duplicados
Olhar um por um é impossível. Crie uma coluna nova chamada "Verificação CPF" e use a fórmula `CONT.SE` (ou `COUNTIF`) para contar quantas vezes aquele CPF aparece na coluna. Filtre essa nova coluna para mostrar valores maiores que 1.

### Dica 3: Datas no Futuro
Use o **Filtro** na coluna "Data de Admissão". O Excel/Sheets costuma agrupar datas por ano. Se você vir um ano muito à frente (ex: 2027, 2030), desmarque os outros anos e veja quem sobra. Ou use uma fórmula auxiliar `=G2 > HOJE()`.

### Dica 4: Departamentos Estranhos
Use o **Filtro** na coluna "Departamento". Ao clicar na setinha do filtro, ele lista todos os valores únicos encontrados. Leia a lista com atenção. Vê algum nome escrito errado (ex: "Finaceiro" ou "Logísticaa")?

### Dica 5: Salários Fora do Padrão
Ordene a tabela primeiro por "Cargo" e depois olhe a coluna "Salário". Ou melhor: use o **Filtro** para olhar cargo por cargo. Um "Estagiário" ganhando o mesmo que um "Gerente" vai saltar aos olhos.

---
🛑 **PARE AQUI SE NÃO QUISER SPOILERS! A RESOLUÇÃO ESTÁ ABAIXO.**
---
.
.
.
.
.
.
.
.
.
.

## 5. Resultado e Resolução Passo a Passo

Aqui estão os 5 erros que foram plantados no desafio e como encontrá-los:

### 1. Nome em Branco (Linha 3)
*   **Como encontrar:** Ao ordenar a coluna **Nome** de A a Z, esta linha apareceu no topo (ou no final) sem nenhum texto.
*   **Ação:** O funcionário de ID 003 não tem nome registrado.

### 2. CPF Duplicado (Linha 4)
*   **Como encontrar:** Usando a fórmula `=CONT.SE(C:C; C4)`, o resultado foi **2**. Isso significa que o CPF `123.456.789-00` aparece duas vezes (na linha 1 e na linha 4).
*   **Ação:** Ana Costa (Linha 4) está com o mesmo CPF de Maria Santos (Linha 1).

### 3. Departamento "Logísticaa" (Linha 5)
*   **Como encontrar:** Ao aplicar o **Filtro** na coluna Departamento, a lista de opções mostrou "Financeiro", "Marketing", "TI", "Vendas" e..."Logísticaa" (com 'a' extra).
*   **Ação:** Erro de digitação no departamento do Pedro Lima.

### 4. Salário Incompatível (Linha 5)
*   **Como encontrar:** Ao ordenar por Cargo ou filtrar apenas "Analista Jr", vemos que a média salarial é ~R$ 3.500. Pedro Lima (Linha 5) é Analista Jr mas ganha **R$ 15.000**, o que é um outlier (valor fora da curva).
*   **Ação:** Salário provavelmente digitado errado (talvez fosse 1.500 ou ele está no cargo errado).

### 5. Data de Admissão Futura (Linha 5)
*   **Como encontrar:** Ao filtrar a coluna Data de Admissão, apareceu o ano **2027**.
*   **Ação:** Pedro Lima tem data de admissão em 01/12/2027. Impossível ele ter sido admitido no futuro.

**Resumo:**
A maioria dos erros estava concentrada na Linha 5 (Pedro Lima é um problema!), mas havia erros espalhados também. Parabéns se achou todos!
