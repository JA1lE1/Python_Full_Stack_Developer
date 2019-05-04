# README

## 第一章 Hello，World

- [Miguel Grinberg的blog](https://blog.miguelgrinberg.com/)的[2017年新版The Flask Mega-Tutorial教程](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [中文参考文档](<https://github.com/luhuisicnu/The-Flask-Mega-Tutorial-zh>)

### 环境

- 系统------>ubuntu 16.04
- python---->工程下的venv（对应linux系统），(venv_win对应win系统)
  - 激活
    - linux---->  source venv/bin/activate
    - win------> venv_win\Scripts\activate
  - 退出虚拟环境
    - linux
      - 直接deactivate
    - win
      - venv_win\Scripts\deactivate.bat

### 由于虚拟环境

```
$ python3 -m venv venv
```

> 译者注：这个命令不一定能够执行成功，比如译者在Ubuntu16.04环境下执行，提示需要先安装对应的依赖。`sudo apt-get install python3-venv`

使用这个命令来让Python运行`venv`包，它会创建一个名为`venv`的虚拟环境。 命令中的第一个“venv”是Python虚拟环境包的名称，第二个是要用于这个特定环境的虚拟环境名称。 如果你觉得这样很混乱，可以用你自定义的虚拟环境名字替换第二个`venv`。我习惯在项目目录中创建了名为`venv`的虚拟环境，所以无论何时`cd`到一个项目中，都会找到相应的虚拟环境。

- ps：这就是强者的世界吗👀

**激活你的全新虚拟环境**，需使用以下命令：

```python
$ source venv/bin/activate
(venv) $ _
# win
$ venv\Scripts\activate
(venv) $ _
```

**退出虚拟环境** 

- deactivate



#### ubuntu

- 创建文件
- git
  - git clone XXXX
  - 

### 总结

- 纲

  - 建立工程文件夹

  - 进入工程文件夹下，建立python虚拟环境

    - ```
      $ python3 -m venv venv
      #ubuntu16.04 apt-get install python3-venv（提前）
      ```

  - 因此，每次进入工程文件夹（迁移到新的环境下）

    - 激活环境

      - ```
        # linux mac ox
        $ source venv/bin/activate
        (venv) $ _
        # win
        $ venv\Scripts\activate （待测试）
        ```

    - 安装环境

      - ```
        pip install flask
        ```

  - ==Hello World 应用==

    - ==项目结构图==

      - ```
        microblog/
          venv/                 # 提供工程环境
          app/					# 提供flask 实例
            __init__.py         #app包的出生证明 - 需要flask 需要app实例 需要
            routes.py			#应用程序路由-视图函数
          microblog.py          # 工程运行”脚本“
          .flaskenv             # 自动加载FLASK_APP 
        ```
      ```
      
      ```
  
  - ```
      __init__/.py 的作用
      ##
      ```
  
    - 
  
      > Files named `__init__.py` are used to mark directories on disk as Python package directories. If you have the files
        >
        > ```py
        > mydir/spam/__init__.py
        > mydir/spam/module.py
        > ```
        >
        > and `mydir` is on your path, you can import the code in `module.py` as
        >
        > ```py
        > import spam.module
        > ```
        >
        > or
        >
        > ```py
        > from spam import module
        > ```
  
    - 就是使得当前文件夹成为module， 可以直接import 文件夹名
  
    - ==当你导入一个包时，`__init__.py`会执行并定义这个包暴露给外界的属性。==
  
- 设置环境变量
  
  - linux，mac
  
    - ```
        (venv) $ export FLASK_APP=microblog.py
        (venv) $ flask run
         * Serving Flask app "microblog"
         * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
        ```
  
  - win
  
    - 把export改成set



### python 新知识

- ==装饰器（未）==
- ==python-dotenv 的作用（未）==





### 待解决

- 这里win的迁移环境问题还未完好解决
  - venv/bin 下的activate貌似==对迁移不是很友好==
  - ==解决== （未验证）
    - 如果原始虚拟环境是在win下建立的，win可迁移，对于linux一样
  - ==README待整理==