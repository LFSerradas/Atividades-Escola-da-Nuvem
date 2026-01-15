"""
4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
"""

pares = []
impares = []

while True:
    entrada = input("Digite um número (ou Enter para encerrar): ")
    if entrada == "":
        break
    numero = int(entrada)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\n--- Resultado ---")
print("Números pares:", pares)
print("Quantidade de pares:", len(pares))
print("Números ímpares:", impares)
print("Quantidade de ímpares:", len(impares))