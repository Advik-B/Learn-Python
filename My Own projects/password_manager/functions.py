def pinput(prompt_text:str = '',prompt:str = '>>> ') -> any:
    """
    This function is basically\n
    `print(prompt_text)`\n
    `some_value = input(prompt)`\n
    """
    print(prompt_text)
    output = input(prompt)
    print()
    return output