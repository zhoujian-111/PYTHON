#try块允许您测试代码块以查找错误
#except块允许处理错误
#finally块允许您执行代码，无论try和except块的结果如何
try:
    print(x)
except:
    print("An exception occurred")

#多个异常
try:
    print(x)
except NameError:
    print("Variable x id not defined")
except:
    print("something else went wrong")

#else  如果没有引发错误就要用else来定义执行代码块
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


#finally  如果指定了finally块，无论try块是否引发错误，都会执行finally块
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


#引发异常
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")