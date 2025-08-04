def add(a, b): 
  return f"The addition of the given numbers is: {a+b}"
def subtract(a,b):
   return f"The subtraction of the given numbers is: {a-b}"  
def multiply(a,b):
   return f"The multiplication of the given numbers is: {a*b}"
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return f"The division of the given numbers is: {a / b}"
    
def get_number(prompt):
  while True:
    try:
      return float(input(prompt + " "))
    except ValueError:
      print("Invalid input. Please enter valid a number") 

print("Welcome to Calculator")

try:
  while True:
    number1 = get_number("Enter the first number:")
    number2 = get_number("Enter the second number:")

    print("Operations Available: + - / *")
    operator = input("Choose the operation you want to perform: ")

    match (operator):
      case '+':
        result = add(number1, number2)
      case '-':
        result = subtract(number1, number2)
      case '*':
        result = multiply(number1, number2)
      case '/':
        result = divide(number1, number2)
      case _:
        result = "Invalid Operator"
    print(result)

    toStop = input("Press 'X' to stop the calculator, Press any other key to continue: ")
    if toStop.lower() == 'x':
      print("Calculator Stopped.")
      break
except Exception as err:
  print(f"Error Occured: {err}")           
