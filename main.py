# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


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

    namesList = ["123", "232333223", 102231]
    print(namesList[1], namesList[0])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
    for value in namesList:
        print(value)

    # 数组常见操作
    name = input("请输入你要添加的名字")
    namesList.append(name)
    print(namesList)