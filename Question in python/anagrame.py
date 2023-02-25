#sorted means arrange alphabet in our real order
a="codex coder"
print(sorted(a))
a=input("Enter your String 1")
b=input("Enter your String 2")
c=sorted(a)
d=sorted(b)
if c==d:
    print("String is a anagrame")
else:
    print("String is not a anagrame")