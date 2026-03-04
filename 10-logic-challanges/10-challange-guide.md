# Guia do Desafio 10: Reconciliação de Estoque (Físico vs. Sistema)

Este guia vai te ajudar a resolver o desafio de reconciliação de estoque, uma das tarefas mais comuns e importantes para analistas de dados e financeiros.

===
## 1 - Apresentação do desafio

**O problema:** Chegou o dia do inventário! Você tem duas tabelas de dados:
1.  **Tabela Sistema:** O que o computador diz que a empresa tem em estoque.
2.  **Tabela Física:** O que a equipe do armazém contou nas prateleiras.

Os dados raramente batem perfeitamente. Produtos somem, são digitados errado ou esquecidos.

**Sua missão:** Cruzar essas duas tabelas para identificar:
*   Produtos que estão no sistema mas não foram encontrados no físico (perda total?).
*   Produtos com quantidades diferentes (divergência).
*   Produtos que estão no físico mas não existem no sistema (sobras ou erros de cadastro).

---

## 2 - Tutorial de técnicas e ferramentas

Para quem nunca fez isso, vamos usar o conceito de "Bater listas". Imagine que você tem duas listas de chamada e quer saber quem faltou.

### As Ferramentas (Fórmulas)

1.  **PROCV (VLOOKUP)**: É o "buscador". Você diz: "Pegue esse código SKU aqui, procure na outra tabela, e me traga a quantidade que está lá".
    *   *Sintaxe:* `=PROCV(o_que_procurar; onde_procurar; numero_da_coluna_que_quer; FALSO)`
    *   *Nota:* O "FALSO" no final é vital para exigir uma correspondência exata do código.

2.  **SEERRO (IFERROR)**: O "protetor". Se o PROCV não achar o código, ele retorna um erro feio (`#N/D`). O SEERRO diz: "Se der erro, escreva 'NÃO ENCONTRADO' em vez disso".
    *   *Sintaxe:* `=SEERRO(sua_formula_procv; "Texto se der erro")`

3.  **CORRESP (MATCH) + ÉNÚM (ISNUMBER)**: Uma dupla dinâmica para verificar existência. O CORRESP tenta achar a posição de um item. O ÉNÚM diz VERDADEIRO se ele achou (é número) e FALSO se não achou.

### Excel vs. Google Sheets (Diferenças básicas)
*   **Separador:** No Excel em português, usamos **ponto e vírgula (;)** para separar as partes da fórmula. No Google Sheets (configuração BR), também. Se seu Sheets estiver em inglês/EUA, use **vírgula (,)**.
*   **Nomes:** O Google Sheets aceita as funções em inglês (VLOOKUP, IFERROR) mesmo se o menu estiver em português. O Excel exige o nome no idioma instalado (PROCV, SEERRO).

---

## 3 - O que é esperado ao final

Você deve chegar a um relatório onde:
1.  Na Tabela do Sistema, cada linha mostre a quantidade contada fisicamente ao lado da quantidade teórica.
2.  Uma coluna de "Status" que diga claramente: **"OK"**, **"Divergente"** ou **"Não encontrado"**.
3.  Na Tabela Física, um alerta para itens que **não existem no sistema** (os "fantasmas").

**Sem spoiler do resultado exato**, mas sua planilha vai apontar automaticamente onde estão os problemas para que o chefe possa investigar apenas as exceções.

---

## 4 - Dicas progressivas

Tente resolver sozinho! Se travar, leia uma dica por vez.

**Dica 1: Trazendo a informação de fora**
Comece na **Tabela A (Sistema)**. Crie uma coluna "Qtd Física". Use o `PROCV` usando o **Código do Produto** (SKU) como chave de busca. A matriz de busca deve ser a Tabela B (Física). Lembre-se de travar a matriz com `$` (ex: `$A$2:$C$26`).

