# 1. Importações e variáveis globais
import requests

usuarios = {
    "101": {"email": "ana@example.com", "senha": "1234"},
    "102": {"email": "joao@example.com", "senha": "abcd"},
    "103": {"email": "maria@example.com", "senha": "4321"},
}

interacoes = {
    "posts_vistos": 0,
    "comentarios_vistos": 0,
    "posts_criados": 0,
}

usuario_logado = None

# 2. Função de login
def login():
    global usuario_logado
    print("\n=== LOGIN ===")
    codigo = input("Digite o código do usuário: ")
    email = input("Digite o e-mail: ")
    senha = input("Digite a senha: ")

    if codigo in usuarios and usuarios[codigo]["email"] == email and usuarios[codigo]["senha"] == senha:
        print("Login bem-sucedido!\n")
        usuario_logado = {"id": codigo, "email": email}
    else:
        print("Usuário ou senha incorretos.\n")
        login()


