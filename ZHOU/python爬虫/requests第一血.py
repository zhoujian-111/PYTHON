#-需求：爬取搜狗页面数据
import requests
if __name__ == "__main__":
    #step1：指定url
    url = 'https://www.sogou.com/'
    #step2：发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url)
    #step3：获取响应数据，text返回的是字符串形式的相应数据
    page_text = response.text
    print(page_text)
    #step4：持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取结束！！！')