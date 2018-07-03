import requests
from bs4 import BeautifulSoup

url = r"GALERIAS/Colaboradores no Oi Bowl Jam.html"
page = open(url)
soup = BeautifulSoup(page.read(), "lxml")

cities = soup.find_all('img', {'class' : 'lum-content-introduction-image lum-primary-name-thumbnail'})

img_nova = ''
for city in cities:
    img = city.attrs['src']
    img = img[1:]
    nome_img = img[83:]
    if (img != img_nova):
        img_nova = img
        print (img)
        r = requests.get(img, allow_redirects=True)
        open(nome_img, 'wb').write(r.content)    
page.close    
