import requests
import json
if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64;rv: 89.0) Gecko / 20100101Firefox / 89.0'
    }
    id_list = []  # 存储企业id
    all_data_list = []  # 存储企业详情数据
    #获取不同企业的id值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    #参数的封装
    for page in range(1,6):
        page = str(page)
    data ={
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
        'applyson': '',
    }
    json_ids = requests.post(url=url,headers=headers,data=data).json()
    for dic in json_ids['list']:
       id_list.append (dic['ID'])
    #获取企业详情数据
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    for id in id_list:
        data = {
            'id':id
    }
        detail_json = requests.post(url=url, headers=headers, data=data).json()
        # print(detail_json,'---------ending-----')
        all_data_list.append(detail_json)
        #持久化存储all_data_list
        fp = open('./allData.json','w',encoding='utf_8')
        json.dump(all_data_list,fp=fp,ensure_ascii=False)
        print('over!')
