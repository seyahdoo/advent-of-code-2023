


def strip_line(line:str):
    return line.strip().strip("\ufeff")

def get_win_count(line):
    winning_numbers = list(map(lambda x: int(x), line.split(":")[1].split("|")[0].split()))
    my_numbers = list(map(lambda x: int(x), line.split(":")[1].split("|")[1].split()))
    win_count = 0
    for number in my_numbers:
        if number in winning_numbers:
            win_count += 1
    return win_count

def get_point_from_win_count(win_count):
    point = 0 if win_count == 0 else pow(2, win_count - 1)
    return point

def main():
    with open("input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = list(map(strip_line, lines))
    sum = 0
    card_counts = list(map(lambda x: 1, lines))
    for i in range(0, len(lines)):
        # Card   1: 57 76 72 11  8 28 15 38 54 46 | 77 87 71 98 40  7 84 43 61 64  5 50 19 83 79 99 36 47  4 95 30 44 37 55 26
        line = lines[i]
        win_count = get_win_count(line)
        card_count = card_counts[i]
        points = get_point_from_win_count(win_count) * card_count
        sum += card_count
        for j in range(1, win_count+1):
            card_counts[i+j] += card_counts[i]
        
    print(sum)
    

main()