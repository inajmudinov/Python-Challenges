a=len(input())

s = [int(s) for s in input().split(" ")]

#s = [10,10,10,10,30,30]

#s=[1,2,3,4,5,6,7,8,0,1,1,1,1,0,4]
def checker(s):
    s.sort()
    summator = 0
    for x in s:
        summator+=s.count(x)/2
        s=s[s.count(x):]
    return int(summator)

print(checker(s))