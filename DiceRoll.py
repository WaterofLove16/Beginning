import stdio
import random

while True:
    stdio.write("Roll the dice? (y/n): ")
    Letter = stdio.readString().lower()
    if Letter == 'y':

        die1 = random.randint(1,6)
        die2 = random.randyint(1,6)

        stdio.writeln(f'({die1}, {die2})')

    elif Letter == 'n':
        stdio.writeln("Thanks for playing!")
        break

    else:
        stdio.writeln('Invalid choice!')
