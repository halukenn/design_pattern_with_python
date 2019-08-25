from display import CharDisplay
from display import StringDisplay
import sys


def execute(arg):
    charDisplay = CharDisplay(arg)
    charDisplay.display()
    stringDisplay = StringDisplay(arg)
    stringDisplay.display()


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print('Illegal Argument Error.')
    else:
        execute(args[1])
