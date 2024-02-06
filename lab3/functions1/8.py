
def spygame(a):
    word007 = ""
    for i in range(len(a)):
        if(a[i] == 0 or a[i] == 7):
            word007 += str(a[i])


    if ("007" in word007): 
        return True
    else:
        return False
    

x = list(map(int, input().split()))
ans = bool(spygame(x))
print(ans)

