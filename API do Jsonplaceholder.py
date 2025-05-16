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


# 3. Função para exibir o menu e receber a escolha do usuário
def menu():
    while True:
        print("=== MENU PRINCIPAL ===")
        print("1 - Visualizar todos os posts")
        print("2 - Visualizar comentários de um post")
        print("3 - Ver meus próprios posts")
        print("4 - Ver posts de outro usuário")
        print("5 - Criar um novo post")
        print("6 - Sair e ver resumo")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            visualizar_posts()
        elif escolha == "2":
            visualizar_comentarios()
        elif escolha == "3":
            ver_meus_posts()
        elif escolha == "4":
            filtrar_por_usuario()
        elif escolha == "5":
            criar_post()
        elif escolha == "6":
            mostrar_resumo()
            break
        else:
            print("Opção inválida. Tente novamente.\n")


# 4. Função para visualizar todos os posts
def visualizar_posts():
    print("\n=== LISTA DE POSTS ===")
    url = "https://jsonplaceholder.typicode.com/posts"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        posts = resposta.json()
        for post in posts:
            print(f"ID: {post['id']} | Título: {post['title']}")
        interacoes["posts_vistos"] += len(posts)
        print(f"\nTotal de {len(posts)} posts exibidos.\n")
    else:
        print("Erro ao buscar os posts.\n")
