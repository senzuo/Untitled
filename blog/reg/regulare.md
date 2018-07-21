# 正则表达式

## 什么是正则表达式

举例：
1. 查找VBird&Vbird V[Bb]ird
2. 在某个目录下的文件中查找制定字符串 grep 'str' dictory
3. 管理员管理日志
4. 服务器开发 eg Spring中的url请求就支持正则表达式

正则表达式是一种字符串的表达式，只要程序支持正则表达式就可以使用
eg vim grep awk sed工具


## 基础正则表达式练习

### 查找特定字符串
``` bash
# basic
grep -n 'the' regular_express.txt	# 在该文件中查找‘the’并且打印行号
grep -vn 'the' regular_express.txt	# 在该文件中查找没有‘the’的行并且打印行号
grep -in 'the' regular_express.txt	# 在该文件中查找没有(不分大小写)‘the’的行并且打印行号
```
### 使用中括号
查找taste和test

``` bash
grep -n 't[ea]st' filename
```
代表括号中的某一个字符，也可以代表不是某一个字符
``` bash
grep -n '[^g]oo' filename
grep -n '[^a-z]oo' filename
```

### 行首与行尾

``` bash
grep -n '^the' filename 	# 匹配 the 开头的行
grep -n '^[^a-zA-Z]' filename	# 不是字母开头的行
grep -n '\.$' filename		# . 结尾的行
grep -n '^$' filename		# 空行
```

### 任意一个字符.与重复字符*

```bash
grep -n 'g..d' filename
# . 代表任意字符
grep -n 'oo*' filename # x* 可以匹配空字符，就是说有没有x都可以
# o*代表可有可无的多个o
grep -n 'goo*g' filename
# 开头结尾都是g，中间仅能存在至少一个o
```

### 限定个数{}
```bash
grep -n 'o\{2\}' filename
```

## 扩展正则表达式
注意使用egrep

- '+' 一个或者多个前一个RE字符
- '?' 零个或者一个前一个RE字符
- '()' 组 

``` bash
egrep -n 'g(la|oo)d' filename	# 查找glad或者是good
egrep -n 'A(xyz)+C' filename	# 查找AxyzC or AxyzxyzC
```







