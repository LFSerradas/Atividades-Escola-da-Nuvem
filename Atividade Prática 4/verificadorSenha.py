"""
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
"""

senha = input("Digite sua senha: ")

tem_tamanho = len(senha) >= 8
tem_numero = any(char.isdigit() for char in senha)

if tem_tamanho and tem_numero:
    print("Senha válida")
else:
    print("Senha inválida")
    if not tem_tamanho:
        print("- A senha deve ter pelo menos 8 caracteres.")
    if not tem_numero:
        print("- A senha deve conter pelo menos um número.")