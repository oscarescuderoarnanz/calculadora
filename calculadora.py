#!/usr/bin/python3
import sys

functions = ["sum", "rest", "div", "mult"]

def arguments_control():
    if(len(sys.argv) != 4):
        print("Usage:", sys.argv[0], "function num1 num2")
        sys.exit()

    found = 0
    for indice in range(4):
        if(sys.argv[1] == functions[indice]):
                funct = sys.argv[1]
                found = 1
    if(found == 0):
        print("You can't use", sys.argv[1], ",use: sum, rest, div or mult")
        sys.exit()
    return funct

def operaciones(funct):
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("You can't use")
        sys.exit()

    if(funct == functions[0]): #Suma
        print(num1+num2)
    if(funct == functions[1]): #Resta
        print(num1-num2)
    try:
        if(funct == functions[2]): #Division
            print(num1/num2)
    except ZeroDivisionError:
        if(num1 != 0):
            print("Infinito")
        else:
            print("0")
    if(funct == functions[3]): #Multiplicacion
        print(num1*num2)

# Main
funct = arguments_control()
operaciones(funct)
