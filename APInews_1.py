import os
import requests
from dotenv import load_dotenv
import json
from pathlib import Path

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
    HISTORICO_ARQUIVO = "historico.json"

    # Carrega histórico existente, se houver
    if Path(HISTORICO_ARQUIVO).exists():
        with open(HISTORICO_ARQUIVO, "r", encoding="utf-8") as f:
            historico = json.load(f)
    else:
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
            if not (1 <= limite <= 25):
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

            registro = {'tema': tema, 'quantidade': limite}
            historico.append(registro)

            # Salva no arquivo .json
            with open(HISTORICO_ARQUIVO, "w", encoding="utf-8") as f:
                json.dump(historico, f, indent=4, ensure_ascii=False)

        elif escolha.lower() == '2':
            if not historico:
                print("⚠️ Nenhuma busca registrada ainda.")
            else:
                print("\n📚 Histórico de Buscas:")
                for item in historico:
                    print(f"- Tema: {item['tema']} | Quantidade: {item['quantidade']}")

        elif escolha.lower() == '3':
            # Mostra resumo final ao sair
            print("\n📊 Resumo final das buscas:")

            total_buscas = len(historico)
            temas_agrupados = {}

            for item in historico:
                tema = item['tema'].lower()
                temas_agrupados[tema] = temas_agrupados.get(tema, 0) + item['quantidade']

            print(f"Total de buscas feitas: {total_buscas}")
            for tema, total in temas_agrupados.items():
                print(f"- Tema: {tema} | Total de notícias buscadas: {total}")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()