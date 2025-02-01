from art import * 

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
operations = {
   "+": add,
   "-": subtract,
   "*": multiply,
   "/":divide,
}

def calculator():
    tprint("calc")
    should_accumulate = True
    num1 = float(input("What is the first number?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operations_symb = input("Pick an operation: ")
        num2 = float(input("What is the second number?: "))
        answer = operations[operations_symb](num1, num2)
        print(f"{num1} {operations_symb} {num2} = {answer}")
        choice = input(f" Type 'y' to continue calculating with {answer}, or type 'n' to start working on a new calculation\n")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()