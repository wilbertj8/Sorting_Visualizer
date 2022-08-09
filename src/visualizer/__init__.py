import random, pygame
from pickle import TRUE, FALSE
pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE
    
    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]
    
    FONT = pygame.font.SysFont('calibri', 30)
    LARGE_FONT = pygame.font.SysFont('calibri', 40)
    SIDE_PAD = 100
    TOP_PAD = 150
    
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Sorting Algorithm Visualization')
        self.set_list(lst)
    
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        self.block_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_PAD // 2

def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    
    controls = draw_info.FONT.render("R - Reset | SPACE - Start | A - Ascending | D - Descending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 5))
    
    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 35))
    
    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info, color_positions={}, clear_bg=False):
    lst = draw_info.lst
    
    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, 
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)
    
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        
        color = draw_info.GRADIENTS[i%3]
        
        if i in color_positions:
            color = color_positions[i]
        
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.block_height * val))
    
    if clear_bg:
        pygame.display.update()
    
def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst
    
    for i in range(len(lst)-1):
        for j in range(len(list)-1-i):
            num1, num2 = lst[j], lst[j+1]
            
            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                # draw_list()
                yield True
    
    return lst

def main():
    run = True
    clock = pygame.time.Clock()
    
    n = 50
    min_val, max_val = 0, 100
    lst = random.sample(range(min_val, max_val), n)
    w, h = 800, 600
    
    sorting = False
    ascending = False
    
    draw_info = DrawInformation(w, h, lst)
    
    while run:
        clock.tick(60)
        
        draw(draw_info)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type != pygame.KEYDOWN:
                continue
            
            if event.key == pygame.K_r:
                lst = random.sample(range(min_val, max_val), n)
                draw_info.set_list(lst)
                sorting = False
            
            elif event.key == pygame.K_SPACE:
                sorting = True
            
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            
            elif event.key == pygame.K_d and not sorting:
                ascending = False
    
    pygame.quit()

if __name__ == "__main__":
    main()