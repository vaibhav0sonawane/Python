#Function:block of statement that perform a specific task
#use to create a repetable code;

#syntax:
# function Defination(def meaning)
#    ||
# def func_name(parameter1,parameter2):
#     some work/process
#     return val


#CAll_FUNCTION

#func_name(arg1,arg2..)

#eg:

def cal_sum(a,b):
    sum=a+b
    print(sum)
    return sum
print("the sum of 2 & 3 is:",cal_sum(2,3))#1 type
cal_sum(13,10)#2 type
cal_sum(21,32)

#avg of 3 num
def avgSum(a,b,c):
    avg=(a+b+c)/3
    print(avg)
    return avg

avgSum(1,3,4)     