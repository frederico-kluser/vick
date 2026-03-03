# Table Generator

Gerador de tabelas compatíveis com **Excel** e **Google Sheets** a partir de instruções simples em português ou inglês.

## Características

- **Linguagem natural**: Crie tabelas usando comandos simples como "crie tabela vendas com colunas: produto, preço"
- **Bilíngue**: Suporta instruções em português e inglês
- **Múltiplos formatos**: Exporta para Excel (.xlsx) e CSV
- **Compatibilidade total**: Arquivos funcionam perfeitamente no Excel, Google Sheets e LibreOffice
- **Estilos personalizáveis**: Cores, fontes e formatação configuráveis
- **Modo interativo**: Interface de linha de comando para criação rápida
- **API programática**: Use diretamente no seu código Python

## Instalação

```bash
# Clone o repositório ou copie os arquivos
cd seu-projeto

# Instale as dependências
pip install -r requirements.txt
```

### Dependências

- **openpyxl** >= 3.1.0 (para exportação Excel)
- Python 3.8+

## Uso Rápido

### Modo Interativo

```bash
python table_generator.py -i
```

Isso abre um terminal interativo onde você pode digitar comandos:

```
> crie tabela vendas com colunas: Produto, Quantidade, Preço
Tabela 'vendas' criada com 3 colunas: Produto, Quantidade, Preço

> adicione linha: Notebook, 5, 3500.00
Linha adicionada: ['Notebook', 5, 3500.0]

> adicione linha: Mouse, 20, 89.90
Linha adicionada: ['Mouse', 20, 89.9]

> exportar xlsx vendas.xlsx
Arquivo Excel criado: vendas.xlsx

> sair
```

### Uso Programático

```python
from table_generator import TableGenerator

gen = TableGenerator()

# Usando instruções em linguagem natural
gen.process("crie tabela funcionarios com colunas: Nome, Cargo, Salário")
gen.process("adicione linha: Maria Silva, Desenvolvedora, 8500")
gen.process("adicione linha: João Santos, Designer, 6500")

# Exporta para Excel
gen.to_excel("funcionarios.xlsx")

# Exporta para CSV
gen.to_csv("funcionarios.csv")
```

## Comandos Disponíveis

### Português

| Comando | Descrição | Exemplo |
|---------|-----------|---------|
| `crie tabela` | Cria uma nova tabela | `crie tabela vendas com colunas: produto, preço, quantidade` |
| `adicione linha` | Adiciona uma linha de dados | `adicione linha: Notebook, 2500, 10` |
| `adicione coluna` | Adiciona uma nova coluna | `adicione coluna: observação` |
| `nova linha` | Alternativa para adicionar linha | `nova linha: Mouse, 89.90, 50` |
| `linha:` | Forma simplificada | `linha: Teclado, 150, 30` |

### English

| Command | Description | Example |
|---------|-------------|---------|
| `create table` | Creates a new table | `create table sales with columns: product, price, quantity` |
| `add row` | Adds a data row | `add row: Laptop, 1299, 10` |
| `add column` | Adds a new column | `add column: notes` |
| `new row` | Alternative for adding row | `new row: Mouse, 29.99, 50` |
| `row:` | Simplified form | `row: Keyboard, 79.99, 30` |

### Comandos de Exportação (Modo Interativo)

| Comando | Descrição |
|---------|-----------|
| `exportar xlsx <arquivo>` | Exporta para Excel |
| `exportar csv <arquivo>` | Exporta para CSV |
| `mostrar` | Exibe a tabela atual |
| `ajuda` | Mostra ajuda |
| `sair` | Encerra o programa |

## Separadores de Valores

Você pode usar diferentes separadores para os valores:

```
# Vírgula (padrão)
adicione linha: valor1, valor2, valor3

# Ponto e vírgula
adicione linha: valor1; valor2; valor3

# Pipe
adicione linha: valor1 | valor2 | valor3
```

