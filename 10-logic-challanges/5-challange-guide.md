# Guia do Desafio 5: Comissões Escalonadas

Este guia vai te ajudar a resolver o 5º desafio de lógica. Siga os passos, leia as dicas e tente fazer sozinho antes de ver a resposta!

===

## 1 - O Desafio

**Cenário:** Você trabalha no financeiro de uma empresa e precisa calcular a comissão dos vendedores. A regra não é fixa: quem vende mais, ganha uma porcentagem maior.

**Regras de Comissão:**
*   Vendas acima de R$ 30.000: **15%**
*   Vendas entre R$ 15.001 e R$ 30.000: **12%**
*   Vendas entre R$ 5.001 e R$ 15.000: **8%**
*   Vendas até R$ 5.000: **5%**

**Sua missão:** Criar uma tabela onde você coloca o valor da venda e a planilha calcula automaticamente a porcentagem e o valor da comissão.

---

## 2 - Tutorial Rápido: O Poder do "SE" (IF)

Para este desafio, vamos usar a função **SE** (ou **IF** em inglês). Ela funciona como um porteiro que toma decisões.

**Como funciona um SE simples:**
Imagine uma regra: "Se chover, levo guarda-chuva. Senão, vou de óculos."
Na planilha seria:
`=SE(Clima="Chuva"; "Guarda-chuva"; "Óculos")`

**O Segredo do "SE Aninhado" (Um dentro do outro):**
E se tivermos mais opções? "Se chover, guarda-chuva. Se estiver nublado, casaco. Se fizer sol, óculos."
Você coloca um SE dentro da resposta "senão" do anterior:
`=SE(Clima="Chuva"; "Guarda-chuva"; SE(Clima="Nublado"; "Casaco"; "Óculos"))`

**Diferença Excel x Google Sheets:**
*   **Excel (Português):** Usa ponto e vírgula (`;`) para separar as partes. Ex: `=SE(A1>10; "Maior"; "Menor")`
*   **Google Sheets (ou Excel Inglês):** Costuma usar vírgula (`,`) ou ponto e vírgula dependendo da configuração regional. Se a fórmula der erro, tente trocar `;` por `,`.

---

## 3 - O que é esperado ao final

Você deve ter uma tabela com os vendedores e, ao lado do valor de vendas de cada um, duas colunas calculadas automaticamente:
1.  **% Comissão:** Mostra 5%, 8%, 12% ou 15% dependendo da venda.
2.  **Valor a Receber:** O valor em Reais (Venda x Porcentagem).

Se você mudar o valor da venda, a comissão deve mudar sozinha para a categoria correta!

---

## 4 - Dicas Progressivas

Tente resolver usando uma dica por vez. Se travar, leia a próxima.

**Dica 1: A Ordem Importa**
Quando temos várias condições (maior que 30k, maior que 15k...), o computador lê da esquerda para a direita e **para na primeira verdade que encontrar**.
*   Estratégia recomendada: Comece testando o valor **mais alto** (Maior que 30.000).
*   Por que? Se você testar primeiro "Maior que 5.000", uma venda de 50.000 também é maior que 5.000, e o computador vai dar a comissão errada (8% em vez de 15%).

**Dica 2: Estrutura da Lógica**
Pense assim:
*   É maior que 30.000? Se sim, 15%.
*   (Se não for), é maior que 15.000? Se sim, 12%.
*   (Se não for), é maior que 5.000? Se sim, 8%.
*   (Se não for nada disso), então só sobrou ser menor ou igual a 5.000, então é 5%.

**Dica 3: Escrevendo a fórmula**
Comece com `=SE(Célula>30000; 15%; ...)` e vá colocando os outros SEs no lugar do "valor se falso".

**Dica 4: Parênteses**
Para cada `SE(` que você abriu, você precisa fechar um parêntese no final. Se usar 3 SEs, terminará com `)))`.

---

## 5 - Resultado e Resolução Passo a Passo

⚠️ **Abaixo está a solução completa. Tente fazer antes de olhar!** ⚠️

.
.
.
.
.

### A Solução Lógica

Para resolver, usamos a técnica de "funções aninhadas". Validamos do maior para o menor.

Supondo que o valor da venda está na célula **B2**.

**Fórmula para a Porcentagem:**

**Excel (Português):**
```excel
=SE(B2>30000; 15%; SE(B2>15000; 12%; SE(B2>5000; 8%; 5%)))
```

**Google Sheets / Excel (Inglês):**
```excel
=IF(B2>30000, 15%, IF(B2>15000, 12%, IF(B2>5000, 8%, 5%)))
```

### Explicação do Raciocínio:
1.  **`SE(B2>30000; 15%; ...`**: O Excel pergunta: "Vendeu mais de 30 mil?". Se sim, escreve 15% e **encerra**.
2.  **`... SE(B2>15000; 12%; ...`**: Se não foi maior que 30 mil, ele pergunta: "Mas foi maior que 15 mil?". Se sim, escreve 12%.
3.  **`... SE(B2>5000; 8%; ...`**: Se não, pergunta: "Foi maior que 5 mil?". Se sim, 8%.
4.  **`... 5%)`**: Se não foi nenhuma das anteriores, só pode ser 5%.

### Bônus: Função SES (IFS)
Nas versões mais novas do Excel e no Google Sheets, existe uma função mais limpa chamada `SES` (ou `IFS`), que não precisa abrir um monte de parênteses dentro do outro.

**Excel (PT):** `=SES(B2>30000;15%; B2>15000;12%; B2>5000;8%; VERDADEIRO;5%)`
**Sheets (EN):** `=IFS(B2>30000,15%, B2>15000,12%, B2>5000,8%, TRUE,5%)`

*Nota: O "VERDADEIRO" (ou TRUE) no final serve como um "caso contrário" para pegar tudo que sobrou.*
