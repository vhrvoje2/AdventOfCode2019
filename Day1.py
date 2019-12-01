#Fuel required to launch a given module is based on its mass. Specifically,
#to find the fuel required for a module, take its mass, divide by three,
#round down, and subtract 2.

lista = []
moduleFuel = []
fuelCounter = 0
extraFuel = 0

with open(r"D:\Git\AdventOfCode2019\Input.txt", 'r') as dat:
    for row in dat.readlines():
        lista.append(int(row))

for elem in lista:
    res = elem//3-2
    moduleFuel.append(res)
    fuelCounter += res

print("Part 1: " + str(fuelCounter))

for elem in moduleFuel:
    additionalFuel = 0
    while (elem//3-2 > 0):
        additionalFuel += elem//3-2
        elem = elem//3-2
    extraFuel += additionalFuel

print("Part 2: " + str(fuelCounter+extraFuel))