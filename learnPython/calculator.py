numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
calculations = ["+", "-", "*", "/", "//", "^", "(", ")", "T", "C", "S", "t", "c", "s"]

def addNumber(input, start):
    i = start
    number = input[i]
    i += 1
    while i < len(input) and input[i] in numbers:
        number += input[i]
        i += 1
    return float(number), i

def makeList(input):
    i = 0
    calculation = []
    while i < len(input):
        print(i)
        print(input[i])
        if input[i] in numbers:
            numberResult = addNumber(input, i)
            number = numberResult[0]
            i += numberResult[1]
            print(number)


input = input("Input calculation: ")
makeList(input)