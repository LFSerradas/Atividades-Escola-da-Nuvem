"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nomeProduto = "Camiseta"
preco = 50.00
desconto = 0.2

print(f"""
    Produto: {nomeProduto}
    Preço: {preco}
    Desconto: {desconto * 100}%
    Valor final: {preco * (1 - desconto)}
""")