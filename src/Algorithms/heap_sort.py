from Visualizer.draw_information import draw_list

def heap_sort(draw_info, ascending=True, delay=10):
    lst = draw_info.lst
    n = len(lst)
    
    # build max heap
    for i in range(n//2 - 1, -1, -1):
        heapify(draw_info, lst, n, i, ascending, delay)
    
    # extract elements
    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        
        draw_list(draw_info, {i: draw_info.SEAGREEN, 0: draw_info.PINK}, True, delay)
        
        heapify(draw_info, lst, i, 0, ascending, delay)

def heapify(draw_info, lst, n, i, ascending, delay):
    idx = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and ((lst[idx] < lst[l] and ascending) or (lst[idx] > lst[l] and not ascending)):
        idx = l
    
    if r < n and ((lst[idx] < lst[r] and ascending) or (lst[idx] > lst[r] and not ascending)):
        idx = r
    
    if idx != i:
        lst[i], lst[idx] = lst[idx], lst[i]
        
        draw_list(draw_info, {i: draw_info.SEAGREEN, idx: draw_info.PINK}, True, delay)
        
        heapify(draw_info, lst, n, idx, ascending, delay)