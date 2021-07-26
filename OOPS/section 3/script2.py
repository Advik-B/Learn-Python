class Example:
    def __init__(self):
        self.x = 10
        self.__y = 50
        self.__z = 100
    def public_methord(self):
        print (self.x)
        print (self.__y)
        print (self.__z)
    def __private_methord(self):
        print ("Inside private methord") 
    def Decript(self):
        self.__private_methord()   

e = Example() 