import os
import requests
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env
load_dotenv()

# Lê a chave da NewsAPI do ambiente
API_KEY = os.getenv("API_KEI_NEWS")
URL = "https://newsapi.org/v2/everything"

def mostrar_menu():
    print("\n==== MENU DE CONSULTAS DE NOTÍCIAS ====")
    print("1. Buscar notícias por tema")
    print("2. Ver histórico de buscas")
    print("3. Sair")

def buscar_noticias(tema, limite):
    """Consulta a NewsAPI e retorna uma lista de dicionários com título, fonte e autor."""
    if not API_KEY:
        print("❌ API_KEY não encontrada. Verifique se está no .env.")
        return []

    params = {
        'q': tema,
        'pageSize': limite,
        'apiKey': API_KEY,
        'language': 'pt',
        'sortBy': 'publishedAt'
    }

    resposta = requests.get(URL, params=params)

    if resposta.status_code != 200:
        print(f"❌ Erro na requisição: {resposta.status_code}")
        return []

    dados = resposta.json()
    artigos = dados.get('articles', [])

    resultados = []
    for artigo in artigos:
        resultados.append({
            'titulo': artigo.get('title'),
            'fonte': artigo.get('source', {}).get('name'),
            'autor': artigo.get('author')
        })

    return resultados

def main():
    historico = []

    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ").strip()

        if escolha.lower() == '1':
            tema = input("Digite o tema da notícia: ").strip()

            if not tema:
                print("❌ Tema inválido. Tente novamente.")
                continue

            limite = input("Quantas notícias deseja buscar (máximo 25)? ").strip()

            if not limite.isdigit():
                print("❌ Digite apenas números inteiros.")
                continue

            limite = int(limite)
            if not (1 <= limite <= 100):
                print("❌ Valor fora do limite permitido (1 a 25).")
                continue

            tema_formatado = tema.lower()
            noticias = buscar_noticias(tema_formatado, limite)

            print(f"\n🔎 Resultados para: '{tema}'")
            if noticias:
                for i, noticia in enumerate(noticias, 1):
                    print(f"\n{i}. {noticia['titulo']}")
                    print(f"   Fonte: {noticia['fonte']} | Autor: {noticia['autor']}")
            else:
                print("Nenhuma notícia encontrada.")

            historico.append({'tema': tema, 'quantidade': limite})

        elif escolha.lower() == '2':
            if not historico:
                print("⚠️ Nenhuma busca registrada ainda.")
            else:
                print("\n📚 Histórico de Buscas:")
                for item in historico:
                    print(f"- Tema: {item['tema']} | Quantidade: {item['quantidade']}")

        elif escolha.lower() == '3':
            print("👋 Encerrando o programa. Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()