import requests
import json
if __name__=="__main__":
    post_url = 'http://www.kfc.com.cn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'
    }
    city = input('输入城市:')
    data = {
        'cname':'',
        'pid':'',
        'keyword': city,
        'pageIndex':'1',
        'oageSize':'40'
    }
    response = requests.get(url=post_url,data=data,headers=headers)
    json_data = requests.json()
    with open('./{}.jsonformat(w)','w',encoding='utf-8') as fp:
        json.dump(json_data,fp,ensure_ascii=False)
        print("查询完毕！！")