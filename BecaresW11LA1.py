while True:

    becaresflavor = input("\nSelect Flavor (Neopolitan/Meat Lover/Pepperoni): ").lower()

    if becaresflavor == "neopolitan":
        print("You Have Selected Neopolitan")

    elif becaresflavor == "meat lover":
        print("You Have Selected Meat Lover")

    elif becaresflavor == "pepperoni":
        print("You Have Selected Pepperoni")

    else:
        print("Invalid Flavor")
        continue

    becaressize = input("Enter Size (Small, Medium, Large): ").lower()

    match becaressize:
        case "small":
            becaresprice = 250

        case "medium":
            becaresprice = 350

        case "large":
            becaresprice = 450

        case _:
            print("Invalid Size")
            continue

    print("Pizza Price:", becaresprice)

    again = input("\nWould you like to order again? (yes/no): ").lower()

    if again != "yes":
        print("Thank you for ordering! ")
        break
