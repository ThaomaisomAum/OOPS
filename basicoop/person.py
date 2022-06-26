class Person:
    def __init__(self,name:str,gender:str,profession:str) -> None:
        self.name = name
        self.gender = gender
        self.profession = profession
        self.study = 0

    def work(self):
        print(f'{self.name} working as a {self.profession}')

    def study(self,hours):
        self.stude = hours

    def show(self):
        print(f'Name: {self.name} Gender: {self.gender} profession: {self.profession} Study: {self.study}')

#peron1
jessa = Person('Jessa','Female','Software Engineer')
jessa.work()
jessa.show()

#peron2
jon = Person('Jon','Male','Docter')
jon.study = 15
jon.work()
jon.show()

#peron3
lisa = Person('Lisa','Female','Singer')
lisa.study = 10
lisa.work()
lisa.show()