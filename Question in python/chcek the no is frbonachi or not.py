def chekphebo(n):
    first = 0
    second = 1
    third = 0
    result = 0
    while result < n:
        result += first
        first = second
        second = third
        third = first + second
    print("By Using While Loop")
    if result == n:
        print(f"Yes Number is phebonachi: {result}\nInput: {n} == Output: {result}")
    else:
        print(f"Not a Phebonachi No: {n}\nInput: {n} == Output: {result}")
n = int(input("Enter No: "))
chekphebo(n)



