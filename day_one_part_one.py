import os

with open("input_day_one.txt", encoding="utf-8") as f:
    lines = f.readlines()
    sum = 0
    for line in lines:
        num1 = 0
        for c in line:
            if c.isnumeric():
                num1 = int(c)
                break
        reverse = line[::-1]
        num2 = 0
        for c in reverse:
            if c.isnumeric():
                num2 = int(c)
                break
        sum += (num1 * 10) + num2
    print(sum)
