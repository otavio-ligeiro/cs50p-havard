def main():
  update_amount_due()

def insert_coin():
  coin = input("Insert Coin: ")
  coin = int(coin)
  return coin

def update_amount_due():
  amount_coin = 0
  amount_due = 50
  while (amount_coin < 50):
    print(f"Amount Due: {amount_due}")
    coin = insert_coin()
    if (coin == 5) or (coin == 10) or (coin == 25):
      amount_coin += coin
      amount_due -= coin
    else:
      continue
  change_owed = amount_coin - 50
  print(f"Change Owed: {change_owed}")


if __name__ == "__main__":
    main()