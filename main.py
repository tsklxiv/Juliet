# Import re for Regex support
import re

# List of operators
operator_list = ["+", "-", "*", "/", "^"]

# Operators for integer
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

# Operators for float
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

# Main function
def main():
    print("Juliet Calculator version 1.0")
    print("Type 'bye' to exit the REPL.")

    while True:
        ipt = input("#") # Ask user input
        result = ipt.split() # Split input into tokens
        
        # If the tokens meets a comment in there('!')
        # or meets a space, then it will skip
        if result[0] == "!" or result == "":
            pass
        # If the tokens meets a integer
        elif re.fullmatch(r"\d+", result[0]):
            # If there's only the integer in the token,
            # Then print it as a int
            if len(result) == 1:
                print(f"{result[0]} :: Int")
                print(int(result[0]))
            # If there's a operator in the next token,
            # Do math
            elif result[1] in operator_list:
                # If there's only first number and the operator,
                # The program will print an error
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
        # This pretty much the same as the first one,
        # Except that it is for float numbers
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
