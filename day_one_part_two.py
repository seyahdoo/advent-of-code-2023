import re

with open("input_day_one.txt", encoding="utf-8") as f:
    lines = f.readlines()

regex = "(one)|(two)|(three)|(four)|(five)|(six)|(seven)|(eight)|(nine)|\\d"
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
    for match in re.finditer(regex, line):
        matches.append(match)
    if len(matches) <= 0:
        continue
    start_val = string_to_value(matches[0].group())
    end_val = string_to_value(matches[-1].group())
    sum += (start_val * 10) + end_val
print(sum)
