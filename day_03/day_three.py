



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

    
def is_touching(lines, position):
    i = position[0]
    j = position[1]
    length = position[2]
    
    x_low = i - 1
    x_high = i + 1
    y_low = j - 1
    y_high = j + length
    
    for i in range(x_low, x_high + 1):
        for j in range(y_low, y_high + 1):
            if is_toucher(lines, i, j):
                return True
    
    return False
    

def is_toucher(lines, i, j):
    if i < 0 or i >= 140:
        return False
    if j < 0 or j >= 140:
        return False
    char = lines[i][j]
    if char.isnumeric() or char == ".":
        return False
    return True

def strip_line(line:str):
    return line.strip().strip("\ufeff")

def main():
    with open("engine.schematic", encoding="utf-8") as f:
        lines = f.readlines()
    
    lines = list(map(strip_line, lines))
    positons = get_positions(lines)

    sum = 0
    for position in positons:
        if is_touching(lines, position):
            number = ""
            i = position[0]
            j = position[1]
            length = position[2]
            for k in range(j, length + j):
                number += lines[i][k]
            sum += int(number)

    print(sum)
    
main()