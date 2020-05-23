count = 0
count2 = 0
startRange = 353096
endRange = 843212

listDouble = ['11', '22', '33', '44', '55', '66', '77', '88', '99']
listTriple = ['111', '222', '333', '444', '555', '666', '777', '888', '999']

def check(num):
    for element in listDouble:
        if element in str(num):
            for y in range(1, len(str(num))):
                if int(str(num)[y-1]) > int(str(num)[y]):
                    return 0
            return element
    return 0

for num in range(startRange, endRange):
    if check(num):
        count +=1

print("Part 1: " + str(count))

def checkTwo(num):
    string = str(num)
    for element in listDouble:
        if element in string:
            index = string.index(element)
            if (string[index-1] != element[0]):
                try:
                    if (string[index+2] != element[0]):
                        for y in range(1, len(string)):
                            if int(string[y-1]) > int(string[y]):
                                return 0
                        return 1
                except:
                    for y in range(1, len(string)):
                        if int(string[y-1]) > int(string[y]):
                            return 0
                    return 1
    return 0

for num in range(startRange, endRange):
    count2 += checkTwo(num)

print("Part 2: " + str(count2))