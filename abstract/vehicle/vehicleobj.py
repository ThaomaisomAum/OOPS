#2
#ตัวอย่างสอบ final (85)
##vehicleobj.py
from vehiclesubclass import *

#create car object
#สร้างตัวแปร Car,"Mazda" มากจาก brand Class Vehicle, 250 มากจาก speed Class Vehicle
c = Car("Mazda",250)
c.year = 2000 #เพิ่มมาใน subclass ของ Car 
c.gear = 7 #มาจาก Class Vehicle สืบทอดแค่ลำดับที่ 2 
c.seat = 4 #มาจาก Class Vehicle สืบทอดแค่ลำดับที่ 2 
c.show_detail() 
c.maintanance = 2022 #เพิ่ม default ของ maintanance(ปีการซ่อมบำรุง)
c.show_maintanance()

#create Truck object ต้องสังเกตลูกศรในโจทย์ 
t = Truck("Isuzu",120)
t.capacity = 1000
t.wheels = 4
t.show_detail()
t.show_price()

#create motocycle object 
m = Motocycle("Honda",100)
m.cc = 160
m.model = "NEW PCX"
m.show_detail()