switch_status = False #เริ่มต้นตั้งสถานะไฟเป็นปิด

def turnon(): #functionเปิดไฟ
    global switch_status
    switch_status = True
    print("ไฟเปิด")

def turnoff(): #functionปิดไฟ
    global switch_status
    switch_status = False
    print("ไฟปิด")

if __name__ == "__main":
print(f'สถานะไฟ:{switch_status}')
turnon()
turnoff()