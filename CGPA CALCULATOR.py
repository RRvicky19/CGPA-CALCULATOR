sublist = [
    "HS815 : Communicative English -",
    "BS8161 : Physics and Chemistry Laboratory -",
    "CY8151 : Engineering Chemistry -",
    "GE8151 : Problem Solving and Python Programming -",
    "GE8152 : Engineering Graphics -",
    "GE8161 : Problem Solving and Python Programming Laboratory -",
    "MA8151 : Engineering Mathematics - I -",
    "PH8151 - Engineering Physics"
    ]
credit_points =[4,2,3,3,4,2,4,3]
grade_list=[["O",10],["A+",9],["A",8],["B+",7],["B",6],["F",0]]
Mark_list=[]
total=0
cre=0
name = input("Enter the Name :")
Regno = int(input("Enter the Register number :")) 
print("Enter the Grade")
for i in sublist:
    print(i,end=" ")
    Mark_list.append(input())
    print("\n")
for i in range(len(Mark_list)):
    x=1
    for j in grade_list:
        if Mark_list[i]==j[0]:
            x=j[1]*credit_points[i]
            if x!=0:
                cre = cre+credit_points[i]
    total=total+x
total = total/cre
print("Your GPA value is :",total)
