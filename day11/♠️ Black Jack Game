import random

print("Welcome to Black Jack Game ♠️")

def random_card():
    return random.randint(1, 11)

def check_computer(computer):
    score = sum(computer)

    if score > 21:
        print("I went BUST! 😵")
        return "bust"

    if 18 <= score <= 21:
        print("I am holding my cards 😎")
        return "hold"

    return "draw"


out_loop = True
while out_loop:
    user = random.choices(range(1, 11), k=2)
    computer = random.choices(range(1, 11), k=2)
    status = check_computer(computer)
    computer_holding=False
    if status == "bust":
        break
    elif status == "hold":
        computer_holding = True
    game_on = True

    while game_on:
        user_score = sum(user)

        print(f"\nYour cards: {user}, Total score: {user_score}")
        print(f"My visible card: {computer[1:]}")

        if user_score > 21:
            print("You went BUST! You lose 😢")
            break

        user_wish = input("Draw a card? Yes or No: ").lower()

        if user_wish == "yes":
           
            user.append(random_card())

            if not computer_holding:
                computer.append(random_card())
                status = check_computer(computer)

                if status == "bust":
                    break
                elif status == "hold":
                    computer_holding = True

        else:
            print("\nComputer is finishing its turn...")
            while not computer_holding:
                computer.append(random_card())
                status = check_computer(computer)

                if status == "bust":
                    break
                elif status == "hold":
                    computer_holding = True
            break

    user_score = sum(user)
    computer_score = sum(computer)

    print("\nFinal Cards:")
    print(f"Your cards: {user}, Score: {user_score}")
    print(f"My cards: {computer}, Score: {computer_score}")

    if user_score > 21 and computer_score > 21:
        print("We both Lost ❌")
    elif user_score > 21:
        print("You Lose ❌")
    elif computer_score > 21:
        print("You Win 🎉")
    elif user_score > computer_score or user_score == 21:
        print("You Win 🎉")
    elif user_score == computer_score:
        print("It's a Draw 🤝")
    else:
        print("I Win 😎")

    Continue_not = input("\nWould you like to play again? yes or no: ").lower()
    if Continue_not != 'yes':
        print("Thank you! Play again whenever you are free 😊")
        out_loop = False
