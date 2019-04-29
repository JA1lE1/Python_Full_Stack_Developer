# README



##  文件

- 写入

  - **write()** 方法用于向文件中写入指定字符串。

    在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。

    如果文件打开模式带 b，那写入文件内容时，str (参数)要用 encode 方法转为 bytes 形式，否则报错：TypeError: a bytes-like object is required, not 'str'。

  - ```
    #!/usr/bin/python
    # -*- coding: UTF-8 -*-
    
    # 打开文件
    fo = open("test.txt", "w")
    print "文件名为: ", fo.name
    str = "菜鸟教程"
    fo.write( str )
    
    # 关闭文件
    fo.close()
    ```





## 生成器与迭代器

- generator
- 参考
  - [知乎](<https://www.zhihu.com/question/20829330>)
    - 生成器是python的一大特点，它对于大规模文本的处理尤为有效
  - [中文博文](<https://foofish.net/iterators-vs-generators.html>)