from lxml import etree
with open("C:/Users/86150/Python004/Week01/bs_info.html",'r',encoding='utf-8') as f:
    content=f.read()
selector=etree.HTML(content)
content=selector.xpath('//div[@class="movie-hover-info"]')
for movie in content:
    movie_name=movie.xpath('./div[@class="movie-hover-title"]/span[@class="name noscore"]/text()|./div[@class="movie-hover-title"]/span[@class="name"]/text()')
    # movie_type=movie.xpath('./div[@class="movie-hover-title"][2]/text()')[1].strip()
    # movie_date=movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()')[1].strip()
    # print('电影名称：{} 电影类型: {} 电影上映时间: {} '.format(movie_name,movie_type,movie_date))
    print(movie_name)