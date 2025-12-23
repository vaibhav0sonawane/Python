#1.Grade students based on marks
marks=int(input("Enter marks obtained by student:"))
print("The student has scored:", marks )
if(marks<=100 and marks>= 90):
    print("The student have got Grade A")
elif(marks<90 and marks>=80):
    print("The student have got Grade B")
elif(marks<80 and marks>=70):
    print("The student have got Grade C")
elif(marks<70 and marks>=0):
    print("The student have got Grade D")
else:
    print("Entered Invalid marks(enter marks out off 100)")
    
