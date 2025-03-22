# def Square(num):
#     if num % 2 == 0:
#      num = num**2
#     return num
# # print(Square(6))


# # def validate(fun, num):
# #     if num % 2 == 0:
# #         return fun(num)

# # or

# def validate(fun):
#     def wrap(num):
#         if num %2 == 0:
#             return fun(num)
#     return wrap
    
# res = validate(Square)
# # print(res)
# res = res(4)
# print(res)

# decorator - decorator is a another function which helps to change the working pattern of existing function without touching it.
# making the same by using decorator

# def validate(fun):
#     def wrapper(num):
#         if num %2 == 0:
#             return (fun(num) - num)
#         else:
#             return "incorrect data"
#     return wrapper   

# @validate
# def getSquare(num):
#     return num*num

# res = getSquare(4)
# print(res)

# 2

# def hidePassword(fun):
#     def Wrapper():
#         res = fun()
#         del res["password"]
#         return res
#     return Wrapper

# @ hidePassword
# def getUserDetails():
#     return { "name" : "anshu",
#              "age" : 12,
#              "password" : "Anshu@123"}
    
# resu = getUserDetails()
# print(resu)

# 3 1st largest number

# li = [2,4,5,45,52]
# # largest = 0
# # for i in li:
# #     if i > largest:
# #         largest = i
# # print(largest)
    
# # 4 : 2nd max number 
# largest = 0
# li2 = []
# for i in li:
#     if i > largest :
#         largest = i
#         li2.append(i)
        
# print(largest, li2)
# print(li2[-2])

# # or
# max_num = 0
# sec_max = 0
# for i in li:
#     if i > max_num:
#         sec_max = max_num
#         max_num = i
#     elif i > sec_max and i != max_num:
#         sec_max = i
# print(max_num, sec_max)
        