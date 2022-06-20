def main():
  fruit_inputed = input_fruit()
  fruits = get_fruits()
  get_calories(fruit_inputed, fruits)

def get_fruits():
  fruits = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "cantaloupe": 50,
    'grapefruit': 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plumns": 70,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 80
  }
  return fruits

def standardize_fruit(fruit):
  fruit = fruit.lower()
  return fruit

def input_fruit():
  fruit = input("Item: ")
  fruit = standardize_fruit(fruit)
  return fruit

def get_calories(fruit_inputed, fruits):
  if fruit_inputed in fruits:
    print(f"Calories: {fruits[fruit_inputed]}")
  else:
    print("")

if __name__ == "__main__":
    main()