# noticias_app.py

def mostrar_menu():
    print("\n==== MENU DE CONSULTAS DE NOTÍCIAS ====")
    print("1. Buscar notícias por tema")
    print("2. Ver histórico de buscas")
    print("3. Sair")


def main():
    historico = []

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            tema = input("Digite o tema da notícia: ")
            limite = input("Quantas notícias deseja buscar (máximo 100)? ")

            # Validação simples
            if not limite.isdigit() or int(limite) < 1 or int(limite) > 100:
                print("Número inválido. Digite entre 1 e 100.")
                continue

            # Aqui depois vamos chamar a função de busca na API
            print(f"Consultando notícias sobre: {tema}...")

            # Armazena no histórico
            historico.append({'tema': tema, 'quantidade': int(limite)})

        elif escolha == '2':
            if not historico:
                print("Nenhuma busca feita ainda.")
            else:
                print("\n=== HISTÓRICO DE BUSCAS ===")
                for item in historico:
                    print(f"Tema: {item['tema']} - Quantidade: {item['quantidade']}")

        elif escolha == '3':
            print("Encerrando o programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()