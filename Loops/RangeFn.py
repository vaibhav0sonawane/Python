#it returns a sequence of numbers starting from 0 by default and increment by 1 and stop before a specific number
#three ways to write range
#if only single value i.e-range(10):here 10 is end value
print("1-10")
for i in range(10):
    print(i)


#if only 2 value i.e-range(2,10):here 10 is end value and 2 is start value
print("10-20")
for i in range(11,20,):
    print(i)
#if only single value i.e-range(10):here 10 is end value,2 is start,3 is step size:increament
print("21-30")
for i in range(21,30,3):
    print(i)