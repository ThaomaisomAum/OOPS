class Employee:
    def __init__(self,id,name,salary) -> None: #เป็นลบใน class diagram จะอยู่ใน class เดียวไม่สืบทอด
        self.id = id
        self.name = name
        self.salary = salary

    def emp_datail(self): #เป็นบวกในclass diagram 
        print(f'id: {self.id}')
        print(f'name: {self.name}')

    def _emp_salary(self): #เป็น#ในคclass diagram สืบทอดไปที่ class ลูกได้แค่ 1 leval เท่านั้น
        print(f'salary: {self.salary}')
