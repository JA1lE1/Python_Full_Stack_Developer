# -*-coding:utf-8-*-
import time
import hashlib
import random
import requests
import json

def define_data(url):
        """有道翻译"""
        input_info = str(input('请输入要翻译的内容:'))
        salt = str(int(time.time()*10000) + random.randint(1, 10))  # 获取Post请求的salt参数
        ts = str(int(time.time()*1000) + random.randint(1, 10))  # 获取Post请求的ts参数
        # print(salt)
        sign = hashlib.md5(('fanyideskweb' + input_info + salt + '1L5ja}w$puC.v_Kz3@yYn').encode('utf-8')).hexdigest()  # 获取Post请求的sign参数
        b = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
        # b = '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'  # 这个值需要替换成自己的浏览器的版本信息，版本信息可以查看user_agent，去掉前面的Mozilla/后面的就是，单值谷歌
        bv = hashlib.md5(b.encode('utf-8')).hexdigest()  # md5加密
        data = {
                'i': input_info,
                'from': 'AUTO',
                'to': 'AUTO',
                'smartresult': 'dict',
                'client': 'fanyideskweb',
                'salt': salt,
                'sign': sign,
                'ts': ts,
                'bv': bv,
                'doctype': 'json',
                'version': '2.1',
                'keyfrom': 'fanyi.web',
                'action': 'FY_BY_REALTlME',
                'typoResult': 'false',
        }

        headers = {
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                # 'Accept-Encoding': 'gzip, deflate',  # 可不要
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Connection': 'keep-alive',
                'Content-Length': '271',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Cookie':'OUTFOX_SEARCH_USER_ID=1750965659@110.81.205.10; P_INFO=null; JSESSIONID=aaa_YsfzNXFsx6rsnBxPw; OUTFOX_SEARCH_USER_ID_NCOO=1885664988.2268775; YOUDAO_MOBILE_ACCESS_TYPE=1; ___rl__test__cookies=1556247687874',
                # 'Cookie': '定义成你自己的cookie，cookie不能少否则请求不到数据',
                'Host': 'fanyi.youdao.com',
                'Origin': 'http://fanyi.youdao.com',
                'Referer': 'http://fanyi.youdao.com/',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
                # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
}

        response = requests.post(url=url, data=data, headers=headers).text  # 请求翻译页
        res = json.loads(response)  # 转换成json格式
        result = res['translateResult'][0][0]["tgt"]  # 取出值
        print('译文：', result)

if __name__ == '__main__':
        url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        define_data(url)