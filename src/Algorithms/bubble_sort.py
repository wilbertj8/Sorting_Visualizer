from Visualizer.draw_information import draw_list

# bubble sort
def bubble_sort(draw_info, ascending=True, delay=10):
    lst = draw_info.lst
    
    for i in range(len(lst)-1):
        for j in range(len(lst)-1-i):
            num1, num2 = lst[j], lst[j+1]
            
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                # redraw list, coloring the changed values accordingly
                draw_list(draw_info, {j: draw_info.SEAGREEN, j+1: draw_info.PINK}, True, delay)