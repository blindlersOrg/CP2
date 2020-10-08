storeInv = {}
itemCost = {}
def addValue(k, qty=1, cost=1):
	storeInv.update({k : qty})
	itemCost.update({k:cost})
	print(storeInv)


storeInv["drink"] = 24
storeInv.update({"coffee":100})
addValue("cookie",50)

print(storeInv)


