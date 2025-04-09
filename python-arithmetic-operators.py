if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    if 1 <= a <= 10**10 and 1 <= b <= 10**10 :
        c = a + b
        d = a - b
        e = a * b
        print (c)
        print (d)
        print (e)
    else:
        print ("error")
