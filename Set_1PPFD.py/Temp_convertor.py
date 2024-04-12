choice = input("Enter 'C' to convert from Celsius to Fahrenheit, or 'F' to convert from Fahrenheit to Celsius: ").upper()

if choice == 'C':
    c = float(input("Enter Celsius temperature: "))
    f = (c * 9/5) + 32
    print("Fahrenheit:", round(f, 2))
elif choice == 'F':
    f = float(input("Enter Fahrenheit temperature: "))
    c = (f - 32) * 5/9
    print("Celsius:", round(c, 2))
else:
    print("Invalid choice. Please enter 'C' or 'F'.")
    