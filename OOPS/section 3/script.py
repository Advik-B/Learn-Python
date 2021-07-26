class Speed:
    def __init__(self):
        self.speed = 10
        self.__new_speed = 80
    
    def get_new_speed(self):
        return self.__new_speed

    def set_new_speed(self,newspeed):
        self.__new_speed = newspeed
    
s = Speed()

print(s.speed)

print(s.get_new_speed())