def banner_text(text):
    screen_width  = 80
    if len(text) > screen_width - 4:
        print('EEK!')
        print('THIS TEXT IS TOO LONG TO FIT IN THE SPICIFIED WIDTH')
    if text == '*':
        print('*'*screen_width)
    else:
        centred_text = text.center(screen_width - 4)
        output_string = f"**{centred_text}**"
        print(output_string)



banner_text("*")
banner_text("Hello from Python")
banner_text("This is Advik from india")
banner_text("*")