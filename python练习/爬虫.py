import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        return ''



wd=input('输入想要翻译的内容：')
#key=['en','']
url="https://fanyi.baidu.com/translate?aldtype=16047\
     &query=&keyfrom=baidu&smartresult=dict&lang=auto2zh#zh/en/"+str(wd)
r=getHTMLText(url)
print(r)
soup=BeautifulSoup(r.text)
print(soup)

input()

