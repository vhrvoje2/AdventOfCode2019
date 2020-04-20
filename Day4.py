count = 0
startRange = 353096
endRange = 843212


def check(x):
    num = x
    numOk = True
    if '11' in str(num) or '22' in str(num) or '33' in str(num) or '44' in str(num) or '55' in str(num) or '66' in str(num) or '77' in str(num) or '88' in str(num) or '99' in str(num):
        for y in range(0, len(str(num))):
            try:
                if int(str(num)[y]) > int(str(num)[y+1]):
                    numOk = False
            except:
                continue
    else:
        numOk = False
    return numOk

""" for x in range(startRange, endRange+1):
    if check(x):
        count +=1 """

print("Part 1: " + str(count))