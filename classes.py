class Car:

	cars = []

	def __init__(self,make, model, year, mpg):
		self.make = make
		self.model = model
		self.year = year
		self.mpg = mpg
		self.cars.append(self)


	def show(self):
		result = (self.make, self.model, self.year, self.mpg)
		result = '{} {} {} {}mpg'.format(self.year, self.make, self.model, self.mpg)

		return result

	@classmethod
	def get_car_list(cls):
		return cls.cars



car = Car('Ford','F150', '2019', 35)
print(car.show())
list = (Car.get_car_list())
for item in list: 
	print(item.show())