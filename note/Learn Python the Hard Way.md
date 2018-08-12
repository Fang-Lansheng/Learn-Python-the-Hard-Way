# Learn Python the Hard Way

## 笨办法更简单！

> 1. 做每一道习题
> 2. 一字不差地写出每一个程序
> 3. 让程序运行起来

- 读和写

- 注重细节

- 发现不同

- 不要复制-粘贴

- 使用书中包含的视频

- 坚持练习、重复练习

- 不要认为自己“过分聪明”



## 3. 习题

### 变量和打印

#### Python %格式化和format格式化

```
格式符
%[(name)][floags][width].[precision]typecode
(name) 可选，用于选择指定的key
flags  可选，可提供的值有：
    · +    右对齐，整数前加正号，负数前加负号
    · -    左对齐，正数钱无符号，负数前加负号；
    · 空格 右对齐；正数前加空格，负数前加负号
    · 0    右对齐，正数前无符号，负数前加负号；用0填充
width   可选，占有宽度
typecode  必选
	%s 字符串（str()的显示）
	%r 字符串 (repr()显示)
	%c 单个字符
	%b 二进制整数 bin
	%i 十进制整数 int
	%o  八进制整数 oct
	%x 十六进制整数 hex
	%f  浮点数
	%e 指数
	%% 字符% （前提是里面要有格式符的话需要这么写）
案例：
a = "i am %s" % "alex"
a = "i am %s age %d " % ("alex",18)
a = "i am %(name)s age %(age)d" % {"name":"alex","age":18}
a = "percent %.2f" % 99.98234
a = "i am %(pp).2f" % {"pp":123.3245}
a = "i am %.2f %%" % {"pp":123.3223455} 
 
format 格式化
type         【可选】格式化类型 •传入” 字符串类型 “的参数 •s，格式化字符串类型数据
•空白，未指定类型，则默认是None，同s
 
•传入“ 整数类型 ”的参数
	•b，将10进制整数自动转换成2进制表示然后格式化
	•c，将10进制整数自动转换为其对应的unicode字符
	•d，十进制整数
	•o，将10进制整数自动转换成8进制表示然后格式化；
	•x，将10进制整数自动转换成16进制表示然后格式化（小写x）
	•X，将10进制整数自动转换成16进制表示然后格式化（大写X）
 
•传入“ 浮点型或小数类型 ”的参数 •e， 转换为科学计数法（小写e）表示，然后格式化；
	•E，转换为科学计数法（大写E）表示，然后格式化;
	•f，转换为浮点型（默认小数点后保留6位）表示，然后格式化；
	•F，转换为浮点型（默认小数点后保留6位）表示，然后格式化；
	•g，自动在e和f中切换
	•G，自动在E和F中切换
	•%，显示百分比（默认显示小数点后6位）
 
 
还是看案例吧
a = "i am {},age {}".format("seven",18,"alex")
b = "i am {},age {}, {}".format(*["seven", 18 ,"alex"])
c = "i am {0}, age {1}, really {0}".format("seven", 18)
d = "i am {0}, age{1}, really {0}".format(*["seven", 18])
e = "i am {name}, age {age}, really {name}".format(name="seven", age = 18)
f = "i am {name}, age {age}, rally {name}".format(**{"name":"seven", "age":18})
g = "i am {0[0]},age{0[1]}, really{0[2]}".format([1,2,3],[11,22,33])
h = "i am {:s}, age {:d}, money {:f}".format("seven", 18, 888.1)
i = "i am {:s}, age {:d}".format(*["seven", 18])
j = "i am {name:s}, age {age:d}".format(name="seven",age=18)
k = "i am {name:s}, age {age:d}".format(**{"name":"seven","age":18})
l = "numers:{:b},{:o},{d},{:x},{:X},{:%}".format(15,15,15,15,15,15.32445,2)
m = "numbers:{0:b},{0:o},{0:d},{0:x},{0:%}".format(15)
tpl = "numbers: {num:b},{num:o},{num:d},{num:x},{num:X}, {num:%}".format(num=15)

更多格式化操作：https://docs.python.org/3/library/string.html
http://www.cnblogs.com/wupeiqi/articles/5484747.html
```

#### Python转义字符

| 转义字符 | 实现功能                                 |
| :------: | ---------------------------------------- |
|    \     | （在行尾时）续行符                       |
|   \\\    | 反斜杠符号                               |
|    \'    | 单引号                                   |
|    \"    | 双引号                                   |
|    \a    | 响铃                                     |
|    \b    | 退格（Backspace）                        |
|    \e    | 转义                                     |
|   \000   | 空                                       |
|    \n    | 换行                                     |
|    \v    | 纵向制表符                               |
|    \t    | 横向制表符                               |
|    \r    | 回车                                     |
|    \f    | 换页                                     |
|   \oyy   | 八进制数yy代表的字符，例如：\o12代表换行 |
|   \xyy   | 十进制数yy代表的字符，例如：\x0a代表换行 |
|  \other  | 其他的字符以普通格式输出                 |

#### Python的字符串内建函数

参考（http://www.runoob.com/python/python-strings.html）

| 方法                                             | 描述                                                         |
| ------------------------------------------------ | ------------------------------------------------------------ |
| string.capitialize()                             | 把字符串的第一个字符大写                                     |
| string.center(width)                             | 返回一个原字符串居中，并使用空格填充值长度width的新字符串    |
| string.count(str, beg=0, end=len(string))        | 返回str在string出现的次数，如果beg或者end指定则返回指定范围内str出现的次数 |
| string.decode(encoding='utf-8', errors='strict') | 以encoding指定的编码格式解码string，如果出错默认报一个ValueError的异常，除非errors指定的是 'ignore' 或者 'replace' |
| string.endswith(obj, beg=0, end=len(string))     | 检查字符串是否以obj结束，如果beg或者end指定则检查指定范围内是否以obj结束，如果是，则返回True，否则返回False |
| string.expandtabs(tabsize=8)                     | 把字符串string中的tab符号转换为空格，tab符号默认的空格数是8  |
| string.find(str, beg=0, end=len(string))         | 检测str是否包含在string中，如果beg和end指定范围，则检查是否包含在指定范围内，如果是则返回开始的索引值，否则返回-1 |
| string.format()                                  | 格式化字符串                                                 |
| string.index(str, beg=0, end=len(string))        | 跟find()方法一样，只不过如果str不在string中会报一个异常      |
| string.isalnum()                                 | 如果string至少有一个字符并且所有字符都是字母或数字则返回True，否则返回False |
| string.isalpha()                                 | 如果string至少有一个字符并且所有字符都是字母则返回True，否则返回False |
| string.isdecimal()                               | 如果string只包含十进制数字则返回True，否则返回False          |
| string.isdigit()                                 | 如果string只包含数字则返回True，否则返回False                |
|                                                  |                                                              |
|                                                  |                                                              |
|                                                  |                                                              |
|                                                  |                                                              |
|                                                  |                                                              |
|                                                  |                                                              |
|                                                  |                                                              |
|                                                  |                                                              |
|                                                  |                                                              |
|                                                  |                                                              |
|                                                  |                                                              |

### 读写文件

- `close`：关闭文件。跟你编辑器的“文件->保存”一个意思
- `read`：读取文件内容。你可以把结果赋给一个变量
- `readline`：读取文本文件中的每一行
- `truncate`：清空文件，请谨慎使用该命令
- `write('stuff')`：将stuff写入文件

