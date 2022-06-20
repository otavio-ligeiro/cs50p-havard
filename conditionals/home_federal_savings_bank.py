def main():
  greeting = input_greeting()
  greeting = standardize_greeting(greeting)
  verify_greeting(greeting)

def input_greeting():
  greeting = input("Greeting: ")
  return greeting

def standardize_greeting(greeting):
  greeting = greeting.lower()
  return greeting

def verify_greeting(greeting):
  if "hello" in greeting:
    print("$0")
  elif greeting[0] == "h":
    print("$20")
  else:
    print("$100")

if __name__ == "__main__":
    main()