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

      try:
        data[line[keys["start"]]].append(line)
      except KeyError:
        data[line[keys["start"]]] = []
        data[line[keys["start"]]].append(line)

      datal.append(int(line[keys["start"]]))

# print(sorted(datal))
# print(data["3"][0][keys["xb"]])

autolijst = []
for i in range(int(keys["ye"])):
  autolijst.append(Vehicle(i))

for t in range(int(key_list[5])):
    rm = 0
    for kt in range(len(datal)):
        if datal[kt] < t:
            rm = kt
    datal = datal[rm:]
    for auto in autolijst:
        if auto.timeTillNextAction == t:
            if auto.action == 'choose':

                if 
                    auto.chooseRide(data[datal[0]][0])
                    datal = datal[1:]

            if auto.action == 'wait':
                auto.waitRide(auto.listRides[-1])


