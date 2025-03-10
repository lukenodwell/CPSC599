def get_preference_index(preferences, current_state):
    # Convert current state to index
    state_index = 0
    if current_state[0] == 'Y':
        state_index += 4
    if current_state[1] == 'Y':
        state_index += 2
    if current_state[2] == 'Y':
        state_index += 1
    return preferences[state_index]

def flip_stone(state, stone_index):
    # Flip the stone at the given index
    new_state = list(state)
    new_state[stone_index] = 'Y' if state[stone_index] == 'N' else 'N'
    return ''.join(new_state)

def solve_voting_round(m, preferences):
    current_state = 'NNN'
    for i in range(m):
        best_flip = None
        best_preference = float('inf')
        for j in range(3):
            new_state = flip_stone(current_state, j)
            preference = get_preference_index(preferences[i], new_state)
            if preference < best_preference:
                best_preference = preference
                best_flip = j
        current_state = flip_stone(current_state, best_flip)
    return current_state

import sys
input = sys.stdin.read
data = input().split()
   
index = 0
n = int(data[index])
index += 1
results = []
    
for _ in range(n):
      m = int(data[index])
      index += 1
      preferences = []
      for _ in range(m):
          preferences.append(list(map(int, data[index:index+8])))
          index += 8
      result = solve_voting_round(m, preferences)
      results.append(result)
    
for result in results:
        print(result)