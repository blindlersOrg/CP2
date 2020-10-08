
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

# print(myMenu)
# print(myInv)

inventoryTxt.close()

infile = "inputFile.txt"

input_text = open(infile,"r")

for line in input_text.readlines():
	print(line[:-1])


print("\n**********************")

input_text = open(infile,"r")
for line in input_text.readlines():
	row = line.split(",")
	print(row)

print("\n**********************")

input_text = open(infile,"r")
for line in input_text.readlines():
	row = line.split(",")
	print(row[0] + "\n----------")
	for i in range(1,len(row)):
		print(row[i])

print("\n**********************")

cars = []
input_text = open(infile,"r")
for line in input_text.readlines():
	row = line.split(",")
	cars.append(row)

print(cars[0][0])


# with open(infile) as f1:
# 	for line in f1:
# 		print(line)

outfile = "outputFile.txt"
output_text = open(outfile,"a")
for car in cars:
	output_text.write(car[0] + "\n")
	
output_text = open(outfile,"a")
for car in cars:
	output_text.write(str(car) + "\n")

