from Visualizer.draw_information import draw_list
import random

def quick_sort(draw_info, ascending=True, delay=10):
    lst = draw_info.lst
    l, r = 0, len(lst)-1

    def quick(l, r):
        # find index of next partition while rearranging array
        def partition(l, r):
            # random pivot
            rand = random.randint(l, r)
            # swap random pivot
            lst[r], lst[rand] = lst[rand], lst[r]
            draw_list(draw_info, {r: draw_info.SEAGREEN, rand: draw_info.PINK}, True, delay)
            
            lo = l
            for i in range(l, r):
                if (lst[i] <= lst[r] and ascending) or (lst[i] >= lst[r] and not ascending):
                    lst[i], lst[lo] = lst[lo], lst[i]
                    lo += 1
                    draw_list(draw_info, {i: draw_info.SEAGREEN, lo: draw_info.PINK}, True, delay)
                    
            lst[lo], lst[r] = lst[r], lst[lo]
            draw_list(draw_info, {lo: draw_info.SEAGREEN, r: draw_info.PINK}, True, delay)
            
            return lo
        
        if l < r:
            pi = partition(l, r)
            quick(l, pi-1)
            quick(pi+1, r)
    
    quick(l, r)