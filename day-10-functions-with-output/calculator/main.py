from art import logo

#calculator

def add(n1,n2):
  return n1 + n2
def substract(n1,n2):
  return n1 - n2
def multiply(n1,n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2

operations = {
  "+": add,
  "-": substract,
  "*": multiply,
  "/": divide
}
def calculator():
  print(logo)
  num1 = float(input("What is the first number?\n"))
  for opr in operations:
    print(opr)
  continue_calculation = True
  while continue_calculation:
    operator = input("Pick an operation?\n")
    num2 = float(input("What is the next number? \n"))
    calculate = operations[operator]
    answer = calculate(n1=num1,n2=num2)
    print(f"{num1} {operator} {num2} = {answer}")
  # give an option to continue the calculation
    choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start new calculation.: ").lower()
    if choice == "y":
      num1 = answer
    elif choice == "n":
      continue_calculation = False
      calculator()
calculator()