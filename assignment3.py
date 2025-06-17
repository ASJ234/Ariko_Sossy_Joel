#Division program including error handling and a ifinite loop
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
        break  # Exit loop if everything is successful

    except ValueError:
        print(" Invalid input. Please enter numeric values.")

    except ZeroDivisionError:
        print(" Cannot divide by zero. Try again.")

    except Exception as e:
        print(f" An unexpected error occurred: {e}")
