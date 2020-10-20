
if __name__ == '__main__':
    oldFileName = input("请输入要拷贝的文件名")
    file = open(oldFileName, 'r')

    if file:
        fileType = oldFileName.rfind('.')
        if fileType > 0:
            fileFlag = oldFileName[fileType:]
        newFileName = oldFileName[:fileType] + '【复件】' + fileFlag

        newFile = open(newFileName, 'w')
        for lineContent in file:
            newFile.write(lineContent)
    newFile.close()
    file.close()