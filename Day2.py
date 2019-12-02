inputValues = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,19,9,23,1,23,6,27,2,27,13,31,1,10,31,35,1,10,35,39,2,39,6,43,1,43,5,47,2,10,47,51,1,5,51,55,1,55,13,59,1,59,9,63,2,9,63,67,1,6,67,71,1,71,13,75,1,75,10,79,1,5,79,83,1,10,83,87,1,5,87,91,1,91,9,95,2,13,95,99,1,5,99,103,2,103,9,107,1,5,107,111,2,111,9,115,1,115,6,119,2,13,119,123,1,123,5,127,1,127,9,131,1,131,10,135,1,13,135,139,2,9,139,143,1,5,143,147,1,13,147,151,1,151,2,155,1,10,155,0,99,2,14,0,0]

#Opcode 1 adds together numbers read from two positions and stores the result in a third 
#position. The three integers immediately after the opcode tell you these three positions 
#- the first two indicate the positions from which you should read the input values, and 
#the third indicates the position at which the output should be stored.

#Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead of adding 
#them.

#Opcode 99 means that the program is finished and should immediately halt.

#testValues = [1,0,0,0,99]
#testValues = [2,3,0,3,99]
#testValues = [2,4,4,5,99,0]
#testValues = [1,1,1,4,99,5,6,0,99]

#1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).             OK
#2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).             OK
#2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801). OK
#1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.       OK

def opcode(values, index):
    if values[index] == 1:
        res = values[values[index+1]] + values[values[index+2]]
        values[values[index+3]] = res
        opcode(values, index+4)
    elif values[index] == 2:
        res = values[values[index+1]] * values[values[index+2]]
        values[values[index+3]] = res
        opcode(values, index+4)
    elif values[index] == 99:
        return

#Once you have a working computer, the first step is to restore the gravity assist program 
#(your puzzle input) to the "1202 program alarm" state it had just before the last computer 
#caught fire. To do this, before running the program, replace position 1 with the value 12 
#and replace position 2 with the value 2. What value is left at position 0 after the program 
#halts?

inputValues[1] = 12
inputValues[2] = 2

#part 1
values = inputValues.copy()
opcode(values, 0)
print(values[0])

#part 2

#Find the input noun and verb that cause the program to produce the output 19690720. What is 
#100 * noun + verb? (For example, if noun=12 and verb=2, the answer would be 1202.)

found = False
for x in range(0, 100):
    for y in range(0, 100):
        if found == False:
            values = inputValues.copy()
            values[1] = x
            values[2] = y
            opcode(values, 0)
            if values[0] == 19690720:
                found == True
                noun = x
                verb = y
        
print(noun, verb)
print(100 * noun + verb)