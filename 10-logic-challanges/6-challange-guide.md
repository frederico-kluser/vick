# Guia do Desafio 6: Planejar entregas com cálculos de dias úteis

## 1. Apresentação do Desafio

Neste desafio, você assumirá o papel de um gerente de logística de uma editora. Seu objetivo é calcular a data prevista de entrega de pedidos de livros, levando em conta que o prazo varia conforme a região do Brasil e que as entregas ocorrem apenas em dias úteis (ignorando finais de semana e feriados).

Além disso, você precisará monitorar quantos dias faltam para a entrega e se os pedidos estão dentro do prazo ou atrasados em relação à data de hoje.

**O que você vai praticar:**
*   **Lógica condicional:** Definir prazos diferentes baseados na região (Se Região X, então Prazo Y).
*   **Cálculos com datas:** Somar dias úteis a uma data para encontrar o prazo final.
*   **Comparação temporal:** Calcular dias restantes e verificar atrasos em tempo real.

---

## 2. Tutorial de Técnicas e Ferramentas

Para quem nunca mexeu com datas no Excel ou Google Sheets, aqui vão os conceitos essenciais de forma simples:

### Datas são Números
Tanto no Excel quanto no Sheets, as datas são armazenadas internamente como números.
*   Exemplo: `10/03/2026` pode aparecer como `46091`.
*   **Como resolver:** Se ver um número estranho onde deveria haver uma data, selecione a célula e mude a formatação (geralmente na barra superior) para "Data Abreviada" ou "Data".

### Função SE (IF)
Usada para o computador tomar decisões por você.
*   Conceito: "Se isso for verdade, faça X; senão, faça Y".
*   Estrutura: `=SE(teste; valor_se_verdadeiro; valor_se_falso)`

### Função DIATRABALHO (WORKDAY)
Esta função é mágica para logística. Ela soma dias a uma data inicial, mas **pula automaticamente sábados e domingos**. Você também pode dar uma lista de feriados para ela pular.
*   Estrutura: `=DIATRABALHO(data_inicial; dias_para_somar; [lista_de_feriados])`

### Função DIATRABALHOTOTAL (NETWORKDAYS)
Conta quantos dias de trabalho existem **entre** duas datas. Útil para responder "quantos dias úteis faltam?".
*   Estrutura: `=DIATRABALHOTOTAL(data_inicial; data_final; [lista_de_feriados])`

### Função HOJE (TODAY)
Retorna a data atual do seu computador. Ela muda sozinha amanhã!
*   Estrutura: `=HOJE()` (Não coloque nada dentro dos parênteses).

### Dica de Ouro: Travando Células ($)
Quando você selecionar a lista de feriados na sua fórmula (ex: `A2:A10`), e depois arrastar a fórmula para baixo, o Excel vai mudar para `A3:A11`, `A4:A12`... e isso vai estragar o cálculo.
*   **Solução:** Use o cifrão para "trancar" a referência. Exemplo: `$A$2:$A$10`. Assim, ao arrastar, a lista de feriados permanece fixa.

---

## 3. O que é esperado ao final

Você deverá ter uma tabela onde, para cada pedido, o sistema calcula automaticamente:
1.  **Prazo em dias:** (ex: 5, 8 ou 12) baseado na região digitada.
2.  **Data Prevista:** A data exata que o cliente receberá o produto.
3.  **Dias Restantes:** Quantos dias úteis faltam de hoje até a entrega.
4.  **Status:** Uma mensagem dizendo "Atrasado" ou "No prazo".

---

## 4. Dicas Progressivas

Tente fazer sozinho! Se travar, leia uma dica por vez.

**Dica 1: Organização**
Crie uma tabela com colunas: `Pedido`, `Data do Pedido`, `Região`.
Em um canto separado da planilha (ou outra aba), faça uma lista com as datas dos feriados.

**Dica 2: Calculando o Prazo (A Lógica)**
Use a função `SE`. Você terá que colocar um "SE dentro de outro SE" (aninhado).
*   Raciocínio: SE a região for "Sudeste", então 5. SENÃO, SE for "Sul", então 5. SENÃO... e assim por diante.
*   *Simplificação:* Se quiser, pode usar a lógica "Se for Norte é 12, se for Nordeste/Centro-Oeste é 8, resto é 5".

**Dica 3: Calculando a Data de Entrega**
Use a função `DIATRABALHO`.
*   Data inicial = Data do Pedido.
*   Dias = A célula onde você calculou o prazo na Dica 2.
*   Feriados = Selecione sua lista de feriados e lembre de trancar com `$` (F4 no teclado).

**Dica 4: Contando Dias Restantes**
Use `DIATRABALHOTOTAL`.
*   Data inicial = `HOJE()`
*   Data final = A Data de Entrega que você calculou na Dica 3.
*   Isso vai te dar um número positivo (dias que faltam) ou negativo (dias que já passaram).

**Dica 5: Status de Atraso**
Use um `SE` simples para comparar datas.
*   Lógica: SE a data de `HOJE()` for maior que a `Data de Entrega`, escreva "Atrasado". Caso contrário, "No prazo".

---

## 5. Resultado e Passo a Passo

Abaixo, veja como chegar na solução final.

!!! ATENÇÃO: SPOILERS ABAIXO !!!
.
.
.
.
.

### Passo 1: O Prazo por Região
Supondo que a Região está na célula **C2**.
Você precisa traduzir a regra de negócio para fórmula.

**Fórmula (Excel/Sheets PT):**
`=SE(C2="Sudeste"; 5; SE(C2="Sul"; 5; SE(C2="Nordeste"; 8; SE(C2="Centro-Oeste"; 8; 12))))`

*Explicação:* O Excel verifica a primeira condição. Se for falsa, passa para o próximo `SE`. Se não for nenhuma das anteriores (Sul, Sudeste, Nordeste, Centro-Oeste), ele assume que é Norte (o último valor, 12).

### Passo 2: A Data de Entrega
Supondo:
*   Data do Pedido em **B2**
*   Prazo (calculado acima) em **D2**
*   Lista de Feriados em **G2:G10**

**Fórmula:**
`=DIATRABALHO(B2; D2; $G$2:$G$10)`

*Explicação:* Parte da data do pedido (B2), avança o número de dias úteis (D2) e pula qualquer data que estiver na lista G2:G10.

### Passo 3: Dias Úteis Restantes
Queremos saber a distância entre Hoje e a Entrega.
Supondo Data de Entrega calculada em **E2**.

**Fórmula:**
`=DIATRABALHOTOTAL(HOJE(); E2; $G$2:$G$10)`

*   Se o resultado for positivo: Faltam X dias.
*   Se for negativo: A data já passou há X dias.

### Passo 4: Status (Atrasado ou Não)
Comparação simples.

**Fórmula:**
`=SE(HOJE() > E2; "Atrasado"; "No prazo")`

### Tabela Final Exemplo

| Pedido | Data Pedido | Região | Prazo (Dias) | Entrega Prevista | Dias Restantes | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| #101 | 10/03/2026 | Sudeste | 5 | 17/03/2026 | 3 | No prazo |
| #102 | 12/03/2026 | Nordeste | 8 | 24/03/2026 | 8 | No prazo |

*Nota: Os valores de "Dias Restantes" e "Status" mudarão dependendo do dia em que você abrir a planilha!*
