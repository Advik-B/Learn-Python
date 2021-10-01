p = print
P = p


upload_file_list = []

try:
    import subprocess
except:
    P(
        'The requirements were not installed.\n'
     'Install the listed requirements and re-run the program.'
     )

    input('Press enter to exit')
    exit()


try:
    
    import random
except:

    subprocess.call('pip install random')
    try:
        import random
    except:
        P(
        'The requirements were not installed.\n'
        'Install the listed requirements and re-run the program.'
         )

try:
    import os
except:
    subprocess.call('pip install os')
    try:
        import os
    except:
        P(
        'The requirements were not installed.\n'
        'Install the listed requirements and re-run the program.'
         )

try:

    import smtplib
except:
    subprocess.call('pip install smtplib')
    try:
        import smtplib
    except:
        P(
            'The requirements were not installed.\n'
            'Install the listed requirements and re-run the program.'
         )


try:
    username = os.getlogin()
except:
    P(
    'Could not get the username.\n'
     )
    p()


folder_path = f'Admissions'

my_email = 'admission.helper.app@gmail.com'

#print(os.getcwd())
default_prompt = '---> '

s = smtplib.SMTP('smtp.gmail.com', 587)



randomcode  = (1234567890)
randomcode2 = (1234567890)
randomcode3 = (1234567890)
randomcode4 = (1234567890)
randomcode5 = (1234567890)
randomcode6 = (1234567890)
randomcode7 = (1234567890)
randomcode8 = (1234567890)
randomcode9 = (1234567890)

# Applying multiple styles
print ("How many admission entries do you want to make")
number_of_entries = int(input(default_prompt))
p()

if number_of_entries == 0:
    exit("You cannot have 0 entries. So the program will exit")

P("What is your email address ?")
p()
email = input(default_prompt)
p()

p ('Do you want the data offline or online ?')
mode = input(default_prompt)

if mode.casefold() == 'Off' or mode.casefold() == "Offline" or mode == 'off' or mode == 'offline':
    mode = None
    folder_path = 'Admissions'
    p ()
    print('Ok the program will work in offline mode')
    email = 'someoneexample44@gmail.com'
else:
    mode = True
    


class Student:
    def __init__(self):
        self.name = None
        self.age = None
        self.remarks = None
        self.sex = None
        self.grade = None
        self.section = None
        self.favorate_hobby = None



s1=Student()


message = (f"Subject: Student Summary\n\n"
  "Hello user\n"
  "\n"
  "Thank you for using Admission-app made by Advik.\n"
  "Here are the details of the students.\n"
  "\n"
  f"Name: {s1.name}\n"
  f"Age: {s1.age}\n"
  f"Sex: {s1.sex}\n"
  f"Section: {s1.section}\n"
  f"Hobby: {s1.favorate_hobby}\n"
  f"Remarks(made by parents): {s1.remarks}\n")



