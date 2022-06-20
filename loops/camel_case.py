def main():
  string = input_string()
  convert_snake_case(string)

def input_string():
  string = input("camelCase: ")
  return string

def convert_snake_case(camel_case):
  snake_case = ""
  capital_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
  "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
  for letter in camel_case:
    if letter in capital_letters:
      snake_case += "_"
      snake_case += letter.lower()
    else:
      snake_case += letter
  print(f"snake_case: {snake_case}")

if __name__ == "__main__":
    main()