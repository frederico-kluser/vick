#!/usr/bin/env python3
"""
Exemplos de uso do Table Generator.
"""

from table_generator import TableGenerator, TableStyle, Table


def exemplo_basico():
    """Exemplo básico: criar tabela com instruções em português."""
    print("=" * 60)
    print("EXEMPLO 1: Uso básico com instruções em português")
    print("=" * 60)

    gen = TableGenerator()

    # Cria tabela usando linguagem natural
    gen.process("crie tabela funcionarios com colunas: Nome, Cargo, Salário")
    gen.process("adicione linha: Maria Silva, Desenvolvedora, 8500")
    gen.process("adicione linha: João Santos, Designer, 6500")
    gen.process("adicione linha: Ana Costa, Gerente, 12000")

    # Exporta para Excel e CSV
    gen.to_excel("funcionarios")
    gen.to_csv("funcionarios")

    print("Arquivos criados: funcionarios.xlsx, funcionarios.csv")
    print()


def exemplo_ingles():
    """Exemplo com instruções em inglês."""
    print("=" * 60)
    print("EXEMPLO 2: Uso com instruções em inglês")
    print("=" * 60)

    gen = TableGenerator()

    gen.process("create table products with columns: Name, Price, Stock")
    gen.process("add row: Laptop, 1299.99, 50")
    gen.process("add row: Keyboard, 79.99, 200")
    gen.process("add row: Monitor, 349.99, 75")

    gen.to_excel("products")
    print("Arquivo criado: products.xlsx")
    print()


def exemplo_programatico():
    """Exemplo de uso programático (sem parser)."""
    print("=" * 60)
    print("EXEMPLO 3: Uso programático direto")
    print("=" * 60)

    gen = TableGenerator()

    # Cria tabela diretamente
    tabela = gen.create_table("vendas_2024", ["Mês", "Receita", "Despesas", "Lucro"])

    # Adiciona dados
    dados = [
        ["Janeiro", 50000, 35000, 15000],
        ["Fevereiro", 55000, 38000, 17000],
        ["Março", 62000, 40000, 22000],
        ["Abril", 58000, 37000, 21000],
        ["Maio", 70000, 42000, 28000],
        ["Junho", 75000, 45000, 30000],
    ]

    tabela.add_rows(dados)

    # Exporta
    gen.to_excel("vendas_2024")
    print("Arquivo criado: vendas_2024.xlsx")

    # Mostra dados como dicionário
    print("\nDados como lista de dicionários:")
    for item in gen.to_dict():
        print(f"  {item}")
    print()


def exemplo_estilo_personalizado():
    """Exemplo com estilo personalizado."""
    print("=" * 60)
    print("EXEMPLO 4: Tabela com estilo personalizado")
    print("=" * 60)

    # Define estilo customizado
    estilo = TableStyle(
        header_bg_color="2E7D32",      # Verde escuro
        header_font_color="FFFFFF",     # Branco
        alternate_row_color="C8E6C9",   # Verde claro
        border_color="81C784",          # Verde médio
        header_bold=True,
        auto_width=True
    )

    gen = TableGenerator(style=estilo)

    gen.process("crie tabela inventario com colunas: Item, Categoria, Quantidade, Localização")
    gen.process("adicione linha: Parafusos M6, Fixadores, 5000, Prateleira A1")
    gen.process("adicione linha: Porcas M6, Fixadores, 5000, Prateleira A1")
    gen.process("adicione linha: Cabo USB-C, Eletrônicos, 200, Prateleira B3")
    gen.process("adicione linha: Fonte 12V, Eletrônicos, 50, Prateleira B4")

    gen.to_excel("inventario_verde")
    print("Arquivo criado: inventario_verde.xlsx (com tema verde)")
    print()


def exemplo_multiplas_tabelas():
    """Exemplo criando múltiplas tabelas."""
    print("=" * 60)
    print("EXEMPLO 5: Múltiplas tabelas exportadas")
    print("=" * 60)

    gen = TableGenerator()

    # Primeira tabela
    gen.process("crie tabela clientes com colunas: ID, Nome, Email, Cidade")
    gen.process("adicione linha: 1, Carlos Lima, carlos@email.com, São Paulo")
    gen.process("adicione linha: 2, Paula Souza, paula@email.com, Rio de Janeiro")
    gen.process("adicione linha: 3, Roberto Alves, roberto@email.com, Curitiba")

    # Segunda tabela
    gen.process("crie tabela pedidos com colunas: Pedido, Cliente_ID, Produto, Valor")
    gen.process("adicione linha: P001, 1, Notebook, 3500")
    gen.process("adicione linha: P002, 2, Smartphone, 2800")
    gen.process("adicione linha: P003, 1, Monitor, 1200")
    gen.process("adicione linha: P004, 3, Teclado, 350")

    # Exporta todas as tabelas
    import os
    os.makedirs("tabelas", exist_ok=True)

    arquivos = gen.export_all("tabelas", format="xlsx")
    print(f"Arquivos criados: {arquivos}")
    print()


