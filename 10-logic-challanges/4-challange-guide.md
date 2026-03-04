# Guia do Desafio 4: Decifrar códigos de produto

## 1. Apresentação do Desafio

Você recebeu uma lista de códigos de produtos de uma empresa. Esses códigos não são aleatórios; eles seguem um padrão lógico estrito: **`CAT-CID-0000`**.

Isso significa que cada código contém três informações escondidas:
1.  **Categoria (CAT):** Os 3 primeiros caracteres (ex: `ELE` para Eletrônicos).
2.  **Cidade (CID):** Os caracteres do meio, nas posições 5, 6 e 7 (ex: `SPO` para São Paulo).
3.  **Número Sequencial:** Os 4 últimos dígitos.

**Sua missão:**
Sua tarefa é "quebrar" (ou *parsear*) esses códigos e preencher três novas colunas na tabela: **Categoria**, **Cidade** e **Número**.

---

## 2. Ferramentas e Técnicas (Tutorial Rápido)

Para realizar este desafio, você precisará de "tesouras" digitais. No Excel e Google Sheets, essas tesouras são as **Funções de Texto**.

Imagine que o texto dentro de uma célula é uma tira de papel com letras escritas em quadradinhos numerados.

| E | L | E | - | S | P | O | - | 0 | 0 | 4 | 2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12|

Aqui estão as ferramentas que você vai usar:

### A. Pegar o começo do texto (Esquerda)
Se você quer cortar as primeiras letras da esquerda para a direita.
*   **Excel (PT-BR):** `=ESQUERDA(texto; num_caracteres)`
*   **Google Sheets / Excel (EN):** `=LEFT(text, num_chars)`
*   *Exemplo:* `=ESQUERDA("BANANA"; 3)` resulta em "BAN".

### B. Pegar o final do texto (Direita)
Se você quer cortar as últimas letras da direita para a esquerda.
*   **Excel (PT-BR):** `=DIREITA(texto; num_caracteres)`
*   **Google Sheets / Excel (EN):** `=RIGHT(text, num_chars)`
*   *Exemplo:* `=DIREITA("BANANA"; 3)` resulta em "ANA".

### C. Pegar o meio do texto (Extrair Texto)
Essa é a mais cirúrgica. Você diz onde começar o corte e quantos caracteres quer pegar.
*   **Excel (PT-BR):** `=EXT.TEXTO(texto; num_inicial; num_caracteres)`
*   **Google Sheets / Excel (EN):** `=MID(text, start_num, num_chars)`
*   **Importante:** A contagem começa no 1 (primeira letra).

---

## 3. O que é esperado ao final

Ao terminar, você terá sua tabela original expandida. Para cada código de produto, você terá as informações separadas e organizadas.

**Exemplo do resultado visual (sem fórmulas):**

| Código | Categoria | Cidade | Número |
| :--- | :--- | :--- | :--- |
| ELE-SPO-0042 | ELE | SPO | 0042 |

**Bônus:** Se você conseguir, tente criar uma coluna extra que traduza a sigla "ELE" para "Eletrônicos", "ROU" para "Roupas", etc.

---

## 4. Dicas Progressivas

Se estiver travado, leia uma dica de cada vez.

**Dica 1: Olhando para a esquerda**
Para a coluna **Categoria**, você precisa apenas das 3 primeiras letras. Qual função pega caracteres a partir do início (esquerda) da célula?

**Dica 2: Atenção aos separadores**
Para a coluna **Cidade**, observe onde ela começa.
`C-A-T-(-)-C...`
1-2-3-4-5...
A cidade começa na posição 5. E ela tem 3 letras. Use a função que extrai texto do meio.

**Dica 3: O final é simples**
Para a coluna **Número**, você precisa dos 4 últimos dígitos. Não importa o tamanho do texto que vem antes, você sempre quer os 4 finais. Use a função que olha para a direita.

**Dica 4 (Bônus): Traduzindo**
Para transformar "ELE" em "Eletrônicos", você precisará da função `SE` (ou `IF`).
A lógica seria: "Se a categoria for igual a 'ELE', escreva 'Eletrônicos'; senão, se for 'ROU'..."

---

<div align="center">
  <br/><br/>
  🛑 <strong>PARE AQUI SE NÃO QUISER VER A RESPOSTA</strong> 🛑
  <br/><br/>
  Role para baixo para ver a solução passo a passo.
  <br/><br/>
  👇
  <br/><br/>
</div>

---

## 5. Resultado e Solução Passo a Passo

Aqui está como resolver o mistério dos códigos.

### Passo 1: Extraindo a Categoria
Na célula B2 (coluna Categoria), digite:

*   **Excel (PT-BR):** `=ESQUERDA(A2; 3)`
*   **Google Sheets / Excel (EN):** `=LEFT(A2, 3)`

*Explicação:* "Excel, olhe para a célula A2 e me dê os 3 primeiros caracteres da esquerda."

### Passo 2: Extraindo a Cidade
Na célula C2 (coluna Cidade), digite:

*   **Excel (PT-BR):** `=EXT.TEXTO(A2; 5; 3)`
*   **Google Sheets / Excel (EN):** `=MID(A2, 5, 3)`

*Explicação:* "Excel, olhe para A2. Pule até a posição 5 (onde começa a cidade) e pegue 3 caracteres a partir dali."

### Passo 3: Extraindo o Número
Na célula D2 (coluna Número), digite:

*   **Excel (PT-BR):** `=DIREITA(A2; 4)`
*   **Google Sheets / Excel (EN):** `=RIGHT(A2, 4)`

*Explicação:* "Excel, pegue os 4 últimos caracteres da direita da célula A2."

### Passo Bônus: Tradução (Avançado)
Se você quis traduzir as categorias, usou uma lógica condicional. Supondo que a categoria extraída esteja na coluna B (célula B2):

*   **Excel (PT-BR):** `=SE(B2="ELE";"Eletrônicos"; SE(B2="ROU";"Roupas"; "Alimentos"))`
*   **Google Sheets / Excel (EN):** `=IF(B2="ELE", "Electronics", IF(B2="ROU", "Clothing", "Food"))`

*Lógica:* "Se B2 for 'ELE', escreva Eletrônicos. Se não for, verifique se é 'ROU'. Se for, escreva Roupas. Se não for nem um nem outro, assumimos que é Alimentos."
