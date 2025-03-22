# by default sorting method in python work on "merge sort"
# bubble sort , selection sort and insertion sort is not mostly used in practical
# merge sort and quick sort are used widely
# "for i in range()" gives index rather than actual value where as "for i in li" gives actual value

# "bubble sort" - jst bagal wale se match kro agar 1st value big h to swap krdo ni to next value ko match kro or end tk jao in one turn
# bubble sort me largest number hmesa last me hoga, gives list in ascending order

li = [4,6,2,5,1,3]
def Bubble_sort(li):
    for ind in range(len(li)-1):
        for i in range(len(li)-1-ind):
            # print(i,i+1)
            if li[i] > li[i+1]:
             li[i],li[i+1] = li[i+1], li[i]
            #  temp = li[i]
            #  li[i] = li[i+1]
            #  li[i+1] = temp
    return li
        
# print(Bubble_sort(li))


# "selection sort" - ek min_index naam ka variable bnayenge . agar bagl wala number greater hua to min_index to update krdenge new value ke index ke or list ke last tk visit krenge or final jo min_index ki value aayegi usko 0 index value se update krenge. 
# by default min_index ki value 0 hogi or harr turn ke badd ek ek increase krenge
# selection sort sort he list in descending order

def Selection_sort(li):
    for i in range(len(li)-1):
        min_index = i
        # or- for j in range(i+1,len(li)):
        for j in range(i , len(li)-1):   
            if li[min_index] < li[j+1]:
                min_index = j+1
        if i != min_index:
            li[min_index],li[i] = li[i],li[min_index]
    return li
# print(Selection_sort(li))



#Insertion sort start with second positon and compare with all previous position and perform swap 

nums = [44, 33,25,66,78,56,44]

def insertion_sort(li):
    for i in range(2,len(li)):
        temp = li[i]
        for j in range(i-1,-1,-1):
          if temp < li[j]:  
            li[j+1] = li[j]
            li[j] = temp
    return li

# print(insertion_sort(nums))



#merge-sort :
#

def merge(left,right):
   combined = []
   i = 0
   j = 0
   while i < len(left) and j < len(right):
      if left[i] < right[j]:
         combined.append(left[i])
         i+=1
      else:
         combined.append(right[j])
         j+=1
   combined.extend(left[i:])
   combined.extend(right[j:])     

   return combined

def merge_sort(li):
   
   if len(li) == 1:
      return li
   
   mid = len(li)//2

   left = li[0:mid]
   right = li[mid:]
   
   left = merge_sort(left)
   right = merge_sort(right)

   return merge(left,right)


print("merge sort : ", merge_sort(nums))

