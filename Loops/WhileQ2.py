#element of the list using loop
#list=[1,4,9,16,15,36,49,64,100]
#i=0
#while i<len(list):
#    print(list[i])
#    i+=1

#2.Search for a number x in this tuple using loop
num=[1,4,9,16,25,36,49,64,81,100]
print(num)
x=int(input("Enter number to find from tupple:"))
i=0
while i<len(num):
    if(x==num[i]):
        print("found")
        print("at position:",i)
        i+=1