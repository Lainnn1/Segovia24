import random

class SlotMachine:
    def __init__(self):
        self.balance = 10
        self.symbols = ['Cherry', 'Apple', 'Banana', 'Orange', 'Lemon','Pear', 'Grapes']
        self.wildcards = {'Good': 0.4, 'Bad': 0.6}

    def spin(self):
        self.balance -= 1
        result = [random.choice(self.symbols) for _ in range(5)]
        print("Your spin result:", result)
        if result.count(result[0]) == 5:
            print("Jackpot! You won 10 coins!")
            self.balance += 20
        elif result.count(result[0]) == 2:
            print("Two of a kind! You won 2 coins!")
            self.balance += 2
        elif result.count(result[0]) == 3:
            print("three of a kind! You won 5 coins!")
            self.balance += 5
        else:
            print("Sorry, you didn't win anything this time.")

        wildcard_chance = random.random()
        if wildcard_chance < self.wildcards['Good']:
            print("You got a Good Wildcard! Your chances of winning next time are increased!")
        elif wildcard_chance < self.wildcards['Bad']:
            print("Uh-oh! You got a Bad Wildcard! Your chances of winning next time are decreased.")

    def play(self):
        while self.balance > 0:
            print("\nBalance:", self.balance, "coins")
            play_again = input("Would you like to spin? (yes/no): ").lower()
            if play_again == 'yes':
                self.spin()
            elif play_again == 'no':
                print("Thanks for playing! Your final balance is:", self.balance, "coins")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if self.balance <= 0:
            print("You've run out of coins. Game over.")

# Main program
if __name__ == "__main__":
    slot_machine = SlotMachine()
    slot_machine.play()
