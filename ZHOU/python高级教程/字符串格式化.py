#format()字符串   方法允许格式化字符串的选定部分
#有时文本一部分无法控制，也许来自数据库或者用户输入？
#要控制此类值，在文本中添加占位符{}，然后通过format（）方法运行值：
price = 52
txt = "The price is {:.2f} dollars"
print(txt.format(price))   #在花括号内添加参数来指定如何转化值
#print(txt.format(price,itemno,count))可以在format后添加更多的值
#可以使用索引号（花括号{0}内的数字）来确保将值放在正确的占位符中
quantity = 3
itemno = 567
price = 52
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))