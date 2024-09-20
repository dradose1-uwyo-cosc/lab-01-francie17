# create a list of bikes
bikes = ["trek","intense","cervelo","ibis","scott"]
# and print the list
print(bikes)


bikes = ["trek", "intense","cervelo","ibis","scott"]
print(bikes[0].title())
# you could also write the print code above as bike equals trek 

cities = ["Laramie","Cheyenne","Big Horn", "Evanston"]
print(cities)
cities[3] = "Lander"

# declare the empty list 
animals = []
print(len(animals)) 
# now add in different animals
animals.append("dog")
animals.append("panda")
animals.append("cat")

print(animals)

cities = ["Laramie","Cheyenne","Big Horn","Evanston"]
print(cities)

cities.insert(1,"Sheridan")
print(cities)

cities = ["Laramie","Casper","Jackson Hole","Cheyenne"]
print(cities)
# the code below will take out index space 1 and shift everything else
del cities[1]
print(cities)
variable = cities.pop()
print(cities)

colors = ["green","orange","yellow"]
print(colors)


cities = ["Laramie","Big Horn","Gillette","Cheyenne","Burns","Rock Springs","Riverton","Torrington"]
print(cities)
# sort will organize the list alphabetically 
cities.sort()
print(cities)