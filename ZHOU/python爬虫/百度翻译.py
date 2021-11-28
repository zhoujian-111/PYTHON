import requests
import json
if __name__ == "__main__":
    #1.指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #2.进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    }
    #3.post请求参数处理（同get请求一致）
    word = input('enter a word:')
    data = {
        'kw':word
    }
    #4.请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    #5获取响应数据:json()方法返回的是obj（如果确认服务器响应数据是json类型的，才可以使用）从Content-type中可以了解到是不是json类型
    dic_obj = response.json()
    #持久化存储
    fileName = word+'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)#中文不能用ascll码
    print('over!!')