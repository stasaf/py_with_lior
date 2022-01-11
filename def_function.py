def print_hello():
    print("hello")
    print("hi")
    print("bye")

#we can call to function only under the func (the interpeter does not recognize it yet)

print_hello()
print_hello()
print_hello()
print_hello()

#send param to func
def function_with_arg(param):
    param *=2
    print(param,"from func with arg")

function_with_arg(10)

def func_with_2_args(x,y,p,g):
    print(x,y, "from func wieh args")

func_with_2_args(2,3,4,5)