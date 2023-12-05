


def strip_line(line:str):
    return line.strip().strip("\ufeff")

def main():
    with open("input.txt", encoding="utf-8") as f:
        lines = f.readlines()
    lines = list(map(strip_line, lines))
    sum = 0
    for line in lines:
        # Card   1: 57 76 72 11  8 28 15 38 54 46 | 77 87 71 98 40  7 84 43 61 64  5 50 19 83 79 99 36 47  4 95 30 44 37 55 26
        winning_numbers = list(map(lambda x: int(x), line.split(":")[1].split("|")[0].split()))
        my_numbers = list(map(lambda x: int(x), line.split(":")[1].split("|")[1].split()))
        win_count = 0
        for number in my_numbers:
            if number in winning_numbers:
                win_count += 1
        point = 0 if win_count == 0 else pow(2, win_count - 1)
        sum += point
    print(sum)
    

main()