#recursion:when a function calls itself repeately
def show(n):
    if(n==0):#base case-to end the recursion
        return
    print("*")
    show(n-1)
show(5)