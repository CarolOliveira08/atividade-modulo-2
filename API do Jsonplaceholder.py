# 1. Importações e variáveis globais

import requests  # Para fazer requisições à API
import sys  # Para encerrar o programa

usuarios = {}  # Simula o banco de dados (email como chave)


# 2. Função de cadastro de usuário
def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    if email in usuarios:
        print("Usuário já cadastrado!")
    else:
        codigo = len(usuarios) + 1
        usuarios[email] = {"codigo": codigo, "nome": nome, "senha": senha}
        print(f"Usuário {nome} cadastrado com sucesso!\n")


# 3. Menu inicial
def menu_inicial():
    while True:
        print("Bem-vindo! Deseja se cadastrar?")
        print("1 - não (Cadastrar)")
        print("2 - sim (Fazer login)")
        print("3 - sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            return "login"
        elif opcao == "3":
            print("Encerrando o sistema. Até logo!")
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")


# Executa o menu inicial
menu_inicial





