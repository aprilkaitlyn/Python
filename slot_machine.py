import random 

MAX_LINES = 3 #constants should be written in all caps
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = { #dictionaries just like godot indeed
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = { #rarer symbol = bigger payout
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

#no ready function

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line] #column 1
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else: #if break is not hit in the for loop
            winnings += values[symbol] * bet
            winning_lines.append(line + 1) #convert from index num to num that makes sense
    return winnings, winning_lines


def get_spin(rows,cols,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #returns key and value for each dict
        for _ in range(symbol_count): #_ is an anonymous variable used in python, avoids unused variable
            all_symbols.append(symbol) #append just like godot

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:] #[:] is used to make a copy of the list, : is the slice operator 
        for row in range(rows):
            value = random.choice(current_symbols) #need to import random to use this
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slots(columns):
    #transposing to turn columns into rows
    for row in range(len(columns[0])): #len = length, then what column we are starting from
        for i, column in enumerate(columns): #enumerate returns the index number too
            if i != len(columns) - 1:
                print(column[row], end=" | ") #end defaults to \n, but we can choose a different string
            else:
                print(column[row], end="")

        print() #adds the defauly \n break, will print one row per for loop

def deposit(): #functions are written with the def keyword
    while True:
        amount = input("How much do you want to gamble? $") #allows user input
        if amount.isdigit(): #check user response is a number
            amount = int(amount)
            if amount > 0:
                break #break will transport us to the return line
            else:
                print("Amount must be greater than $0")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): 
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}") #add f before string to use variables & convert them to strings
        else:
            print("Please enter a number")
    return amount   

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

    slots = get_spin(ROWS, COLS, symbol_count)
    print_slots(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines", *winning_lines) #* will pass every winning line from the list to this print statement
    return winnings - total_bet


def main(): 
    balance = deposit() #variables dont need to be defined before using them
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin or q to quit ")
        if answer == "q":
            break
        balance += spin(balance) #update balance based on result of spin

    print(f"You left with ${balance}")

main() #python runs top to bottom and functions can be called by themselves like this
