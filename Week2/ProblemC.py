import sys

input_data = sys.stdin.read()

lines = input_data.splitlines()

num_of_cases = int(lines[0])
case_offset = 1

for case in range(1, num_of_cases + 1):
        num_canidates = int(lines[case_offset])
        total_votes = 0
        canidate_num = 0
        canidate_votes = 0
        canidate_votes_list = []

        for num in range(1 + case_offset, case_offset + num_canidates + 1):
                vote_count = int(lines[num])
                total_votes += vote_count
                canidate_votes_list.append(vote_count)
                if int(lines[num]) > canidate_votes:
                        canidate_votes = vote_count
                        canidate_num = num - case_offset

        canidate_votes_list.sort(reverse=True)

        if canidate_votes_list[0] == canidate_votes_list[1]:
                print("no winner")
        elif canidate_votes / total_votes > 0.5:
                print("majority winner", canidate_num)
        elif canidate_votes / total_votes <= 0.5: 
                print("minority winner", canidate_num)
        case_offset += num_canidates + 1