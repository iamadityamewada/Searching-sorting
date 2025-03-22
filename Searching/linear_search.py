nums = [1,5,7,8,9,5,2,1]
target = 99

def linear_search(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

print("Index:", linear_search(nums,target))
        
def linear(li,t):
    try:
        return li.index(t)
    except:
        return -1  
     
print("Index:", linear(nums,target))
         
