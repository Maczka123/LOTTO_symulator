import random


# Function is asking user to select 6 numbers, then sort them.
def selected_numbers():
    try:
        user_number_list = []
        for i in range(1, 7):
            user_number = int(input(f"Select {i} number in range 1 - 49: "))
            if user_number not in user_number_list and user_number > 0 and user_number < 50:
                user_number_list.append(user_number)
            else:
                print("Selected number isn't in range 1 - 49 or it's already selected.")
                user_number = int(input(f"Select {i} number in range 1 - 49: "))
        user_number_list.sort()
    except ValueError:
        print("It's no a number")
    return user_number_list


# Function is drawing 6 random numbers in range 1 - 49, then sort them.
def random_numbers():
    drawn_numbers = list(range(1, 50))
    random.shuffle(drawn_numbers)
    drawn_numbers = drawn_numbers[:6]
    drawn_numbers.sort()
    return drawn_numbers

# Function print numbers selected by user and drawn by computer,
# then check how many user numbers are compare to drawn numbers.
def lotto():
    user_numbers = selected_numbers()
    print(f"Your numbers: {user_numbers}")
    computer_numbers = random_numbers()
    print(f"Drawn numbers: {computer_numbers}")
    matches = 0
    for number in user_numbers:
        if number in computer_numbers:
            matches += 1
    if matches > 2:
        print(f"Nice, You hit correctly {matches} numbers. You won a lot of money")
    elif matches <= 2:
        print(f"You lose, try again later. you hit correctly {matches} numbers.")
    return


lotto()
