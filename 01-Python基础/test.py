
def calNum(num):
    i = 1
    result = 1
    while i <= num:
        result *= i
        i += 1
    return result
if __name__ == '__main__':
    ret = calNum(13)
    print(ret)