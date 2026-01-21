import art
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    return n1 / n2

operation = {
    "+" : add,
    "-":  sub,
    "*" : mul,
    "/" : div,
}
def calculator():
    print(art.logo)


    should_accumulate = True
    num1 = float(input("Type the first Number:"))\

    while should_accumulate:
        for symbols in operation:
            print(symbols)
        mathematical_operator = input("Type the mathematical_operator int(+,_,*,/):")
        num2 = float(input("Type the second number:"))
        answer = operation[mathematical_operator](num1,num2)
        print(f"{num1} {mathematical_operator} {num2} = {answer}")
        choice = input(f"if 'y' you continue with {answer}:, if 'n' to start again")

        if choice == 'y':
            num1 = answer
        else:
            should_accumulate = False
            print("\n")
            calculator()


calculator()




