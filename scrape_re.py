import re
from html import unescape

with open('dp.html') as f:
    html = f.read()

for partial_html in re.findall('<td class="left"><a.*?</td>', html, re.DOTALL):
    matched_url_str = re.search('<a href="(.*?)">', partial_html)
    url = matched_url_str.group(1)
    url = 'http://www.hanbit.co.kr' + url
    title = re.sub('<.*?>', '', partial_html)
    title = unescape(title)
    print('url:', url)
    print('title:', title)
    print('---')
