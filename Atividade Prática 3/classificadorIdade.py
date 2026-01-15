"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).
"""

def classificarIdade(idade):
    match idade:
        case i if 0 <= i <= 12:
            return "Criança"
        case i if 13 <= i <= 17:
            return "Adolescente"
        case i if 18 <= i <= 59:
            return "Adulto"
        case i if 60 <= i:
            return "Idoso"
        case _:
            return "Valor inválido"


idade = eval(input("Idade: "))
print(classificarIdade(idade))