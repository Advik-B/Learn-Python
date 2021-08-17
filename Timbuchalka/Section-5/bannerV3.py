def banner_text(text=' ',screen_width=80):
    """
    This will create a banner with text with the string and width provided.
    example: 
        banner_text('*',10)
        banner_text('Hello',10)
        banner_text('*',10)

    `int`
    
    if no width is provided... it will default to 80
    example:
        banner_text('Hello world')
    

    if neither string , nor width have been provided... it will print a blank line 
    """
    if len(text) > screen_width - 4:
        raise ValueError(f'String {text} is larger than specified width {screen_width}')
    if text == '*':
        print('*'*screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = f"**{centred_text}**"
        print(output_string)
# banner_text("*")
# banner_text("Hello from Python")
# banner_text()
# banner_text("This is Advik from india")
# banner_text("*")