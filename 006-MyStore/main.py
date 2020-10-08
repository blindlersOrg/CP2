path = "006-MyStore"
from menu_item import MenuItem


inventory = [] 
menu = {}

item = MenuItem("apples",1.09,150)

def load_inventory():
	with open('006-MyStore/inventory.txt') as f:
		for line in f:
			print(line)
			name, cost, qty = line.split(',')
			inventory.append(MenuItem(name,float(cost), int(qty)))
	
	#print(inventory)


def print_menu():
	pass

def show_inventory():
	pass

def sync_menu():
	
	for item in inventory:
		key, value = item.name,item.cost
		menu.update({key:value})
	




load_inventory()

print(inventory[0].cost)
inventory[0].cost = -25.13
print(inventory[0].cost)

inventory[0].name = -25.13

