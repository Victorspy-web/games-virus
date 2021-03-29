import random
from .inner import create_game_dirs, game_booster


# UN-COMMENT TO CREATE DIRS
create_game_dirs()


# THE COMPUTER CHOOSE A RANDOM NUMBER AND YOU HAVE T0 GUESS IT
try:
    def guess(x):
        game_booster()
        random_number = random.randint(1, x)
        guess = 0

        while guess != random_number:
            guess = int(input(f"Enter a guess b/n 1 and {x}: "))

            if guess < random_number:
                print("Sorry your guess is too low!")

            elif guess > random_number:
                print("Sorry your guess is too high")

        print(f"Yah! you guessed the number {random_number} correct.")

except ValueError:  # Inappropriate argument value (of correct type).
    print("\nYour answer cannot be equal to low and high")
    print("\nGame Over")
except TypeError:
    print("\nNo target number detected")
except Exception as e:
    print("Error located at", e)


# YOU CHOOSE A RANDOM NUMBER AND THE COMPUTER TRIES TO GUESS IT MEANWHILE ASKING COMFIRMATIONS FROM YOU
try:
    def computer_guess(x):
        game_booster()
        low = 0
        high = x
        feedback = ''

        while feedback != "c":
            if low != high:
                c_guess = random.randint(low, high)
            else:
                low = high  # It can vice versa because high can be equal to low in this case

            feedback = input(
                f"Is {c_guess} too high (h), too low (l) or correct (c): ")

            if feedback == "h":
                high = c_guess - 1

            elif feedback == 'l':
                low = c_guess + 1

        print(f"Yah! The computer guessed the number {c_guess} correct!")

except ValueError:
    print("\nYour answer cannot be equal to low and high")
    print("\nGame Over")
except TypeError:
    print("\nNo target number detected")
except Exception as e:
    print("Error located at", e)


# THE COMPUTER CHOOSES A RANDOM BETWEEN 2 VALUES GIVEN BY YOU AND TRIES TO RE-GUESS IT BY ITSELF
try:
    def computer_guess_and_comfirm(num_target):
        game_booster()
        low = 0
        high = 100
        count = 0

        while low or high != num_target:
            guess = random.randint(low, high)
            count += 1

            if guess < num_target:
                low = guess + 0
                print(
                    f"Computer is guessing the numbers between {low} and {high}!")
                print("Too low")
                print(str(count) + " Trials\n")

            elif guess > num_target:
                high = guess - 0
                print(
                    f"Computer is guessing the numbers between {low} and {high}!")
                print("Too high")
                print(str(count) + " Trials\n")

            else:
                break

        print(
            f"Yah the computer guess the number {num_target} in {count} trials")

except ValueError:
    print("\nYour target provided cannot be found!")
    print("\nGame Over")
except TypeError:
    print("\nNo target number detected")
except Exception as e:
    print("Error located at", e)


# UNCOMMENT ANY TO RUN, MADE SIMPLE.

# guess(100)
# computer_guess(100)
# computer_guess_and_comfirm(100)
