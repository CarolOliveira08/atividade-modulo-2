# Simulando um "banco de dados" de usuários
usuarios = {
    "001": {"email": "joao@email.com", "senha": "1234"},
    "002": {"email": "maria@email.com", "senha": "abcd"},
}

# Função para normalizar e-mails
def normalizar_email(texto):
    return texto.strip().lower()

# Função de login
def login():
    print("===== LOGIN =====")
    codigo = input("Informe seu código de usuário: ").strip()
    email = normalizar_email(input("Informe seu e-mail: "))
    senha = input("Informe sua senha: ").strip()

    if codigo in usuarios:
        user = usuarios[codigo]
        if normalizar_email(user['email']) == email and user['senha'] == senha:
            print("Login realizado com sucesso!\n")
            return codigo
    print("Usuário ou senha inválidos.\n")
    return None


# Função do menu
def menu():
    print("\n=== MENU INTERATIVO ===")
    print("1. Visualizar posts e comentários")
    print("2. Visualizar meus posts")
    print("3. Filtrar posts por outro usuário")
    print("4. Criar novo post")
    print("5. Sair")

# Loop principal
def main():
    usuario_logado = None
    while not usuario_logado:
        usuario_logado = login()

    interacoes = {"posts_visualizados": 0, "comentarios_visualizados": 0, "posts_criados": 0}

    while True:
        menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            print("Visualizando posts e comentários...")
            interacoes["posts_visualizados"] += 1
            interacoes["comentarios_visualizados"] += 1

        elif opcao == "2":
            print(f"Visualizando posts do usuário {usuario_logado}...")
            interacoes["posts_visualizados"] += 1

        elif opcao == "3":
            user = input("Informe o código do outro usuário: ").strip()
            print(f"Filtrando posts do usuário {user}...")
            interacoes["posts_visualizados"] += 1

        elif opcao == "4":
            print("Criando novo post...")
            interacoes["posts_criados"] += 1

        elif opcao == "5":
            print("Saindo...")
            print("\n=== RESUMO DAS INTERAÇÕES ===")
            print(f"Posts visualizados: {interacoes['posts_visualizados']}")
            print(f"Comentários visualizados: {interacoes['comentarios_visualizados']}")
            print(f"Posts criados: {interacoes['posts_criados']}")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()


