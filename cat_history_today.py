# -*- coding: utf-8 -*-
import io
import sys
import mysql.connector
import urllib2 as urllib
# import MySQLdb
import requests  
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

def getHtml(url):
    request = urllib.Request(url)
    page = urllib.urlopen(request)
    html = page.read()
    return html


def insert(url_md):
    conn = mysql.connector.connect(user='root', password='', database='city_weather') 
    cursor = conn.cursor()
    url = "http://www.tianqi.com/index.php?c=history&md=%s" % url_md
    html = getHtml(url)

    soup = BeautifulSoup(html,"html.parser")
    # print(soup)
    li_all = soup.select('ul > a > li')
    for li in li_all:
        event_all = li.get_text().split(' ')
        history_date = event_all[0].encode('utf-8')
        event = event_all[1].encode('utf-8')
        query = "insert into `history_today`( `date`, `history_date`,`event`) values ('%s','%s','%s');" % (url_md,history_date,event)
        # print(query)
        cursor.execute(query)
        conn.commit()

    cursor.close()
    conn.close()
# CREATE TABLE `history_today` (
#   `id` int(11) NOT NULL AUTO_INCREMENT primary key,
#   `date` char(11) NOT NULL,
#   `history_date` char(20) NOT NULL,
#   `event` text NOT NULL
# ) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='id';
    
if __name__ == '__main__':
    month = [31,29,31,30,31,30,31,31,30,31,30,31] # 闰年
    md = []
    for i in range(0,12):
        for j in range(0,month[i]):
            md.append(str(i+1).zfill(2)+str(j+1).zfill(2))
    # print(md)
    for url_md in md:
        insert(url_md)
        print(url_md)