for o in range (0,number_of_entries):
    
    p (o)
    while True:
        p ()
        p ("Name of the student:")
        s1.name = (input(default_prompt))
        p ()
        P ("Age of the student:")
        s1.age = int(input(default_prompt))
        p ()
        p("grade or 'class' of the student (in numbers):")
        s1.grade = int(input(default_prompt))
        p ()
    
        while True:
            p ("Sex of the student [Male/Female/Non-binary] :")
            p()
            tempdata = input(default_prompt)
            if tempdata != None:
                    if tempdata.capitalize() == "Male" or tempdata.capitalize() == "M" or tempdata.capitalize() == "m":
                        s1.sex = "Boy"
                        del tempdata
                        break
                    elif tempdata.capitalize() == "Boy" or tempdata.capitalize() == "B" or tempdata.capitalize() == "b":
                        s1.sex = "Boy"
                        del tempdata
                        break
                    elif tempdata.capitalize() == "Female" or tempdata.capitalize() == "F" or tempdata.capitalize() == "f":
                        s1.sex = "Girl"
                        del tempdata
                        break
                    elif tempdata.capitalize() == "Girl" or tempdata.capitalize() == "G" or tempdata.capitalize() == "g":
                        s1.sex = "Girl"
                        del tempdata
                        break
                    elif tempdata.capitalize() == "Non-binary" or tempdata.capitalize() == "Nb" or tempdata.capitalize() == "Gay":
                        s1.sex = "Student"
                        del tempdata
                        break
                    else:
                        p ("Sorry.. invalid gender")
        
        while True:
            p (f"What section would you like your {s1.sex} to be in (A/B/C/D).")
            p ()
            section = input(default_prompt)

            if section.capitalize() == "A" or section.capitalize() == "a":
                s1.section = "A"
                del section
                break
            elif section.capitalize() == "B" or section.capitalize() == "b":
                s1.section = "B"
                del section
                break
            elif section.capitalize() == "C" or section.capitalize() == "c":
                s1.section = "C"
                del section
                break
            elif section.capitalize() == "D" or section.capitalize() == "d":
                s1.section = "D"
                del section
                break
            else:
                p ("Sorry we don`t have that section just yet")
        p ("Any favorate hobbies that your child loves. put 'n' if there is none")
        s1.favorate_hobby = input(default_prompt)
        p()
        P("Any futher remarks. put 'n' if there are no remarks")
        s1.remarks = input(default_prompt)
        
        p()
        P("That is all we need. thank you")
        P()
        P("Your child`s admission number will be generated shortly.")
        input()
        break
    p ()

    randomcode0 = int(random.randint(randomcode,randomcode2*randomcode3*randomcode4*randomcode4*randomcode5*randomcode6//randomcode9))
    admin_number = (randomcode0//(randomcode8*randomcode7)//(randomcode6*randomcode))




    if s1.sex == "Student":
        s1.sex = "non-binary"
    elif s1.sex == "Boy":
        s1.sex = "Male"
    elif s1.sex == "Girl":
        s1.sex = "Female"
    if s1.remarks == "no" or s1.remarks == "No" or s1.remarks == "" or s1.remarks == "None" or s1.remarks == "none" or s1.remarks == "n":
        s1.remarks = "None"
    if s1.favorate_hobby == "no" or s1.favorate_hobby == "n":
        s1.favorate_hobby = "None"
    p ()
    
    if mode == True:
        s.starttls()
        s.login(my_email, "Dec@2612")
        s.sendmail(my_email, email, message)
        s.quit()
        
    # Python code to illustrate Sending mail from
# your Gmail account
    p (f"your child`s admisison number is #{admin_number}")
    p ()
    print = ("Press Enter to quit")
    input()


temp = 'Admissions'

if os.path.isdir(temp) == False:
    os.mkdir(temp)

file_path = f'{temp}/{s1.name}#{admin_number}.txt'

class ReportGenerate:
      def __init__(self):

            f= open(file_path,"w+")
            
            f.write(" \n")

            f.write(f"Name: {s1.name}\n")
            
            f.write(" \n")
            
            f.write(f"Age: {s1.age}\n")
            
            f.write(" \n")
            
            f.write(f"sex:{s1.sex}\n")
            
            f.write(" \n")
            
            f.write(f"Grade: {s1.grade}\n")
            
            f.write(" \n")
            
            f.write(f"Favorate hobbies: {s1.favorate_hobby}\n")
            
            f.write(" \n")
            
            f.write(f"Section: {s1.section}\n")
            
            f.write(" \n")
            
            f.write(f"Remarks made by parents:{s1.remarks}\n")

            f.write(" \n")

            f.write(f"Admmission number:{admin_number}\n")

            f.close()

            upload_file_list[o] = file_path


RepGen = ReportGenerate
RepGen()


for upload_file in upload_file_list:
	gfile = drive.CreateFile({'parents': [{'id': '1pzschX3uMbxU0lB5WZ6IlEEeAUE8MZ-t'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.

p ("Press Enter to quit")
input()
#workbook.save(f"{path}/Admissions Data.xls")#TODO Remove this shit