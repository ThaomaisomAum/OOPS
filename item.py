
class Item :
    def __init__(self,name:str,price:float,quantily=1):
        #ตรวจสอบ price, quantily ว่าต้อง >0
        assert price > 0,f"price {price} must greater than 0"
        assert quantily > 0,f"quantily {quantily} must greater than 0"

        self.name = name
        self.price = price 
        self.quantily = quantily


    #instance method ต้องมีคำว่า self เสมอ
    #จะเรียกใช้ method นี้ต้องมีการสร้่าง object

    def total_price(self):
        return self.price * self.quantily
        #self.total = self.price * self.quantily
        #return self.tatal

    def __del__(self):
        print("object was destroyed")

if __name__ == "__main__":
    item1 = Item("monitor",5600,1)
    item2 = Item("mouse",5600,2)
    print("=== total price ==")
    print(f"{item1.name} : {item1.total_price():,.2f}")
    print(f"{item2.name} : {item2.total_price():,.2f}")