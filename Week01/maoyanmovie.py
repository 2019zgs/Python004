import scrapy
from maoyan.items import MaoyanItem
from scrapy.selector import Selector
from lxml import etree
def remove(string):
   return "".join(string.split())

class MaoyanmovieSpider(scrapy.Spider):
    name = 'maoyanmovie'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films']
#本地验证
# from lxml import etree
# with open("C:/Users/86150/Python004/Week01/bs_info.html",'r',encoding='utf-8') as f:
#     content=f.read()
# selector=etree.HTML(content)
# content=selector.xpath('//div[@class="movie-hover-info"]')
# for movie in content:
#     movie_name=movie.xpath('./div[@class="movie-hover-title"]/span[@class="name noscore"]/text()|./div[@class="movie-hover-title"]/span[@class="name"]/text()')
#     movie_type=movie.xpath('./div[@class="movie-hover-title"][2]/text()')[1].strip()
#     movie_date=movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()')[1].strip()
#     print('电影名称：{} 电影类型: {} 电影上映时间: {} '.format(movie_name,movie_type,movie_date))

    def parse(self, response):
        content=Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in content:
            movie_nametmp=movie.xpath('./div[1]/span/text()')
            #电影名称
            movie_name="".join(movie_nametmp.extract())
            movie_typetmp=movie.xpath('./div[@class="movie-hover-title"][2]/text()')[1]
            #电影类型
            movie_type=remove(movie_typetmp.extract().strip())
            movie_datetmp=movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()')[1]
            #电影上映时间
            movie_date=(movie_datetmp.extract().strip())
            print('电影名称：{} 电影类型: {} 电影上映时间: {} '.format(movie_name,movie_type,movie_date))
            # print(movie_name)
            yield {
            'movie_name':movie_name,
            'movie_type':movie_type,
            'movie_date':movie_date
            }

        
