# Link: https://adventofcode.com/2019/day/1
def fuel_for_mass(given_mass):
    return int(given_mass / 3) - 2

def fuel_for_fuel_for_mass(given_mass):
    curr_mass, sum = given_mass, 0
    while curr_mass > 0:
        curr_mass = max(fuel_for_mass(curr_mass), 0)
        sum += curr_mass
    return sum

def main():
    print("Part 1")
    with open("01_rocket_equation/input.txt", "r") as f:
        total_fuel = sum([fuel_for_mass(int(line)) for line in f])
        print(total_fuel)

    print("Part 2")
    with open("01_rocket_equation/input.txt", "r") as f:
        total_fuel_for_fuel = sum([fuel_for_fuel_for_mass(int(line)) for line in f])
        print(total_fuel_for_fuel)

if __name__ == "__main__":
    main()