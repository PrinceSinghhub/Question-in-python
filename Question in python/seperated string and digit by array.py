from numpy import *
def Stringq(Str):
    a = array(Str)
    String = ''
    Num = ''
    Data = str(a)
    for i in Data:
        if i.isalpha():
            String += i
        if i == 'x':
            String += ' '
    for i1 in Data:
        if i1.isdigit():
            Num += i1

    Int = Num
    SUM = 0
    for x in Int:
        SUM = int(x) + SUM
    String = array(String)
    Num = array(Num)
    Stn = 0
    String = str(String)
    for y in String:
        if y.isalpha():
            Stn += 1
        if y == ' ':
            Stn += 1
    Ln = 0
    Num = str(Num)
    for x1 in Num:
        if x1.isdigit():
            Ln += 1
    print(
        f"Input is: {a}\nOutput String is: {String}\nOutput Number is: {Num}\nSum of Output Number is: {SUM}\nLenth of Output Sting is: {Stn}\nLenth of Output Integer is: {Ln}")
    # print(f"Output Number is: {Num}")
    # print(f"Sum of Output Number is: {SUM}")
    # print(f"Lenth of Output Sting is: {Stn}")
    # print(f"Lenth of Output Integer is: {Ln}")

Stringq("codex12cod079er")


