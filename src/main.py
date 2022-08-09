import pygame, random
from Algorithms.bubble_sort import bubble_sort
from Algorithms.insertion_sort import insertion_sort
from Algorithms.quick_sort import quick_sort
from Algorithms.heap_sort import heap_sort
from Algorithms.selection_sort import selection_sort
from Visualizer.draw_information import DrawInformation, draw

# implement game
def main():
    run = True
    
    # initialize sample data
    n = 50
    min_val, max_val = 0, 100
    lst = random.sample(range(min_val, max_val), n)
    w, h = 800, 600
    
    # initialize sorting data
    sorting = False
    ascending = True
    delay = 10
    
    draw_info = DrawInformation(w, h, lst)
    
    sorting_algorithm = bubble_sort
    sort_algo_name = "Bubble Sort"
    
    while run:
        
        if sorting:
            sorting_algorithm(draw_info, ascending, delay)
            sorting = False
        else:
            draw(draw_info, sort_algo_name, ascending)
        
        # implement controls based on keyboard input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            elif event.type != pygame.KEYDOWN:
                continue
                
            if run and not sorting:
            
                if event.key == pygame.K_r:
                    lst = random.sample(range(min_val, max_val), n)
                    draw_info.set_list(lst)
                    sorting = False
                
                elif event.key == pygame.K_SPACE:
                    sorting = True
                
                elif event.key == pygame.K_a:
                    ascending = True
                
                elif event.key == pygame.K_d:
                    ascending = False
                
                elif event.key == pygame.K_i:
                    sorting_algorithm = insertion_sort
                    sort_algo_name = "Insertion Sort"
                
                elif event.key == pygame.K_b:
                    sorting_algorithm = bubble_sort
                    sort_algo_name = "Bubble Sort"
                
                elif event.key == pygame.K_q:
                    sorting_algorithm = quick_sort
                    sort_algo_name = "Quick Sort"
                
                elif event.key == pygame.K_h:
                    sorting_algorithm = heap_sort
                    sort_algo_name = "Heap Sort"
                
                elif event.key == pygame.K_s:
                    sorting_algorithm = selection_sort
                    sort_algo_name = "Selection Sort"
                
    pygame.quit()

if __name__ == "__main__":
    main()