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
