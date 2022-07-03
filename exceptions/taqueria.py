def main():
    dishes = get_dishes()
    calculate_total_cost(dishes)


def get_dishes():
    dishes = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    return dishes

def calculate_total_cost(dishes):
    total_cost = 0
    while True:
        try:
            item = input("\nItem: \n").title()
            if item in dishes:
                total_cost += dishes[item]
                print(f"Total: ${total_cost:.2f}\n")
        except KeyError:
             pass
        except EOFError:
            break


if __name__ == "__main__":
    main()