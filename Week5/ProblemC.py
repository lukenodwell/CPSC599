import sys

input_data = sys.stdin.read()
lines = input_data.splitlines()

n = int(lines[0])

for i in range(1, n * 2, 2):
    m = int(lines[i])
    distances = list(map(int, lines[i + 1].split()))
    
    dp = {0: (0, "")}
    
    for distance in distances:
        new_dp = {}
        for height in dp:
            current_max_height, sequence = dp[height]
            
            up_height = height + distance
            down_height = height - distance
            
            new_max_height = max(current_max_height, up_height)
            new_sequence = sequence + "U"
            if up_height not in new_dp or new_dp[up_height][0] > new_max_height:
                new_dp[up_height] = (new_max_height, new_sequence)
            
            if down_height >= 0:
                new_max_height = max(current_max_height, down_height)
                new_sequence = sequence + "D"
                if down_height not in new_dp or new_dp[down_height][0] > new_max_height:
                    new_dp[down_height] = (new_max_height, new_sequence)
        
        dp = new_dp
    
    if 0 in dp:
        min_max_height, sequence = dp[0]
        print(sequence)
    else:
        print('IMPOSSIBLE')