from logger import setup_logger
from browser import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd


logger = setup_logger(__name__)


def main():
    browser = Browser()
    result_ = []
    for i in range(1, 51):
        logger.info(f"running page: {i}")
        url = f"https://books.toscrape.com/catalogue/page-{i}.html"
        response = browser.get(url)
        soup = bs(response.content, 'html.parser')
        books = soup.find_all('article')
        for book in books:
            linq = book.find('a')['href']
            link = "https://books.toscrape.com/"+linq
            title = book.find('h3').find('a')['title']
            price = book.find('p', class_='price_color').get_text()[1:]
            result = {
                'title': title,
                'price': price,
                'link': link
            }
            result_.append(result)

    return result_


if __name__ == '__main__':
    results = main()
    df = pd.DataFrame(results)
    df.to_csv('data.csv', index=False)

