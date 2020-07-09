class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=5
        

    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        print(long_name)

    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def undate_odometer(self,milesage):
       self.odometer_reading+=milesage
