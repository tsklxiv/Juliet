import os
import re

operator_list = ["+", "-", "*", "/", "^"]

class IntOperator:
    def Plus(first, second):
        print(int(first) + int(second))

    def Minus(first, second):
        print(int(first) - int(second))

    def Multiply(first, second):
        print(int(first) * int(second))

    def Divide(first, second):
        print(int(first) / int(second))

    def Power(first, second):
        print(int(first) ** int(second))

class FloatOperator:
    def Plus(first, second):
        print(float(first) + float(second))

    def Minus(first, second):
        print(float(first) - float(second))

    def Multiply(first, second):
        print(float(first) * float(second))

    def Divide(first, second):
        print(float(first) / float(second))

    def Power(first, second):
        print(float(first) ** float(second))

def main():
    print("Juliet Calculator version 1.0")
    print("Type 'bye' to exit the REPL.")

    while True:
        ipt = input("#")
        result = ipt.split()

        if result[0] == "!" or result == "":
            pass
        elif re.fullmatch(r"\d+", result[0]):
            if len(result) == 1:
                print(f"{result[0]} :: Int")
                print(int(result[0]))
            elif result[1] in operator_list:
                if len(result) == 2:
                    print("Error: Missing second number")
                elif result[1] == "+":
                    IntOperator.Plus(result[0], result[2])
                elif result[1] == "-":
                    IntOperator.Minus(result[0], result[2])
                elif result[1] == "*":
                    IntOperator.Multiply(result[0], result[2])
                elif result[1] == "/":
                    IntOperator.Divide(result[0], result[2])
                elif result[1] == "^":
                    IntOperator.Power(result[0], result[2])
        elif re.fullmatch(r"\d+\.\d+", result[0]):
            if len(result) == 1:
                print(f"{result[0]} :: Float")
                print(float(result[0]))
            elif result[1] in operator_list:
                if len(result) == 2:
                    print("Error: Missing second number")
                elif result[1] == "+":
                    FloatOperator.Plus(result[0], result[2])
                elif result[1] == "-":
                    FloatOperator.Minus(result[0], result[2])
                elif result[1] == "*":
                    FloatOperator.Multiply(result[0], result[2])
                elif result[1] == "/":
                    FloatOperator.Divide(result[0], result[2])
                elif result[1] == "^":
                    FloatOperator.Power(result[0], result[2])
        elif result[0] == "bye":
            break
        else:
            print(f"Invalid command: {result[0]}")


if __name__ == "__main__":
    main()
