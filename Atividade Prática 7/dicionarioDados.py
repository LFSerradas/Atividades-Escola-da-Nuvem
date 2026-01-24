"""
3- Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON.
Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo.
Para isso:

 * Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).
 * Solicite ao usuário o nome do arquivo JSON.
* Salve os dados no arquivo usando o módulo `json`.
 * Após salvar, leia o mesmo arquivo e imprima os dados carregados.
 * Trate possíveis erros como ausência do arquivo ou problemas na escrita.

 Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.
"""

import json

def salvar_e_ler_json():
    # Cria um dicionário com dados fictícios
    pessoa = {
        "nome": "Ana",
        "idade": 25,
        "cidade": "São Paulo"
    }
    
    # Solicita ao usuário o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo JSON (ex: dados.json): ")
    
    try:
        # Salva os dados no arquivo JSON
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso no arquivo '{nome_arquivo}'.")
        
        # Lê os dados do mesmo arquivo
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            dados_carregados = json.load(arquivo)
        print("Dados carregados do arquivo:")
        print(dados_carregados)
    
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado.")
    except Exception as e:
        print("Erro ao manipular o arquivo:", e)

# Executa a função
salvar_e_ler_json()