def exemplo_csv_google_sheets():
    """Exemplo focado em compatibilidade com Google Sheets."""
    print("=" * 60)
    print("EXEMPLO 6: CSV otimizado para Google Sheets")
    print("=" * 60)

    gen = TableGenerator()

    gen.process("crie tabela dados_sheets com colunas: Data, Descrição, Valor, Status")
    gen.process("adicione linha: 2024-01-15, Venda produto A, 1500.50, Concluído")
    gen.process("adicione linha: 2024-01-16, Venda produto B, 2300.00, Concluído")
    gen.process("adicione linha: 2024-01-17, Serviço consultoria, 5000.00, Pendente")

    # CSV com ponto-e-vírgula (melhor para Excel BR)
    gen.to_csv("dados_excel_br", delimiter=";")

    # CSV padrão (melhor para Google Sheets)
    gen.to_csv("dados_google_sheets", delimiter=",")

    print("Arquivos criados:")
    print("  - dados_excel_br.csv (separador: ponto-e-vírgula)")
    print("  - dados_google_sheets.csv (separador: vírgula)")
    print()


def exemplo_batch_processing():
    """Exemplo processando várias instruções de uma vez."""
    print("=" * 60)
    print("EXEMPLO 7: Processamento em lote")
    print("=" * 60)

    gen = TableGenerator()

    # Lista de instruções para processar
    instrucoes = [
        "crie tabela notas com colunas: Aluno, Matemática, Português, Ciências, Média",
        "linha: Ana, 8.5, 9.0, 7.5, 8.33",
        "linha: Bruno, 7.0, 8.0, 9.0, 8.00",
        "linha: Carla, 9.5, 9.5, 9.0, 9.33",
        "linha: Diego, 6.5, 7.0, 8.0, 7.17",
        "linha: Elena, 10.0, 9.0, 9.5, 9.50",
    ]

    # Processa todas de uma vez
    resultados = gen.process_batch(instrucoes)

    print("Resultados do processamento:")
    for r in resultados:
        print(f"  {r}")

    gen.to_excel("notas_turma")
    print("\nArquivo criado: notas_turma.xlsx")
    print()


def exemplo_leitura_arquivo():
    """Exemplo lendo instruções de um arquivo."""
    print("=" * 60)
    print("EXEMPLO 8: Instruções de arquivo texto")
    print("=" * 60)

    # Cria arquivo de exemplo
    instrucoes_arquivo = """
crie tabela tarefas com colunas: Tarefa, Responsável, Prazo, Status
adicione linha: Desenvolver API, João, 2024-02-15, Em andamento
adicione linha: Criar testes, Maria, 2024-02-10, Concluído
adicione linha: Documentação, Carlos, 2024-02-20, Pendente
adicione linha: Deploy, Ana, 2024-02-28, Pendente
    """

    with open("instrucoes.txt", "w", encoding="utf-8") as f:
        f.write(instrucoes_arquivo.strip())

    print("Arquivo instrucoes.txt criado.")

    # Lê e processa
    gen = TableGenerator()

    with open("instrucoes.txt", "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha:
                resultado = gen.process(linha)
                print(f"  {resultado}")

    gen.to_excel("tarefas")
    print("\nArquivo criado: tarefas.xlsx")
    print()


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("  TABLE GENERATOR - Exemplos de Uso")
    print("=" * 60 + "\n")

    try:
        exemplo_basico()
        exemplo_ingles()
        exemplo_programatico()
        exemplo_estilo_personalizado()
        exemplo_multiplas_tabelas()
        exemplo_csv_google_sheets()
        exemplo_batch_processing()
        exemplo_leitura_arquivo()

        print("=" * 60)
        print("  Todos os exemplos executados com sucesso!")
        print("=" * 60)
        print("\nArquivos gerados:")
        print("  - funcionarios.xlsx / .csv")
        print("  - products.xlsx")
        print("  - vendas_2024.xlsx")
        print("  - inventario_verde.xlsx")
        print("  - tabelas/clientes.xlsx")
        print("  - tabelas/pedidos.xlsx")
        print("  - dados_excel_br.csv")
        print("  - dados_google_sheets.csv")
        print("  - notas_turma.xlsx")
        print("  - tarefas.xlsx")

    except ImportError:
        print("\nATENÇÃO: Para gerar arquivos Excel, instale openpyxl:")
        print("  pip install openpyxl")
        print("\nOs exemplos de CSV ainda funcionarão.")
