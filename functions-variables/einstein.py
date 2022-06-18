def main():
    m = input_mass()
    calculate_energy(m)


def input_mass():
    m = int(input("m: "))
    return m


def calculate_energy(m):
    c = 300000000
    E = m * (pow(c, 2))
    print(f"E: {E}")


main()