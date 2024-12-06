new_list_left = list()
new_list_right = list()
list_sum = list()
sum = int()

with open("2024\Day 1\input.txt", "r") as file:
    for i in file:
        i = i.split("   ")
        new_list_left.append(int(i[0]))
        new_list_right.append(int(i[1]))

new_list_left.sort()
new_list_right.sort()

for i in range(0, len(new_list_left)):
    list_sum.append(abs(new_list_left[i] - new_list_right[i]))


for i in list_sum:
    sum += i

print(sum)