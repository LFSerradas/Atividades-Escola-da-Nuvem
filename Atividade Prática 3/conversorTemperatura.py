"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""
def conversaoCelsiusKelvin(temperatura):
    return temperatura + 273.15

def conversaoCelsiusFahrenheit(temperatura):
    return (temperatura * (9/5) + 32)

def conversaoFahrenheitCelsius(temperatura):
    return (temperatura - 32) * (5/9)

def conversaoFahrenheitKelvin(temperatura):
    return (temperatura - 32) * (5/9) + 273.15

def conversaoKelvinCelsius(temperatura):
    return temperatura - 273.15

def conversaoKelvinFahrenheit(temperatura):
    return ((temperatura - 273.15) * (9/5) + 32)


temperatura = input("Temperatura: ")
unidadeMedida = input("Unidade (C, F ou K): ")
unidadeConversao = input("Unidade a ser convertida (C, F ou K): ")


def conversor(medida, unidade, conversao):
    if unidade in "cC":
        if conversao in "cC":
            return medida
        elif conversao in "fF":
            return conversaoCelsiusFahrenheit(medida)
        elif conversao in "kK":
            return conversaoCelsiusKelvin(medida)
    elif unidade in "fF":
        if conversao in "cC":
            return conversaoFahrenheitCelsius(medida)
        elif conversao in "fF":
            return medida
        elif conversao in "kK":
            return conversaoFahrenheitKelvin(medida)
    elif unidade in "kK":
        if conversao in "cC":
            return conversaoKelvinCelsius(medida)
        elif conversao in "fF":
            return conversaoKelvinFahrenheit(medida)
        elif conversao in "kK":
            return medida
    else:
        print("Valor Inválido")

print(f"""
    Temperatura {unidadeMedida.upper()}°: {temperatura}
    Conversão para {unidadeConversao.upper()}°: {conversor(float(temperatura), unidadeMedida, unidadeConversao)}
""")