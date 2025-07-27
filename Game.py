import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == 'rock' and computer == 'scissors') or
        (user == 'scissors' and computer == 'paper') or
        (user == 'paper' and computer == 'rock')
    ):
        return "user"
    else:
        return "computer"

def show_result(user, computer, winner):
    print(f"\n🧍 You chose: {user}")
    print(f"💻 Computer chose: {computer}")
    if winner == "tie":
        print("🤝 It's a Tie!")
    elif winner == "user":
        print("✅ You Win!")
    else:
        print("❌ You Lose!")

def main():
    print("🎮 Welcome to Rock-Paper-Scissors!")
    user_score = 0
    computer_score = 0

    while True:
        print("\nChoose: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("⚠️ Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        show_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"📊 Score: You {user_score} - {computer_score} Computer")

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            print("\nThanks for playing! 👋")
            break

if __name__ == "__main__":
    main()
