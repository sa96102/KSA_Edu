import requests
import lxml.html

response = requests.get('http://www.hanbit.co.kr/store/books/new_book_list.html')
root = lxml.html.fromstring(response.content)
root.make_links_absolute(response.url)
for a in root.cssselect('.view_box a'):
    url = a.get('href')
    if "javascript:;" in url:
        continue
    else:
        print(url)
