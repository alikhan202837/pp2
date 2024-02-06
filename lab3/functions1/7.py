def has33(nums):
    for i in range(len(nums) - 1):
    
        if nums[i] == nums[i+1] and nums[i] == 3:
            return True
        
    return False  


n = int(input("Size: "))
a = []
for i in range(n):
    x = int(input())
    a.append(x)

print(has33(a))
