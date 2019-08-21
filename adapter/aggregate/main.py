import sys
from print import print_banner


def execute(arg):
    banner = print_banner()
    banner.print_weak(arg)
    banner.print_strong(arg)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print('Illegal Argument Error.')
    else:
        execute(args[1])
