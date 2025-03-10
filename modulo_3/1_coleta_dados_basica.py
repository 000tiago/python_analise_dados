import requests
from bs4 import BeautifulSoup
import pandas

# Criando uma variável para armazenar a URL
url = 'https://kantaribopemedia.com/conteudo/dados-rankings/audiencia-de-tv-pnt-top-10-24-02-25-a-02-03-25'

# Realizando uma requisição GET para acessar o conteúdo da página
print('Request: ')
response = requests.get(url)  # Envia a requisição HTTP para a URL
print(response.text[:600])  # Exibe os primeiros 600 caracteres do HTML bruto da página, em texto corrido

# Analizando o HTML com BeautifulSoup
print('BeautifulSoups: ')
soup = BeautifulSoup(response.text, 'html.parser')  # Utiliza o parser para analisar o HTML
print(soup.prettify()[:600])  # Exibe os primeiros 600 caracteres do HTML formatado de forma legível, pulando linha

# Extraindo tabelas HTML com pandas
print('Pandas: ')
url_dados = pandas.read_html(url)  # Lê todas as tabelas HTML da página e as armazena como DataFrames
print(url_dados[1].head(10))  # Exibe as primeiras 10 linhas da segunda tabela encontrada (índice 1)
