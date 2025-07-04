import stdio
import random

while True:
    stdio.writeln("Guess a number between 1 and 1000: ")
    number = stdio.readInt()

    correct = random.randint(1,1000)

    if number == correct:
        stdio.writeln("Correct! Thank you for playing!")
        break

    elif number > correct:
        stdio.writeln("Too High.")

    elif number < correct:
        stdio.writeln("Too Low.")