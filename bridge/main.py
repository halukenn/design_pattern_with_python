from bridge import Display
from bridge import CountDisplay
from bridge import DisplayImpl
from bridge import SringDisplayImpl

if __name__ == "__main__":
    display1 = Display(SringDisplayImpl('Hello,World'))
    display2 = CountDisplay(SringDisplayImpl('Hello,World'))
    display1.display()
    display2.multi_display(5)
