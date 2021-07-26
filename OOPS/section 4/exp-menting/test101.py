from zipfile import ZipFile
import os
import time

class Zippp:
    def unpack(self,filepath,saveas):
        with ZipFile(filepath,'r') as zip:
            
            while True:
                
                print("files will be unzipped. Do you want to continue [Y/N]")
                self.usr_confirm = input("--->")
                if self.usr_confirm == "Y" or self.usr_confirm =="y":
                    zip.printdir()
                    zip.extractall(saveas)
                    print()
                    print("Extraction complete!")
                    break
                elif self.usr_confirm == "N" or self.usr_confirm == "n":
                    break
                else:
                    print ("Sorry wrong input please put a 'Y' or a 'N'")
    def pack(self,folpat,folsave,name):

        self.save = folsave.replace("\\","/")

        self.fname = (name+".zip") 
        
        self.pat = (self.save+'/'+self.fname)

        with ZipFile(self.pat,'w') as zip:
            for data in folpat:
                zip.write(data)
        print ("All files have been packed successfully")
            

Zip_file = Zippp()


print ("Do you want to zip files or unpack them?")
user = input("--->")

while True:

    if user == "unpack" or user == "Unpack":

        print ("In what path is your file in ?")
        filepat = input("--->")
        print()
        print("In which path do you want to save the extract in ?")
        savas = input("--->")
        Zip_file.unpack(filepat,savas)
    elif user == "zip" or user == "Zip":

        print ("In what path is your folder in?")
        folpathh = input("--->")
        print ("In which folder do you want to zip to?")
        folsavee = input("--->")
        print("What is the should the name of your zipfile be")
        folname = input("--->")
        
        Zip_file.pack(folpathh,folsavee,folname)