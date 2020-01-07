#!/usr/local/bin/python3
import requests
from bs4 import BeautifulSoup
url = 'http://158.69.76.135/level0.php'
parametros_del_form = {'id': '1160', 'holdthedoor': 'Enviar'}
for i in range(1, 1025):
    respuesta = requests.post(url, data=parametros_del_form)
soup = BeautifulSoup(respuesta.text, 'html.parser')
