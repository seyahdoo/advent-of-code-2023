

def get_length_of_number(lines, i, j):
    line = lines[i]
    k = j
    while k < len(line) and line[k].isnumeric():
        k += 1
    return k - j

def get_positions(lines):
    positons = []
    for i in range(0, len(lines)):
        line = lines[i]
        # noinspection PyRedeclaration
        is_not_on_number = True
        for j in range(0, len(line)):
            char:str = line[j]
            if is_not_on_number and char.isnumeric():
                positons.append((i,j, get_length_of_number(lines, i, j)))
            is_not_on_number = not char.isnumeric()
    return positons

    
def is_touching(lines, number_position, gear_position):
    i = number_position[0]
    j = number_position[1]
    length = number_position[2]
    
    x_low = i - 1
    x_high = i + 1
    y_low = j - 1
    y_high = j + length
    
    for i in range(x_low, x_high + 1):
        for j in range(y_low, y_high + 1):
            if i == gear_position[0] and j == gear_position[1]:
                return True
    return False
    

def strip_line(line:str):
    return line.strip().strip("\ufeff")

def get_number(lines, position):
    number = ""
    i = position[0]
    j = position[1]
    length = position[2]
    for k in range(j, length + j):
        number += lines[i][k]
    return int(number)
    
def main():
    with open("engine.schematic", encoding="utf-8") as f:
        lines = f.readlines()
    
    lines = list(map(strip_line, lines))
    positons = get_positions(lines)

    sum = 0
    for i in range(0, 140):
        for j in range(0, 140):
            if (lines[i][j] == "*"):
                # for each gear
                toucher_positions = []
                for position in positons:
                    if is_touching(lines, position, (i,j)):
                        toucher_positions.append(position)
                if len(toucher_positions) == 2:
                    ratio = get_number(lines, toucher_positions[0]) * get_number(lines, toucher_positions[1])
                    sum += ratio
    print(sum)
    
main()