import os


# -------------[打开文件]-------------
def openFile():
    f = open('test.txt', 'w')
    f.write('hello word, iam here!')



    f.close()

    f = open('test.txt', 'r')
    content = f.read()
    print(content)

    f.close()

if __name__ == '__main__':
# -------------[文件重命名、删除]-------------

    # os.rename('test.txt', 'newtest.txt')  //文件重命名
    # os.remove('newtest.txt') #删除文件

    # os.mkdir('filetest')
    os.getcwd() #获取当前目录
    os.chdir('../') #改变默认目录
    print(os.listdir('../01-Python基础/')) #获取目录列表及文件