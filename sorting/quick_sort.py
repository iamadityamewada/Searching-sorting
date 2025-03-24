arr = [10,20,30,40,58,45,14,12]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = []
    right = []
    middle = []
    for i in arr:
        if i < arr[mid]:
            left.append(i)
        elif i > arr[mid]:
            right.append(i)
        else:
            middle.append(i)   

    # print("left: " ,left)
    # print('right :' ,right)
    # print("middle : ", middle)

    left = quick_sort(left)
    right = quick_sort(right)

    return left + middle + right

print("Quick Sort : ", quick_sort(arr))    

