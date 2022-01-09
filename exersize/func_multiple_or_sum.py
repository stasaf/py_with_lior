
#Create a function that will take two numbers as parameters
#Next, Inside a function, multiply two numbers and save their product in a product variable
#Next, use the if condition to check if the product >1000. If yes, return the product
#Otherwise, use the else block to calculate the sum of two numbers and return it.

def multiple_or_sum(num1,num2):
    result = num1 * num2
    if result <= 1000:
        return result
    else:
        return num1 + num2

calc = multiple_or_sum (20,30)
print("the result is" , calc)

calc = multiple_or_sum (40,30)
print("the result is" , calc)

