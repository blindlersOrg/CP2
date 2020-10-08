import turtle

class Polygon:
	
	def __init__(self, name, sides, length):
		self.name = name
		self.sides = sides
		self.length = length
		self.sumOfInteriorAngles = 180 * (self.sides - 2)
		self.eachAngle = self.sumOfInteriorAngles/self.sides

	def show(self):
		print(self.name, self.sides, self.sumOfInteriorAngles, self.eachAngle, self.length)
		turtle.color("blue")
		turtle.pensize(5)
		turtle.penup()
		turtle.goto(-self.length,self.length)
		turtle.pendown()


		for i in range(self.sides):
			turtle.forward(self.length)
			turtle.right(180-self.eachAngle)

		
		turtle.done()


	def update(self):
		self.sumOfInteriorAngles = 180 * (self.sides - 2)
		self.eachAngle = self.sumOfInteriorAngles/self.sides


