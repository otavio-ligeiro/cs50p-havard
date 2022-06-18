def main():
    message = input_message()
    make_faces(message)


def input_message():
    message = input()
    return message


def make_faces(message):
    message = message.replace(":)", "\U0001F603")
    message = message.replace(":(", "\U0001F614")  
    print(message)
    

main()