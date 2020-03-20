a = [12,9,61,5,14,]

for x in a:
    if x > 0 and str(x)==str(x)[::-1]:
        print(True)
        break
    
    if x < 0 and str(x)!=str(x)[::-1]:
        print(False)
        break