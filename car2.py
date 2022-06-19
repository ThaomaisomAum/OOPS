class Car:
    brand = "toyota"
    def __init__(self,model:str,colour:str,year:int,price:int) -> None:
        self.model = model
        self.colour = colour
        self.year = year
        self.price = price
        #instance methond
    def printcardetail(self):
        print(f"brand: {self.brand}")
        print(f"model: {self.model}")
        print(f"colour: {self.colour}")
        print(f"year: {self.year}")
        print(f"price: {self.price:,.2f}")

    #static methond ไม่มีคำว่า self
    @staticmethod
    def get_static_methond():
        text = "static"
        print(f"In {text} methond")
        #ตัวแปร text ไม่สามารถถูกเรียกใช้ใน printCarDetail()ได้
        #ตัวแปร text ใช้ได้แต่เฉพาะ get_static_methond ()เท่านั้น

    #class methond ต้อวมีคำว่า cls
    @classmethod
    def get_class_methond(cls):
        my_text = "Class"
        print(f"this is {my_car}")


    def __del__(self):
        print("object was destroyed")
if __name__ == "__main__":
    my_car = Car("cross","white",2022,1500000)
    my_car.printcardetail()

    #เรียกใช้ static methond
    Car.get_static_methond() #  เรียกผ่าน class
    my_car.get_static_methond() #เรียกผ่าน instance methond

    #เรียกใช้ class methond