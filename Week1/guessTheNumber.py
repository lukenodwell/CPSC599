upper = 1000
lower = 1
current_guess = (upper + lower) // 2

print(current_guess)

response = input().strip()
if response == "correct":
    exit()

guesses = 9
while guesses != 0:
        if response == "lower":
                upper = current_guess - 1
        elif response == "higher":
                lower = current_guess + 1
        current_guess = (upper + lower) // 2
        print(current_guess)
        response = input().strip()
        if response == "correct":
                exit()
        guesses -= 1
