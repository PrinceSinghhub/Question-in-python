# class codex:
#     def __init__(self,a):
#         self.name=a
#     # todo addition
#     def __add__(self,other):
#         sum=self.name+other.a+other.b
#         return sum
#
#     def __sub__(self, other):
#         return self.name-other.a-other.b
#
#
#     def __mul__(self, other):
#         return self.name * other.a * other.b
#
#     def __str__(self,other):
#         return self.name + other.a + other.b
#
#     def __truediv__(self, other):
#         return self.name / other.a / other.b
#
#     def __floordiv__(self, other):
#         return self.name // other.a // other.b
#
#
# class coder:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def __add__(self, other):
#         return self.a+self.b+other.a1
#
#     def __mod__(self, other):
#         return self.a % other.a1
#
#     def __pow__(self, power):
#         return self.a ** power.a1
#
#     def __rshift__(self, other):
#         return self.a >> other.a1
#
#     def __lshift__(self, other):
#         return self.a << other.a1
#
#     def __and__(self, other):
#         return self.a & other.a1
#
#     def __or__(self, other):
#         return self.a | other.a1
#
#     def __xor__(self, other):
#         return self.a ^ other.a1
#
#
# class khushi:
#     def __init__(self,a):
#         self.a1=a
#
# a=codex(20)
# b=coder(5,500)
# c=khushi(3)
# print("AND: ",b & c)
# print("OR: ", b|c)
# print("XOR: ", b^c)
# a=codex("100")
# b=coder("200500","coder")
# print(a+b)
# todo comparession
class comparession:
    def __init__(self,a):
        self.num=a

    def __isub__(self, other):

        self.num  -= other.num1
        return self.num

    def __iadd__(self, other):
        self.num += other.num1
        return self.num
class khushi:
    def __init__(self,a):
        self.num1=a
x=comparession(30)
y=khushi(20)
x+=y
print(x)
