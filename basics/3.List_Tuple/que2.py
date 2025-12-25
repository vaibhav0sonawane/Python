#check if list is in form of palindrome 
#same from end to start and start to end
list=[1,2,3,4,3,2,1]
print("orignal list:",list)
list1=list.copy()
list1.reverse()
print("Reversed list:",list)
if(list==list1):
    print("list is pallidrome")
else:
    print("List is not pallidrome")
