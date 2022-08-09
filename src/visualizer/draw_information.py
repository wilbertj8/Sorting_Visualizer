import pygame
pygame.init()

class DrawInformation:
    # colors for use throughout
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    PINK = 255, 182, 193
    SEAGREEN = 32, 178, 170
    LIGHTGREY = 220, 220, 220,
    CORAL = 240, 128, 128
    MINT = 189, 252, 201
    ROYALBLUE = 39, 64, 139
    BACKGROUND_COLOR = ROYALBLUE
    
    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]
    
    # fonts for use throughout
    FONT = pygame.font.SysFont('calibri', 25)
    LARGE_FONT = pygame.font.SysFont('calibri', 40)
    # padding top and sides of window
    SIDE_PAD = 100
    TOP_PAD = 150
    
    # initialize window
    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        
        # actually create window using pygame
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Sorting Algorithm Visualizer')
        self.set_list(lst)
    
    # helper method to initialize list and its variables
    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)
        
        # width of each column is proportional to # of list elements
        self.block_width = round((self.width - self.SIDE_PAD) / len(lst))
        # height of each column is proportional to # of list elements between max and min
        self.block_height = int((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        # start drawing after side pad
        self.start_x = self.SIDE_PAD // 2

# method to draw entire window
def draw(draw_info, algo_name, ascending, delay=10):
    # clear screen
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    
    # initialize and draw titles
    title = draw_info.LARGE_FONT.render(f"{algo_name} - {'Ascending' if ascending else 'Descending'}", 1, draw_info.CORAL)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2, 5))
    
    # initialize controls
    controls = draw_info.FONT.render("R - Reset | SPACE - Start | A - Ascending | D - Descending",
                                     1, draw_info.MINT)
    # centralize controls text
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2, 50))
    
    sorting = draw_info.FONT.render("I - Insertion | B - Bubble | Q - Quick | H - Heap | Selection", 1, draw_info.MINT)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 80))
    
    draw_list(draw_info)
    # display changes
    pygame.time.delay(delay)
    pygame.display.update()

# method to draw list only
def draw_list(draw_info, color_positions={}, clear_bg=False, delay=10):
    lst = draw_info.lst
    
    # used to clear the area encompassing the list only (keep controls)
    if clear_bg:
        clear_rect = (draw_info.SIDE_PAD//2, draw_info.TOP_PAD, 
                      draw_info.width - draw_info.SIDE_PAD, draw_info.height - draw_info.TOP_PAD)
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)
    
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        # draw from top down
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height
        
        # switch colors to differentiate between columns
        color = draw_info.GRADIENTS[i%3]
        
        # color switching columns differently
        if i in color_positions:
            color = color_positions[i]
        
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.block_height * val))
    
    # update if just the list is being updated
    if clear_bg:
        pygame.time.delay(delay)
        pygame.display.update()