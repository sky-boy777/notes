import requests
import re
import json

url = "http://www.haha56.net/xiaohua/neihan/"
headers = {
    "Referer": "http://www.haha56.net/xiaohua/neihan/",
    "Sec-Fetch-Dest": "image",
    "Sec-Fetch-Mode": "no-cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36"
     }

html = requests.get(url, headers = headers)
html_str = html.content.decode("gbk")

#替换
html_str = re.sub(r"(\s|&rdquo;|&ldquo;|&lsquo;|<br />\\n)", "", html_str)

#匹配
html_list = re.findall("<p>(.*?)</p>|<hr />(.*?)<hr />", html_str, re.S)
print(html_list)

with open("段子.txt", "w", encoding="utf-8") as f:
    for i in html_list:
        f.write(json.dumps(i, ensure_ascii=False))
        f.write("\n\n")


