# Link: https://adventofcode.com/2019/day/4
from collections import Counter

def is_increasing(num_list):
    return all(num_list[i] >= num_list[i-1] for i in range(1, len(num_list)))

def has_adjacent_equal_digits(num_list):
    return any(num_list[i] == num_list[i-1] for i in range(1, len(num_list)))

def increasing_with_adjacent_digits(num):
    num_list = [int(i) for i in str(num)]
    return is_increasing(num_list) and has_adjacent_equal_digits(num_list)

def increasing_with_distinct_adjacent_digits(num):
    num_list = [int(i) for i in str(num)]
    # If the list is increasing, adjacent values must be beside each other
    return is_increasing(num_list) and 2 in Counter(num_list).values()

def run_tests():
    assert increasing_with_adjacent_digits(111111) == True
    assert increasing_with_adjacent_digits(223450) == False
    assert increasing_with_adjacent_digits(123789) == False

    assert increasing_with_adjacent_digits(112233) == True
    assert increasing_with_distinct_adjacent_digits(112233) == True
    assert increasing_with_adjacent_digits(123444) == True
    assert increasing_with_distinct_adjacent_digits(123444) == False
    assert increasing_with_adjacent_digits(111122) == True
    assert increasing_with_distinct_adjacent_digits(111122) == True

def main():
    # Run examples provided in question
    run_tests()

    print("Part 1")
    with open("04_secure_container/input.txt", "r") as f:
        num_passwords = 0
        range_start, range_end = tuple(f.read().split("-"))
        for i in range(int(range_start), int(range_end)):
            if increasing_with_adjacent_digits(i):
                num_passwords += 1
        print(num_passwords)

    print("Part 2")
    with open("04_secure_container/input.txt", "r") as f:
        num_passwords = 0
        range_start, range_end = tuple(f.read().split("-"))
        for i in range(int(range_start), int(range_end)):
            if increasing_with_distinct_adjacent_digits(i):
                num_passwords += 1
        print(num_passwords)

if __name__ == "__main__":
    main()