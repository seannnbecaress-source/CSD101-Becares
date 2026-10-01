salary = {
    "E104":{
         "EmpName": "Selena Gomez",
         "DailyHrs": [8, 9, 8.5, 10, 8]
},
"E601": {
    "EmpName": "Nikka Salonga",
    "DailyHrs": [9, 10, 8, 8, 9]
}
}

emp_id = input("Enter Employee ID: ")

if emp_id not in salary:
    print("not found")
else:
    employee = salary[emp_id]
    name = employee["EmpName"]
    hours = employee["DailyHrs"]

    print("\nEmployee Name:", name)
    print("Daily Hours:, hours" )

    weeklybasic = 9000
    rateperhour = weeklybasic / 40
    total_hours = sum(hours)

    print("Total Weekly Hours:", total_hours)
    print("Rate per Hour:", rateperhour)

    overtime = 0
    for h in hours:
        if h > 8:
            excess = h - 8
            overtime += excess * 1.5 * rateperhour

    print("Overtime:", overtime)

    grosspay = (40 * rateperhour) + overtime

    print("Gross Pay:", grosspay)


