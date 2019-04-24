# README

## 2019.4.24

:point_down:

## 正则

- 遇到疑难

  - 在匹配分组->提取区号的地方

- 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

  ```
  >>> import re
  # 编译:
  >>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
  # 使用：
  >>> re_telephone.match('010-12345').groups()
  ('010', '12345')
  >>> re_telephone.match('010-8086').groups()
  ('010', '8086')
  ```

  编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。

- re.split

- re.escape

  - 应该是把str转换成所需要进行匹配的格式

- re.compile

  - 生成匹配模板（预处理）

### 官方的文档

- [链接](<https://docs.python.org/zh-cn/3/library/re.html?highlight=compile#>)