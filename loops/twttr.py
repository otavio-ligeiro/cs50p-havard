def main():
  message = input_message()
  remove_vowels(message)

def input_message():
  message = input("Input: ")
  return message

def remove_vowels(message):
  vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
  for vowel in vowels:
    if vowel in message:
      message = message.replace(vowel, "")
  print(f"Output: {message}")

if __name__ == "__main__":
    main()