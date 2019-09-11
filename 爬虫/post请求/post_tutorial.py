import requests

formdata = {
    "type":"AUTO",
    "i":"i love python",
    "doctype":"json",
    "xmlVersion":"1.8",
    "keyfrom":"fanyi.web",
    "ue":"UTF-8",
    "action":"FY_BY_ENTER",
    "typoResult":"true"
}
fromdata = {
    'i':'你还',
    'from':'AUTO',
    "to":"AUTO",
    "smartresult":"dict",
    "client": "fanyideskweb",
    "salt": "15562460270095",
    "sign": "8edac290116a503ef4ab0d7e876020a2",
    "ts": "1556246027009",
    "bv": "480d4d031d1b5d96a168887200f77a94",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME",
}

# url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

headers={ "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

response = requests.post(url, data = fromdata, headers = headers)

print (response.text)

# 如果是json文件可以直接显示
print (response.json())

# 'i': '你还'
# "from": "AUTO"
# "to": "AUTO"
# "smartresult": "dict"
# "client": "fanyideskweb"
# "salt": "15562460270095"
# "sign": "8edac290116a503ef4ab0d7e876020a2"
# "ts": "1556246027009"
# "bv": "480d4d031d1b5d96a168887200f77a94"
# "doctype": "json"
# "version": "2.1"
# "keyfrom": "fanyi.web"
# "action": "FY_BY_REALTlME"