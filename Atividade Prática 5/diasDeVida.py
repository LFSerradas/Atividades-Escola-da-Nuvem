"""
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
"""

from datetime import datetime

data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

hoje = datetime.today()
dias_vividos = (hoje - nascimento).days

print(f"Você está vivo há {dias_vividos} dias.")