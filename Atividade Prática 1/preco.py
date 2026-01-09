"""
4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

nomeProduto = "Cadeira Infantil"
precoUnitario = 12.40
quantidade = 3

print(f"""
    Produto: {nomeProduto}
    Preço únitário: {precoUnitario}
    Quantidade: {quantidade}
    Total a pagar: {precoUnitario * quantidade}
""")