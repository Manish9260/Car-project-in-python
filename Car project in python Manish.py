# This is a Car project and By TechManish......😍
print("**************************************")
print("---------|| Car Project ||------------")
print("**************************************")
print("--------|| By : TechManish ||---------")
print("**************************************")

# Define Car Functions
def kia():
    print("\nWelcome to Kia Company:")
    print("Colors: Red, Green, Blue, White")
    print("Engine: 45 HP")
    print("Top Speed: 300 km/h")
    print("Fuel Type: Petrol")
    print("Price: 13.45 - 34.4 Lakh")
    print("Thanks for Visiting Kia Company!\n")

def XUV700():
    print("\nWelcome to XUV700 Company:")
    print("Colors: Red, Green, Blue, White")
    print("Engine: 45 HP")
    print("Top Speed: 300 km/h")
    print("Fuel Type: Petrol")
    print("Price: 13.45 - 34.4 Lakh")
    print("Thanks for Visiting XUV700 Company!\n")

def Brezza():
    print("\nWelcome to Brezza Company:")
    print("Colors: Red, Green, Blue, White")
    print("Engine: 45 HP")
    print("Top Speed: 300 km/h")
    print("Fuel Type: Petrol")
    print("Price: 13.45 - 34.4 Lakh")
    print("Thanks for Visiting Brezza Company!\n")

# Dictionary to map car names (optional use)
car_function = {
    "kia": kia,
    "XUV700": XUV700,
    "Brezza": Brezza
}

# Main menu loop
while True:
    print("\n============ Car Menu ===========")
    print("1. View Kia Details")
    print("2. View XUV700 Details")
    print("3. View Brezza Details")
    print("4. Exit Project")
    print("==================================")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        kia()
    elif choice == "2":
        XUV700()
    elif choice == "3":
        Brezza()
    elif choice == "4":
        print("Exiting the Car Project. Goodbye!")
        break
    else:
        print("Invalid Input! Please Choose from 1 to 4.")
