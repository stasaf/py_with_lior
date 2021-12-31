import time

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
                dot_to_print > dot_counter
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