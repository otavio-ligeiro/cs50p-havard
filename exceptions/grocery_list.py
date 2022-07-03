def main():
    grocery_list = create_grocery_list()
    print_grocery_list(grocery_list)

def create_grocery_list():
    grocery_list = {}
    while True:
        try:
            item = input("")
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except KeyError:
            pass
        except EOFError:
            break
    return grocery_list

def print_grocery_list(grocery_list):
    grocery_list_sorted = dict(sorted(grocery_list.items()))
    for item, quantity in grocery_list_sorted.items():
        print(f"{quantity} {item.upper()}")

if __name__ == "__main__":
    main()