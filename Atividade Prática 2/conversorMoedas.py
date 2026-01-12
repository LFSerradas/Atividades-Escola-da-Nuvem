"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

real = eval(input("Insira um valor: R$ "))
realDolar = real * 5.2
realEuro = real * 6.15

print(f"""
    Real (BRL) → \t R$: {real}
    Euro (EUR) → \t €: {realDolar}
    Dólar (USD) → \t $: {realEuro}
""")
