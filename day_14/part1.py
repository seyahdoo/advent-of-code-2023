



def main():
    with open("input.txt", encoding="utf-8") as f:
        lines = f.readlines()
        lines = list(map(lambda x: x.strip().strip("\ufeff"), lines))
    # lines = read_debug_input()
    rock_matrix = list(map(lambda x: list(x), lines))
    rock_matrix = roll_to_north(rock_matrix)
    print(calculate_north_load(rock_matrix))
    return 

def read_debug_input():
    debug_input = """
        O....#....
        O.OO#....#
        .....##...
        OO.#O....O
        .O.....O#.
        O.#..O.#.#
        ..O..#O..O
        .......O..
        #....###..
        #OO..#....
        """
    return debug_input.strip().split()

def roll_to_north(rock_matrix):
    for i in range(len(rock_matrix)):
        for x in range(1, len(rock_matrix)):
            for y in range(len(rock_matrix[0])):
                try:
                    if rock_matrix[x][y] == "O" and rock_matrix[x-1][y] == ".":
                        rock_matrix[x][y] = "."
                        rock_matrix[x-1][y] = "O"
                except Exception as e:
                    pass
    return rock_matrix

def calculate_north_load(rock_matrix):
    total_weight = 0
    l = len(rock_matrix)
    for x in range(l):
        weight = l-x
        for y in range(len(rock_matrix[0])):
            if rock_matrix[x][y] == "O":
                total_weight += weight
    return total_weight
 
if __name__ == '__main__':
    main()        