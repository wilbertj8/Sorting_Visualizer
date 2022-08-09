from visualizer import draw_list

# insertion_sort
def insertion_sort(draw_info, ascending=True, delay=10):
    lst = draw_info.lst
    
    for i in range(1, len(lst)):
        current = lst[i]
        
        while True:
            ascending_sort = i > 0 and lst[i-1] > current and ascending
            descending_sort = i > 0 and lst[i-1] < current and not ascending
            
            if not ascending_sort and not descending_sort:
                break
            
            lst[i] = lst[i-1]
            i -= 1
            lst[i] = current
            draw_list(draw_info, {i: draw_info.RED, i-1: draw_info.GREEN}, True, delay)
    
    return lst