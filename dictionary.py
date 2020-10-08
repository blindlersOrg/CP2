menu = {}

menu = {"apple": 1.90,
"bannana": 2.50,
"pineapple": 5}

menu.update({"apple" : 1.3})
print(menu)

menu.update({"pear": 10})
print(menu)

menu["apple"] = 3.6
print(menu)
print()
print(menu["apple"])

def addValue(k, v=10):
	menu.update({k : v})
	print(menu)

addValue("strawberry",25)



