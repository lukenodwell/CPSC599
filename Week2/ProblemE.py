import sys

input_data = sys.stdin.read()

lines = input_data.splitlines()

num_of_bdays = lines[0].split()

lines.pop(0)

bdayNums = []

jan = 31
feb = 28
mar = 31
apr = 30
may = 31
jun = 30
jul = 31
aug = 31
sep = 30
oct = 31
nov = 30
dec = 31
start_of_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]

# Convert all birthdays to a number
for line in lines:
        bdayInfo = line.split()
        bday = bdayInfo[1].split('-')
        bdayNum = int(bday[1])
        bdayNum += start_of_month[int(bday[0]) - 1]
        bdayNums.append(bdayNum)

bdayNums.sort()

# Find the largest difference between two birthdays
largest_diff = 0
for i in range(1, len(bdayNums) + 1):
        if i == len(bdayNums):
                # print(bdayNums[i - 1])
                # print(bdayNums[0])
                diff = (365 - bdayNums[i - 1]) + bdayNums[0]
                # print(diff)
        else:
                diff = bdayNums[i] - bdayNums[i - 1]
        # print(diff)
        if diff > largest_diff:
                largest_diff = diff
# print(largest_diff)
print(bdayNums)