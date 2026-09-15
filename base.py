import operator
operations = {"+": operator.add, "-": operator.sub, "/": operator.truediv, "*": operator.mul }

def calculate(o,num1,num2,operations):
    return operations[o](num1,num2)




ui = input("Enter your opertaion:")
a = ui.split(" ")
print(a)
c = calculate(a[1],int(a[0].strip()),int(a[2].strip()),operations)
print("Answer: "+str(c))
