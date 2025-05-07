
# Matplotlib - module for drawing plots,
import matplotlib.pyplot as plt


# Main drawing function. Start_num is base for next graph, print_steps and draw_graph - optional values
def draw_collatz_sequence(start_num: int, print_steps: bool = True, draw_graph: bool = True) -> None:
    x = 0                   # x
    current_num = start_num # y

    # Lists for containing every dot position
    data_x = []
    data_y = []

    # Statistics of graph to show at last
    stats = {'steps_passed': 0,
             'max_value': 0,
             'up_dirs': 0,
             'down_dirs': 0}
    
    # Direction of current step to print
    dir = ''

    # Creating grahps and setup settings
    fig, ax = plt.subplots()
    ax.set_title(f'Collatz Sequence for {start_num}')
    ax.set_xlabel('X')
    ax.set_ylabel('Heigth')
    ax.set_autoscale_on(True)
    line, = ax.plot([], [], marker='o', markersize=3)

    if draw_graph:
        # Enabling interactive mode for window viewport and showing it
        plt.ion()
        plt.show()

    # In collatz algorithm at 1 appears infinite loop called 4-2-1
    while current_num != 1:

        # Updating and setting graph data
        data_x.append(x)
        data_y.append(current_num)
        line.set_data(data_x, data_y)
        ax.relim()
        ax.autoscale_view()

        stats['max_value'] = max(current_num, stats['max_value'])
        if print_steps: print(f'dir: {dir} x: {x}, y: {current_num}')

        # Main rule of sequence: if x(n) % 2 == 0 (num is odd) ==> x(n+1) = x(n)/2
        if current_num % 2 == 0:
            current_num //= 2
            stats['down_dirs'] += 1
            dir = '↓'
        # Else if x(n) % 2 != 0 (num isn't odd) ==> x(n+1) = 3x(n) + 1
        else:
            current_num = (3 * current_num) + 1
            stats['up_dirs'] += 1
            dir = '↑'
        # Example: 3 => 10 => 5 => 16 => 8 => 4 => 2 => 1 => 4...
        
        x += 1
        plt.pause(0.01)
    
    stats['steps_passed'] = x
    print(f'--- Total stats for {start_num} --- \nSteps passed: {stats.get('steps_passed')}\nUp / Down: {stats.get('up_dirs')} / {stats.get('down_dirs')}\n Max reached number: {stats.get('max_value')}')
    plt.pause(20)

draw_collatz_sequence(27)
# draw_collatz_sequence(1541581097960455658929045308190)
