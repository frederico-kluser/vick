# Guia do Desafio 7: Mapa de Calor de Vendas

===
1 - Apresentação do desafio e dizer o que ele pede
2 - Tutorial de tecnicas e ferramentas utilizadas (bem simples para alguem que nunca usou excell/google sheets)
3 - Dizer o que é esperado ao final (sem spoiler do resultado)
4 - Dicas progressivas para o desafio
5 - Resultado e como ele foi obtido com o passo a passo
===

## 1. O Desafio: Visualizando Padrões de Vendas

Você é o gerente regional de uma rede de cafeterias com 6 filiais. Você recebeu uma tabela com as vendas diárias de uma semana inteira, mas é difícil tirar conclusões olhando apenas para um monte de números.

**Seu objetivo:** Transformar essa tabela "chata" em um **mapa de calor** colorido que revele instantaneamente:
1. Quais filiais vendem mais.
2. Quais dias são mais fracos.
3. Se alguma filial tem um comportamento estranho (vende muito pouco em certos dias).

Para isso, usaremos a **Formatação Condicional**, uma ferramenta que muda a cor das células automaticamente baseada no valor que está dentro delas.

---

## 2. Ferramentas: Formatação Condicional para Iniciantes

A Formatação Condicional é como um "marcador de texto automático". Em vez de você pintar as células manualmente, o Excel/Google Sheets faz isso para você seguindo regras que você define.

### No Excel:
Tudo acontece na aba **Página Inicial** (Home), botão **Formatação Condicional**.
*   **Escalas de Cor:** Pinta todas as células selecionadas com um gradiente (ex: do vermelho para o verde) dependendo do valor. O menor valor fica vermelho, o maior verde, e os médios ficam em tons de laranja/amarelo.
*   **Barras de Dados:** Cria uma pequena barra de progresso dentro da célula, proporcional ao valor. Ótimo para comparar totais visualmente.
*   **Regras de Realce:** Permite criar regras específicas como "Pinte de amarelo se o valor for menor que 1000".

### No Google Sheets:
Tudo acontece no menu **Formatar > Formatação condicional**.
*   Ao abrir o painel lateral, você tem duas abas: 
    *   **Cor única:** Para regras específicas (como "menor que 1000").
    *   **Escala de cores:** Para criar o gradiente (mapa de calor).

---

## 3. O que esperar ao final

Ao terminar, você não terá mais apenas números pretos no fundo branco. Sua tabela será visualmente rica e informativa:
*   As vendas altas estarão em tons de **verde**.
*   As vendas baixas estarão em tons de **vermelho**.
*   Os dias com vendas críticas (abaixo de R$ 1.000) estarão destacados em **amarelo com negrito**, chamando sua atenção imediatamente para o problema.
*   Você conseguirá ver padrões claros, como filiais que "morrem" no fim de semana e outras que "bombam", apenas olhando para as cores.

---

## 4. Dicas Progressivas

Se você travou, tente seguir estas dicas na ordem:

**Dica 1: Prepare os dados**
Copie a tabela abaixo para sua planilha (digite ou copie e cole). Certifique-se de que os valores sejam entendidos como números (não coloque "R$" manualmente digitando, use a formatação de moeda do próprio programa).

| Filial       | Seg   | Ter   | Qua   | Qui   | Sex   | Sáb   | Dom   |
|-------------|-------|-------|-------|-------|-------|-------|-------|
| Centro      | 2800 | 2650 | 2900 | 3100 | 3500 | 4200 | 3800 |
| Shopping    | 3200 | 3100 | 3000 | 3300 | 4000 | 5500 | 5200 |
| Bairro Sul  | 1200 | 1100 | 1300 | 1250 | 1800 | 2100 | 1900 |
| Aeroporto   | 4100 | 4000 | 3800 | 4200 | 4500 | 3900 | 3700 |
| Universidade| 2500 | 2400 | 2600 | 2700 | 2200 | 800   | 600   |
| Praia       | 1500 | 1400 | 1600 | 1500 | 2800 | 4800 | 5000 |

