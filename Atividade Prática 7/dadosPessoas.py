"""
1- Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV.
Para isso:

 * Crie uma lista de listas com dados fictícios de pelo menos três pessoas.
 * Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.
 * Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.
 * Confirme a gravação exibindo uma mensagem com o nome do arquivo.
 * Trate possíveis erros de escrita de arquivo.

 Dica: Use `csv.writer()` para escrever os dados linha por linha.
"""

import csv

def salvar_dados():
    # Lista de listas com dados fictícios
    pessoas = [
        ["Nome", "Idade", "Cidade"],  # Cabeçalhos
        ["Ana", 25, "São Paulo"],
        ["Bruno", 30, "Rio de Janeiro"],
        ["Carla", 22, "Belo Horizonte"]
    ]
    
    # Solicita ao usuário o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo CSV (ex: dados.csv): ")
    
    try:
        # Abre o arquivo para escrita
        with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo)
            
            # Escreve os dados linha por linha
            for pessoa in pessoas:
                escritor.writerow(pessoa)
        
        print(f"Dados gravados com sucesso no arquivo '{nome_arquivo}'.")
    
    except Exception as e:
        print("Ocorreu um erro ao gravar o arquivo:", e)

# Executa a função
salvar_dados()