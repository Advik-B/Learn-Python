import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def cprint(text: str = '', *effects: str) -> None:
    """
    Print `text` using the ANSI sequences to change colour, etc

    :param text: The text to print.
    :param effects: The effect we want.  One of the constants
        defined at the start of this module.

    The arguments:
    `BLACK`
    `RED`
    `GREEN`
    `YELLOW`
    `BLUE`
    `MAGENTA` 
    `CYAN`
    `WHITE`
    `RESET`

    `BOLD`
    `UNDERLINE` 
    `REVERSE`
    
    """

    effect_string = "".join(effects)
    colorama.init()
    output_string = f"{effect_string}{text}{RESET}"
    print(output_string)
    colorama.deinit()

cprint("oop" , CYAN, BOLD, UNDERLINE)
input()