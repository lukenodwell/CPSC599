import sys

def min_distance_to_destination(n, m, k, r, straightaways, curves):
    # Initialize DP table with infinity
    dp = [[float('inf')] * (m + 1) for _ in range(n)]
    
    # Base case: start at lane 1 on the first straightaway
    dp[0][1] = 0
    
    # Fill the DP table for each straightaway
    for i in range(n):
        for j in range(1, m + 1):
            if dp[i][j] != float('inf'):
                # Consider lane changes within the same straightaway
                for lane_change in range(-1, 2):
                    new_lane = j + lane_change
                    if 1 <= new_lane <= m:
                        dp[i][new_lane] = min(dp[i][new_lane], dp[i][j] + (k + r) * abs(lane_change))
        
        # Add the length of the current straightaway to the distance
        for j in range(1, m + 1):
            dp[i][j] += straightaways[i]
        
        # If not the last straightaway, update for the next curve
        if i < n - 1:
            s, c = curves[i]
            for j in range(1, m + 1):
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + s + c * j)
    
    # The result is the minimum distance to reach lane 1 at the end of the last straightaway
    return dp[n - 1][1]

n, m = map(int, sys.stdin.readline().split())
k, r = map(int, sys.stdin.readline().split())

straightaways = [int(sys.stdin.readline()) for _ in range(n)]
curves = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n - 1)]

print(min_distance_to_destination(n, m, k, r, straightaways, curves))