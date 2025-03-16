Ecsape
def calculate(num1, num2, operation):
  """Performs the specified mathematical operation on two numbers."""
  if operation == '+':
    return num1 + num2
  elif operation == '-':
    return num1 - num2
  elif operation == '*':
    return num1 * num2
  elif operation == '/':
    if num2 == 0:
      return "Division by zero!"
    else:
      return num1 / num2
  else:
    return "Invalid operation"

while True:
  try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    result = calculate(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")

    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
      break

  except ValueError:
    print("Invalid input. Please enter numbers only.")
  except Exception as e:
    print(f"An error occurred: {e}")