def main():
    message = input_message()
    change_to_lowercase(message)


def input_message():
    message = input()
    return message


def change_to_lowercase(message):
    message = message.lower()
    print(message)


main()
