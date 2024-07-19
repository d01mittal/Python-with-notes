class train:
    def __init__(self, name, seats, fare):
        self.name=name
        self.seats=seats
        self.fare=fare
    def getstatus(self):
        print(f"The name of the train is: {self.name}")
        print(f"The number of the seats available in this train are: {self.seats}")
    def fareinfo(self):
        print(f"The fare of the ticket is: Rs. {self.fare}")
    def booking(self):
        if(self.seats>0):
            print(f"your ticket has been booked! Your seat number is {self.seats}")
            self.seats-=1
        else:
            print(f"Sorry this train is full. Kindly try in tatkal")
intercity=train("Intercity Express", 2, 525)
intercity.fareinfo()
intercity.booking()
intercity.getstatus()
intercity.booking()
intercity.getstatus()
intercity.booking()