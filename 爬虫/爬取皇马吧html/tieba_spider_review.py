# -*-coding=utf-8-*-
"""
Wherever smart people work, doors are unlocked. -- Steve Wozniak
"""

# 爬取曼联吧的前五页

#一个类 spider_tieba
## 属性包括 name,headers,total_num_page
## 方法包括 get_url, parse_url, save_html,run

import requests

class spider_tieba_review:
    def __init__(self, name, headers, total_num_page):
        self.name = name
        self.headers = headers
        self.total_num_page = total_num_page

    def get_url(self):
        url_list = []
        for i in range(self.total_num_page):
            url = 'https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={:d}'.format(self.name, i*50)
            url_list.append(url)
        return url_list
    
    def url_parse(self, url_raw):
        r = requests.get(url_raw, headers=self.headers)
        return r.content.decode()

    def save_html(self, page_num, url_get_parsed):
        with open('{}吧的第{}页.html'.format(self.name,page_num),'w',encoding='utf-8') as f:
            f.write(url_get_parsed)


    def run(self):
        for page_num, url in enumerate(self.get_url()):
            self.save_html(page_num+1, self.url_parse(url))

if __name__ == "__main__":
    name = '曼联'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    total_num_page = 5
    tieba_MU_spider = spider_tieba_review(name=name, headers=headers,total_num_page = total_num_page)
    tieba_MU_spider.run()

## 写在后面
## 需要啊再次对比 总结