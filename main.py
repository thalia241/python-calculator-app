# Charity Deel
def calculator():
    print("Welcome to the Calculator App!")
    print("Available operations: +, -, *, /")
    print("Type 'exit' to quit the application.")

    while True:
        # Get user input
        user_input = input("\nEnter your calculation (e.g., 5 + 3): ")

        # Exit condition
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            # Split the input into parts
            operands = user_input.split()
            if len(operands) != 3:
                raise ValueError("Invalid format. Use: number operator number")

            num1 = float(operands[0])
            operator = operands[1]
            num2 = float(operands[2])

            # Perform calculation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2
            else:
                raise ValueError("Invalid operator. Use +, -, *, or /.")

            print(f"Result: {result}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except Exception as e:
            print(f"Unexpected error: {e}")


# Run the calculator

if __name__ == "__main__":
    calculator()