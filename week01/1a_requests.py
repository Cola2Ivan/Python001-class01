import requests
from bs4 import BeautifulSoup as bs
import lxml

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = { 'user-agent':user_agent}

# myurl = 'https://movie.douban.com/top250'
url_detail = 'https://movie.douban.com/subject/1292052/'

# response = requests.get(myurl,headers=header)
response = requests.get(url_detail,headers=header)

#打印对应信息
# print(response.text)
# print(f'返回码是:{response.status_code}')

#beautiful soup 4使用
# bs_info = bs(response.text,'html.parser')

# for tags in bs_info.find_all('div',attrs={'class': 'hd'}):
#     for atag in tags.find_all('a',):
#         #获取链接
#         print(atag.get('href'))
#         #获取名称
#         print(atag.find('span',).text)

#lxml使用
#xml化处理
selector = lxml.etree.HTML(response.text)

#电影名称
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')
print(f'电影名称：{film_name}')

#上映日期
plan_data = selector.xpath('//*[@id="info"]/span[10]/text()')
print(f'上映日期：{plan_data}')

#评分
rating = selector.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
print(f'评分:{rating}')

mylist = [film_name,plan_data,rating]

#数据保存
# import pandas as pd

# movie1 = pd.DataFrame(data = mylist)

# movie1.to_csv('.\movies.csv',encoding='gbk',index=False,header=False)

#自动翻页
def get_url_name(myurl):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    header = { 'user-agent':user_agent}

    response = requests.get(myurl,headers=header)

    bs_info = bs(response.text,'html.parser')
    for tags in bs_info.find_all('div',attrs={'class': 'hd'}):
        for atag in tags.find_all('a',):
            #获取链接
            print(atag.get('href'))
            #获取名称
            print(atag.find('span',).text)

#生成包含所有页面的元组
#推导式写法
urls= tuple(f'https://movie.douban.com/top250?start={ page *25 }&filter=' for page in range(10))

print(urls)

# 控制请求的频率，引入了time模块
from time import sleep

sleep(20)

for page in urls:
    get_url_name(page)
    sleep(20)