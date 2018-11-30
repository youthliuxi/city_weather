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


def insert(url):
    conn = mysql.connector.connect(user='root', password='612', database='city_weather') 
    cursor = conn.cursor()

    html = getHtml(url)

    soup = BeautifulSoup(html,"html.parser")
    # print(soup)
    div = soup.find_all(class_ ="citybox")

    provinces = div[0].find_all('h2')
    # print(div_one)
    i = 4
    for province in provinces:
        # print(province.encode('utf-8'))
        # print(province.next_sibling)
        i += 1
        if i <= 4 :
            cities = province.next_sibling.find_all('a')
            for city in cities:
                # print(city.get_text())
                pass
        else:
            # province_childs = province.next_sibling.children
            # for province_child in province_childs:
            #     # print(province_child.name)
            #     if (province_child.name)
            cities = province.next_sibling.find_all('h3')
            for city in cities:
                city_name = city.find_all('a')[0]
                print(city_name)
                counties_list = city.find_next_siblings()
                for county in counties_list:
                    if county.name == "h3":
                        break
                    print(county.get_text())
        

    #     query = "insert into `csdn_note` values(0,'"+MySQLdb.escape_string(insert_title)+"','"+MySQLdb.escape_string(insert_author)+"','"+MySQLdb.escape_string(insert_content)+"');"
    #     # print(query)
    #     cursor.execute(query)
    #     conn.commit()
    #     # break

    cursor.close()
    conn.close()
# CREATE TABLE `cities` (
#   `id` int(11) NOT NULL,
#   `province_id` int(11) NOT NULL,
#   `city` char(20) NOT NULL
# ) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='id';
# CREATE TABLE `counties` (
#   `id` int(11) NOT NULL,
#   `city_id` int(11) NOT NULL,
#   `county` char(20) NOT NULL
# ) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='id';
# CREATE TABLE `provinces` (
#   `id` int(11) NOT NULL,
#   `province` char(20) NOT NULL
# ) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='id';
    
if __name__ == '__main__':
    url = "http://www.tianqi.com/chinacity.html"
    insert(url)