## Conversão Automática de Tipos

O parser converte automaticamente os valores para os tipos apropriados:

| Entrada | Tipo Convertido | Resultado |
|---------|-----------------|-----------|
| `42` | int | `42` |
| `3.14` | float | `3.14` |
| `2500,50` | float | `2500.5` (formato BR) |
| `verdadeiro` | bool | `True` |
| `false` | bool | `False` |
| `texto` | str | `"texto"` |

## API Completa

### Classe `TableGenerator`

```python
from table_generator import TableGenerator, TableStyle

# Inicialização
gen = TableGenerator()                    # Estilo padrão
gen = TableGenerator(style=estilo)        # Estilo personalizado

# Processamento de instruções
resultado = gen.process("instrução")           # Processa uma instrução
resultados = gen.process_batch(["i1", "i2"])   # Processa várias instruções

# Criação programática
tabela = gen.create_table("nome", ["col1", "col2"])

# Exportação
gen.to_excel("arquivo.xlsx")              # Exporta para Excel
gen.to_excel("arquivo.xlsx", tabela)      # Exporta tabela específica

gen.to_csv("arquivo.csv")                 # Exporta para CSV
gen.to_csv("arquivo.csv", delimiter=";")  # CSV com separador personalizado

# Exportar todas as tabelas
arquivos = gen.export_all("diretorio", format="xlsx")

# Converter para dicionário
dados = gen.to_dict()
# [{'col1': 'val1', 'col2': 'val2'}, ...]
```

### Classe `Table`

```python
from table_generator import Table

# Criação direta
tabela = Table(name="vendas", columns=["Produto", "Preço"])

# Adicionar dados
tabela.add_row("Notebook", 3500)
tabela.add_rows([
    ["Mouse", 89.90],
    ["Teclado", 150.00]
])
```

### Classe `TableStyle`

```python
from table_generator import TableStyle

estilo = TableStyle(
    header_bg_color="4472C4",      # Cor de fundo do cabeçalho (hex)
    header_font_color="FFFFFF",     # Cor da fonte do cabeçalho
    header_bold=True,               # Cabeçalho em negrito
    alternate_row_color="D9E2F3",   # Cor de linhas alternadas
    border_color="B4C6E7",          # Cor das bordas
    auto_width=True                 # Ajuste automático de largura
)
```

## Exemplos de Uso

### 1. Tabela de Vendas Simples

```python
from table_generator import TableGenerator

gen = TableGenerator()

gen.process("crie tabela vendas com colunas: Produto, Quantidade, Preço, Total")
gen.process("linha: Notebook Dell, 5, 3500, 17500")
gen.process("linha: Mouse Logitech, 20, 89.90, 1798")
gen.process("linha: Monitor LG, 8, 899, 7192")

gen.to_excel("vendas.xlsx")
```

### 2. Processamento em Lote

```python
from table_generator import TableGenerator

gen = TableGenerator()

instrucoes = [
    "crie tabela notas com colunas: Aluno, Nota1, Nota2, Média",
    "linha: Ana, 8.5, 9.0, 8.75",
    "linha: Bruno, 7.0, 8.0, 7.5",
    "linha: Carla, 9.5, 9.5, 9.5",
]

gen.process_batch(instrucoes)
gen.to_excel("notas.xlsx")
```

### 3. Múltiplas Tabelas

```python
from table_generator import TableGenerator

gen = TableGenerator()

# Tabela 1
gen.process("crie tabela clientes com colunas: ID, Nome, Email")
gen.process("linha: 1, João Silva, joao@email.com")
gen.process("linha: 2, Maria Santos, maria@email.com")

# Tabela 2
gen.process("crie tabela pedidos com colunas: Pedido, Cliente_ID, Valor")
gen.process("linha: P001, 1, 1500")
gen.process("linha: P002, 2, 2300")

# Exporta todas
gen.export_all("output", format="xlsx")
# Cria: output/clientes.xlsx e output/pedidos.xlsx
```

