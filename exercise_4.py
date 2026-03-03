from table_generator import TableGenerator

def create_exercise_4_data():
    """
    Cria o arquivo de dados para o Exercício 4 do full-speed-learning.md.
    O Exercício 4 ("O Painel do Gerente") requer uma tabela de vendas para criar Tabelas Dinâmicas e Gráficos.
    """
    print("Gerando dados para o Exercício 4...")
    
    gen = TableGenerator()
    
    # Cria a tabela Vendas
    gen.process("crie tabela Vendas com colunas: ID_Venda, Data, Vendedor, Produto, Categoria, Quantidade, Valor_Unitario")
    
    # Dados do Gabarito (20 linhas)
    vendas = [
        "linha: 1, 03/01/2025, Ana, Fone Bluetooth, Eletrônicos, 3, 89.90",
        "linha: 2, 05/01/2025, Bruno, Película, Acessórios, 8, 15.00",
        "linha: 3, 06/01/2025, Carla, Teclado Mecânico, Informática, 1, 249.90",
        "linha: 4, 07/01/2025, Diego, Capa de Celular, Acessórios, 5, 29.90",
        "linha: 5, 08/01/2025, Ana, Mouse Wireless, Informática, 2, 79.90",
        "linha: 6, 09/01/2025, Bruno, Fone Bluetooth, Eletrônicos, 4, 89.90",
        "linha: 7, 10/01/2025, Carla, Carregador USB, Eletrônicos, 6, 45.50",
        "linha: 8, 11/01/2025, Diego, Teclado Mecânico, Informática, 1, 249.90",
        "linha: 9, 13/01/2025, Ana, Película, Acessórios, 10, 15.00",
        "linha: 10, 14/01/2025, Bruno, Mouse Wireless, Informática, 3, 79.90",
        "linha: 11, 15/01/2025, Carla, Capa de Celular, Acessórios, 7, 29.90",
        "linha: 12, 16/01/2025, Diego, Fone Bluetooth, Eletrônicos, 2, 89.90",
        "linha: 13, 18/01/2025, Ana, Carregador USB, Eletrônicos, 5, 45.50",
        "linha: 14, 19/01/2025, Bruno, Teclado Mecânico, Informática, 2, 249.90",
        "linha: 15, 20/01/2025, Carla, Fone Bluetooth, Eletrônicos, 3, 89.90",
        "linha: 16, 22/01/2025, Diego, Película, Acessórios, 9, 15.00",
        "linha: 17, 24/01/2025, Ana, Capa de Celular, Acessórios, 4, 29.90",
        "linha: 18, 26/01/2025, Bruno, Carregador USB, Eletrônicos, 6, 45.50",
        "linha: 19, 28/01/2025, Carla, Mouse Wireless, Informática, 2, 79.90",
        "linha: 20, 30/01/2025, Diego, Capa de Celular, Acessórios, 3, 29.90"
    ]
    
    # Processa todas as linhas
    gen.process_batch(vendas)
    
    # Exporta para Excel (recomendado para o exercício) e CSV
    gen.to_excel("exercicio_4_vendas.xlsx")
    gen.to_csv("exercicio_4_vendas.csv")
    
    print("Arquivos criados: exercicio_4_vendas.xlsx e exercicio_4_vendas.csv")
    print("\nInstruções para o Exercício 4:")
    print("1. Abra o arquivo 'exercicio_4_vendas.xlsx' no Excel ou Google Sheets.")
    print("2. Siga as instruções do 'DESAFIO 4: O Painel do Gerente' no arquivo full-speed-learning.md.")
    print("3. Objetivo: Criar 3 Tabelas Dinâmicas e um Dashboard.")

if __name__ == "__main__":
    create_exercise_4_data()
