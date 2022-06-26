class Measure:
    def __init__(self) -> None:
        self.resulf = 0   #(เดิมที่ใช้จะมีหรือไม่มีก็ได้)

    def inch__cm(self,number): #instance class ทุกตัวไม่จำเป็นต้องมี init
        self.resulf = number * 2.54
        return number * 2.54

    def cm_inch(self,number:float):
        self.resulf = number / 2.54
        return self.resulf


