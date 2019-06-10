# Author Zhanhai

import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def fillProgramList(programInfo, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            programInfo.append([tds[0].string, tds[1].string, tds[3].string,tds[4].string,tds[5].string])

def printProgramList(programInfo):
    print("{:^10}\t{:^10}\t{:^20}\t{:^10}\t{:^10}".format("2019","2018","Programming Language","Ratings","Change"))
    num = len(programInfo)
    for i in range(num):
        p = programInfo[i]
        print("{:^10}\t{:^10}\t{:^20}\t{:^10}\t{:^10}".format(p[0],p[1],p[2],p[3],p[4]))

def main():
    programInfo = []
    url = 'https://www.tiobe.com/tiobe-index/'
    html = getHTMLText(url)
    fillProgramList(programInfo, html)
    printProgramList(programInfo) # 20 programs

main()
