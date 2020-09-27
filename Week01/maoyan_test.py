import requests
from bs4 import BeautifulSoup as bs
import csv
#要求安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。

#解析本地html
with open('./bs_info.html','r',encoding='utf-8') as f:
    content=f.read()
bs_info = bs(content,'html.parser')
#去除空格
def remove(string):
   return "".join(string.split())

for tags in bs_info.find_all('div',attrs={'class':'movie-hover-info'},limit=10):
    for tag in tags.find_all('span', attrs={'class': 'name'},limit=10):
        movie_name=(tag.text)
        #使用了contenst 方法 输出tag的所有内容为列表
        movie_type=(remove(tags.contents[3].text))
        movie_date=(remove(tags.contents[7].text))
        a_list="电影名称：{} {} {}".format(movie_name,movie_type,movie_date)
        print(a_list)
        #写入csv文件
        with open('./maoyan_movie.csv','a',encoding='utf-8',newline='') as f:
            w=csv.writer(f)
            w.writerow([movie_name,movie_type,movie_date])






            




       
            

                
        





        # for atag in tag.find_all('span',attrs={'class':'name'}):
        #     print(atag.text)

    
    
              
           
       

        
        


        
