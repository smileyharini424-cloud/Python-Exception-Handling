try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program execution completed.")
