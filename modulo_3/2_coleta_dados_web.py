import requests
from bs4 import BeautifulSoup

# -------------------------
# Configuração da URL e requisição
# -------------------------
url = 'https://wiki.python.org.br'  # URL da página para extração
requisicao = requests.get(url)  # Envia uma requisição HTTP GET para a URL e obtém a resposta
extracao = BeautifulSoup(requisicao.text, 'html.parser')  # Analisa o HTML da resposta usando BeautifulSoup

# -------------------------
# Contando as tags <h2>
# -------------------------
h2_tags = extracao.find_all('h2')  # Encontra todas as tags <h2> e atribui a uma variável
quantidade_h2 = len(h2_tags)  # Conta o número de tags <h2> e atribui o valor a uma variável
print(f"\nQuantidade de tags <h2>: {quantidade_h2}\n")

# Exibindo o conteúdo das tags <h2>
for h2 in h2_tags:
    print(f"Conteúdo da tag <h2>: {h2.text.strip()}") # Pega o texto dentro da tag <h2> e remove espaços em branco indesejados

# -------------------------
# Contando as tags <p>
# -------------------------
p_tags = extracao.find_all('p')  # Encontra todas as tags <p>
quantidade_p = len(p_tags)  # Conta o número de tags <p>
print(f"\nQuantidade de parágrafos: {quantidade_p}\n")

for p in p_tags:
    print(f"Conteúdo do parágrafo: {p.text.strip()}")

# -------------------------
# Contar quantidade de títulos e parágrafos no total
# -------------------------
contar_titulo = 0
contar_paragrafo = 0

for linha_texto in extracao.find_all(['h2', 'p']):
    if linha_texto.name == 'h2':
        contar_titulo += 1  # contar_titulos = contar_titulos + 1
    elif linha_texto.name == 'p':
        contar_paragrafo += 1  # contar_paragrafo = contar_paragrafo + 1

print(f"\nTotal títulos: {contar_titulo}")
print(f"Total parágrafos: {contar_paragrafo}")
