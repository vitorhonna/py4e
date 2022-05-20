import re
total = 0

with open('regex_sum_1559327.txt', 'r') as fh:
    for line in fh:
        line = line.strip()
        # print(line)
        numbers = re.findall('[0-9]+', line)
        for number in numbers:
            total += int(number)

print(total)
