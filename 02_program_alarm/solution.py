# Link: https://adventofcode.com/2019/day/2

def intcode_add(idx, intcode):
    intcode[intcode[idx+3]] = intcode[intcode[idx+1]] + intcode[intcode[idx+2]]
    return intcode

def intcode_mult(idx, intcode):
    intcode[intcode[idx+3]] = intcode[intcode[idx+1]] * intcode[intcode[idx+2]]
    return intcode

def intcode_output(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb
    return run_intcode(intcode)[0]

def run_intcode(intcode):
    idx = 0
    while idx < len(intcode):
        if intcode[idx] == 99:
            return intcode
        elif intcode[idx] == 1:
            intcode = intcode_add(idx, intcode)
        elif intcode[idx] == 2:
            intcode = intcode_mult(idx, intcode)
        else:
            print("Invalid intcode")
            return intcode
        idx += 4
    return intcode

def find_inputs_for_code(orig_intcode, des_num):
    for noun in range(99):
        for verb in range(99):
            if intcode_output(orig_intcode.copy(), noun, verb) == des_num:
                return 100 * noun + verb
    return None

def run_tests():
    assert run_intcode([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run_intcode([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert run_intcode([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert run_intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

def main():
    # Run examples provided in question
    run_tests()

    print("Part 1")
    with open("02_program_alarm/input.txt", "r") as f:
        intcode = list(map(int, f.read().split(",")))
        # Dealing with Error Code 1202
        intcode[1] = 12
        intcode[2] = 2
        print(run_intcode(intcode)[0])

    print("Part 2")
    with open("02_program_alarm/input.txt", "r") as f:
        intcode = list(map(int, f.read().split(",")))
        print(find_inputs_for_code(intcode, 19690720))

if __name__ == "__main__":
    main()