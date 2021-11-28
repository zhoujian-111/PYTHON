#UA伪装：User-Agent(请求载体的身份标识)
#门户网站的服务器会检测对应请求的载体身份标识，如果检测到的身份标识位某一浏览器，
#说明请求的是一个正常的请求，但是如果检测到请求的载体身份标识不是某一浏览器的，则表示该基于爬虫
#若检测到是一个爬虫，则服务器就可能拒绝该次请求
#UA伪装:让爬行对应的请求载体身份标识伪装成某一浏览器
#导包
import requests
if __name__=="__main__":
    #UA伪装:将对应的user-agent封装到一个字典中
    headers ={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    }
    url = 'https://www.baidu.com/baidu?'
    #封装url携带的参数：封装到字典里面
    kw = input('enter a word:')
    param = {
        'quary':kw
    }
    #对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理了参数
    response = requests.get(url=url,params=param,headers=headers)
    page_text = response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功！！')