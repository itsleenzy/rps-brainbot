import random

# Variables
user_points = 0
leepy_points = 0
user_history = []
choices = ["rock", "paper", "scissors"]

# Predict and counter the user's move
def predict_and_counter():
    if len(user_history) < 3:
        return random.choice(choices)

    last_moves = user_history[-3:]
    most_common = max(set(last_moves), key=last_moves.count)

    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    elif most_common == "scissors":
        return "rock"

# Determine the winner
def determine_winner(user, leepy):
    if user == leepy:
        return "It's a Tie!"
    elif (user == "rock" and leepy == "scissors") or \
         (user == "paper" and leepy == "rock") or \
         (user == "scissors" and leepy == "paper"):
        return "User Wins!"
    else:
        return "LeePy Wins!"

# Game loop
def play_game():
    global user_points, leepy_points  # no need to declare user_history since we're just appending to it

    while True:
        print("\nChoose: rock, paper, or scissors (or type 'quit' to exit):")
        user_input = input("> ").lower()
        
        if user_input == "quit":
            print(f"\nFinal Score — User: {user_points} | LeePy: {leepy_points}")
            break

        if user_input not in choices:
            print("Invalid input! Try again.")
            continue

        user_history.append(user_input)
        leepy_choice = predict_and_counter()

        print(f"LeePy's Choice: {leepy_choice}")
        result = determine_winner(user_input, leepy_choice)
        print(result)

        if result == "User Wins!":
            user_points += 1
        elif result == "LeePy Wins!":
            leepy_points += 1

        print(f"Score — User: {user_points} | LeePy: {leepy_points}")

# Start the game
play_game()
