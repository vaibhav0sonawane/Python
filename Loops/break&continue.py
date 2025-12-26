num=[1,4,9,16,25,36,49,64,81,100]
print(num)
x=int(input("Enter number to find from tupple:"))
i=0
while i<len(num):
    if(x==num[i]):
        print("found")
        print("at position:",i)
        break#use to break the iteration 
    else:
        print("finding...")
    i+=1


#continue
i=0
while i<=5:
    if(i==3):
        i+=1
        continue #when it is true it skips the next steps and goes to next iteration(skips)
    print(i)
    i+=1