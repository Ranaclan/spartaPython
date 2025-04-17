numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
operators = ["+", "-", "*", "/", "%", "^", "(", ")", "T", "C", "S", "t", "c", "s"]

def makeList(input):
    i = 0
    calculation = []
    numberIndices = []
    while i < len(input):
        #print("i:", i)
        #print("character:", input[i])

        if input[i] in operators:
            calculation.append(input[i])
        elif input[i] in numbers:
            if i > 0 and input[i - 1] in numbers:
                calculation[-1] = str(calculation[-1]) + input[i]
            else:
                calculation.append(input[i])
                numberIndices.append(len(calculation) - 1)

        i += 1

    for i in numberIndices:
        calculation[i] = float(calculation[i])

    return calculation

def negatives(calculation):
    i = 0
    while i < len(calculation)-1:
        if calculation[i] == "-":
            if i == 0 or (calculation[i - 1] in operators and calculation[i - 1] != ")"):
                calculation.pop(i)
                calculation[i] *= -1
                i -= 1
        i += 1
    return calculation

def brackets(calculation):
    i = 0
    openBrackets = 0

    while i < len(calculation):
        if calculation[i] == "(":
            openBrackets += 1
            i += 1
            if openBrackets == 1:
                openPosition = i - 1
            continue
        elif calculation[i] == ")":
            openBrackets -= 1
            print(openBrackets)
            i += 1
            if openBrackets == 0:
                closePosition = i
                bracketContents = calculation[openPosition+1:closePosition-1]
                i -= len(bracketContents)
                calculation[openPosition] = doCalculation(bracketContents)[0]
                del calculation[openPosition + 1:closePosition]
            continue
        i += 1

    return calculation

def exponentiation(calculation):
    for i in range(len(calculation) - 1, 0, -1):
        if calculation[i] == "^":
            calculation[i] = pow(calculation[i - 1], calculation[i + 1])
            calculation.pop(i - 1)
            calculation.pop(i)
    return calculation

def division(calculation):
    i = 0
    while i < len(calculation)-1:
        if calculation[i] == "/":
            calculation[i - 1] = calculation[i - 1] / calculation[i + 1]
            calculation.pop(i)
            calculation.pop(i)
            i -= 2
        i += 1
    return calculation

def modulus(calculation):
    i = 0
    while i < len(calculation)-1:
        if calculation[i] == "%":
            calculation[i - 1] = calculation[i - 1] % calculation[i + 1]
            calculation.pop(i)
            calculation.pop(i)
            i -= 2
        i += 1
    return calculation

def multiplication(calculation):
    i = 0
    while i < len(calculation)-1:
        if calculation[i] == "*":
            calculation[i - 1] = calculation[i - 1] * calculation[i + 1]
            calculation.pop(i)
            calculation.pop(i)
            i -= 2
        i += 1
    return calculation

def addition(calculation):
    i = 0
    while i < len(calculation)-1:
        if calculation[i] == "+":
            calculation[i - 1] = calculation[i - 1] + calculation[i + 1]
            calculation.pop(i)
            calculation.pop(i)
            i -= 2
        i += 1
    return calculation

def subtraction(calculation):
    i = 0
    while i < len(calculation)-1:
        if calculation[i] == "-":
            calculation[i - 1] = calculation[i - 1] - calculation[i + 1]
            calculation.pop(i)
            calculation.pop(i)
            i -= 2
        i += 1
    return calculation

def doCalculation(calculation):
    calculation = negatives(calculation)
    calculation = brackets(calculation)
    calculation = exponentiation(calculation)
    calculation = division(calculation)
    calculation = modulus(calculation)
    calculation = multiplication(calculation)
    calculation = addition(calculation)
    calculation = subtraction(calculation)

    return calculation

input = input("Input calculation: ")
print(doCalculation(makeList(input))[0])