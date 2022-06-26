class Switch():
    def __init__(self) -> None:
        self.switch_status = False

    def turnon(self): #functionเปิดไฟ
        self.switch_status = True
    
    def turnoff(self): #functionปิดไฟ
        self.switch_status = False
    
    def show(self):
        if (self.switch_status):
            print(f"ไฟเปิด")
        else:
            print(f"ไฟปิด")

#สร้างวัตถุหรือ object
sobj = Switch()

if __name__ == "__main__":
    sobj.show()
    sobj.turnon()
    sobj.show()
    sobj.turnoff()
    sobj.show()
    sobj.turnoff()
    sobj.show()
    sobj.turnoff()
    sobj.show()
