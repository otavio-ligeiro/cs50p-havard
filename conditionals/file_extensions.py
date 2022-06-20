def main():
  file_name = input_file_name()
  print_file_extension(file_name)

def input_file_name():
  file_name = input("File Name: ")
  return file_name

def print_file_extension(file_name):
  if ".gif" in file_name:
    print("image/gif")
  elif (".jpg" in file_name) or (".jpeg" in file_name):
    print("image/jpeg")
  elif ".png" in file_name:
    print("image/png")
  elif ".pdf" in file_name:
    print("application/pdf")
  elif ".txt" in file_name:
    print("text/plain")
  elif ".zip" in file_name:
    print("application/zip")
  else:
    print("application/octet-stream")

if __name__ == "__main__":
    main()