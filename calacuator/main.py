import func

num1 = input ("enter num1: \n")
num2 = input ("enter num2: \n")
print("\n \n \n")
print("sellect operator: \n")
print("1. Multipe.")
print("2. Add")
print("3. Reduce")
print("4. Devide")
operator = input("")
#operator = input ("enter operator: add , minus, ")
num1 = int(num1)
num2 = int(num2)
if operator == "1":
    print (func.calc ("multiple",num1,num2))
elif operator == "2":
    print (func.calc ("add",num1,num2))
elif operator == "3":
    print (func.calc ("reduce",num1,num2))
elif operator == "4":
    print (func.calc ("dev",num1,num2))
else:
    print("wrong operator")