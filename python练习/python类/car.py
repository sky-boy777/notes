from car_fu import Car

#电瓶类
class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def describe_battery(self):
        print('电池容量：'+str(self.battery_size))

    def get_range(self):
        if self.battery_size==70:
            range=240
        elif self.abttery_size==90:
            range=300

        message="汽车还能行驶"+str(range)+"公里。"
        print(message)

#Car子类
class ddcar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)

        #调用电瓶类
        self.battery=Battery()

    




