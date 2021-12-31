import time


x=0
while(x < 10):
    print("I'm in a loop number",x)
    x += 1
print("bye")

# #*************************************
dot_counter=0
inc = True
while_counter=1
while (while_counter<100):
    print("."*dot_counter,"$")
    time.sleep(0.1)
    if(inc):
        dot_counter += 1
        if(dot_counter>100):
            inc = False
    else:
        dot_counter -= 1
        if(dot_counter < 1):
            inc = True
            while_counter += 1

def print_dots(
    dot_counter,
    number_of_iterations,
    speed,
):
    inc = True
    current_number_of_iterations = 0
    dot_to_print = 1

    while (
        current_number_of_iterations < number_of_iterations
    ):
        print(f'{"." * dot_to_print}$')
        time.sleep(speed)
        if(inc):
            dot_to_print += 1
            if(
                dot_to_print>dot_counter
            ):
                inc = False
        else:
            dot_to_print -= 1
            if(
                dot_to_print < 1
            ):
                inc = True
                current_number_of_iterations += 1

for i in range(20):
    print_dots(
        dot_counter=i+1,
        number_of_iterations=1,
        speed=(i+1) * 0.001,
    )


# print_dots(
#     10,
#     3,
#     0.01,
# )

# print_dots(
#     5,
#     2,
#     0.1,
# )