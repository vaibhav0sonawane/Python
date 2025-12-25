num1=int(input("Enter first number:"))
num2=int(input("Enter Second number:"))
num3=int(input("Enter Third number:"))
if(num1>num2 and num1>num3):
    print("number  ",num1," is greater")
elif(num2>num3):
    print("number ",num2," is greater")
else:
    print("number ",num3," is greater")