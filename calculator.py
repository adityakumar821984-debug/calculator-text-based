# A Simple calculator program authored by: [ADITYA KUMAR]
print("****************** BHAI KA CALCULATOR *******************")
print('MADE BY ADITYA KUMAR')
print("\n")
k = float(input("Enter the first number: "))
l = float(input("Enter the second number: "))
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponentiation")
choice = input("Enter choice(1/2/3/4/5/6): ")
print("\n")
if choice == "1":
    print(k, "+", l, "=", k + l)
elif choice == "2":
    print(k, "-", l, "=", k - l)
elif choice == "3":
    print(k, "*", l, "=", k * l)
elif choice == "4":
    if l == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print(k, "/", l, "=", k / l)
elif choice == "5":
    if l == 0:
        print("Error: Modulus by zero is not allowed.")
    else:
        print(k, "%", l, "=", k % l)
elif choice == "6":
    if k == 0 and l < 0:
        print("Error: Zero cannot have a negative exponent.")
    else:
        print(k, "**", l, "=", k ** l)
else:
    print("Invalid choice! Please select between 1 and 6.")
    
