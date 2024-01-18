def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
def calculate(num1):

    operations={
        "+":add,
        "-":subtract,
        "*":multiply,
        "/":divide
    }
    for symbol in operations:
        print(symbol)
    operation_symbol=input("Select the operation:")
    num2=int(input("Enter the second number:"))
    operation=operations[operation_symbol]
    answer=operation(num1,num2)
    print(f"{num1}{operation_symbol}{num2}={answer}")
    return answer
more='n'
while(more=='yes' or more=='n'):
    if(more=='yes'):
        ans=calculate(ans)
    elif more=='n':
        num1 = int(input("Enter the first number:"))
        ans = calculate(num1)
    more = input("Type 'yes' to continue with the same calculation/Type 'n' to start with a new calculation:")