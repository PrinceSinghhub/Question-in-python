n=int(input("Num 1: "))
n1=int(input("Num 1: "))
for i in range(n):
    for j in range(n1):
        if j%2==0:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()
