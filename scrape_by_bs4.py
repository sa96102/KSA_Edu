from bs4 import BeautifulSoup

with open('full_book_list.html', encoding="utf-8") as f:
    soup = BeautifulSoup(f, 'html.parser')

for a in soup.find_all('a'):
    print(a.get('href'), a.text)
