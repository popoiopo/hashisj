import csv

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

print(sorted(datal))
print(data["3"][0][keys["xb"]])
