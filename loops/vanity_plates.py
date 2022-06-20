def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    continue 

def verify_plate_length(plate):
  plate_length = len(plate)
  if (plate_length >= 2) and (plate_length <= 6):
    return True
  else:
    return False

def verify_first_characters(plate):
  first_two_characters = plate[:2]
  if first_two_characters.isalpha():
    return True
  else:
    return False

def verify_numbers_between_letters(palte):
  

def verify_ponctuation(plate):
  ponctuation = ["!", "'", '"', "#", "$", "%", "&", "(", ")", "*", "+", ",", "-", ".", "/", ":",
  ";", "<", "=", ">", "?", "@", "[", "^", "_", "`", "{", "|", "}", "~"]
  if plate in ponctuation:
    return False
  else:
    return True

def verify_space(plate):
  if " " in plate:
    return False
  else:
    True

main()