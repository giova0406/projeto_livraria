from bs4 import BeautifulSoup
import requests
import csv

url =  'http://books.toscrape.com/'
resposta = requests.get(url) 

if resposta.status_code != 200:
    print('Erro na conexao')
    exit()
else:
    print('Conexao bem sucedida')

conteudo = resposta.text
soup = BeautifulSoup(conteudo, 'html.parser')
print(soup.title.text)

livros_html = soup.find_all('article', class_='product_pod')
print(len(livros_html))

dados_extraidos = []

for livro in livros_html:
    titulo = livro.find('h3').find('a')['title'] 
    preco = livro.find('p', class_='price_color').text

    livro_dict = {
        'titulo': titulo,
        'preco': preco
    }

    dados_extraidos.append(livro_dict)


with open('relatorio_livro.csv', 'w', newline='', encoding='utf-8') as arquivo:
    gravador = csv.DictWriter(arquivo, fieldnames=['titulo', 'preco'])

    gravador.writeheader()
    gravador.writerows(dados_extraidos)

print('Relatório CSV gerado com sucesso!')