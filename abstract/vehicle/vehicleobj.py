from vehiclesubclass import *

c = Car("Mazda",250)
c.year = 2000
c.gear = 7
c.seat = 4
c.show_detail()
c.maintanance = 2022
c.shoe_maintanance()

t = Truck("Isuzu",120)
t.capacity = 1000
t.wheels = 4
t.show_detail()
t.show_price()

m = Motocycle("Honda",100)
m.cc = 160
m.model = 