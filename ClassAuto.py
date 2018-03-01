class Vehicle:
	
	def __init__(self, id):
		self.id = id
		self.x = 0
		self.y = 0
		self.timeTillNextAction = 0
		self.listRides = []
		self.nextAction = 'choose'
		#choose, wait
	
	# Volgende actie: hij is op beginpunt
	def chooseRide(self, ride):
		self.timeTillNextAction = abs(self.x - ride.xb) + abs(self.y - ride.yb) + self.timeTillNextAction
		self.x = ride.xb
		self.y = ride.yb
		self.nextAction = 'wait'
		self.listRides.append(ride.id)
		
	#Volgende actie: hij is op eindpunt
	def waitRide(self, ride):
		self.timeTillNextAction = abs(ride.xe - ride.xb) + abs(ride.ye - ride.yb) + max(self.timeTillNextAction, ride.start)
		self.x = ride.xe
		self.y = ride.ye
		self.nextAction = 'choose'
		
	