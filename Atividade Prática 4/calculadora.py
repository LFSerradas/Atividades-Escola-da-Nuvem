"""
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
"""

n1 = float(input("Insira o 1° valor: "))
operacao = input("Escreva a operação desejada (Soma, Subtração, Multiplicação, Divisão): ")
n2 = float(input("Insira o 2° valor: "))
match operacao:
    case "Soma":
        print(f"A soma entre {n1} e {n2} é {n1 + n2}")
    case "Subtração":
        print(f"A subtração entre {n1} e {n2} é {n1 - n2}")
    case "Divisão":
        print(f"A divisão entre {n1} e {n2} é {n1 / n2}")
    case "Multiplicação":
        print(f"A multiplicação entre {n1} e {n2} é {n1 * n2}")