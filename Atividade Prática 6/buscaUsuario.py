"""
2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
"""

import requests

def buscar_usuario():
    try:
        # Fazendo a requisição à API
        resposta = requests.get("https://randomuser.me/api/")
        resposta.raise_for_status()  # Lança erro se status != 200

        # Convertendo para JSON
        dados = resposta.json()
        usuario = dados["results"][0]

        # Extraindo informações
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]

        # Exibindo resultados
        print("Nome:", nome)
        print("Email:", email)
        print("País:", pais)
    except requests.exceptions.RequestException:
        print("Falha na conexão com a API.")

# Executando a função
buscar_usuario()