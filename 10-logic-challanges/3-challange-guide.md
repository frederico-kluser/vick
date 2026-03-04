# Guia do Desafio 3: Montar um Pedido Automático

## 1. Apresentação do Desafio

Imagine que você trabalha na administração de um restaurante. Você tem duas listas importantes:
1.  **O Cardápio (Catálogo):** Uma lista fixa com códigos (ex: P001), nomes dos pratos e seus preços.
2.  **O Pedido:** Uma tabela onde os garçons anotam os pedidos das mesas.

Atualmente, o garçom precisa escrever o nome do prato e o preço manualmente toda vez que anota um código. Isso demora e gera erros.

**Sua missão:** Criar uma planilha inteligente onde o garçom digita *apenas* o **Código do Produto** e a **Quantidade**. O Excel/Google Sheets deve preencher automaticamente o **Nome do Produto** e o **Preço Unitário**, além de calcular o **Subtotal**.

---

## 2. Tutorial de Técnicas e Ferramentas

Para este desafio, usaremos a função mais famosa para "buscar coisas" em planilhas: o **PROCV** (no Excel) ou **VLOOKUP** (no Google Sheets/Inglês).

### O que o PROCV faz?
Pense nele como um bibliotecário. Você dá um código a ele (ex: "P001") e diz: "Vá até a estante de produtos, procure este código na primeira coluna e me traga o que estiver escrito na coluna ao lado".

### Estrutura da Fórmula
A função precisa de 4 informações, separadas por ponto e vírgula (`;`) no Excel em português ou vírgula (`,`) no Google Sheets:

1.  **O que procurar?** (O código que o garçom digitou no pedido).
2.  **Onde procurar?** (A tabela inteira do cardápio, selecionando desde o código até o preço).
3.  **Qual coluna retornar?** (O número da coluna que você quer trazer: 1 para código, 2 para nome, 3 para preço).
4.  **Procura exata?** (Sempre coloque `FALSO` ou `0` para dizer que você quer exatamente aquele código, não algo parecido).

### Diferenças Importantes
*   **Excel (Português):** Usa `PROCV` e separa com `;`
    *   Ex: `=PROCV(A2; D2:F10; 2; FALSO)`
*   **Google Sheets / Excel (Inglês):** Usa `VLOOKUP` e separa com `,`
    *   Ex: `=VLOOKUP(A2, D2:F10, 2, FALSE)`

### Travando a Tabela ($)
Quando você arrastar a fórmula para baixo, a referência da tabela de produtos vai descer junto e estragar a busca. Para evitar isso, usamos o cifrão `$` antes das letras e números da tabela (ex: `$A$2:$C$20`). Isso fixa a tabela no lugar.

---

## 3. O que é esperado ao final

Ao terminar, sua tabela de pedidos deve funcionar assim:
*   Você digita `P001` na coluna de Código.
*   Magicamente, a célula ao lado mostra "Hambúrguer".
*   A próxima célula mostra "R$ 25,90".
*   Se você digitar a quantidade `2`, a última coluna calcula o total sozinha.
*   Se você mudar o código para `P002`, o nome e o preço mudam automaticamente para "Pizza".

---

## 4. Dicas Progressivas

**Dica 1: Preparando o terreno**
Crie uma tabela pequena em algum lugar (ou em outra aba) com uns 3 produtos para servir de cardápio.
Colunas: Código | Produto | Preço.
Dados ex: P001 | Burger | 25.00

**Dica 2: A primeira busca (Nome)**
Na tabela de pedidos, clique onde deve aparecer o nome do produto. Comece sua fórmula `PROCV`.
*   O valor procurado é a célula do código *nesta linha do pedido*.
*   A matriz/tabela é o seu cardápio inteiro.

**Dica 3: Trazendo a coluna certa**
O cardápio tem 3 colunas:
1. Código
2. Produto
3. Preço
Se você quer o nome do produto, qual número deve colocar no índice da coluna?

**Dica 4: Não esqueça do "FALSO"**
Se você não escrever `FALSO` (ou `0`) no final da fórmula, o Excel pode trazer o produto errado se a lista não estiver em ordem alfabética.

**Dica 5: Buscando o Preço**
A fórmula para o preço é quase idêntica à do nome. O que muda? Apenas o número da coluna que você quer trazer.

**Dica 6: O cálculo final**
Para o subtotal, você não precisa de PROCV. É uma conta matemática simples: `Preço Unitário * Quantidade`. Use o asterisco `*` para multiplicar.

---

⬇️ **A SOLUÇÃO ESTÁ LOGO ABAIXO** ⬇️
.
.
.
.
.
.
.

---

## 5. Resultado e Passo a Passo

Aqui está como construir a solução ideal.

### Passo 1: O Cardápio
Vamos supor que seu cardápio (Lista de Produtos) esteja no intervalo **F2:H5** (para simplificar, na mesma folha).
*   F: Código
*   G: Produto
*   H: Preço

### Passo 2: A Fórmula do Produto
Na célula **B2** (onde deve aparecer o nome do produto do primeiro pedido), usamos:

**Excel (PT-BR):**
`=PROCV(A2; $F$2:$H$5; 2; FALSO)`

**Google Sheets / Inglês:**
`=VLOOKUP(A2, $F$2:$H$5, 2, FALSE)`

**Explicação:**
*   `A2`: Olha para o código digitado (ex: P001).
*   `$F$2:$H$5`: Busca nesse intervalo (os cifrões `$` garantem que a tabela não "saia do lugar" ao copiar a fórmula).
*   `2`: Traz a informação da **segunda coluna** (o Nome do Produto).
*   `FALSO`: Garante que só traga se achar o código exato.

### Passo 3: A Fórmula do Preço
Na célula **C2** (Preço Unitário), a lógica é a mesma, só muda a coluna:

**Excel (PT-BR):**
`=PROCV(A2; $F$2:$H$5; 3; FALSO)`

**Google Sheets / Inglês:**
`=VLOOKUP(A2, $F$2:$H$5, 3, FALSE)`

*   Note que mudamos o `2` para `3`, pois o preço está na terceira coluna do cardápio.

### Passo 4: O Subtotal
Na célula **E2** (Subtotal), multiplicamos o preço encontrado pela quantidade digitada:

`=C2 * D2` (Preço * Quantidade)

Agora, basta arrastar essas fórmulas para as linhas de baixo, e seu sistema de pedidos automático está pronto!
