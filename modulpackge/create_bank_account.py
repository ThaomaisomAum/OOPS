#โจทย์
#เรียกใช้ packeg เพื่อเข้าถึง Customer,Account
from bank.customer import Customer
from bank.account import Account

#สร้างข้อมูล object เพื่อเปิดบัญชีใหม่ของ Paul
paul = Customer()
paul.new_customer()

#สร้าง object ของ Account เพื่อเปิดบัญชีใหม่ของ Paul
paul_acc = Account()
paul_acc.open_account(paul.name,'Saving','0123-45678',500)

#แสดงข้อมูลของ customer paul
print(paul.cus_info())

#แสดงข้อมูลเงินคงเหลือของ paulus
print(paul_acc.display_balance())