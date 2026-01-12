"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

distanciaPercorrida = 300
litrosCombustivel = 25

print(f"""
    Distância: {distanciaPercorrida}
    Gasolina gasta: {litrosCombustivel}
    Consumo médio: {round(distanciaPercorrida / litrosCombustivel, 2)}
""")