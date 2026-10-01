BecaresName = input("Enter your name: ")
BecaresTitle = BecaresName.title()
print(f"TITTLE: {BecaresTitle}")

print("1.Power")
print("2.Voltage")
print("3.Current")

BecaresChoice = input("Choose: ")

if BecaresChoice == "1":
    BecaresV = float(input("Enter Voltage: "))
    BecaresI = float(input("Enter Current: "))
    BecaresP = BecaresV * BecaresI
    print(f"Power: {BecaresP:.2f}")

elif BecaresChoice == "2":
        BecaresP = float(input("Enter power: "))
        BecaresI = float(input("Enter current: "))
        BecaresV = BecaresP / BecaresI
        print(f"Voltage: {BecaresV:.2f}")

elif BecaresChoice == "3":
        BecaresP = float(input("Enter power: "))
        BecaresV = float(input("Enter voltage: "))
        BecaresI = BecaresP / BecaresV
        print(f"Current: {BecaresI:.2f}")

else:
    print("Invalid Choice")