### 4. Estilo Personalizado (Tema Verde)

```python
from table_generator import TableGenerator, TableStyle

estilo = TableStyle(
    header_bg_color="2E7D32",
    header_font_color="FFFFFF",
    alternate_row_color="C8E6C9",
    border_color="81C784"
)

gen = TableGenerator(style=estilo)
gen.process("crie tabela inventario com colunas: Item, Quantidade, Local")
gen.process("linha: Parafusos, 5000, A1")
gen.to_excel("inventario_verde.xlsx")
```

### 5. CSV para Google Sheets

```python
from table_generator import TableGenerator

gen = TableGenerator()

gen.process("crie tabela dados com colunas: Data, Descrição, Valor")
gen.process("linha: 2024-01-15, Venda A, 1500.50")

# CSV padrão (melhor para Google Sheets)
gen.to_csv("dados.csv", delimiter=",")

# Para importar no Google Sheets:
# 1. Abra o Google Sheets
# 2. Arquivo > Importar > Upload
# 3. Selecione o arquivo .csv
```

### 6. Lendo Instruções de Arquivo

```python
from table_generator import TableGenerator

gen = TableGenerator()

with open("instrucoes.txt", "r", encoding="utf-8") as f:
    for linha in f:
        linha = linha.strip()
        if linha:
            gen.process(linha)

gen.to_excel("resultado.xlsx")
```

**instrucoes.txt:**
```
crie tabela tarefas com colunas: Tarefa, Status, Prazo
linha: Desenvolver API, Em andamento, 2024-02-15
linha: Criar testes, Pendente, 2024-02-20
linha: Documentação, Concluído, 2024-02-10
```

## Compatibilidade

### Microsoft Excel
- Arquivos `.xlsx` abrem diretamente no Excel 2007+
- Formatação, cores e estilos são preservados
- Para CSV em português, use `delimiter=";"` para melhor compatibilidade

### Google Sheets
- **Excel (.xlsx)**: Importar via "Arquivo > Importar > Upload"
- **CSV**: Importar diretamente ou fazer upload para Google Drive

### LibreOffice Calc
- Suporta tanto `.xlsx` quanto `.csv`
- Formatação Excel é mantida

## Executando os Exemplos

```bash
# Executa todos os exemplos
python examples.py

# Modo interativo
python table_generator.py -i
```

## Estrutura do Projeto

```
├── table_generator.py   # Módulo principal
├── examples.py          # Exemplos de uso
├── requirements.txt     # Dependências
└── README.md           # Documentação
```

## Dicas de Uso

1. **Nomes de colunas**: Use nomes sem caracteres especiais para melhor compatibilidade
2. **Números decimais**: Use ponto (3.14) ou vírgula (3,14) - ambos são aceitos
3. **Datas**: Use formato ISO (2024-01-15) ou brasileiro (15/01/2024)
4. **Exportação múltipla**: Use `export_all()` para exportar várias tabelas de uma vez
5. **Google Sheets**: Prefira CSV com vírgula para importação mais suave

## Solução de Problemas

### Erro: "openpyxl não está instalado"

```bash
pip install openpyxl
```

### Caracteres especiais aparecem errados no Excel

Use a codificação UTF-8 com BOM (padrão do `to_csv()`):

```python
gen.to_csv("arquivo.csv", encoding="utf-8-sig")
```

### CSV não abre corretamente no Excel (Brasil)

Use ponto-e-vírgula como separador:

```python
gen.to_csv("arquivo.csv", delimiter=";")
```

## Licença

MIT License - Use livremente em seus projetos.

## Referências

- [openpyxl Documentation](https://openpyxl.readthedocs.io/)
- [XlsxWriter Documentation](https://xlsxwriter.readthedocs.io/)
- [Google Sheets Import Guide](https://support.google.com/docs/answer/40608)
