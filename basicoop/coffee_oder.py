##ตัวอย่างข้อสอบ
from re import S


class Coffee_order:
    menu_type = "Coffee"
    total = 0    

    def __init__(self, menu:str, total:float, customer_name:str, num:int = 1, size:str = 'R', price:float = 0):
        self.menu = menu
        self.total = total
        self.customer_name = customer_name
        self.num = num
        self.size = size
        self.price = price

    def check_menu(self): 
        self = self.menu()
        if self == 'Cafe Mocha':
            return self.menu("CM")
        elif self == 'Cappuccino':
            return self.menu("CP")
        elif self == 'Americano':
            return self.menu("AM")
        elif self == 'Vanila Latetl':
            return self.menu("VL")
        elif self == 'Espresso':
            return self.menu("ES")
        else:
            return

    def compute_price(self):
        self = self.size()
        if self == 'L':
            return self.price + 1
        elif self == 'XL':
            return self.price + 1.5
        else:
            return

    def display_detail(self):
        print(f"ราคา  : {self.customer_name}")
        print(f"เมนู  : {self.menu}")
        print(f"ขนาด  : {self.size}")
        print(f"ราคา  : {self.price:.2f}")


if __name__ == "__main__":
    order =Coffee_order("Espresso", "john",  1, "XL")
    order.display_detail()


#เฉลย
class CoffeeOrder:
    menu_type = "Coffee"
    total = 0

    def __init__(self,customer_name:str,menu:str,num = 1,size = 'R') -> None:
        self.customer_name = customer_name
        self.menu = menu.upper()
        self.num = num
        self.size = size.upper()
        self.price = 0

    def check_menu(self):
        menu_dictionary = {
            'CM':5.99,
            'CP':4.99,
            'AM':4.99,
            'CL':4.99,
            'VL':4.75,
            'ES':3.00
        }

        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def compute_price(self):
        if self.size == 'L':
            self.price += 1
        elif self.size == 'XL':
            self.price += 1.5
        else:
            self.price
        
        CoffeeOrder.total = self.price * self.num
        
    def display_detail(self):
        self.check_menu()
        self.compute_price()
        return f'{self.customer_name}, {self.menu} ({self.num}{self.size} * ${self.price} => ${CoffeeOrder.total}'

    def __del__(self):
        print("Object was destroyed")

if __name__ == "__main__":
    order1 = CoffeeOrder("John","es")
    order2 = CoffeeOrder("Mary","am",2,"L")
    
    print(order1.display_detail())
    print(order2.display_detail())
