def main():
  answer = input_answer()
  answer = standardize_answer(answer)
  verify_answer(answer)

def input_answer():
  answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
  return answer

def standardize_answer(answer):
  answer = answer.lower()
  return answer

def verify_answer(answer):
  if (answer == "42") or (answer == "forty two") or (answer == "forty-two"):
    print("Yes")
  else:
    print("No")

if __name__ == "__main__":
    main()