def main():
  expression = input_expression()
  operators = remove_space(expression)
  print_result(operators)

def input_expression():
  expression = input("Expression: ")
  return expression

def remove_space(expression):
  operators = expression.split(" ")
  return operators

def print_result(operators):
  x = float(operators[0])
  y = operators[1]
  z = float(operators[2])

  if (y == "+"):
    print(f"{x+z}")
  elif (y == "-"):
    print(f"{x - z}")
  elif (y == "*"):
    print(f"{x * z}")
  elif (y == "/"):
    if (z == 0):
      print("It's not possible to make this operation")
    else:
      print(f"{x / z}")

if __name__ == "__main__":
    main()