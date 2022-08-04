import random, pygame
pygame.init()

class DrawInformation:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BACKGROUND_COLOR = WHITE
    
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
        self.blobk_height = round((self.height - self.TOP_PAD) / (self.max_val - self.min))