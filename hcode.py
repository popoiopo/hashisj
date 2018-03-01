import csv


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
	self.timeTillNextAction = abs(self.x - int(ride[str(keys["xb"])])) + abs(self.y - int(ride[str(keys["yb"])])) + self.timeTillNextAction
	self.x = ride[str(keys["xb"])]
	self.y = ride[str(keys["yb"])]
	self.nextAction = 'wait'
	self.listRides.append(ride)

  #Volgende actie: hij is op eindpunt
  def waitRide(self, ride):
	self.timeTillNextAction = abs(int(ride[str(keys["xe"])]) - int(ride[str(keys["xb"])])) + abs(int(ride[str(keys["ye"])]) - int(ride[str(keys["yb"])])) + max(self.timeTillNextAction, int(ride[str(keys["start"])]))
	self.x = ride[str(keys["xe"])]
	self.y = ride[str(keys["ye"])]
	self.nextAction = 'choose'



# volledige datastructuur:
data = {}

# ordered list van vertrektijden
datal = []
counter = 1

with open("easy.csv") as csvfile:
	csv_read = csv.DictReader(csvfile)

	for line in csv_read:
	  key_list = line.keys()
	  keys = {"xb": key_list[0], "yb": key_list[1], "xe": key_list[2], "ye": key_list[3], "start": key_list[4], "end": key_list[5]}
	  line["id"] = counter
	  counter += 1
	  try:
		data[line[keys["start"]]].append(line)
	  except KeyError:
		data[line[keys["start"]]] = []
		data[line[keys["start"]]].append(line)

	  datal.append(int(line[keys["start"]]))

datal = sorted(datal)
# print(data["3"][0][keys["xb"]])

autolijst = []
for i in range(int(keys["ye"])):
  autolijst.append(Vehicle(i))
print(datal)
for t in range(int(key_list[5])):
	rm = 0
	for kt in range(len(datal)):
		if datal[kt] < t:
			rm = kt
	datal = datal[rm:]
	for auto in autolijst:
		print(auto.timeTillNextAction)
		if auto.timeTillNextAction == t:
				print(t)
				if auto.nextAction == 'choose':

					#print(data[str(datal[0])][0])
					print("choosingchoosingchoosingRAWHIIIIIIIIIDEE DUDUTUM")
					auto.chooseRide(data[str(datal[0])][0])
					datal = datal[1:]
					#print(datal[1])

				elif auto.nextAction == 'wait':
					print("waitingwaitingwaitingRAWHIIIIIIIIIDEE DUDUTUM")
					auto.waitRide(auto.listRides[-1])

				print("NIKSDOENNIKSDOENNIKSDOENRAWHIIIIIIIIIDEE DUDUTUM")
		# print("YANNICK IS EEN PEDAALEMMER")


for auto in autolijst:
	print("auto ", auto.id, auto.nextAction)
	for rit in auto.listRides:
		print("rit", rit)

	print("==================")


