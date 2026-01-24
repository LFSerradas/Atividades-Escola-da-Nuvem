"""
3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.
"""

import requests

def consultar_cep(cep):
    # Validação básica
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido. Digite apenas 8 números.")
        return
    
    try:
        # Fazendo requisição à API ViaCEP
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url)
        resposta.raise_for_status()
        
        dados = resposta.json()
        
        # Verificando se o CEP existe
        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            print("Logradouro:", dados.get("logradouro"))
            print("Bairro:", dados.get("bairro"))
            print("Cidade:", dados.get("localidade"))
            print("Estado:", dados.get("uf"))
    
    except requests.exceptions.RequestException:
        print("Falha na conexão com a API.")

# Programa principal
cep_usuario = input("Digite o CEP (apenas números): ")
consultar_cep(cep_usuario)