#find the factorial of first n numbers
n=int(input("enter a number for factorial:"))
sum=1

for i in range(1,n+1) :
    sum=sum*i
print("factorial of the given number is:",sum)
 