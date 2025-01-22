# def average(a,b=1,c=1):
#     print("Average is: ", (a + b + c)/2)

# # average(4,9)    

# average(5,6)

def average(*numbers):
    sum = 0    
    for i in numbers:
        sum += i
    return  sum / len(numbers)
    
c = average(5,6,7,8)
print(c)