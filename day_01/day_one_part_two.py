import re

with open("input_day_one.txt", encoding="utf-8") as f:
    lines = f.readlines()

regex = "^((one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|\\d)"
numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
sum = 0

def string_to_value(s:str):
    if(s[0].isnumeric()):
        return (int)(s[0])
    for i in range(1, 10):
        if(s == numbers[i]):
            return i
    return None

for line in lines:
    matches = []
    length = len(line)
    for i in range(0, length):
        match = re.match(regex, line)
        if match:
            matches.append(match.group())
        line = line[1:]
    if len(matches) <= 0:
        continue
    start_val = string_to_value(matches[0])
    end_val = string_to_value(matches[-1])
    sum += (start_val * 10) + end_val
    
print(sum)
