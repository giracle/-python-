#!-*- coding:utf-8 -*-
# 编译环境: VSCode
# Python版本 3.7.0
# __author__ == giracle
# __time__ == 2019/8/1
from bs4 import BeautifulSoup
import requests
import time
import re
import json
def getHtml(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36',
        'Host': 'www.caibow.com',
        'Referer': 'https://www.caibow.com/ssq/kj/',
        'Cookie': 'test_ip_res=no; newtcb_test_over=2019-07-08+23%3A05; PHPSESSID=a76qqckq3lme52rjkra9mlaas0; Hm_lvt_186a10a59d1dd2902fb3b56529328ef3=1562671994; UM_distinctid=16bd6862bbf72f-0cce614553f035-e343166-144000-16bd6862bc088a; CNZZDATA1252898950=95037069-1562670470-https%253A%252F%252Fwww.caibow.com%252F%7C1562670470; IESESSION=alive; _qddaz=QD.h7bllp.dp8qex.jxvqphws; _qdda=3-1.ypyib; _qddab=3-aczfm.jxvqphwu; _qddamta_800024868=3-0; pgv_pvi=2901236736; pgv_si=s3499366400; Hm_lpvt_186a10a59d1dd2902fb3b56529328ef3=1562672495'
    }
    response = requests.get(url=url,headers=headers)
    response.encoding='utf-8'
    # print(response.text)
    # exit(0)
    return response.text

def parser_html(html):
    # dataDict = {}
    soup = BeautifulSoup(html,'html.parser')
    soup_list_red = soup.find_all('span', class_='fl all_ball {color}_ball color_white mr10'.format(color="red"))
    soup_list_blue = soup.find_all('span', class_='fl all_ball {color}_ball color_white mr10'.format(color="blue"))
    # print(soup_list)
    # exit(0)
    pattern_red = re.compile('.*?<span class="fl all_ball red_ball color_white mr10">(\d+)</span>.*?')
    pattern_blue = re.compile('.*?<span class="fl all_ball blue_ball color_white mr10">(\d+)</span>.*?')
    items = re.findall(pattern_red,str(soup_list_red))  
    items_blue = re.findall(pattern_blue,str(soup_list_blue))  
    # print(items)  
    # exit(0)
    
    count=0
    cplist = []
    cplistBig = []
    for item in items:
        count+=1
        if count % 6 !=0:
            cplist.append(int(item))
        else:
            cplist.append(int(item))
            count=0
            cplistBig.append(cplist)
            cplist = []
    for i in range(len(items_blue)):
        cplistBig[i].append(int(items_blue[i]))
    print(cplistBig)
    # print("共有{num}期CP".format(num=len(cplistBig)))
    
    # print(dataDict)
    return cplistBig #获取到每一期CP的号码


if __name__ == "__main__":
    dictNum = {}
    count=0
    for num in range(1,11):
        url = 'https://www.caibow.com/ssq/kj/p{num}/'.format(num=num)
        html = getHtml(url)
        cplistBig = parser_html(html)
        dictNum[num] = cplistBig
        count += len(cplistBig)
        # time.sleep(3)
    with open(r'backup/ssq/cpNumber{num}.json'.format(num=count),'a')as fw:
        fw.write(json.dumps(dictNum))
    print("共有{num}期".format(num=count))
