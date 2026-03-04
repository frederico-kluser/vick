# Desafio 8: Analisar a distribuição do orçamento familiar

===
1 - Apresentação do desafio e dizer o que ele pede

Neste desafio, você analisará as finanças de uma família que deseja entender para onde o dinheiro está indo. Eles registraram todas as despesas do mês atual e do mês anterior e querem saber:
1. Qual porcentagem do salário é gasta em cada categoria.
2. Como os gastos variaram de um mês para o outro (aumentaram ou diminuíram?).
3. Se a distribuição do orçamento segue a regra 50/30/20 (50% para necessidades, 30% para desejos e 20% para investimentos).

**Seu objetivo:** Criar uma tabela que mostre essas informações de forma clara e calcular os totais por tipo de despesa para verificar se a regra 50/30/20 está sendo cumprida.

===
2 - Tutorial de tecnicas e ferramentas utilizadas

Para este desafio, usaremos conceitos fundamentais de análise de dados em planilhas. Não se preocupe se nunca usou, é mais simples do que parece!

*   **Cálculo de Porcentagem (Parte pelo Todo):** Para saber quanto uma parte representa do todo, dividimos a parte pelo total.
    *   *Exemplo:* Se gastei 50 de um salário de 100, a conta é `50 / 100 = 0,5` (ou 50%).
    *   *Dica:* Use o botão de porcentagem `%` na barra de ferramentas para formatar o número.

*   **Referências Absolutas ($):** O "cifrão" serve para travar uma célula na fórmula.
    *   *Por que usar?* Quando você arrasta uma fórmula para baixo, o Excel/Sheets ajusta as células automaticamente (A1 vira A2, A3...). Se você quer fixar uma célula (como o valor do Salário Total, que é o mesmo para todas as contas), use o cifrão antes da letra e do número (ex: `$B$10`). Assim, ela não muda ao copiar a fórmula.
    *   *Atalho:* Pressione `F4` após selecionar a célula na fórmula.

*   **SOMASE (SUMIF):** Uma função que soma valores apenas se eles atenderem a uma condição.
    *   *Estrutura:* `=SOMASE(onde_procurar_o_tipo; qual_tipo_procurar; onde_estão_os_valores_para_somar)`
    *   *No Google Sheets e Excel em português:* `SOMASE`
    *   *No Excel em inglês/Sheets em inglês:* `SUMIF`

===
3 - Dizer o que é esperado ao final

Você terá uma tabela detalhada onde, para cada despesa (como Aluguel ou Mercado), saberá exatamente quantos % do salário ela consome e se o valor aumentou ou diminuiu em relação ao mês passado. 
Além disso, terá um pequeno quadro de resumo mostrando se a família está gastando muito em "Desejos" ou "Necessidades" comparado à meta deles (50/30/20).

===
4 - Dicas progressivas para o desafio

**Dica 1: Preparação**
Copie a tabela de dados do desafio para sua planilha. Certifique-se de que o valor do **Salário Líquido** (R$ 6.500) esteja em uma célula separada e fácil de acessar (por exemplo, na célula B11, logo abaixo dos totais).

**Dica 2: Calculando a % do Salário**
Para a primeira despesa (Aluguel), a fórmula é uma divisão simples: `Valor do Aluguel / Salário Líquido`. Lembre-se de formatar a célula como Porcentagem (%).

**Dica 3: Travando o Salário**
Se você arrastar a fórmula da Dica 2 para baixo, vai dar erro! Isso acontece porque a referência do salário "desce" junto para uma célula vazia. Volte na primeira fórmula e coloque cifrões na célula do salário (ex: `$B$11`) para travá-la. Agora pode arrastar.

**Dica 4: Variação Mês a Mês**
Para saber quanto variou, a lógica é comparar a diferença com o valor original: `(Valor Atual - Valor Anterior) / Valor Anterior`. Isso mostra o crescimento ou queda percentual.

**Dica 5: Resumo por Tipo (A regra 50/30/20)**
Crie uma tabelinha separada com os tipos: Necessidade, Desejo, Investimento. Use a função `SOMASE` para somar todos os valores da tabela principal que tenham o tipo "Necessidade", depois "Desejo", etc. Depois, divida esses totais pelo Salário Líquido para ver as grandes porcentagens.

===
5 - Resultado e como ele foi obtido com o passo a passo

**⚠️ ALERTA DE SPOILER: A SOLUÇÃO ESTÁ LOGO ABAIXO ⚠️**

---
---
---

### Passo a Passo da Solução

**Passo 1: Organizar os Dados**
Suponha que seus dados estejam organizados assim:
*   Coluna A: Categoria (A2: Aluguel...)
*   Coluna B: Mês Atual (B2: 1800...)
*   Coluna C: Mês Anterior (C2: 1800...)
*   Coluna D: Tipo (D2: Necessidade...)
*   Célula **B11**: Salário Líquido (6500)

**Passo 2: Calcular % do Salário (Coluna E)**
Na célula E2 (ao lado do Tipo), digite a fórmula:
`=B2/$B$11`
*   *O que faz:* Divide o gasto de Aluguel (B2) pelo Salário Total fixo ($B$11).
*   *Ação:* Aperte Enter, clique na célula novamente, clique no botão `%` e arraste a alça de preenchimento até o final da tabela.

**Passo 3: Calcular Variação Mês a Mês (Coluna F)**
Na célula F2, digite:
`=(B2-C2)/C2`
*   *O que faz:* Calcula a diferença entre o mês atual e o anterior `(B2-C2)` e divide pelo valor anterior `C2` para achar a proporção.
*   *Ação:* Formate como % e arraste para baixo.
    *   *Nota:* Valores negativos indicam economia (o gasto diminuiu).

**Passo 4: Criar o Resumo (Regra 50/30/20)**
Crie uma nova tabela ao lado:
*   H2: Necessidade
*   H3: Desejo
*   H4: Investimento

Na célula I2 (Total Atual), use o SOMASE:
*   **Em Português:** `=SOMASE($D$2:$D$10; H2; $B$2:$B$10)`
*   **Em Inglês:** `=SUMIF($D$2:$D$10, H2, $B$2:$B$10)`
*   *Explicação:*
    1. `$D$2:$D$10`: Onde procurar o tipo (coluna Tipo).
    2. `H2`: O critério (a palavra "Necessidade").
    3. `$B$2:$B$10`: Onde somar os valores (coluna Mês Atual).

Repita para "Desejo" e "Investimento".

**Passo 5: Analisar o Resultado**
Divida o total encontrado em cada tipo pelo Salário Líquido (`=I2/$B$11`) para ver a porcentagem real da categoria.

**Resultado Final Esperado:**
*   **Necessidades:** R$ 3.750 (**57,7%**) -> *Acima do ideal de 50%.*
*   **Desejos:** R$ 1.330 (**20,5%**) -> *Abaixo do limite de 30% (ótimo).*
*   **Investimentos:** R$ 500 (**7,7%**) -> *Muito abaixo da meta de 20%.*

**Conclusão:** A família precisa reduzir as Necessidades e aumentar os Investimentos para atingir o equilíbrio financeiro.
