# 有道翻译爬虫

-------

2019.4.29

---------------

- 不看上次笔记自行练习一次，再对比笔记查缺补漏

## Review

### 代码之前的分析

\1. 需求:爬取有道词典的翻译返回值，当然是有输入(post请求)的前提下

\2. 通过在有道翻译主页键入你好在chrome浏览器查找的Network中找到transxxx的请求，

\3. Header 中 Request Method：POST,请求参数均在Headers中，只是有hash加密方式

\4. 在Response中找到对应的json,确实有对应的hello，也就是只用post方式正确，提取Response的json中对应的值即可

\5. 可以通过对比发现在post请求的From Data中 salt，sign，ts，bv均是 需求“查找”(反爬)的加密内容

\6. 反爬机制一般可以在js文件中找到，这里在Sources中居然直接找到-fanyi.mini.js了！（不知道其他的在线翻译是怎样的机制）

\7. 在fanyi.mini.js中同时找到ts,bv,salt,sign的有关加密内容。打断点debug查看加密方法的raw_data

\8. sign:(""fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE""), 其中e是请求翻译的内容（输入值） i是

​    e = 输入请求值

​    t = n.md5("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36")

​    r = "" + (new Date).getTime()

​    i = r + parseInt(10 * Math.random(), 10);

​    \# 需将以上的js内容翻译成python代码

​    ts = r  ## 应该是实时时间

​    bv = t  ## 应该是客户端信息的md5加密

​    salt = i ## 应该是实时时间+随机数





### 遇到的问题

- 请求需要get还是直接post，post里面是只有fromdata还是url+headers+from_data
  - 这里我瞧了一眼代码，它把所有的Headers都加进去了，准确的说是Request_Headers
  - ==疑问==
    - ==如果我需要大量的请求，那么我应该要有其他的cookie或者是代理防止被封，如何？==
  
- ==字符串的输出==

  - 将它作为元组传递：

    ```python
    print("Total score for %s is %s  " % (name, score))
    ```

    或使用新样式字符串格式：

    ```python
    print("Total score for {} is {}".format(name, score))
    ```

    或者传递值作为参数，打印将做它：

    ```python
    print("Total score for", name, "is", score)
    ```

    如果不希望通过打印自动插入空格，请更改sep参数：

    ```python
    print("Total score for ", name, " is ", score, sep='')
    ```

  - ==我比较习惯用"sdasfs{}".format(xxxx) 这种方法==

#### 代码解读

```python
        sign = hashlib.md5(('fanyideskweb' + input_info + salt + '1L5ja}w$puC.v_Kz3@yYn').encode('utf-8')).hexdigest()  # 获取Post请求的sign参数

```

- 这个地方为什么需要encode？
  - ==str.encode('utf-8')的返回值是bytes类型?==
- 什么使用用encode，什么使用用decode?

### hashlib

