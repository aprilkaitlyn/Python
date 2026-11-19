import random

COLORS = ["R", "O", "Y", "G", "B", "V"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []

    for _ in range(CODE_LENGTH): #can use _ as a placeholder
        color = random.choice(COLORS)
        code.append(color)

    return code 

def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ") #split makes a list based on a delimiter like "G G" -> ["G","G"]

        if len(guess) != CODE_LENGTH: #get length
            print(f"You must guess {CODE_LENGTH} colors")
            continue #start the loop over

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}, try again")
                break
        else:
            break

    return guess

def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts: #add color if not in dict
            color_counts[color] = 0
        color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code): #zip combines the 2 args into a 'tuple' like ["X","Y"] and ["A","B"] -> [("X", "A"),("Y","B")]
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos

def game():
    print(f"Welcome, you have {TRIES} tries to guess the code...")
    print("Valid colors are:", *COLORS)
    code = generate_code()
    for attempts in range(1, TRIES+1): #range doesnt include the second var so +1 is needed
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break

        print(f"Correct positions: {correct_pos} | Incorrect positions: {incorrect_pos}")

    else:
        print("You lose, the code was", *code)

if __name__ == "__main__":
    game() #run game just one time
