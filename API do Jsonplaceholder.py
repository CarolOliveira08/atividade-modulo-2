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


# 4. Função de login
def fazer_login():
    print("\n--- Login de Usuário ---")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    if email in usuarios and usuarios[email]["senha"] == senha:
        print(f"Login realizado com sucesso! Bem-vindo(a), {usuarios[email]['nome']}.\n")
        return usuarios[email]  # Retorna os dados do usuário logado
    else:
        print("E-mail ou senha inválidos. Tente novamente.\n")
        return None


# Reutiliza o menu para tentar login até funcionar
usuario_logado = None
while not usuario_logado:
    if menu_inicial() == "login":
        usuario_logado = fazer_login()


# 5. Contadores de interações
interacoes = {
    "posts_vistos": 0,
    "comentarios_vistos": 0,
    "posts_criados": 0
}

# 6. Menu principal de ações
def menu_usuario(usuario):
    while True:
        print("\n--- Menu Principal ---")
        print("1 - Ver todos os posts")
        print("2 - Ver comentários de um post")
        print("3 - Ver meus próprios posts")
        print("4 - Ver posts de outro usuário")
        print("5 - Criar um novo post")
        print("6 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            ver_todos_os_posts()
        elif escolha == "2":
            ver_comentarios()
        elif escolha == "3":
            ver_posts_usuario(usuario["codigo"])
        elif escolha == "4":
            filtrar_por_usuario()
        elif escolha == "5":
            criar_novo_post(usuario["codigo"])
        elif escolha == "6":
            print("\nResumo das interações:")
            print(f"Posts visualizados: {interacoes['posts_vistos']}")
            print(f"Comentários visualizados: {interacoes['comentarios_vistos']}")
            print(f"Posts criados: {interacoes['posts_criados']}")
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# 7. Ver todos os posts (primeiros 5)
def ver_todos_os_posts():
    print("\n--- Todos os Posts ---")
    url = "https://jsonplaceholder.typicode.com/posts"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        posts = resposta.json()
        for post in posts[:5]:  # Mostra só os primeiros 5
            print(f"\nID: {post['id']}")
            print(f"Título: {post['title']}")
            print(f"Corpo: {post['body']}")
            interacoes["posts_vistos"] += 1
    else:
        print("Erro ao buscar os posts. Tente novamente mais tarde.")


# 8. Ver comentários de um post
def ver_comentarios():
    print("\n--- Comentários de um Post ---")
    post_id = input("Digite o ID do post: ")

    url = f"https://jsonplaceholder.typicode.com/comments?postId={post_id}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        comentarios = resposta.json()
        if comentarios:
            print(f"\nComentários do Post {post_id}:")
            for c in comentarios[:3]:  # Mostra apenas 3 comentários
                print(f"\nNome: {c['name']}")
                print(f"E-mail: {c['email']}")
                print(f"Comentário: {c['body']}")
                interacoes["comentarios_vistos"] += 1
        else:
            print("Nenhum comentário encontrado para esse post.")
    else:
        print("Erro ao buscar os comentários.")

# 9. Ver posts do usuário logado
def ver_posts_usuario(user_id):
    print("\n--- Meus Posts ---")
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        posts = resposta.json()
        if posts:
            for post in posts[:3]:  # Mostra até 3 posts
                print(f"\nID: {post['id']}")
                print(f"Título: {post['title']}")
                print(f"Corpo: {post['body']}")
                interacoes["posts_vistos"] += 1
        else:
            print("Você ainda não tem posts.")
    else:
        print("Erro ao buscar seus posts.")


# 10. Ver posts de outro usuário
def filtrar_por_usuario():
    print("\n--- Ver Posts de Outro Usuário ---")
    outro_id = input("Digite o ID do outro usuário (1 a 10): ")

    url = f"https://jsonplaceholder.typicode.com/posts?userId={outro_id}"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        posts = resposta.json()
        if posts:
            for post in posts[:3]:  # Mostra até 3 posts
                print(f"\nID: {post['id']}")
                print(f"Título: {post['title']}")
                print(f"Corpo: {post['body']}")
                interacoes["posts_vistos"] += 1
        else:
            print("Nenhum post encontrado para esse usuário.")
    else:
        print("Erro ao buscar os posts.")


# 11. Criar novo post
def criar_novo_post(user_id):
    print("\n--- Criar Novo Post ---")
    titulo = input("Digite o título do post: ")
    corpo = input("Digite o conteúdo do post: ")

    dados = {
        "title": titulo,
        "body": corpo,
        "userId": user_id
    }

    url = "https://jsonplaceholder.typicode.com/posts"
    resposta = requests.post(url, json=dados)

    if resposta.status_code == 201:
        post_criado = resposta.json()
        print("\nPost criado com sucesso!")
        print(f"ID: {post_criado['id']}")
        print(f"Título: {post_criado['title']}")
        print(f"Corpo: {post_criado['body']}")
        interacoes["posts_criados"] += 1
    else:
        print("Erro ao criar o post.")
