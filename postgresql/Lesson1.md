# Lesson1

## 参考

- [postgresql轻松学](https://pg.sjk66.com/postgresql/order-by.html)

## 准备步骤

- 环境
  - GCP Ubuntu 18.04 LTS

- ```bash
  #!/bin/sh
  wget https://pg.sjk66.com/static/attach/download-sample-database/dvdrental.zip
  apt-get update
  apt-get install zip
apt-get install postgresql
  unzip dvdrental.zip
  sudo su postgres
  createdb dvdrental;
  pg_restore -U postgres -d dvdrental dvdrental.tar
  psql dvdrental
  \dt
  # 对应的写一下脚本
  # bash的写法是否可以模仿下v2ray的写法
  # 是否能免除 chmod +x 的赋权？
  ```
  
- 

## 疑问

- 创建数据库时指定编码utf-8？
- ER图？
- 数据库的设计？