from art import logo
print(logo)

# #my solution

# #add
# def add(n1, n2):
#     return n1 + n2

# #subtract
# def subtract(n1, n2):
#     return n1 - n2
    
# #multiply
# def multiply(n1, n2):
#     return n1 * n2

# #divide
# def divide(n1, n2):
#     return n1 / n2

# operations = {
# "+": add,
# "-": subtract,
# "*": multiply,
# "/": divide,
# }


# num1 = int(input("What's the first number? \n"))
# num2 = int(input("What's the second number? \n"))


# for symbols in operations:
#     print(symbols)

# operation_symbol = input("Pick an operator from the line above: ")

# calculation_function = operations[operation_symbol]
# answer = calculation_function(num1, num2)
    
# print(f"{num1} {operation_symbol} {num2} = {answer}")


#add
def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2
    
#multiply
def multiply(n1, n2):
    return n1 * n2

#divide
def divide(n1, n2):
    return n1 / n2

calculation_finished = False

operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": divide,
}

num1 = int(input("What's the first number? \n"))
for symbols in operations:
    print(symbols)
operation_symbol = input("Pick an operator from the line above: ")
num2 = int(input("What's the second number? \n"))
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")


##############################################################################################################
while not calculation_finished:
    cont_calc = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.").lower()
    if cont_calc == "n":
        calculation_finished = True
    else:
        num1 = answer
        for symbols in operations:
            print(symbols)
        operation_symbol = input("Pick an operator from the line above: ")
        num2 = int(input("What's the second number? \n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")


# operation_symbol = input("Pick an operator from the line above: ")

# num3 = int(input("What's the second number? \n"))

# calculation_function = operations[operation_symbol]

# second_answer = calculation_function(first_answer, num3)

# print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")


