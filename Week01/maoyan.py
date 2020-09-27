#要求安装并使用 requests、bs4 库，爬取猫眼电影的前 10 个电影名称、电影类型和上映时间，并以 UTF-8 字符集保存到 csv 格式的文件中。
import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent
import csv
#代理用户
ua = UserAgent()
user_agent= ua.ie
# 模拟正常访问网页，避免反爬虫冲虚
header = {
    'Cookie': '__mta=213679019.1601002064466.1601018754510.1601018782223.13; uuid_n_v=v1; uuid=7B41A740FED911EA805853CB23A5B1A23E6478EBBBFC4E73ADAFC9434484779E; _lxsdk_cuid=174c328c850c8-0b0f49152c88aa-d373666-144000-174c328c850c8; _lxsdk=7B41A740FED911EA805853CB23A5B1A23E6478EBBBFC4E73ADAFC9434484779E; mojo-uuid=7dd284c3de1f067935c41bc6913ed21f; _csrf=a9938cc720c29b662c757ab399a50dbac39880e935d2cb1ed2f5549eba68d03c; mojo-session-id={"id":"185070e9757b4529d8c74b57403458c5","time":1601130642312}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1601003108,1601004777,1601019922,1601130642; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; mojo-trace-id=4; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1601131079; __mta=213679019.1601002064466.1601018782223.1601131078650.14; _lxsdk_s=174cad2bbf4-825-a3-7d0%7C%7C8',
    'user-agent': user_agent}

myurl = 'https://maoyan.com/films?showType=3'
#print(header)
#使用request库的get方法

response = requests.get(myurl, headers=header)
#print(f'返回的代码是： {response.status_code}')
bs_info = bs(response.text, 'html.parser')
#print(bs_info)
#print(bs_info)
# 将网页写入到文件，避免导致不能访问
# with open('./bs_info.html','a+',encoding='utf-8') as f:
#   f.write(str(bs_info))


#解析本地html
# with open('./bs_info.html','r',encoding='utf-8') as f:
#     content=f.read()
# bs_info = bs(content,'html.parser')
#去除空格
def remove(string):
   return "".join(string.split())

for tags in bs_info.find_all('div',attrs={'class':'movie-hover-info'},limit=10):
    #print(tags)
    for tag in tags.find_all('span', attrs={'class': 'name'},limit=10):
        movie_name=tag.text
        #使用了contenst 方法 输出tag的所有内容为列表
        movie_type=remove(tags.contents[3].text)
        movie_date=remove(tags.contents[7].text)
        a= "电影名称：{} {} {}".format(movie_name,movie_type,movie_date)
        #print(a)
        with open('./maoyan_movie.csv','a',encoding='utf-8',newline='') as f:
            w=csv.writer(f)
            w.writerow([movie_name,movie_type,movie_date])






            




       
            

                
        





        # for atag in tag.find_all('span',attrs={'class':'name'}):
        #     print(atag.text)

    
    
              
           
       

        
        


        

    
    
              
           
       

        
        


        
