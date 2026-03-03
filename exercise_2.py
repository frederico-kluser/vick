#!/usr/bin/env python3
"""
Exercise 2: Desafio Analista de Vendas Júnior
Based on full-speed-learning.md
"""

from table_generator import TableGenerator

def create_exercise_2_data():
    """Generates the Vendas table for Exercise 2."""
    gen = TableGenerator()

    # Create table with columns
    gen.process("crie tabela vendas com colunas: ID_Venda, Data, Vendedor, Produto, Categoria, Quantidade, Valor_Unitario")

    # Add data rows based on the gabarito
    data = [
        "1, 03/01/2025, Ana, Fone Bluetooth, Eletrônicos, 3, 89.90",
        "2, 05/01/2025, Bruno, Película, Acessórios, 8, 15.00",
        "3, 06/01/2025, Carla, Teclado Mecânico, Informática, 1, 249.90",
        "4, 07/01/2025, Diego, Capa de Celular, Acessórios, 5, 29.90",
        "5, 08/01/2025, Ana, Mouse Wireless, Informática, 2, 79.90",
        "6, 09/01/2025, Bruno, Fone Bluetooth, Eletrônicos, 4, 89.90",
        "7, 10/01/2025, Carla, Carregador USB, Eletrônicos, 6, 45.50",
        "8, 11/01/2025, Diego, Teclado Mecânico, Informática, 1, 249.90",
        "9, 13/01/2025, Ana, Película, Acessórios, 10, 15.00",
        "10, 14/01/2025, Bruno, Mouse Wireless, Informática, 3, 79.90",
        "11, 15/01/2025, Carla, Capa de Celular, Acessórios, 7, 29.90",
        "12, 16/01/2025, Diego, Fone Bluetooth, Eletrônicos, 2, 89.90",
        "13, 18/01/2025, Ana, Carregador USB, Eletrônicos, 5, 45.50",
        "14, 19/01/2025, Bruno, Teclado Mecânico, Informática, 2, 249.90",
        "15, 20/01/2025, Carla, Fone Bluetooth, Eletrônicos, 3, 89.90",
        "16, 22/01/2025, Diego, Película, Acessórios, 9, 15.00",
        "17, 24/01/2025, Ana, Capa de Celular, Acessórios, 4, 29.90",
        "18, 26/01/2025, Bruno, Carregador USB, Eletrônicos, 6, 45.50",
        "19, 28/01/2025, Carla, Mouse Wireless, Informática, 2, 79.90",
        "20, 30/01/2025, Diego, Capa de Celular, Acessórios, 3, 29.90",
    ]

    for row in data:
        gen.process(f"adicione linha: {row}")

    # Export to Excel
    filename = "exercise_2_vendas"
    gen.to_excel(filename)
    print(f"File created: {filename}.xlsx")

if __name__ == "__main__":
    create_exercise_2_data()
