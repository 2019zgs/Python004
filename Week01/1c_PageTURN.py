import requests
#import lxml.etree
from bs4 import BeautifulSoup as bs
def get_url_name(myurl):
    user_agent ='Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    header={'user-agent': user_agent}
    #myurl='https://movie.douban.com/top250'
    #使用request库的get方法
    response=requests.get(myurl,headers=header)
    bs_info=bs(response.text,'html.parser')
    #puthon 中使用for in 形式循环
    for tags in bs_info.find_all('div',attrs={'class':'hd'}):
        for atag in tags.find_all('a',):
            print(atag.get('href'))
            #获取所有连接
            print(atag.find('span',).text)
    #获取电影名
urls=tuple(f'https://movie.douban.com/top250?start={page * 25 }&filter' for page in range(10))

#print(f'urls 是：{urls}')

from time import sleep
sleep(10)
for page in urls:
    get_url_name(page)
    sleep(5)
# print(get_url_name('https://movie.douban.com/top250?start=25&filter'))
