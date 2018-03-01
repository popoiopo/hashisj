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
    self.timeTillNextAction = abs(self[keys["xe"]] - ride[keys["xb"]]) + abs(self[keys["y"]] - ride[keys["yb"]]) + self.timeTillNextAction
    self.x = ride[keys["xb"]]
    self.y = ride[keys["yb"]]
    self.nextAction = 'wait'
    self.listRides.append(ride[keys["id"]])

  #Volgende actie: hij is op eindpunt
  def waitRide(self, ride):
    self.timeTillNextAction = abs(ride[keys["xe"]] - ride[keys["xb"]]) + abs(ride[keys["ye"]] - ride[keys["yb"]]) + max(self.timeTillNextAction, ride[keys["start"]])
    self.x = ride[keys["xe"]]
    self.y = ride[keys["ye"]]
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

datal = sorted(datal)
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
            if auto.nextAction == 'choose':

                auto.chooseRide(data[str(datal[0])][0])
                datal = datal[1:]

            if auto.nextAction == 'wait':
                auto.waitRide(auto.listRides[-1])


