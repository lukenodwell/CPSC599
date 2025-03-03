import sys

input_data = sys.stdin.read()

lines = input_data.splitlines()

num_of_bdays = lines[0].split()

lines.pop(0)

bdayNums = []

october28 = 302 # Added one for the date offset by 1

start_of_month = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
end_of_month = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]

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
largest_diff_index = 0
time_to_october28 = float('inf')
for i in range(1, len(bdayNums) + 1):
    if i == len(bdayNums):
        diff = (365 - bdayNums[i - 1]) + bdayNums[0]
        diff_index = bdayNums[0]
    else:
        diff = bdayNums[i] - bdayNums[i - 1]
        diff_index = bdayNums[i]

    if diff > largest_diff:
        largest_diff = diff
        largest_diff_index = diff_index
        if largest_diff_index < october28:
            time_to_october28 = (365 - october28) + diff_index
        else:
            time_to_october28 = largest_diff_index - october28

    elif diff == largest_diff:
        if diff_index < october28:
            temp_time_to_october28 = (365 - october28) + diff_index
        else:
            temp_time_to_october28 = diff_index - october28
        if temp_time_to_october28 < time_to_october28:
            largest_diff = diff
            largest_diff_index = diff_index
            time_to_october28 = temp_time_to_october28

# Convert the largest_diff_index to a date

fake_date = 0
fake_month = 0

for month_index in range(12):
    if start_of_month[month_index] <= largest_diff_index <= end_of_month[month_index]:
        fake_date = largest_diff_index - start_of_month[month_index] - 1 # Offset by 1
        fake_month = month_index + 1
        if fake_date == 0:
            fake_month -= 1
            if fake_month == 0:
                fake_month = 12
            fake_date = end_of_month[month_index - 1] - start_of_month[month_index - 1]
        break

formatted_date = f"{fake_month:02d}-{fake_date:02d}"
print(formatted_date)