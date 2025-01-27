import sys

input_data = sys.stdin.read()

lines = input_data.splitlines()

info = lines[0].split()

questions = [int(q) for q in lines[1].split()]

time_remaining = 300
Num_AC = 0
current_time = 0
penalty_time = 0

if (time_remaining - questions[int(info[1])] >= 0):
        time_remaining -= questions[int(info[1])]
        current_time += questions[int(info[1])]
        penalty_time += current_time
        Num_AC += 1
        questions.pop(int(info[1]))

        questions.sort()

        for question in questions:
                if time_remaining - int(question) >= 0:
                        time_remaining -= question
                        current_time += question
                        penalty_time += current_time
                        Num_AC += 1

print(Num_AC, penalty_time)