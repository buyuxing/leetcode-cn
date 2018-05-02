def isEndWith0(bits):
    count = len(bits)
    if bits[count-1] != 0:
        return False
    if count == 1:
        return True
    r = True
    i = count - 2
    while(i >= 0):
        if bits[i] == 0:
            break
        i-=1
        r = not r
    return r

def main():
    print(isEndWith0([1,1,0]))

if __name__ == '__main__':
    main()