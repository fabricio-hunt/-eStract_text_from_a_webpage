import requests
from bs4 import BeautifulSoup
url = "https://www.bemol.com.br/ar-e-ventilacao"  # Substitua com a URL desejada
css_class = "description-category"  # Substitua com a classe CSS desejada
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/58.0.3029.110"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all(class_=css_class)

    # Abre um arquivo TXT para salvar o texto
    txt_file = open("output.txt", "w")
    for element in elements:
        txt_file.write(element.text + "\n")
    txt_file.close()
    print(f'Texto extraído e salvo em "{txt_file.name}".')
else:
    print(f'Falha ao acessar a URL. Código de status: {response.status_code}')
