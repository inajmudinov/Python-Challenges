length=input()

list=[int(i) for i in input().split(",")]

b = any(str(i)==str(i)[::-1] for i in list)

c = all( i>0 for i in list)

print(b and c)


