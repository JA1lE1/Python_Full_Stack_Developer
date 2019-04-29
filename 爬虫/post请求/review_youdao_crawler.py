# -*-coding:utf-8-*-
import time
import random
import hashlib
import requests
import json
'''
1. 需求:爬取有道词典的翻译返回值，当然是有输入(post请求)的前提下
2. 通过在有道翻译主页键入你好在chrome浏览器查找的Network中找到transxxx的请求，
3. Header 中 Request Method：POST,请求参数均在Headers中，只是有hash加密方式
4. 在Response中找到对应的json,确实有对应的hello，也就是只用post方式正确，提取Response的json中对应的值即可
5. 可以通过对比发现在post请求的From Data中 salt，sign，ts，bv均是 需求“查找”(反爬)的加密内容
6. 反爬机制一般可以在js文件中找到，这里在Sources中居然直接找到-fanyi.mini.js了！（不知道其他的在线翻译是怎样的机制）
7. 在fanyi.mini.js中同时找到ts,bv,salt,sign的有关加密内容。打断点debug查看加密方法的raw_data
8. sign:(""fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE""), 其中e是请求翻译的内容（输入值） i是
    e = 输入请求值
    t = n.md5("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36")
    r = "" + (new Date).getTime()
    i = r + parseInt(10 * Math.random(), 10);
    # 需将以上的js内容翻译成python代码
    ts = r  ## 应该是实时时间
    bv = t  ## 应该是客户端信息的md5加密
    salt = i ## 应该是实时时间+随机数


建类
    1. 属性
        1. 客户端信息
            1. 浏览器信息-"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
            2. 输入请求值- "待用户输入内容"
        2. Request需求信息
            1. url- Request URL: "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
            2. "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
        3. From_data
            "i": "你好"
            "from": "AUTO"
            "to": "AUTO"
            "smartresult": "dict"
            "client": "fanyideskweb"
            "salt": ""
            "sign": ""
            "ts": ""
            "bv": ""
            "doctype": "json"
            "version": "2.1"
            "keyfrom": "fanyi.web"
            "action": "FY_BY_REALTlME"
        4. Request_Headers:
            "Accept": "application/json, text/javascript, */*; q=0.01"
            "Accept-Encoding": "gzip", "deflate"
            "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7"
            "Connection": "keep-alive"
            "Content-Length": "251"
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8""
            "Cookie": "OUTFOX_SEARCH_USER_ID=1750965659@110.81.205.10; P_INFO=null; OUTFOX_SEARCH_USER_ID_NCOO=1885664988.2268775; YOUDAO_MOBILE_ACCESS_TYPE=1; JSESSIONID=aaa7JfwJheHAAggGDmNPw; ___rl__test__cookies=1556509551025"
            "Host": "fanyi.youdao.com"
            "Origin": "http://fanyi.youdao.com"
            "Referer": "http://fanyi.youdao.com/"
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"
            "X-Requested-With": "XMLHttpRequest"

## 草稿
1556510283850
15565102838505

## 说明
- 代码为RAW版 未整理
'''

class review_youdao:
    def __init__(self, From_data, Request_Headers, Request_url):
        self.From_data = From_data
        self.Request_Headers = Request_Headers
        self.Request_url = Request_url

    def run(self,):
        r = requests.post(self.Request_url, data=self.From_data, headers=self.Request_Headers)
        result = json.loads(r.text)
        # result = result['translateResult'][0][0]["tgt"]          # 仔细看json的内容为两个0
        result = result['translateResult'][0][0]["tgt"]
        
        return result




def data_prepare(input_data):
    # r = "" + (new Date).getTime()
    # i = r + parseInt(10 * Math.random(), 10);
    #8. sign:(""fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE""), 其中e是请求翻译的内容（输入值） i是
    # e = 输入请求值
    # t = n.md5("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36")
    # r = "" + (new Date).getTime()
    # i = r + parseInt(10 * Math.random(), 10);
    # # 需将以上的js内容翻译成python代码
    # ts = r  ## 应该是实时时间
    # bv = t  ## 应该是客户端信息的md5加密
    # salt = i ## 应该是实时时间+随机数
    r = str(int(time.time()*1000))
    i = r + str(random.randint(0,10))        ## 可能有误
    t = hashlib.md5(b"5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36").hexdigest()
    e = input_data         ## 这个地方需要考虑编码的问题吗？
    ts = r
    bv = t
    salt = i
    sign = hashlib.md5(("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE").encode('utf-8')).hexdigest()

    From_data = {
        "i": e,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "bv": bv,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    Request_Headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        #"Accept-Encoding": "gzip", "deflate",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Connection": "keep-alive",
        "Content-Length": str(len(input_data)),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=1750965659@110.81.205.10; P_INFO=null; OUTFOX_SEARCH_USER_ID_NCOO=1885664988.2268775; YOUDAO_MOBILE_ACCESS_TYPE=1; JSESSIONID=aaa7JfwJheHAAggGDmNPw; ___rl__test__cookies=1556509551025",
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }


    Request_url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    return From_data, Request_Headers, Request_url


if __name__ == "__main__":
    input_data = input("请输入所要翻译的内容:")    ### 这里需要转换类型？
    From_data, Request_Headers, Request_url = data_prepare(input_data)
    spider = review_youdao(From_data, Request_Headers, Request_url)
    result = spider.run()
    print("有道翻译的结果为:{}".format(result))