**Dica 2: Lidando com o vazio**
Alguns produtos do sistema não serão achados na tabela física. O PROCV vai retornar erro. Envolva sua fórmula inteira com `=SEERRO( ... ; "NÃO ENCONTRADO")`. Assim fica mais limpo.

**Dica 3: Calculando a diferença**
Crie uma coluna "Diferença". É simples matemática: `Sistema - Físico`.
*Problema:* Se o físico for "NÃO ENCONTRADO" (texto), a matemática vai dar erro. Use um `SE` para verificar isso antes de subtrair:
`=SE(celula_fisica="NÃO ENCONTRADO"; "---"; sistema - fisico)`

**Dica 4: Classificando (O "Semaforo")**
Crie uma coluna "Status". Use a função `SE` aninhada (um SE dentro de outro).
*   Se for "NÃO ENCONTRADO" -> Status "Desaparecido"
*   Se a Diferença for 0 -> Status "OK"
*   Caso contrário -> Status "Divergente"

**Dica 5: O caminho inverso (A Pegadinha)**
E se tiver um produto na prateleira (Tabela B) que não está no sistema? O PROCV na Tabela A não vê isso.
Vá na **Tabela B (Física)** e crie uma coluna "Checagem Sistema". Use `CORRESP` para ver se o código daquele item existe na lista do Sistema.

---

<div align="center">
  <h3>🚧 ÁREA DE RESOLUÇÃO E SPOILERS ABAIXO 🚧</h3>
  <p>Continue apenas se já tentou resolver ou se travou completamente.</p>
</div>

<br><br><br>

---

## 5 - Resultado e Passo a Passo

Aqui está como construímos a solução ideal para reconciliação completa.

### Passo 1: Buscar a quantidade física (Na Tabela Sistema)
Na célula D2 (assumindo que Qtd Sistema é C2), insira:

**Excel (PT):**
```excel
=SEERRO(PROCV(A2;Física!$A$2:$C$26;3;FALSO);"NÃO ENCONTRADO")
```
**Google Sheets / Excel (EN):**
```excel
=IFERROR(VLOOKUP(A2,Physical!$A$2:$C$26,3,FALSE),"NOT FOUND")
```
*Explicação:* Busca o código A2 na tabela da aba 'Física'. Se achar, traz a coluna 3 (Qtd). Se não achar, escreve o texto de aviso.

### Passo 2: Calcular a Diferença
Na célula E2:
```excel
=SE(D2="NÃO ENCONTRADO";"—";C2-D2)
```
*Explicação:* Evita erro de cálculo se não houve contagem. Se houve, subtrai Sistema - Físico.

### Passo 3: Classificação Automática
Na célula F2 (Status):
```excel
=SE(D2="NÃO ENCONTRADO";"⚠ Não encontrado";SE(E2=0;"✓ OK";"⚠ Divergente"))
```
*Explicação:* Resolve primeiro o caso mais grave (não encontrado), depois verifica se está perfeito (zero diferença), e o que sobra é divergência.

### Passo 4: O "Pulo do Gato" (Itens fantasmas na Tabela Física)
Muitos esquecem de verificar o inverso. Vá na Tabela Física e use esta fórmula para ver se o item existe no sistema:

**Excel (PT):**
```excel
=SE(ÉNÚM(CORRESP(A2;Sistema!$A$2:$A$26;0));"No sistema";"⚠ SOMENTE FÍSICO")
```
**Google Sheets / Excel (EN):**
```excel
=IF(ISNUMBER(MATCH(A2,System!$A$2:$A$26,0)),"In system","⚠ PHYSICAL ONLY")
```
*Explicação:* `CORRESP` tenta achar o código na lista do sistema. Se achar, retorna um número (a posição). `ÉNÚM` confirma que é um número (Verdadeiro). O `SE` final escreve o aviso se não for encontrado.

**Conclusão do Desafio:**
Com essas colunas, você consegue filtrar rapidamente tudo que não é "OK" e entregar um relatório de anomalias pronto para a auditoria, em vez de conferir linha por linha manualmente.
