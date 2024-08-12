import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

for start_num in range(0, 250, 25):

    response = requests.get(
        f'https://movie.douban.com/top250?start={start_num}', headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.findAll('span', attrs={'class': 'title'})
    all_quotes = soup.findAll('span', attrs={'class': 'inq'})

    # for title in all_titles:
    #     title_string = title.string
    #     if '/' not in title_string:
    #         print(title.string)

    for title, quote in zip(all_titles, all_quotes):
        title_string = title.string
        if '/' not in title_string:
            print('电影片名: ', title.string, "引言: ", quote.string)
