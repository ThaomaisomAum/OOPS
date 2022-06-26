from cusorder import customer,Order
from modulpackge.cusorder.order import Order

cus = customer.Customer("Jame","Nontaburi")
ord = order,Order("15-06-2022","packed")

print(f'Order of {cus.cus_name} on {ord.data} is {ord.status}')


