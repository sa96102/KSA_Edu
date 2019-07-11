import re
import requests
import lxml.html

def main():
    session = requests.Session()
    response = session.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
    urls = scrape_list_page(response)

    for url in urls:
        response = session.get(url)
        ebook = scrape_detail_page(response)
        print(ebook)
        break

def scrape_list_page(response):
        root = lxml.html.fromstring(response.content)
        root.make_links_absolute(response.url)
        for a in root.cssselect('.view_box span a'):
            url = a.get('href')
            if "javascript:;" not in url:
                yield url

def scrape_detail_page(response):
    root = lxml.html.fromstring(response.content)
    ebook = {
        'url' : response.url,
        'title' : root.cssselect('.store_product_info_box h3')[0].text_content(),
        'price' : root.cssselect('.pbr strong')[0].text_content(),
        'content' : [p.text_content()\
                for p in root.cssselect('#tabs_3 .hanbit_edit_view p')]
    }
    return ebook

if __name__ == '__main__':
    main()
