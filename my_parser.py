from bs4 import BeautifulSoup
import urllib.request


class Parser:

    raw_html = None
    html = None
    results = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = urllib.request.urlopen(self.url)
        self.raw_html = req.read()
        self.html = BeautifulSoup(self.raw_html, 'html.parser')

    def parsing(self):
        news = self.html.find_all('li', class_='liga-news-item')
        for item in news:
            title = item.find('span', class_='d-block').get_text(strip=True)
            desc = item.find('span', class_='name-dop').get_text(strip=True)
            href = item.a.get('href')
            self.results.append({
                'title': title,
                'desc': desc,
                'href': href
            })

    def save(self):
        with open(self.path, 'w', encoding='utf-8') as f:
            for index, line in enumerate(self.results, start=1):
                f.write(
                    f'Новость № {index}\n\nНазвание: {line["title"]}\nОписание: {line["desc"]}\nСсылка: {line["href"]}\n\n**********\n')

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
