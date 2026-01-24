"""
2- Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela.
Para isso:

 * Solicite ao usuário o nome do arquivo CSV a ser lido.
 * Utilize o módulo `csv` para abrir o arquivo e ler os dados.
 * Exiba cada linha completa como uma lista.
 * Trate erros como arquivo inexistente ou problemas na leitura.

 Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.
"""

import csv

def ler_csv():
    # Solicita ao usuário o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo CSV a ser lido: ")
    
    try:
        # Abre o arquivo para leitura
        with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            
            # Percorre cada linha e imprime como lista
            for linha in leitor:
                print(linha)
    
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print("Erro ao ler o arquivo:", e)

# Executa a função
ler_csv()