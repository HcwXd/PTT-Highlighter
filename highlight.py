import requests
from bs4 import BeautifulSoup
from pretty_tools import pretty_print

NOT_EXIST = BeautifulSoup('<a>本文已被刪除</a>', 'lxml').a

url = 'https://www.ptt.cc/bbs/Soft_Job/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
articles = soup.find_all('div', 'r-ent')

for article in articles:
    meta = article.find('div', 'title').find('a')
    if meta == None:
        continue
    else:
        title = meta.getText().strip()
        link = meta.get('href')
        push = article.find('div', 'nrec').getText()
        if push == "":
            push = 0
        date = article.find('div', 'date').getText()
        author = article.find('div', 'author').getText()

        print(push, title, date, author)
