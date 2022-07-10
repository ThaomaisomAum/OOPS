class JuiceOrder:
    menu_type = "Juice"
    total = 0    

    def __init__(self, menu:str, size:str = 'R', price:int = 0,num=1):
        self.menu = menu
        self.size = size
        self.price = price
        self.num = num

    def check_menu(self):
        menu_dictionary = {
            'OJ':25.00,
            'AJ':25.00,
            'WJ':30.00,
            'PJ':30.00,
        }
        if self.menu in menu_dictionary:
            self.price = menu_dictionary.get(self.menu)

    def compute_price(self):
        if self.size == 'R':
            self.price += 0.00
        elif self.size == 'L':
            self.price += 5.00
        else:
            self.price
        
        JuiceOrder.total = self.price* self.num
        
    def display_detail(self):
        self.check_menu()
        self.compute_price()
        return f'{self.menu} {self.size} * {self.price}baht => {JuiceOrder.total}baht'

    def __del__(self):
        print("Object was destroyed")

if __name__ == "__main__":
    order1 = JuiceOrder("WJ","L")
    order2 = JuiceOrder("OJ","R")
    order3 = JuiceOrder("PJ","L")
    
    print(order1.display_detail())
    print(order2.display_detail())
    print(order3.display_detail())