- 字符串

  - +b + u +r
    - [参考](<https://blog.csdn.net/qq_16234613/article/details/79448203>)
      - 这个参考也可作为字符串之间的转换

- ==输入参数必须是b+'str'?== 转成bytes类型？

  - ```python
    type(b'str')
    <class 'bytes'>
    ```

  
  - ```python
    type('str'.encode('utf-8'))
    <class 'bytes'>
    ```
  
  - 



### get

- 字典元素之间需要加=='逗号'== ，==最后一个元素需要加逗号吗？==

### request

- r(response)
  - r.content :point_right: 二进制内容
  - r.text :point_right: 获取响应内容
- ==自带的json方法貌似不带好用==
  - 使用json.loads(r.text)来解决

### json

- json.loads 和json.load 有什么区别？


### Debug

- result
  {'errorCode': 50}

#### 经验

- 参数
  - 所以这个在设置参数的时候要格外注意，特别是代码拥有居多参数
  - 参数的格式错误
  - 编码问题
  - 可能前后不一致，code的过程中很有可能思路有了变化



---

## 源
- [本代码fork地址](https://github.com/a15572775981/youdao/blob/master/youdao_crawler.py)
## 问题
- 如何得知post请求参数的加密方法

## 想法
- 对比微信请求的加密方法，学习hashlib.md5的加密方法

---

## 爬虫

### post模块

#### 图

- ![image](.\pictures\爬虫\Network-post.png)

- request 返回要么是str 要么是byte类型
- jason.loads
- jason.downs?



### 新的思路

- 由于post模板可能会遇到很多的加密sign或者token，因此需要学习hashlib.md5等 进行学习

  - [参考github有道翻译post](<https://github.com/a15572775981/youdao/blob/master/youdao_crawler.py>)
  - 对于加密内容破解的学习应该也是爬虫的重点之一

- ==有道翻译的反爬机制==

  - [参考1](<https://www.jianshu.com/p/71e7d6b147fd>)

    - 介绍的方法与自己的基本一致，通过chrome分析，Network查看网络请求，找到post的Fromdata

    - 找到response确实存在我们所需要的json文件（网站服务器的返回值）

    - 对post请求参数-from_data进行分析，salt和ts应该说是==先验证知识得知？== 还是和sign一样都是在后面的分析中得到的

    - 对于sign的解密过程

      - 这个地方我看不懂的是他在分析elements审查元素的时候，为什么需要去找所有的**js文件**

      - ==网页中的js文件是用来做什么的==

        - 加密都是通过JS?

      - ==在sources-page下==

        - 直接ctrl+f找对应的js 然后下面有 pretty-print 左下角有对应的按钮，左上角有！提示

        - 通过在prettyed下的js查找sign

          - 找到如下代码

          - ```javascript
            define("newweb/common/service", ["./utils", "./md5", "./jquery-1.7"], function(e, t) {
                var n = e("./jquery-1.7");
                e("./utils");
                e("./md5");
                var r = function(e) {
                    var t = n.md5(navigator.appVersion)
                      , r = "" + (new Date).getTime()
                      , i = r + parseInt(10 * Math.random(), 10);
                    return {
                        ts: r,
                        bv: t,
                        salt: i,
                        sign: n.md5("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE")
                    }
                };
            ```

          - 好了sign是n的md5加密方式，ts直接就是时间戳了，salt是时间戳加上随机码了，bv就是navigator.appVersion的md编码了

            - 这个地方是*user_agent* 去掉前面的Mozilla 但是这是如何得知的呢
            - ==Mozilla的先验知识==
            - ==这个地方我没有找到e的定义在哪里，但是意义知道的是它是输入值，因此可以猜测是用户的输入请求值==

        - 搜索translate得到下面的

  - [参考2](<https://tangx1.com/youdao/>)

    - 我直接从这个中get到了新的思路--chrome大法好，chrome居然还可以调试代码，强无敌！
    - 依然在Sources下找==与加密有关的js文件==，当然已经知道是**fanyi.min.js**
    - 在 sign: n.md5("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE") 这一行打断点，**直接点左边的8318即可**打断点效果如下图
    - ![image](.\pictures\爬虫\chrome_debug.png)
    - ![image](.\pictures\爬虫\chrome_debug_1.png)
    - ![image](.\pictures\爬虫\chrome_debug_2.png)
    - ==在chrome的调试环境下鼠标移到变量e还能直接显示变量值==，简直了，当然在右边的Scope的Local变量里面也能看到
    - ==还有鼠标移到navigator.appVersion也看到了bv的raw_data== 上面的问题也解决了
    - ==新get==
      - 貌似fanyi.min.js 是直接打开Sources就看到了然后直接pretty然后就。。。。。

  - [参考3](<http://www.zhongruitech.com/840050082.html>)

    - 前两个是对于反爬机制的探索，这个可以对代码的写作思路提供一种方法，方便下次练习使用

  - [参考4](http://liujunworld.com/2018/05/07/python3爬虫与GUI-基于有道词典的词典小工具/)

    - 参考4提供了找js的方法(用火狐浏览器)，这个可能以后有用！
    - 提供了GUI的方式，对Further work也是一种思路

### 遇到的问题

- cookie 写

- 写headers或者是post-data时经常少了**逗号**

- ```python
   sign = hashlib.md5(('fanyideskweb' + input_info + salt + '1L5ja}w$puC.v_Kz3@yYn').encode('utf-8')).hexdigest()  # 获取Post请求的sign参数
  # 这句为本次爬虫学习的重点
  ```

- ```
  define("newweb/common/requestMoreTrans", ["./service", "./utils", "./md5", "./jquery-1.7"], function(e, t) {
      var n = e("./jquery-1.7")
        , r = e("./service");
      e("./utils");
      e("./md5");
      var i = null;
      t.asyRequest = function(e) {
          var t = e.i
            , o = r.generateSaltSign(t);
          i && i.abort(),
          i = n.ajax({
              type: "POST",
              contentType: "application/x-www-form-urlencoded; charset=UTF-8",
              url: "/bbk/translate_m.do",
              data: {
                  i: e.i,
                  client: e.client,
                  salt: o.salt,
                  sign: o.sign,
                  ts: o.ts,
                  bv: o.bv,
                  tgt: e.tgt,
                  from: e.from,
                  to: e.to,
                  doctype: "json",
                  version: "3.0",
                  cache: !0
              },
              dataType: "json",
              success: function(t) {
                  t && 0 == t.errorCode ? e.success && e.success(t) : e.error && e.error(t)
              },
              error: function(e) {}
          })
      }
  }),
  ```

- 注意data的部分



### get

- [yanpy](<https://github.com/a15572775981?tab=repositories>) 这个人目前应该是主要在学爬虫可借鉴其
- [github](https://github.com/search?o=desc&q=翻译爬虫&s=updated&type=Repositories) 搜索翻译爬虫 摘取他人目前在翻译api上的爬虫工作



### 解密技术

- js解密sign参数： 通过execjs加载网页js加密sign参数相关代码，提取sign参数值？





### 解决的曙光

- 谷歌 hashlib 有道翻译



### Future work

- hashlib的学习使用

- 结合==参考3==  进行下面的练习(前提是对于反爬机制已经了如指掌，参考1，==参考2==)

- 金山词霸的练习

- 百度翻译的练习

- 谷歌翻译的练习

- **GUI**(==参考4==) 估计没时间做

  



## 