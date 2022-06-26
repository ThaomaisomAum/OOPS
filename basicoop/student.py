class Student:

    def __init__(self,id:str,name:str,major:str) -> None:
        self.id = id
        self.name = name
        self.major = major

    def printstudentDetail(self):
        print(f"Id{self.id}")
        print(f"Name{self.name}")
        print(f"Major{self.major}")

    def __del__(self):
        print("Object was destroyed")

if __name__ == "__main__":
    #peron1
    jessica = Student('111','Jessica','IT')
    jessica.printstudentDetail()

    #peron2
    john = Student('112','John','MKT')
    john.printstudentDetail()



#เขียนแบบที่2
    class Student :
        def __init__(self,id:str,name:str,major="it") -> None:
            self.id = id
            self.name = name
            self.major = major
    
        def didplay_detail(self):
            print(f"id: {self.id}")
            print(f"name: {self.name}")
            print(f"major: {self.major}")

    def __del__(self):
            print("object was destroyed")

    if __name__ == "__main__":

        #person1
        jessica = Student(111,"jessica","it")
        jessica.didplay_detail()

        #person2
        john = Student(112,"john","mkt")
        john.didplay_detail()

        #person3
        jame = Student(112,"jame",)
        jame.didplay_detail()