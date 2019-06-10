# Author Zhanhai

import urllib
from bs4 import BeautifulSoup
import traceback

def get_url_content(url):
    content = ""
    try:
        req = urllib.request.Request(url)
        req.add_header("GET",url)
        content = urllib.request.urlopen(req).read()
    except Exception as e:
            print(traceback.format_exc())
            raise
    return content

def get_data(list,html):
    soup = BeautifulSoup(html, "html.parser")
    infos = soup.find("ul",attrs={"class":"sellListContent"}).find_all('li')
    with open(r'lianjia.csv','a',encoding='utf-8') as f:
        for info in infos:
            name = info.find('div',{'class':'title'}).find('a').get_text()
            price =info.find('div',{'class':'priceInfo'}).find('div',{'class','totalPrice'}).find('span').get_text()
            f.write("{},{}\n".format(name, price))

def main():
    depth = 10
    info_list =[]
    for i in range(depth):
        url = start_url + str(i)
        html = get_url_content(url)
        get_data(info_list,html)

start_url = "https://bj.lianjia.com/ershoufang/pg"
main()