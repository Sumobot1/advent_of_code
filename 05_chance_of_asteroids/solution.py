# Link: https://adventofcode.com/2019/day/5
def get_item_with_mode(idx, intcode, mode):
    if mode == 0:
        return intcode[intcode[idx]]
    else:
        return intcode[idx]

def gen_codes(num):
    opcode = num % 100
    modes = [int(x) for x in str(int(num / 100))]
    modes = [0] * (3-len(modes)) + modes
    return opcode, list(reversed(modes))

def intcode_add(idx, intcode, modes):
    intcode[intcode[idx+3]] = get_item_with_mode(idx+1, intcode, modes[0]) + get_item_with_mode(idx+2, intcode, modes[1])
    return intcode, idx+4

def intcode_mult(idx, intcode, modes):
    intcode[intcode[idx+3]] = get_item_with_mode(idx+1, intcode, modes[0]) * get_item_with_mode(idx+2, intcode, modes[1])
    return intcode, idx+4

def intcode_input(idx, intcode, modes, input):
    intcode[intcode[idx+1]] = input
    return intcode, idx+2

def intcode_output(idx, intcode, modes):
    print(get_item_with_mode(idx+1, intcode, modes[0]))
    return intcode, idx+2

def intcode_jump_true(idx, intcode, modes):
    if get_item_with_mode(idx+1, intcode, modes[0]) != 0:
        return intcode, get_item_with_mode(idx+2, intcode, modes[1])
    return intcode, idx+3

def intcode_jump_false(idx, intcode, modes):
    if get_item_with_mode(idx+1, intcode, modes[0]) == 0:
        return intcode, get_item_with_mode(idx+2, intcode, modes[1])
    return intcode, idx+3

def intcode_less_than(idx, intcode, modes):
    intcode[intcode[idx+3]] = 1 if get_item_with_mode(idx+1, intcode, modes[0]) < get_item_with_mode(idx+2, intcode, modes[1]) else 0
    return intcode, idx+4

def intcode_equals(idx, intcode, modes):
    intcode[intcode[idx+3]] = 1 if get_item_with_mode(idx+1, intcode, modes[0]) == get_item_with_mode(idx+2, intcode, modes[1]) else 0
    return intcode, idx+4

def run_intcode(intcode, given_input=None):
    idx = 0
    while idx < len(intcode):
        code = int(intcode[idx])
        opcode, modes = gen_codes(int(intcode[idx]))
        if opcode == 99:
            return intcode
        elif opcode == 1:
            intcode, idx = intcode_add(idx, intcode, modes)
        elif opcode == 2:
            intcode, idx = intcode_mult(idx, intcode, modes)
        elif opcode == 3:
            intcode, idx = intcode_input(idx, intcode, modes, given_input)
        elif opcode == 4:
            intcode, idx = intcode_output(idx, intcode, modes)
        elif opcode == 5:
            intcode, idx = intcode_jump_true(idx, intcode, modes)
        elif opcode == 6:
            intcode, idx = intcode_jump_false(idx, intcode, modes)
        elif opcode == 7:
            intcode, idx = intcode_less_than(idx, intcode, modes)
        elif opcode == 8:
            intcode, idx = intcode_equals(idx, intcode, modes)
        else:
            print("Invalid intcode")
            return intcode
    return intcode

def run_tests():
    # Make sure tests from Day 2 still work
    assert run_intcode([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run_intcode([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert run_intcode([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert run_intcode([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99]

    # Run Examples Provided in Day 5
    assert run_intcode([1002,4,3,4,33], 0) == [1002, 4, 3, 4, 99]
    assert run_intcode([1101,100,-1,4,0], 0) == [1101, 100, -1, 4, 99]
    print("Output Should be 0:")
    run_intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 0)
    print("Output Should be 1:")
    run_intcode([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], 1)
    print("Output Should be 0:")
    run_intcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 0)
    print("Output Should be 1:")
    run_intcode([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], 1)

def main():
    # Run examples provided in question
    run_tests()

    print("Part 1")
    with open("05_chance_of_asteroids/input.txt", "r") as f:
        diag_output = list(map(int, f.read().split(",")))
        print(run_intcode(diag_output.copy(), 1)[0])

    print("Part 2")
    with open("05_chance_of_asteroids/input.txt", "r") as f:
        diag_output = list(map(int, f.read().split(",")))
        print(run_intcode(diag_output.copy(), 5)[0])

if __name__ == "__main__":
    main()