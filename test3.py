import re
import time

import requests

save_route = './2019年统计用区划代码和城乡划分.txt'  # 数据储存路径
results2 = []
results3 = []
results4 = []
results5 = []
Dates1 = []
kv = {'user-agent': 'Mozilla/5.0'}
n = 0
url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html'
r = requests.get(url, headers=kv)
r.raise_for_status()
r.encoding = r.apparent_encoding
pattern = re.compile("<a href='(.*?)'>(.*?)<")  # 正则表达式
result1 = list(set(re.findall(pattern, r.text)))  # 从主页面获取子页面的html
print('result1')
# print(result1)
i2 = 0
for i2 in range(len(result1)):
    try:
        url2a = result1[i2][0]
        address1 = result1[i2][1]  # 一级地址
        i2 += 1
        url2 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/' + url2a
        r2 = requests.get(url2, headers=kv)
        r2.raise_for_status()
        r2.encoding = r2.apparent_encoding
        pattern2 = re.compile("<a href='(.*?)'>(.*?)<")  # 正则表达式提取目标字段
        result2 = list(set(re.findall(pattern2, r2.text)))
        result2a = []
        for i2a in result2:  # 爬取的城市信息和城市代码混在一起，需要将代码清除
            if '0' in i2a[1]:
                n += 1
            else:
                result2a.append(i2a)
        print('result2a')
    except:
        print('错误')
        with open(save_route, 'a', encoding='utf-8')as f:
            f.write('一级错误 一级错误 一级错误 一级错误')
            f.write('\n')
        continue
    i3 = 0
    for i3 in range(len(result2a)):
        try:
            url3a = result2a[i3][0]
            address2 = result2a[i3][1]  # 二级地址
            i3 += 1
            url3 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/' + url3a
            r3 = requests.get(url3, headers=kv)
            r3.raise_for_status()
            r3.encoding = r3.apparent_encoding
            pattern3 = re.compile("<a href='(.*?)'>(.*?)<")
            result3 = list(set(re.findall(pattern3, r3.text)))
            result3a = []
            for i3a in result3:
                if '0' in i3a[1]:
                    n += 1
                else:
                    result3a.append(i3a)
            print('result3a')
        except:
            print('错误')
            with open(save_route, 'a', encoding='utf-8')as f:
                f.write('二级错误 二级错误 二级错误 二级错误')
                f.write('\n')
            continue
        i4 = 0
        for i4 in range(len(result3a)):
            try:
                url4a = result3a[i4][0]
                address3 = result3a[i4][1]  # 二级地址
                i4 += 1
                url4 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/' + url4a[3:5] + '/' + url4a
                r4 = requests.get(url4, headers=kv)
                r4.raise_for_status()
                r4.encoding = r4.apparent_encoding
                pattern4 = re.compile("<a href='(.*?)'>(.*?)<")
                result4 = list(set(re.findall(pattern3, r4.text)))
                result4a = []
                for i4a in result4:
                    if '0' in i4a[1]:
                        n += 1
                    else:
                        result4a.append(i4a)
                print('result4a')
            except:
                print('错误')
                with open(save_route, 'a', encoding='utf-8')as f:
                    f.write('三级错误 三级错误 三级错误 三级错误')
                    f.write('\n')
                continue
            i5 = 0
            for i5 in range(len(result4a)):
                try:
                    url5a = result4a[i5][0]
                    address4 = result4a[i5][1]  # 二级地址
                    i5 += 1
                    url5 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/' + url5a[3:5] + '/' + url5a[5:7] + '/' + url5a
                    r5 = requests.get(url5, headers=kv)
                    r5.raise_for_status()
                    r5.encoding = r5.apparent_encoding
                    pattern5 = re.compile("<tr class='villagetr'><td>(.*?)</td><td>(.*?)</td><td>(.*?)</td></tr>")
                    result5 = list(set(re.findall(pattern5, r5.text)))
                    print(len(result5))
                    result5a = []
                    for i in range(len(result5)):
                        cun = result5[i][2]
                        result5a.append(cun)
                    print('result5a')
                except:
                    print('错误')
                    with open(save_route, 'a', encoding='utf-8')as f:
                        f.write('四级错误 四级错误 四级错误 四级错误')
                        f.write('\n')
                    continue
                results6 = []
                i6 = 0
                for i6 in range(len(result5a)):
                    try:
                        address5 = result5a[i6]
                        i6 += 1
                        address = str(address1) + ',' + str(address2) + ',' + str(address3) + ',' + str(
                            address4) + ',' + str(address5)
                        print(address)
                        with open(save_route, 'a', encoding='utf-8')as f:
                            f.write(address)
                            f.write('\n')
                    except:
                        print('错误')
                        with open(save_route, 'a', encoding='utf-8')as f:
                            f.write('五级错误 五级错误 五级错误 五级错误')
                            f.write('\n')
                        continue
time.sleep(1)
print('well_done')