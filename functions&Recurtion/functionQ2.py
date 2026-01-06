#find the factorial of n
def fact_num(a):
    fact=1
    for el in range(1,a+1):
        fact=fact*el
    print("factorial is:",fact)
    return fact
fact_num(5)