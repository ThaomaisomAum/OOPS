class Person:
    def __init__(self,name:str,gender:str,profession:int,study:int) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = study

    def work(self): #metode นับแค่บรรทัดนี้บรรทัดเดียว
        print(f'{self.name} working as a {self.profession}') 

    def show(self): #metode นับแค่บรรทัดนี้บรรทัดเดียว 
        print(f'Name: {self.name} Gender: {self.gender} profession: {self.profession} Study: {self.study}')

    def __del__(self):
        print("Object was destroyed")

if __name__ == "__main__":
    #peron1
    jessa = Person('Jessa','Female','Software Engineer',0)
    jessa.work()
    jessa.show()

    #peron2
    jon = Person('Jon','Male','Docter',15)
    jon.work()
    jon.show()

    #peron3
    lisa = Person('Lisa','Female','Singer',10)
    lisa.work()
    lisa.show()