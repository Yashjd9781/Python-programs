import time
t = time.strftime("%H:%M:%S")
hour = int(time.strftime("%H"))
hour = int(input("Enter hour"))
print(hour)

if(hour>=0 and hour<12):
    print("Good morning Yash")
elif(hour>=12 and hour<17):
    print("Good afternoon Yash")
elif(hour>=17 and hour<12):
    print("Good night Yash")
