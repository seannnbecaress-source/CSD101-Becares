BecaresStudents={"Ana":[98,85,82],
          "Kirk":[72,73,78],
          "Liza":[69,71,83]
}

BecaresHighest = 0
Becaresnamehighest = ""
Becareslowest = 100
Becaresnamelowest = ""
Becarestally = 0

for name,grade in BecaresStudents.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "Average:", average)
    if average > BecaresHighest:
        BecaresHighest = average
        Becaresnamehighest = name
    if average < Becareslowest:
        Becareslowest = average
        Becaresnamelowest = name
    for g in grade:
        if g < 75:
            tally = Becarestally + 1

print(f"\nStudent {Becaresnamehighest} got the highest average: {BecaresHighest}")
print(f"Student {Becaresnamelowest} got the lowest average: {Becareslowest}")
print(f"There are {Becarestally} grades which are below 75.")