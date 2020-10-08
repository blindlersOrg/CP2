inFile = "inputFile.txt"

### I was here

input_text = open(inFile,"r" )
for line in input_text.readlines():
	print(line[:-1])

print('*******')

input_text = open(inFile,"r" )
for line in input_text.readlines():
	row = line.split(',')
	print(row)


print('*******')

input_text = open(inFile,"r" )
for line in input_text.readlines():
	row = line.split(',')
	print(row[0],':\n',"----")
	for i in range(1,len(row)):
		print(row[i])
		word = row[i]
		# for j in range(len(word)):
		# 	print(word[j])


# word = "someword"

# for i in range(len(word)):
# 	print(word[i])

print('*******')

cars = []
input_text = open(inFile,"r" )
for line in input_text.readlines():
	row = line.split(", ")
	cars.append(row)


# with open(inFile) as f1:
# 	for line in f1:
# 		print(line[:-1])

outFile = "outputFile.txt"
output_text = open(outFile,"a")

for car in cars:
	output_text.write(str(car) + "\n")
	


