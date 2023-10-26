
secret_world = "Darshit"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess != secret_world and not(out_of_guess):
    if guess_count < guess_limit:
        guess = input("Enter Any Guessed Name :")
        guess_count += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("You Lose !!!")
else:
    print("You Win !!!")

