# 1. simple list

# l = [1,2,3,"Yash",True,76,23,56,37,99]
# print(l)
# print(type(l))
# print(l[1])

# print(l[-3]) # Negative index
# print(l[len(l)-3]) # Positive index
# print(l[5-3]) # Positive index
# print(l[2]) #Positive index


# if 8 in l:
#     print("yes")
# else:
#     print("no")    
# # output    no
# yes
# if "ash" in "yash":
#     print("yes")
# else:
#     print("no")
    
# # output yes    
    
# print(l)    
# print(l[1:9])
# print(l[1:9:3])    
        
# list comprehension

lst = [i*i for i in range(10)]
print(lst)

lst = [i*i for i in range(10) if i%2 == 0]
print(lst)