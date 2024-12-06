new_list_left = list()
new_list_right = list()
count_index = int()
count = int()
similarity_score = int()

with open("2024\Day 1\input.txt", "r") as file:
    for i in file:
        i = i.split("   ")
        new_list_left.append(int(i[0]))
        new_list_right.append(int(i[1]))

new_list_left.sort()
new_list_right.sort()

for i in new_list_left:
    for j in range(count_index, len(new_list_right)):
        if(i == new_list_right[j]):
            count += 1
            if(new_list_right[j] > new_list_right[j-1]):
                count_index = j
        if(new_list_right[j] > i):
            break

    similarity_score += (i * count)
    count = int()

print(similarity_score)