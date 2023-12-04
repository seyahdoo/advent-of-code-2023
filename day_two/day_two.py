


with open("day_two.input", encoding="utf-8") as f:
    lines = f.readlines()

def is_process_impossible(pulls):
    for pull in pulls:
        count_colors = pull.split(",")
        for count_color in count_colors:
            count_color_split = count_color.strip().split(" ")
            count = int(count_color_split[0])
            color = count_color_split[1]
            if color == "red" and count > 12:
                return True
            if color == "green" and count > 13:
                return True
            if color == "blue" and count > 14:
                return True
    return False

sum = 0

for line in lines:
    # Game 1: 4 red, 5 blue, 9 green; 7 green, 7 blue, 3 red; 16 red, 7 blue, 3 green; 11 green, 11 blue, 6 red; 12 red, 14 blue
    id = line.split(":")[0].split(" ")[1]
    pulls = line.split(":")[1].split(";")
    if not is_process_impossible(pulls):
        sum += int(id)
            
print(sum)