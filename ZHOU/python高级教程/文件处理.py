#在 Python 中使用文件的关键函数是 open() 函数。

#open() 函数有两个参数：文件名和模式。

#有四种打开文件的不同方法（模式）：

#"r" - 读取 - 默认值。打开文件进行读取，如果文件不存在则报错。
#"a" - 追加 - 打开供追加的文件，如果不存在则创建该文件。
#"w" - 写入 - 打开文件进行写入，如果文件不存在则创建该文件。
#"x" - 创建 - 创建指定的文件，如果文件存在则返回错误。
#此外，您可以指定文件是应该作为二进制还是文本模式进行处理。

#"t" - 文本 - 默认值。文本模式。
#"b" - 二进制 - 二进制模式（例如图像）。
f = open("demofile.txt")
f = open("demofile.txt","rt")#  rt为读取文本（两个都是默认的，所以上下两个等同）


#文件打开
f = open("demofile.txt","r")
print(f.read())  #确保demofile.txt文件存在   read后可以加数字，返回字符数
#读行的话
#使用readline（）
#关闭文件最后写上   f.close（）


#   a  追加
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()
#追加后，打开并读取改文件
f = open("demofile2.txt", "r")
print(f.read())


#    w     覆盖全部内容
f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
# 写入后，打开并读取该文件：
f = open("demofile3.txt", "r")
print(f.read())

#     x      创建空文件
f = open("myfile.txt", "x")


#删除文件必须导入OS模块，并运行os.remove()函数
import os
os.remove("文件名")
#如果删除整个文件夹使用os.rmdir（）
import os
os.rmdir("文件夹名")