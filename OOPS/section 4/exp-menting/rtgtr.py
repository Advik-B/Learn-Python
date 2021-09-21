from zipfile import ZipFile
class P:
    def pack(self,folpat,folsave,name):

            self.save = folsave

            self.fname = (name+".zip") 
            
            self.pat = (self.save+'/'+self.fname)

            with ZipFile(self.pat,'w') as zip:
                for data in folpat:
                    zip.write(data)
            print ("All files have been packed successfully")

unzip = P()

a = "C:/Users/advik.ADVIK-PC/Downloads"

b = "C:\S"

c = "hope"

unzip.pack(a,b,c)
