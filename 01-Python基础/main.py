# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print_hi("test")
    print_hi("test1")
    age = 10
    print_hi("test%s"%age)
    names = "shabi"
    print("名字是%s"%(names))
    print("huanhang \n haha")

    # password = input()
    # print("你输入的密码是%s"%password)
    num = 1
    if age == 1:
        print("out 1")
        if age == 2:
            print("test")
        else:
            print("sss")
    if age == 1 or num == 1:
        print("test")

    i = 0
    while i < 10000:
        print("当前数值:%s" % i)
        i += 1

    name = "luolianix"
    for x in name:
        print(x)
    print(name[1])
    # print(name[10])
    print(name[0:3])
    print(name[3:])
    print(name[::3])
    print(name[1:-1])

    namesList = ["123", "232333223", 102231, 12112, 33223]
    print(namesList[1], namesList[0])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    for value in namesList:
        print(value)

    # 数组常见操作
    # name = input("请输入你要添加的名字")
    namesList.append(name)
    namesList.insert(1, 2)
    b = [1, 23]
    namesList.extend(b)
    print(namesList)

    for v in namesList:
        if v == "123":
            continue
        if v == 102231:
            break
        print(v)

    if "123" in namesList:
        print("找到了相同的字符串")
    else:
        print("没有找到相同的字符串")

    if "123" not in namesList:
        print("--这个字符串不存在")
    else:
        print("--这个字符串存在")

    a = ['a', 'b', 'c', 'a', 'b']
    # a.index('a', 1, 3)  # 注意是左闭右开区间
    print(a.count('b'))
    print(a.index('a', 1, 4))

    print(a)
    del a[1] #删除指定位置
    print(a)

    a.pop() #删除最后一个
    print(a)

    a.remove('a') #删除指定值
    print(a)

    # 排序 sort reverse
    a.reverse() #逆序
    print(a)

    a.sort(reverse=True) #正序
    print(a)


#     -------------[一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配]-------------------
# 定义一个列表用来保存3个办公室
offices = [[],[],[]]

# 定义一个列表用来存储8位老师的名字
names = ['A','B','C','D','E','F','G','H']

i = 0
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)

i = 1
for tempNames in offices:
    print('办公室%d的人数为:%d'%(i,len(tempNames)))
    i+=1
    for name in tempNames:
        print("%s"%name,end='')
    print("\n")
    print("-"*20)
print(offices)


# ---------[元组]--------------
# 元组与数组相似，不同之处在于元祖元素不能修改
aTuple = ('ep', 77, 99, 9)
print(aTuple)
print(aTuple[1])

# ---------[字典]------------------
#字典和列表一样，也能够存储多个数据
# 列表中找某个元素时，是根据下标进行的
# 字典中找某个元素时，是根据'名字'（就是冒号:前面的那个值，例如上面代码中的'name'、'id'、'sex'）
# 字典的每个元素由2部分组成，键:值。例如 'name':'班长' ,'name'为键，'班长'为值
info = {'test':'banzhang', 'id': 10}
print(info)
print(info['test'])
info.get('test')
# info('s') #不存在键报错
info['id'] = 11

## 字典的常见操作
print(len(info))  #字典长度
print(info.values()) #字典values
print(info.items()) #返回字典元组列表
# print(info.has_key('test')) #如果key存在，返回ture python2.0

## 字典遍历
for value in info:
    print(value)
#遍历字典key
for key in info.keys(): #遍历key
    print(key)
for value in info.values(): #遍历值
    print(value)
for item in info.items():   #遍历元组元素
    print(item)
for key,value in info.items():  #遍历键值对
    print(key,value)

# 引用 在python中，值是靠引用来传递来的。
# 我们可以用id()来判断两个变量是否为同一个值的引用。 我们可以将id值理解为那块内存的地址标示。
a = 1
print(id(a))
print(id(info['test']))

