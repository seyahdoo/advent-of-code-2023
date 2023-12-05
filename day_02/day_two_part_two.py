


with open("day_two.input", encoding="utf-8") as f:
    lines = f.readlines()

def get_power(pulls):
    reds = 0
    greens = 0
    blues = 0
    for pull in pulls:
        count_colors = pull.split(",")
        for count_color in count_colors:
            count_color_split = count_color.strip().split(" ")
            count = int(count_color_split[0])
            color = count_color_split[1]
            if color == "red":
                reds = max(count, reds)
            if color == "green":
                greens = max(count, greens)
            if color == "blue":
                blues = max(count, blues)
    return reds * greens * blues            

sum = 0

for line in lines:
    # Game 1: 4 red, 5 blue, 9 green; 7 green, 7 blue, 3 red; 16 red, 7 blue, 3 green; 11 green, 11 blue, 6 red; 12 red, 14 blue
    id = line.split(":")[0].split(" ")[1]
    pulls = line.split(":")[1].split(";")
    power = get_power(pulls)
    sum += power
            
print(sum)