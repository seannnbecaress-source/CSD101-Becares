#Becares PROJECT
becares = input("Enter your name: ").title()
print(f"Mayong Buntag, {becares}!")

becareschoice = input("\n1.[Power]\n2.[Voltage]\n3.[Current]\nOption: ")

if becareschoice == "1":
    becaresv = float(input("Enter Voltage: "))
    becaresc = float(input("Enter Current: "))
    becaresp = becaresv * becaresc
    print(f"Power: {becaresp:.2f} W")

elif becareschoice == "2":
    becaresp = float(input("Enter Power: "))
    becaresc = float(input("Enter Current: "))
    becaresv = becaresp / becaresc
    print(f"Voltage: {becaresv:.2f} V")

elif becareschoice == "3":
    becaresp = float(input("Enter Power: "))
    becaresv = float(input("Enter Voltage: "))
    becaresc = becaresp / becaresv
    print(f"Current: {becaresc:.2f} A")

else:
    print("Invalid option.")
