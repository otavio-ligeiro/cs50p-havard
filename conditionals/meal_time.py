def main():
    time = get_time()
    time = convert(time)
    print_meal(time)

def get_time():
  time = input("What time is it? ")
  return time

def convert(time):
  list_time = time.split(":")
  minutes = round(int(list_time[1]) / 60, 2) * 100
  minutes = int(minutes)
  time = list_time[0] + "." + str(minutes)
  time = float(time)
  return time

def print_meal(time):
  if (time >= 7) and (time <= 8):
    print("breakfast time")
  elif (time >= 12) and (time <= 13):
    print("lunch time")
  elif (time >= 18) and (time <= 19):
    print("dinner time")
  else:
    print("")


if __name__ == "__main__":
    main()