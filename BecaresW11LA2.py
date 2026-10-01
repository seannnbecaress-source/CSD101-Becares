BecaresStudents = [("Jonah Perez", "BSCS", 1),
            ("Alex Santos", "BSMT", 2),
            ("Micah Mendoza", "BSCS", 2),
            ("Allen Torres", "BSMT", 1),
            ("Meljay Ronquillo", "BSCS", 3),
            ("Clarence Clemen", "BSMT", 4),
            ("Daniel Reyes", "BSCS", 3),
            ("Mark Villanueva", "BSMT", 4),
            ("Sofia Cruz", "BSCS", 3),
            ("Angela Garcia", "BSMT", 4)]


print(f"\n{'STUDENT INFORMATION':*^40}")
print ("Student Information: ")
BecaresProgram = input("Enter Program: ")
BecaresYear = int(input("Enter Year Level: "))
found = False

for BecaresStudents in BecaresStudents:
    if BecaresStudents[1] == BecaresProgram and BecaresStudents[2] == BecaresYear:
       print ("\nName: ", BecaresStudents[0])
       print ("Program: ", BecaresStudents[1])
       print ("Year Level: ", BecaresStudents[2])
    found = True

if not found:
    print("Input Capital Letter!")