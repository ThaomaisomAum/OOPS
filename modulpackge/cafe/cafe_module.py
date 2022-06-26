class Desserts:
    def __init__(self) -> None:
        self.desserts = ['ข้าวเหนียวมะม่วง''ข้าวเหนียวทุเรียน','ไอศครีม']

    def show_desserts(self):
        return f'Desserts Mrnu: {self.desserts}'

class Drinks:
    def __init__(self) -> None:
        self.drinks = ['กาแฟ','น้ำอัดลม' ,'ชา','ไวน์']

    def add_drink(self,new_drink):
        self.drinks.append(new_drink)

    def show_drinks(self):
        return f'Drinks Menu: {self.drinks}'