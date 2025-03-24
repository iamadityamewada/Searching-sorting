arr = [12,14,26,26,45,89,98,101]
target = 98
arr.sort()
print(arr)

def binary_search(arr,tar):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right)//2
        if arr[mid] == tar:
            return mid 
        elif tar < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

print ("linear Search : ", binary_search(arr,target))
