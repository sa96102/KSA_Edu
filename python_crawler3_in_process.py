import requests
import lxml.html

def main():
    session = requests.Session()
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)

    for url in urls:
    if url != "":
        print(url)