**Dica 2: A Escala de Cores**
Selecione APENAS os números das vendas (de B2 até H7, ou onde você colou). Não selecione os nomes das filiais nem os cabeçalhos (dias da semana).
*   **Excel:** Formatação Condicional > Escalas de Cor > A primeira opção (Verde - Amarelo - Vermelho).
*   **Sheets:** Formatar > Formatação condicional > Aba "Escala de cores" > Preview "Verde para Vermelho" (pode precisar inverter se o padrão for vermelho para verde).

**Dica 3: Totais Semanais**
Crie uma nova coluna chamada "Total Semanal" ao lado de "Dom". Use a função `=SOMA(B2:H2)` para somar a linha da primeira filial e arraste para baixo para as outras.
Agora, selecione esses totais e aplique **Barras de Dados** (Excel) ou deixe sem (o Sheets não tem Barras de Dados nativas tão fáceis no menu, mas você pode usar a função `SPARKLINE` se quiser avançar, mas foque na Escala de Cores por enquanto).

**Dica 4: A Regra do "Alerta Amarelo"**
Selecione novamente os números das vendas diárias (a matriz principal).
*   **Excel:** Formatação Condicional > Realçar Regras das Células > É menor do que... > Digite 1000 > Escolha "Preenchimento Amarelo e Texto Amarelo Escuro" (ou personalizado).
*   **Sheets:** Adicionar outra regra > "É menor que" > 1000 > Estilo de formatação: Fundo amarelo, Negrito.

---

⬇️ **SOLUÇÃO E RESULTADO ABAIXO** ⬇️
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
## 5. Solução Passo a Passo e Análise

### Como fazer:

1.  **Copiar os dados:** Insira os dados na planilha conforme a tabela da Dica 1.
2.  **Escala de Cores (O Mapa de Calor):**
    *   Selecione o intervalo de vendas (ex: B2:H7).
    *   **Excel:** Vá em `Página Inicial > Formatação Condicional > Escalas de Cor` e escolha a escala `Verde-Amarelo-Vermelho`. Isso fará com que os maiores valores fiquem verdes e os menores vermelhos.
    *   **Sheets:** Vá em `Formatar > Formatação condicional > Aba Escala de cores`. Escolha o gradiente de Verde (máximo) para Vermelho (mínimo). Se as cores estiverem invertidas (vermelho no maior valor), clique na prévia das cores para inverter a ordem.
3.  **Destaque de Baixo Desempenho (< 1000):**
    *   Com os dados ainda selecionados (B2:H7).
    *   **Excel:** Vá em `Formatação Condicional > Nova Regra` (ou Realçar Regras das Células). Escolha `Formatar apenas células que contenham` ou `É menor do que`. Defina o valor como `1000`. Clique em `Formatar`, vá na aba `Preenchimento` e escolha Amarelo, e na aba `Fonte` escolha Negrito. Dê OK.
    *   **Sheets:** Clique em `Adicionar outra regra`. Vá na aba `Cor única`. Em "Formatar células se...", escolha `Menor que`. No valor, digite `1000`. Em "Estilo de formatação", clique no ícone do balde (cor de preenchimento) e escolha amarelo, e clique no **B** (negrito). Clique em Concluído.

### Análise do Resultado (O "Pulo do Gato"):

Ao olhar para o seu mapa de calor finalizado, dois padrões devem saltar aos olhos imediatamente, sem precisar ler os números individualmente:

1.  **A Filial "Universidade" (Linha 5):** Ela mantém uma cor média (amarela/verde clara) durante a semana, mas fica **vermelha** (ou amarela destacada pela regra de <1000) no Sábado e Domingo.
    *   *Insight:* Como é uma universidade, não há aulas no fim de semana, então o público (estudantes e professores) desaparece.
2.  **A Filial "Praia" (Linha 6):** Ela é vermelha/laranja durante a semana (vendas baixas), mas fica **verde escuro** no Sábado e Domingo.
    *   *Insight:* É o oposto da universidade. O movimento explode no fim de semana com a chegada de turistas e pessoas buscando lazer.

**Conclusão:** Você acabou de usar dados brutos para entender o comportamento do consumidor. Um gerente poderia usar essa informação visual para, por exemplo, reduzir a equipe da filial Universidade no fim de semana e reforçar a equipe da filial Praia nesses mesmos dias. Isso é inteligência de negócios básica usando apenas cores!
