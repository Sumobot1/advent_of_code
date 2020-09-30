# Link: https://adventofcode.com/2019/day/3

def gen_path(instruction_set):
    x, y, total_steps = 0, 0, 0
    final_path = {}
    for inst in instruction_set:
        dir, dist = inst[0], int(inst[1:])
        for i in range(dist):
            total_steps += 1
            if dir == "R":
                x += 1
                final_path[(x, y)] = total_steps
            elif dir == "L":
                x -= 1
                final_path[(x, y)] = total_steps
            elif dir == "U":
                y += 1
                final_path[(x, y)] = total_steps
            elif dir == "D":
                y -= 1
                final_path[(x, y)] = total_steps
    return final_path

def find_collisions(paths):
    shortest, longest = (paths[0], paths[1]) if len(paths[0]) < len(paths[1]) else (paths[1], paths[0])
    return [pos for pos in shortest if pos in longest]

def manhattan_dist(coord):
    return abs(coord[0]) + abs(coord[1])

def total_steps(collision, paths):
    return sum([path[collision] for path in paths])

def find_closest_collision(directions):
    paths = [gen_path(dirset) for dirset in directions]
    collisions = find_collisions(paths)
    distances = list(map(manhattan_dist, collisions))
    return min(distances)

def find_collision_with_fewest_steps(directions):
    paths = [gen_path(dirset) for dirset in directions]
    collisions = find_collisions(paths)
    distances = [total_steps(collision, paths) for collision in collisions]
    return min(distances)

def run_tests():
    ex1 = [["R75","D30","R83","U83","L12","D49","R71","U7","L72"],
           ["U62","R66","U55","R34","D71","R55","D58","R83"]]
    ex2 = [["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"],
           ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]]
    assert find_closest_collision(ex1) == 159
    assert find_closest_collision(ex2) == 135
    assert find_collision_with_fewest_steps(ex1) == 610
    assert find_collision_with_fewest_steps(ex2) == 410

def main():
    # Run examples provided in question
    run_tests()

    print("Part 1")
    with open("03_crossed_wires/input.txt", "r") as f:
        lines = [line.split(",") for line in f]
        print(find_closest_collision(lines))

    print("Part 2")
    with open("03_crossed_wires/input.txt", "r") as f:
        lines = [line.split(",") for line in f]
        print(find_collision_with_fewest_steps(lines))

if __name__ == "__main__":
    main()