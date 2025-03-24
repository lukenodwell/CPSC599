def digits(n):
        n = str(n)
        combos = {"1" : "1234567890",
                "2" : "2356890",
                "3" : "369",
                "4" : "4567890",
                "5" : "56890",
                "6" : "69",
                "7" : "7890",
                "8" : "890",
                "9" : "9",
                "0" : "0"}
        a = True
        i = 0
        while i < len(n) - 1:
                a = a and n[i+1] in combos[n[i]]
                i += 1
        return a

n = int(input())
for i in range(0, n):
        t = int(input())
        i = 0
        while not digits(t + i) and not digits(t - i):
                i += 1
        if digits(t + i):
                print(t + i)
        else:
                print(t - i)