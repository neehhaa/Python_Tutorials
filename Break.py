list=[1,2,3,4]
count = 0;
for i in list:
    if i==3:
        print("Item matched")
        count=count+1
        break
print("found at",count,"location")