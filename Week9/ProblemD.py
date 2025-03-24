import sys
s = ""
ways = [1] * 101
ans = 0

input = sys.stdin.read
s = list(input().strip())

def isvalid():
    hasL = False
    isvowel = True
    cnt = 0
    for c in s:
        if c == 'L':
            hasL = True

        if c in 'AEIOU':
            if isvowel:
                cnt += 1
            else:
                isvowel = True
                cnt = 1
        else:
            if isvowel:
                isvowel = False
                cnt = 1
            else:
                cnt += 1

        if cnt >= 3:
            return False

    return hasL

def solve(i):
    global ans
    if i == len(s):
        if isvalid():
            count = 1
            for j in range(len(s)):
                count *= ways[j]
            ans += count
        return

    if s[i] != '_':
        solve(i + 1)
    else:
        # try L
        s[i] = 'L'
        solve(i + 1)

        # try consonant
        s[i] = 'B'
        ways[i] = 20
        solve(i + 1)

        # try vowel
        s[i] = 'A'
        ways[i] = 5
        solve(i + 1)

        s[i] = '_'
        ways[i] = 1

solve(0)
print(ans)