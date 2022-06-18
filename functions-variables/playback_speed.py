def main():
    message = input_message()
    replace_spaces(message)


def input_message():
    message = input()
    return message


def replace_spaces(message):
    message = message.replace(" ", "...")
    print(message)


main()