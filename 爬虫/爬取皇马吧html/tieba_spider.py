# -*-coding=utf-8-*-
"""
Wherever smart people work, doors are unlocked. -- Steve Wozniak
"""
#############
#需求分析
#1. 需要有url_list
#2. 需要get并且decode_url
#3. 保准html页面
##属性
# 通过分析贴吧url:https://tieba.baidu.com/f?ie=utf-8&kw=%E6%9B%BC%E8%81%94&fr=search
# 发现的是只需要修改kw(key_word)后面的str即可改变访问哪个贴吧
# pn = 0 代表第一页，pn = 50 带表第二页 ，依次类推
## 1. 贴吧的名字
## 2. 需要爬取的页数
## 3. requests请求头

## 方法
# 1.获取url
# 2.url get + decode
# 3.html保存

## 发现的问题
# 1. class name 后面不用()
# 2. request的get的url需要使用type(str)
# 3. 为什么存放url用的是list而不是例如tuple
#    - list是可变对象 而tuple是不可变的对象？
# 4.属性缺失爬虫的请求头
# 5. utf 经常写成uft

## 不熟练的地方
# 1. str 的 format
# 2. 类名需要使用大驼峰命名法
# 3. python 对文件的操作 with open 等用法
#############
import requests

class SpiderTieba:
    def __init__(self, name, page_num_total, headers):
        self.name = name
        self.page_num_total = page_num_total
        self.headers = headers
    
    def url_source(self):
        url_list = []
        for page_num in range(self.page_num_total):
            url_new = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'.format(self.name, page_num*50)
            url_list.append(url_new)
        return url_list
    
    def url_parse(self, url):
        response = requests.get(url=url, headers=self.headers)
        return response.content.decode()

    def save_html(self, url_parsed_file, page_num):
        '''[summary]
        
        Arguments:
            url_parsed_file {[html]} -- [description:url解析后的文件，由url_parse()返回结果得到]
            page_num {[number]} -- [description:页码]
        '''
        html_save_path = '.\{}吧的第{}页.html'.format(self.name, page_num)
        with open(html_save_path, "w", encoding = 'utf-8') as f:
            f.write(url_parsed_file)

    def run(self):
        url_list = self.url_source()
        for (page_num, url) in enumerate(url_list):
            self.save_html(self.url_parse(url), page_num+1)

if __name__ == "__main__":
    name = '皇马'
    page_num_total = 5
    headers = headers ={'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'} 
    
    Spider_Tieba_Huangma = SpiderTieba(name, page_num_total, headers)
    Spider_Tieba_Huangma.run()
        

