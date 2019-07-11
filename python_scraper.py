import sqlite3
import re
from urllib.request import urlopen
from html import unescape

def main():
    html = fetch('http://www.hanbit.co.kr/store/books/full_book_list.html')
    books = scrape(html)
    save('books.db', books)

def fetch(url):
    f = urlopen(url)
    encoding = f.info().get_content_charset(failobj="utf-8")
    html = f.read().decode(encoding)
    return html

def scrape(html):
    books = []
    for partial_html in re.findall('<td class="left"><a.*?</td>', html, re.DOTALL):
        url = re.search('<a href="(.*?)">', partial_html).group(1)
        url = 'http://www.hanbit.co.kr' + url
        title = re.sub('<.*?>','',partial_html)
        title = unescape(title)
        books.append({'url':url, 'title':title})
    return books

def save(db_path, books):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS books')
    c.execute('''
            CREATE TABLE books(
                    title text,
                    url text
            )
    ''')
    c.executemany('INSERT INTO books VALUES(:title,:url)', books)
    conn.commit()
    conn.close()
    

if __name__ == '__main__':
    main()
