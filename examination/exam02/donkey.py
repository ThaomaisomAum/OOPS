class Donkey:
    def __init__(self, max_height:float, name:str, color:str) -> None:
        super().__init__(max_height, name, color)
        self.age = "2"
        self.weight = "100"
    
    def age(self,age):
        self.age = age
        print(f'age: {self.age}')

    def weight(self,weight):
        self.weight = weight
        print(f'weight: {self.weight}')
    
    def sound(self):
        self.sound = "Donkey makes eeyore sound"
        return(f'run: {self.sound}')
    
    def show_info(self):
        print(f'Age: {self.age}year-old')
        print(f'Weight: {self.weight}kg')