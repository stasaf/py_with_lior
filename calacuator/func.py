#function get 2 number and operation , return the result.

def calc (operation,x,y):
    if (operation == "add"):
        num = x+y
        return num
    elif (operation == "reduce"):
        num = x-y
        return num
    elif (operation == "multiple"):
        num = x*y
        return num
    elif (operation == "dev"):
        num = x/y
        return num
    else:
        str = "invalid operation"
        return str



        
