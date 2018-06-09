import requests
import time
from bs4 import BeautifulSoup

NOT_EXIST = BeautifulSoup('<a>本文已被刪除</a>', 'lxml').a

url = 'https://www.ptt.cc/bbs/Soft_Job/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

max_index = soup.find_all('a', 'btn wide')
previous_page = max_index[1].get('href')
previous_index = int(previous_page.split('index')[1].split('.')[0])
articles = soup.find_all('div', 'r-ent')

PAGES = 20

for index in range(previous_index+1, previous_index - PAGES, -1):
    time.sleep(0.01)
    url = 'https://www.ptt.cc/bbs/Soft_Job/index'+str(index)+'.html'
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
            if push == "" or push[0] == "X":
                push = 0
            if push == "爆":
                push = 9999
            date = article.find('div', 'date').getText()
            author = article.find('div', 'author').getText()

            if int(push) > 50:
                print('%4s\t%s' % (push, title))
                print("https://www.ptt.cc"+link)
