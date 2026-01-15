"""
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
"""

preco = float(input("Digite o preço do produto: R$ "))
desconto = float(input("Digite a porcentagem de desconto (%): "))

valor_desconto = preco * (desconto / 100)

preco_final = preco - valor_desconto

print(f"\nPreço original: R$ {preco:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")