# Guia do Desafio 1: Classificação de Candidatos

===
1 - Apresentação do desafio e o que ele pede

**Cenário:** Você trabalha no RH de uma empresa e precisa avaliar candidatos para um programa de estágio.
Cada candidato possui duas informações essenciais:
1.  **Nota na prova** (0 a 100).
2.  **Conclusão de curso técnico** (Sim ou Não).

**As regras para classificação são:**
*   **Aprovado:** Se tiver Nota maior ou igual a 70 **E** Curso Técnico "Sim".
*   **Lista de espera:** Se tiver Nota maior ou igual a 70 **OU** Curso Técnico "Sim" (mas não ambos).
*   **Reprovado:** Caso não atenda a nenhuma das condições acima.

**Sua missão:**
Criar uma planilha com os dados fornecidos e, na coluna D, desenvolver uma fórmula que classifique automaticamente cada candidato.

**Dados para copiar e colar na sua planilha (começando na célula A1):**

| Candidato | Nota | Curso Técnico | Classificação |
| :--- | :--- | :--- | :--- |
| Ana | 85 | Sim | |
| Bruno | 60 | Sim | |
| Carla | 75 | Não | |
| Diego | 50 | Não | |
| Eva | 90 | Sim | |

===
2 - Tutorial de técnicas e ferramentas utilizadas

Para resolver este desafio, você usará **Funções Lógicas**. Vamos entender as ferramentas:

*   **SE (IF):** É a função que toma decisões. Ela pergunta: "Isso é verdade?". Se sim, faz uma coisa. Se não, faz outra.
    *   *Estrutura:* `=SE(teste_lógico; valor_se_verdadeiro; valor_se_falso)`
*   **E (AND):** Serve para exigir que **todas** as condições sejam verdadeiras.
    *   *Exemplo:* `=E(Nota>=70; Curso="Sim")` -> Só retorna VERDADEIRO se ambas as coisas acontecerem.
*   **OU (OR):** Serve para aceitar se **pelo menos uma** das condições for verdadeira.
    *   *Exemplo:* `=OU(Nota>=70; Curso="Sim")` -> Retorna VERDADEIRO se tiver nota azul OU se tiver o curso.

**Diferença entre Excel e Google Sheets:**
*   **Excel (Português):** As funções são `SE`, `E`, `OU`. Os separadores são **ponto e vírgula (;)**.
*   **Google Sheets (ou Excel Inglês):** As funções podem ser `IF`, `AND`, `OR`. Os separadores costumam ser **ponto e vírgula (;)** se o seu Sheets estiver em Português do Brasil, mas podem ser **vírgula (,)** se estiver em Inglês.
    *   *Dica:* Observe a ajuda que aparece enquanto você digita a fórmula, ela mostra qual separador usar.

===
3 - O que é esperado ao final

Ao final, a coluna "Classificação" deverá estar preenchida automaticamente para todos os candidatos com base nas regras.

Exemplos de verificação:
*   **Ana** tem nota alta e curso. Ela deve ser **Aprovada**.
*   **Bruno** tem curso, mas nota baixa. Ele deve ir para **Lista de espera**.
*   **Diego** não tem nota nem curso. Ele deve ser **Reprovado**.

Você deve construir uma única fórmula na primeira célula de resultado e arrastá-la para as demais, funcionando corretamente para todos os casos.

===
4 - Dicas progressivas

**Dica 1: Comece pelo caso mais restritivo**
A condição mais difícil de atender é a de "Aprovado", pois exige DUAS coisas ao mesmo tempo. Teste isso primeiro.

**Dica 2: Entendendo a função E (AND)**
Como escrever "Nota (B2) maior ou igual a 70 E Curso (C2) igual a Sim"?
Fica assim: `E(B2>=70; C2="Sim")`. Tente colocar isso numa célula sozinha e veja se dá VERDADEIRO ou FALSO para a Ana.

**Dica 3: O "Senão" do primeiro SE**
A função SE tem três partes: Teste, Valor se Verdadeiro, Valor se Falso.
*   Teste: O aluno é Aprovado? (usando a Dica 2)
*   Verdadeiro: Escreva "Aprovado".
*   Falso: Aqui entra o segredo. Se não é aprovado, ele ainda pode ser "Lista de Espera" ou "Reprovado". Você precisará de **outro SE** dentro desta parte "Falsa".

**Dica 4: A lógica da Lista de Espera**
Se o aluno já falhou no teste de "Aprovado", sobra verificar se ele tem *pelo menos um* dos requisitos. Use a função **OU**.
`OU(B2>=70; C2="Sim")`.

===
5 - Resultado e Solução Passo a Passo

!!! ALERTA DE SPOILER ABAIXO !!!
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
**Raciocínio da Solução:**

1.  Primeiro, verificamos se o candidato é **Aprovado**. Para isso, usamos `E` para checar se `Nota >= 70` e `Curso = "Sim"`.
2.  Se isso for verdade, escrevemos "Aprovado".
3.  Se não for verdade (caiu no "falso" do primeiro SE), abrimos um novo `SE`.
4.  Nesse segundo `SE`, verificamos se ele serve para **Lista de espera**. Usamos `OU` para checar se `Nota >= 70` ou `Curso = "Sim"`.
5.  Se isso for verdade (lembre-se, quem tinha os dois já ficou no passo 2), escrevemos "Lista de espera".
6.  Se nem isso for verdade, sobrou a opção "Reprovado".

**Fórmula Final (Excel Português / Google Sheets Brasil):**
Copie e cole na célula D2 (assumindo que seus dados começam na linha 2):

```excel
=SE(E(B2>=70; C2="Sim"); "Aprovado"; SE(OU(B2>=70; C2="Sim"); "Lista de espera"; "Reprovado"))
```

**Fórmula Final (Google Sheets Inglês):**

```excel
=IF(AND(B2>=70, C2="Yes"), "Approved", IF(OR(B2>=70, C2="Yes"), "Waitlist", "Rejected"))
```
