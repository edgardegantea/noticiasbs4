import requests
from bs4 import BeautifulSoup

# extraer datos de una pagina
website = 'https://www.milenio.com'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# Entrar a seccion que contiene bloques
layout = soup.find('section', class_="row")
print(layout)


# Entrar a seccion que contiene bloques
layout = soup.find('section', class_="ctr-modules-twelve")
# print(layout)

# Entrar a seccion que contiene articulos y mostrar su cantidad
blocks = layout.find_all(class_='sn-base-base-noheading', recursive=True)
print(len(blocks))

for block in blocks:
    for href in block.find('a', href=True):
        print('Titulo: ' + href.get_text())

        Noticia = block.find('li', class_='sn-base-base-noheading__abstract').get_text()
        print('Noticia: ' + Noticia)

        print()


