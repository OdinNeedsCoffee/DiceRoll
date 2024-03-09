import random
import time


class DiceRoll:
    def __init__(self):
        self.max_val = None
        self.min_val = None
        self.start = 0
        self.stop = 0
        self.valid_responses = ""
        self.dice_quant = 0
        self.dice1 = None
        self.dice2 = None
        self.roll_again = "y"
        self.waiting = []

        self.greeting = input("Would you like to try your luck? (y/n)").strip().lower()
        if self.greeting.lower() != "y":
            print("See you next time")
        else:
            self.set_dice_quant()

    def set_dice_quant(self):
        try:
            self.valid_responses = ["1", "one", "2", "two"]
            self.dice_quant = input("Would you like to roll one or two dice?").strip().lower()
            if self.dice_quant.lower() not in self.valid_responses:
                raise ValueError("1/ one or 2/ two only")
            else:
                self.roll_it()
        except ValueError as e:
            print(e)

    def roll_it(self):
        self.min_val = 1
        self.max_val = 6
        while self.roll_again.lower() == "y":
            if self.dice_quant == "2" or self.dice_quant == "two":
                print("Rolling the dice:")
                for i in range(1, 5):
                    self.waiting += ["."]
                    print(" ".join(map(str, self.waiting)))
                    time.sleep(0.5)
                self.waiting.clear()
                self.dice1 = random.randint(self.min_val, self.max_val)
                self.dice2 = random.randint(self.min_val, self.max_val)
                print(f'The values are {self.dice1} & {self.dice2}')
                self.roll_again = input("Roll again? (y/n)")
            else:
                print("Rolling the die:")
                for i in range(1, 5):
                    self.waiting += ["."]
                    print(" ".join(map(str, self.waiting)))
                    time.sleep(0.5)
                self.waiting.clear()
                dice_1 = random.randint(self.min_val, self.max_val)
                print('The value is: {}'.format(dice_1))

                self.roll_again = input("Roll again? (y/n)")
        print("Thank you for gambling.")


DiceRoll()
