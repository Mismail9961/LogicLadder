import random

# Mapping choices to full names and emojis
choices = {
    'r': ('Rock', '🪨'),
    'p': ('Paper', '📄'),
    's': ('Scissors', '✂️')
}

# Rules: what beats what
winning_rules = {
    'r': 's',  # Rock beats Scissors
    'p': 'r',  # Paper beats Rock
    's': 'p'   # Scissors beats Paper
}

def get_computer_choice():
    return random.choice(['r', 'p', 's'])

def get_player_choice():
    while True:
        choice = input("Choose (r)ock, (p)aper, or (s)cissors: ").lower()
        if choice in ['r', 'p', 's']:
            return choice
        else:
            print("Invalid input. Please type 'r', 'p', or 's'.")

def decide_winner(player, computer):
    if player == computer:
        return "tie"
    elif winning_rules[player] == computer:
        return "player"
    else:
        return "computer"

def play_game():
    print("\n🪨📄✂️ Welcome to Rock, Paper, Scissors! 🪨📄✂️\n")

    player_score = 0
    computer_score = 0
    ties = 0

    while player_score < 2 and computer_score < 2:
        print(f"\n🎮 Round {player_score + computer_score + ties + 1}")
        player = get_player_choice()
        computer = get_computer_choice()

        print(f"You chose {choices[player][0]} {choices[player][1]}")
        print(f"Computer chose {choices[computer][0]} {choices[computer][1]}")

        result = decide_winner(player, computer)

        if result == "player":
            print("✅ You win this round!")
            player_score += 1
        elif result == "computer":
            print("❌ Computer wins this round!")
            computer_score += 1
        else:
            print("😐 It's a tie!")
            ties += 1

        print(f"Score: You {player_score} - Computer {computer_score} (Ties: {ties})")

    # Final result
    print("\n🏁 Final Result:")
    if player_score > computer_score:
        print("🎉 You are the overall winner!")
    else:
        print("💻 Computer wins the game!")

    # Final stats
    print(f"\n📊 Game Summary:")
    print(f"✅ Wins: {player_score}")
    print(f"❌ Losses: {computer_score}")
    print(f"😐 Ties: {ties}")

# Start the game
play_game()
