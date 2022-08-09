from Visualizer.draw_information import draw_list

def selection_sort(draw_info, ascending=True, delay=10):
    lst = draw_info.lst
    
    for i in range(len(lst)):
        idx = i
        # find greatest/smallest element in unsorted portion of array
        for j in range(i+1, len(lst)):
            if (lst[j] < lst[idx] and ascending) or (lst[j] > lst[idx] and not ascending):
                idx = j
        lst[idx], lst[i] = lst[i], lst[idx]
        draw_list(draw_info, {i: draw_info.SEAGREEN, idx: draw_info.PINK}, True, delay)