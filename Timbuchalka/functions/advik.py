def read(path):
    file  = open(path)
    content  = file.read()
    file.close()
    return (content)

def write(path,content,number_of_lines=None):
    file  = open(path,'w')
    if number_of_lines == None:
        number_of_lines = 1
    for i in range(0,number_of_lines):
        file.write(content+'\n')    