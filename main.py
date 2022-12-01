# wat hier eigenlijk staat:
# for line in f:
#   lines.append(line.rstrip())
with open('day1.txt') as f:
    lines = [line.rstrip() for line in f]

part1 = 0
calories = []
part2 = []
for line in lines:
    if line == '':
        total_calories = sum(calories)
        part2.append(total_calories)
        if total_calories > part1:
            part1 = total_calories
        calories = []
    else:
        calories.append(int(line))

# print(part1)

part2.sort(reverse=True)
part2 = sum(part2[:3])
# or:
# part2 = part2[0] + part2[1] + part2[2]
print(part2)
