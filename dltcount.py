#! -*- coding:utf-8 -*-
# 编译环境: VSCode
# Python版本 3.7.0
# __author__ == giracle
# __time__ == 2019/8/1
"""
TODO: 用于显示dlt全部号码的变化曲线图，也可以只显示某一个球一号码所出现的号码对（即 显示选择第一个球及当期该球所出现的所有号码对）
"""
import json
from matplotlib import pyplot

# jsonfile = json.load(r'C:\Users\giracle\Desktop\cplist\cpNumber2433.json')
with open(r'backup/dlt/dltNumber150.json','r') as f:
    jsonfile = json.load(f)
# print(jsonfile)
keylist = []
valuelist = []
for key in jsonfile:
    # print(key)
    # keylist.append(key)
    for i in range(len(jsonfile[key])):
        valuelist.append(jsonfile[key][i])
    # valuelist.append(jsonfile[key])
# print(keylist)
# print(valuelist)
# for k in range(1,len(valuelist)+1):
#     keylist.append(k)
# print(keylist)
# exit(0)
num1list = []#第一个数
num2list = []#第二个数
num3list = []#第三个数
num4list = []#第四个数
num5list = []#第五个数
num6list = []#第六个数
num7list = []#第七个数
choice = 1
num = 1
if choice == 1:
    for i in range(len(valuelist)):
        if int(valuelist[i][0]) == num:
            num1list.append(valuelist[i][0])
            num2list.append(valuelist[i][1])
            num3list.append(valuelist[i][2])
            num4list.append(valuelist[i][3])
            num5list.append(valuelist[i][4])
            num6list.append(valuelist[i][5])
            num7list.append(valuelist[i][6])
            keylist.append(i+1)
            print("num=={}时的数字对为{}".format(num,valuelist[i]))
elif choice==0:
    for i in range(len(valuelist)):
        num1list.append(valuelist[i][0])
        num2list.append(valuelist[i][1])
        num3list.append(valuelist[i][2])
        num4list.append(valuelist[i][3])
        num5list.append(valuelist[i][4])
        num6list.append(valuelist[i][5])
        num7list.append(valuelist[i][6])
        keylist.append(i+1)
# print('num1list.count(1):'+num1list.count(1))
#每个列表中都是150条数据
# print(len(num1list))
# print(len(num2list))
# print(len(num3list))
# print(len(num4list))
# print(len(num5list))
# print(len(num6list))
# print(len(num7list))

#统计每个列表中数字出现的个数
for k1 in set(num1list):
    print("数字{}出现{}次".format(k1,num1list.count(k1)))
print("===================")
# print(set(num2list))
# print(num2list)
for k2 in set(num2list):
    print("数字{}出现{}次".format(k2,num2list.count(k2)))
print("===================")
for k3 in set(num3list):
    print("数字{}出现{}次".format(k3,num3list.count(k3)))
print("===================")
for k4 in set(num4list):
    print("数字{}出现{}次".format(k4,num4list.count(k4)))
print("===================")
for k5 in set(num5list):
    print("数字{}出现{}次".format(k5,num5list.count(k5)))
print("===================")
for k6 in set(num6list):
    print("数字{}出现{}次".format(k6,num6list.count(k6)))
print("===================")
for k7 in set(num7list):
    print("数字{}出现{}次".format(k7,num7list.count(k7)))
print("===================")

# #横坐标
# year = [2010,2012,2014,2016]
# #纵坐标
# perple = [20,40,60,100]
#生成折线图:polt函数
pyplot.plot(keylist[:100],num1list[:100],color='blue',marker="o",label="R1")
pyplot.plot(keylist[:100],num2list[:100],color='red',marker="_",label="R2")
pyplot.plot(keylist[:100],num3list[:100],color='yellow',marker="x",label="R3")
pyplot.plot(keylist[:100],num4list[:100],color='green',marker="p",label="R4")
pyplot.plot(keylist[:100],num5list[:100],color='black',marker="*",label="R5")
pyplot.plot(keylist[:100],num6list[:100],color='pink',marker=">",label="B1")
pyplot.plot(keylist[:100],num7list[:100],color='purple',marker="s",label="B2")
#设置横坐标说明
pyplot.ylabel("numbers")
#设置纵坐标说明
pyplot.xlabel("times")
#添加标题
pyplot.title("cpPoint")

#设置纵坐标刻度
pyplot.yticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35])
#显示网格
pyplot.grid(True)
pyplot.legend(fontsize=7,loc=1) # 用于显示lebel, loc 表示lebel的位置， 1表示右上角，2表示左上角 3表示左下角，4表示右上角
#显示图标
pyplot.show()
