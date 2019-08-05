#!-*- coding:utf-8 -*-
# 编译环境: VSCode
# Python版本 3.7.0
# __author__ == giracle
# __time__ == 2019/8/1

"""
TODO: 只显示大乐透蓝球的变化曲线
"""
import json
from matplotlib import pyplot as plt

with open(r'backup/dlt/dltbule150.json','r') as f:
    jsonfile = json.load(f)
num = 3 # num表示想显示的某个数字，比如num==1，则只显示num==1时曾出现过的数字对,num>12以外的数字，则表示生成一个全部号码的图片，切记要将choice改为0
choice = 0 # choice==1表示只显示单个数字所对应的所有号码  choice==0表示所有数字对应的所有号码
blue_list = []
blueNum1List = []
blueNum2List = []
keylist = []
for key in jsonfile:
    # print(jsonfile[key])
    for i in range(len(jsonfile[key])):
        blue_list.append(jsonfile[key][i])
# print(len(blue_list))
if choice == 1:
    for k in range(len(blue_list)):
        # print(type(blue_list[k][0]))
        if int(blue_list[k][0]) == num:  # 只显示数字7及后一位数 B1最大为11
            blueNum1List.append(int(blue_list[k][0]))
            blueNum2List.append(int(blue_list[k][1]))
            keylist.append(k+1) # keylist 长度要和blueNum（1/2）list长度相同
else:
    for k in range(len(blue_list)):
        # print(type(blue_list[k][0]))
        blueNum1List.append(int(blue_list[k][0]))
        blueNum2List.append(int(blue_list[k][1]))
        keylist.append(k+1) # keylist 长度要和blueNum（1/2）list长度相同
# print(keylist)
# exit(0)
# print(blueNum1List)
# print(blueNum2List)
#统计某个数字出现的次数
for a in set(blueNum1List):
    print("数字{}出现{}次".format(a,blueNum1List.count(a)))
print("============================")
for a in set(blueNum2List):
    print("数字{}出现{}次".format(a,blueNum2List.count(a)))

plt.plot(keylist,blueNum1List,color='blue',marker='>',label='B1')
plt.plot(keylist,blueNum2List,color='green',marker='s',label='B2')

plt.xlabel('times')
plt.ylabel('numbers')
plt.title("BLUE Numbers")
plt.yticks([1,2,3,4,5,6,7,8,9,10,11,12])
plt.grid(True)  #显示网格
plt.legend(fontsize=7,loc=1)
plt.savefig(r"picture/num{}.png".format(num))
plt.show(True)



