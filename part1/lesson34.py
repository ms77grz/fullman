import urllib.request
from bs4 import BeautifulSoup


url = 'https://www.ua-football.com/sport'


def get_html(url):
    return urllib.request.urlopen(url).read()


soup = BeautifulSoup(get_html(url), 'html.parser')

news = soup.find_all('li', class_='liga-news-item')
results = []

for item in news:
    title = item.find('span', class_='d-block').get_text(strip=True)
    desc = item.find('span', class_='name-dop').get_text(strip=True)
    href = item.a.get('href')
    results.append({
        'title': title,
        'desc': desc,
        'href': href
    })

with open('news.txt', 'w', encoding='utf-8') as f:
    for index, line in enumerate(results, start=1):
        f.write(
            f'Новость № {index}\n\nНазвание: {line["title"]}\nОписание: {line["desc"]}\nСсылка: {line["href"]}\n\n**********\n'
        )
