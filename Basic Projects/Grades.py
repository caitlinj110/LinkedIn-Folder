print("Gradebook")
print()

student_grade=[]
student_name=[]
x=0

while True:
    
    print()
    fname=str(input("Student first name:"))
    lname=str(input("Student last name:"))
    user_grade=int(input("Enter Grade:"))

    student_name.append(fname +" "+lname)
    student_grade.append(user_grade)

    x+=user_grade

    print(student_name)
    print(student_grade)
    print(x)


   

