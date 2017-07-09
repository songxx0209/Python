
import urllib2, pymysql
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

response = urllib2.urlopen(url)
print response.getcode()

html_doc = response.read()

# print html_doc

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')

# links = soup.find_all('img')
# for link in links:
#   print link['src']

link_node = soup.find('img', width='270')
spider_url = link_node['src']

connect = pymysql.Connect(
    user='root',
    passwd='123456',
    db='test',
    charset='utf8'
)

cursor = connect.cursor()

# cursor.execute('create table spider (id varchar(20) primary key, url varchar(200))')
# cursor.execute('insert into spider (id, url) values (%s, %s)', ['1', spider_url])
# print(cursor.rowcount)
# connect.commit()
# cursor.close()

# 从数据库中拉取数据
cursor = connect.cursor()
cursor.execute('select * from spider where id = %s', ('1',))
values = cursor.fetchall()
print(values)

cursor.close()
connect.close()