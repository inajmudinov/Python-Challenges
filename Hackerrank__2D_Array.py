arr = [[int(x) for x in input().split(" ")] for y in range(9)]

def max_num(arr):
    return(sum(max(arr)))


print(max_num(arr))
