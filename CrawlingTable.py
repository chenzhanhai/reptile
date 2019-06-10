# Author Zhanhai

import requests

from pyquery import PyQuery as pq

def get_page(url):
    """发起请求 获得源码"""
    r = requests.get(url)
    r.encoding = 'utf8'
    html = r.text
    return html

def parse(text):
    doc = pq(text)
    # 获得每一行的tr标签
    tds = doc('table.table tbody tr.alt').items()
    with open('collegelist.csv', 'a+', encoding='utf8') as f:
        for td in tds:
            rank = td.find('td:first-child').text()
            name = td.find('div').text()
            city = td.find('td:nth-child(3)').text()
            score = td.find('td:nth-child(4)').text()
            f.write(rank + ',')
            f.write(name + ',')
            f.write(city + ',')
            f.write(score + ',\n')
    print("complete!")

if __name__ == "__main__":
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html"
    text = get_page(url)
    parse(text)