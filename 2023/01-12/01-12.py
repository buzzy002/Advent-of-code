"""
Partie 1 :
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration 
value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit 
and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

-------------------------------------------------------------------------------------------------------------------------------

Partie 2 :
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
"""

def TxtFileReader(path):
    list_input = list()
    with open(path) as file :
        for line in file:
            list_input.append(line)
    return list_input

def Resolver(list_input:list):
    list_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list_calibratrion_values = list()
    sum = int()
    for item in list_input:
        temp_value = "aa"
        first_digit = False
        last_digit = False
        for i in range(0, len(item)):
            if(item[i] in list_digit and not first_digit):
                temp_value = item[i] + temp_value[1]
                first_digit = True
            if(item[-i-1] in list_digit and not last_digit):
                last_digit = True
                temp_value = temp_value[0] + item[-i-1]
            len_item = len(item)
            if(first_digit and last_digit):
                list_calibratrion_values.append(temp_value)
                break
            
    for i in list_calibratrion_values:
        sum += int(i)
    return sum

def ResolverP2():
    list_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list_calibratrion_values = list()
    sum = int()
    with open("/home/buzzy/Documents/Advent-of-code/2023/01-12/input.txt") as file:
        data = file.read().strip()
    data = (
        data.replace("one", "1")
        .replace("two", "2")
        .replace("three", "3")
        .replace("four", "4")
        .replace("five", "5")
        .replace("six", "6")
        .replace("seven", "7")
        .replace("eight", "8")
        .replace("nine", "9")
    )
    data_list = data.split("\n")
    for item in data_list:
        temp_value = "aa"
        first_digit = False
        last_digit = False
        for i in range(0, len(item)):
            if(item[i] in list_digit and not first_digit):
                temp_value = item[i] + temp_value[1]
                first_digit = True
            if(item[-i-1] in list_digit and not last_digit):
                last_digit = True
                temp_value = temp_value[0] + item[-i-1]
            if(first_digit and last_digit):
                list_calibratrion_values.append(temp_value)
                break
        
    for i in list_calibratrion_values:
        sum += int(i)
    return sum

list_input = TxtFileReader("/home/buzzy/Documents/Advent-of-code/2023/01-12/input.txt")
print(Resolver(list_input))
print(ResolverP2())



