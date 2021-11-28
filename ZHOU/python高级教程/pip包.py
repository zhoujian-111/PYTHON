import camelcase
c = camelcase.CamelCase()
txt ="Hello World"
print(c.hump(txt))
###pip包安转的时候    首先查看一下自己pip的版本  命令：pip --version
#然后再安装相应的包  pip install camelcase    如果出现失败，根据提示到相应的文件下WARNING: You are using pip version 21.1.3; however, version 21.3.1 is available.
#You should consider upgrading via the 'c:\users\27324\appdata\local\programs\python\python39\python.exe -m pip install --upgrade pip command.
#然后再安装   pip install camelcase包
#完成后检查一下pip安装    pip list