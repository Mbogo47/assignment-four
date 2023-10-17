math = int(input("Input your Math Grade? "))
physics = int(input("Input your Physics Grade? "))
geo = int(input("Input your Geo Grade? "))
chem = int(input("Input your Chem Grade? "))

grade = (math + physics + geo + chem) / 4

print(grade)

if grade < 0 or grade > 100:
     print("Unrecognized marks/avg")
elif grade >= 0 and grade <= 30:
     print("GRADE: D")
elif grade >= 31 and  grade <= 50:
     print("GRADE: C")
elif grade >= 51 and grade <= 70:
    print("GRADE: B")
else:
     print("GRADE A")


