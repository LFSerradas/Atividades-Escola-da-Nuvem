"""
4 - Crie um programa que realize consultas a em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.
"""

import requests

def consultar_cotacao(moeda):
    try:
        url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        resposta = requests.get(url)
        resposta.raise_for_status()
        
        dados = resposta.json()
        
        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada.")
            return
        
        cotacao = dados[chave]
        
        print(f"Cotação {moeda}/BRL")
        print("Valor atual:", cotacao["bid"])
        print("Máximo:", cotacao["high"])
        print("Mínimo:", cotacao["low"])
        print("Última atualização:", cotacao["create_date"])
    
    except requests.exceptions.RequestException:
        print("Falha na conexão com a API.")

# Programa principal
moeda_usuario = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
consultar_cotacao(moeda_usuario)