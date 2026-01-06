#WAP to calculate the sum of first natural number
def num(n):
    sum=0
    if(n==0):
        return 0
    return num(n-1) + n
    
sum=num(5)
print(sum)