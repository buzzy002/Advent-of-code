"""
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration 
value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit 
and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
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

def ResolverP2(list_input:list):
    list_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    dict_trad_digit = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
    list_calibratrion_values = list()
    sum = int()
    for item in list_input:
        temp_value = "aa"
        first_digit = False
        last_digit = False
        values = dict_trad_digit.keys()
        for i in range(0, len(item)):
            if((item[i] in list_digit or item[i] in dict_trad_digit.values()) and not first_digit):
                if(item[i] in dict_trad_digit.keys()):
                    digit = dict_trad_digit[item[i]]
                else:
                    digit = item[i]
                temp_value = digit + temp_value[1]
                first_digit = True
            if(item[-i-1] in list_digit and not last_digit):
                if(item[i] in dict_trad_digit.keys()):
                    digit = dict_trad_digit[item[i]]
                else:
                    digit = item[i]
                last_digit = True
                temp_value = temp_value[0] + digit
            len_item = len(item)
            if(first_digit and last_digit):
                list_calibratrion_values.append(temp_value)
                break
            
    for i in list_calibratrion_values:
        sum += int(i)
    return sum


list_input = TxtFileReader("/home/buzzy/Documents/Advent-of-code/2023/01-12/input.txt")
print(ResolverP2(list_input))