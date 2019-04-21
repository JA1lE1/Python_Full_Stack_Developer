# Learning_log



## *2019年4月18日*

## Mysql

### Ubuntu 环境下

- [初始使用参考](<https://www.jianshu.com/p/694d7d0a170b>)

### Client 

- [navicat](E:\work\学习\研究生\助教\软件\NavicatForMysql\Navicat for MySQL)

### 登录mysql 的方式

- server端

  - 好像只能用

  - ```
    mysql -u root -p
    ```

### server端上的mysql数据库外网的链接方式

- [参考链接](<https://blog.csdn.net/w20228396/article/details/70143500>)
- 注意事项
  - 当前我在腾讯云上设置的全网监听全网可链接
  - 对应的mysql配置地址：/etc/mysql/mysql.cnf（具体课件参考链接中也有修改**blind-address**）
  - 后面的那个12****是设置登录的密码
- **小get**
  - |grep **的使用

### 卸载Mysql

- [参考链接](<https://blog.csdn.net/w3045872817/article/details/77334886>)

```
sudo apt-get remove mysql-common
##下面这个命令注意版本号
sudo apt-get autoremove --purge mysql-server-5.7
##再用dpkg --list|grep mysql查看，还剩什么就卸载什么

最后清楚残留数据：

dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P
```


