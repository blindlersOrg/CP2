quiz_bank = []

def load_data():
	l = []
	with open('qanda.dat') as f:
		for line in f:
			definition, word = line.split(',')
			#definition = definition[1:-1]
			word = word[:-1]
			l.append([definition,word])
	return l
			
	
quiz_bank = load_data()
print(quiz_bank)


