#search num X in tupple using loop
tuple=(1,4,9,16,25,36,49,64,81,100)
print(tuple)
x=int(input("Enter a number to Search from the tupple:"))
for el in tuple:
    if(el==x):
        print(el,"found")
        break
    else:
        print("not found")
    