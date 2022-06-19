def main():
  expression = get_expression()
  members_of_expression = remove_space(expression)
  print(members_of_expression[1])

def get_expression():
  expression = input("Expression: ")
  return expression

def remove_space(expression):
  members_of_expression = expression.strip(" ")
  return members_of_expression

if __name__ == "__main__":
    main()