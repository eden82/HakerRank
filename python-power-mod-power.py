if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    m = int(input().strip())
    
    if 1<= a <= 10 and 1<=b <= 10 and 2 <= m <= 1000:
        print(pow(a,b))
        print (pow(a,b,m))
