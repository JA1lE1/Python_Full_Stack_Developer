# LOG

## 6.25

### 对应中南的前端设计

- Topic-Visualization 好像是使用WordPress的前端设计
  - WordPress好像真的很好很强大
  - 好像腾讯的神马实验室也有对应的教程 youtube上也有 找时间试一下gcp+wordpress的方式？
    - 如何使用word press 做 数据可视化的网站等
    - GCP市场上有WordPress和MongoDB的解决方案（Google天下第一）
- 而北理这位大佬使用的是Flask python 的轻量级设计

### 运行环境(本地)

- 由于所需的很多包在虚拟环境env_full_stack 因此最好在终端执行flask run的操作

  - 注意要到对应的文件夹IEServer下执行

  - ```pyhton
    set FLASK_APP=app.py
    flask run
    ```



### Bug

- python的文件路径访问法
  - 
- 如果直接在flask run 下打开 http://127.0.0.1:5000/         就会没有结果
  - 打开 http://127.0.0.1:5000/BITIE/ 才是对应的结果
  - 具体的设置对应的是路由文件-----init_route.py 文件

### 参考

- 自己的python_full_stack 的flask的模块

### 所需包

install summa