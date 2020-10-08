key2 = 10
d = { "key1" : "value1",
key2: 20}
carstats = {"modelYear": 2000}
year = carstats.get("modelYear")

menu = {"apple": 1.90,
"bannana": 2.50,
"pineapple": 5}

menu.update({"apple" : 1.3})


menu.update({"pear": 10})


menu["apple"] = 3.6


def addValue(k, v=10):
	menu.update({k : v})
	#print(menu)

addValue("strawberry",25)

print(menu.values())



list = [1,2,3]
list2 = [1,2,3]
if list == list2: print('yes')
tuple = (1,2,3)



# test = input ("enter a W: ").lower()
# #test = test.lower()
# if test == 'w': print('w')
# if test == 'W': print('W')


inventoryTxt = open("inventory.txt", "r")
#for line in inventoryTxt.readlines():
#v = line.split(':')[1].strip()






myMenu = {}

# line = inventoryTxt.readline()

# print(line)
# key =line.split(':')[0]
# value = line.split(':')[1]
myInv = {}
#print(list[0])
for line in inventoryTxt.readlines():
	k = line.split(':')[0]
	v = line.split(':')[1].strip()
	q = line.split(':')[2].strip()
	myMenu.update({k:v})
	myInv.update({k:q})

print(myMenu)
print(myInv)

inventoryTxt.close()