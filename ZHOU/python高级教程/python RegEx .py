#RegEx或正则表达式是形成搜索模式的字符序列
#RegEx可用于检查字符串是否包含指定的搜索模式
import re   #导入re的内置包，处理正则表达式

txt = "China is a great country"
x = re.search("^China.*country$", txt)

if (x):
  print("YES! We have a match!")
else:
  print("No match")
#   findall  返回包含所有匹配项的列表
#   search   如果字符串中的任意位置存在匹配，则返回match对象
#   split    返回每次匹配时拆分字符串的列表
#   sub      则字符串替换一个或多个匹配项


#findall
import re

str = "China is a great country"
x =re.findall("a",str)
print(x)



#search
import re
str = "China is a great country"
x = re.search("\s",str)
print("The first white-space character is located in position:",x.start())


#split
import re
str = "China is a great country"
x = re.split("\s",str) #在str后加上数字可以指定maxsplit参数出现的次数
print(x)



#sub
import re
str = "China is a great country"
x = re.sub("\s","9",str) #用9替换所有的空格  可以在str后加上数字，来控制替换的次数
print(x)

#match用来搜索有关的结果信息的对象