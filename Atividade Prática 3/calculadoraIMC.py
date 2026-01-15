"""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

imc = eval(input("IMC: "))
match imc:
    case i if 0 < i < 18.5:
        print("Abaixo do peso")
    case i if 18.5 <= i < 25:
        print("Peso normal")
    case i if 25 <= i < 30:
        print("Sobrepeso")
    case i if 30 <= i:
        print("Obeso")
    case _:
        print("Valor inválido")