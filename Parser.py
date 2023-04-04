from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup
import requests # импортируем библиотеку requests

def parse():
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250' # передаем необходимы URL адрес
    page = requests.get(url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code) # смотрим ответ
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4

    films= soup.findAll('td', class_='titleColumn')
    ratings= soup.findAll('td', class_='ratingColumn imdbRating')
    list =[]
    slov={}
    count = len(films)
    for i in range(0,count):
        list.append(str(i+1)+". "+films[i].text[16:-8])
        slov.setdefault(list[i],ratings[i].text[1:-1])
    print(slov)
