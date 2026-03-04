# Guia do Desafio 2: Caçando Duplicatas

Este arquivo é um guia auxiliar para você realizar o Desafio 2. Ele contém explicações, dicas e, no final, a resposta completa. Tente fazer sozinho antes de olhar a solução!

---

## 1. O Desafio

**Cenário:** Você trabalha em uma loja online e recebeu uma lista com **50 endereços de e-mail** de clientes. A suspeita é que alguns clientes se cadastraram mais de uma vez para ganhar cupons de desconto em dobro.

**Sua missão:**
1.  Identificar quantas vezes cada e-mail aparece na lista.
2.  Criar uma coluna avisando automaticamente se o e-mail é "Duplicado" ou "Único".
3.  Descobrir quantos clientes **reais** (únicos) existem na lista.

---

## 2. Tutorial Rápido (Para quem nunca usou planilhas)

Para resolver este problema, vamos usar duas ferramentas mágicas das planilhas:

### A Função "Contar Se" (CONT.SE / COUNTIF)
Imagine que você tem uma cesta de frutas e quer saber quantas "Maçãs" existem. Você pega uma fruta, olha se é maçã, e conta. O Excel faz isso com a função `CONT.SE`.
Ela pede duas coisas:
1.  **Onde procurar?** (A cesta inteira).
2.  **O que procurar?** (A palavra "Maçã").

### A Âncora ($) - O segredo dos profissionais
Quando você cria uma fórmula para a primeira linha e a "arrasta" para baixo para aplicar nas outras, o Excel tenta ser inteligente e desce as referências junto.
*   Se você mandou ele olhar as linhas 2 até 51, na próxima ele vai olhar 3 até 52, depois 4 até 53...
*   Isso é ruim! A lista de e-mails é fixa (da linha 2 até a 51). Não queremos que ela ande.
*   **Solução:** Colocamos um cifrão `$` antes da letra e do número (ex: `$B$2:$B$51`). Isso "trava" a lista. Chamamos isso de **Referência Absoluta**.

---

## 3. O que é esperado ao final

Você terá uma tabela mais ou menos assim (os valores são exemplos):

| E-mail | Contagem | Status |
| :--- | :--- | :--- |
| ana@email.com | 1 | Único |
| joao@email.com | 2 | Duplicado |
| joao@email.com | 2 | Duplicado |

E deverá ter um número final respondendo: "Existem X e-mails únicos".

---

## 4. Dicas Progressivas

Tente seguir uma dica por vez. Se travar, leia a próxima.

**Dica 1:**
Comece na coluna C (ao lado do e-mail). Você vai precisar da função `CONT.SE` (em português) ou `COUNTIF` (em inglês/Google Sheets).

**Dica 2:**
A estrutura da fórmula é: `=CONT.SE(intervalo_onde_procurar; o_que_procurar)`.
*   O *intervalo* é a lista completa de e-mails (do primeiro ao último).
*   O *critério* é o e-mail que está na mesma linha da sua fórmula.

**Dica 3 (Crucial):**
Antes de arrastar a fórmula para baixo, lembre-se da "Âncora". Selecione a parte da fórmula que se refere à lista completa e aperte a tecla `F4` (ou digite os `$` manualmente). A referência ao e-mail individual **não** deve ter `$`, pois ela precisa mudar linha a linha.

**Dica 4:**
Para a coluna "Status" (Coluna D), use a função `SE` (`IF`). A lógica é: "Se o número na coluna da contagem for maior que 1, escreva 'Duplicado', senão escreva 'Único'".
Estrutura: `=SE(teste_lógico; valor_se_verdadeiro; valor_se_falso)`.

**Dica 5 (Para o total):**
Para saber quantos únicos existem, você pode usar uma função moderna do Google Sheets chamada `UNIQUE` junto com `COUNTA` (Contar Valores), ou simplesmente filtrar a coluna "Status" para mostrar apenas os "Únicos" e ver a contagem no rodapé da planilha.

---

⬇️ **A SOLUÇÃO ESTÁ LOGO ABAIXO** ⬇️
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

## 5. Resolução Passo a Passo

Aqui está como chegar no resultado:

### Passo 1: Contar as ocorrências (Coluna C)
1.  Clique na célula **C2**.
2.  Digite a fórmula:
    *   **Excel (PT):** `=CONT.SE($B$2:$B$51; B2)`
    *   **Sheets/Excel (EN):** `=COUNTIF($B$2:$B$51, B2)`
    *   *Nota: O intervalo `$B$2:$B$51` representa sua lista fixa de e-mails. O `B2` é o e-mail daquela linha.*
3.  Aperte Enter.
4.  Clique no quadradinho no canto inferior direito da célula C2 e arraste até o final da lista (ou dê um clique duplo nele).

### Passo 2: Classificar (Coluna D)
1.  Clique na célula **D2**.
2.  Digite a fórmula:
    *   **Excel (PT):** `=SE(C2>1; "Duplicado"; "Único")`
    *   **Sheets/Excel (EN):** `=IF(C2>1, "Duplicado", "Único")`
3.  Arraste para baixo até o fim da lista.

### Passo 3: Contagem Final
Para responder quantos e-mails únicos existem:

**Opção Simples (Visual):**
1.  Selecione a coluna D (Status).
2.  Ative o "Filtro" (ícone de funil).
3.  Filtre para mostrar apenas "Único".
4.  Selecione os dados filtrados e olhe a contagem no canto inferior direito da tela.

**Opção "Pro" (Google Sheets):**
Em uma célula vazia, digite: `=COUNTA(UNIQUE(B2:B51))`
Isso conta quantos valores únicos existem na lista original.

**Resultado Esperado:**
Ao finalizar, você verá que os e-mails que aparecem 2 ou mais vezes estarão marcados como "Duplicado", permitindo que você limpe sua base de dados facilmente!
