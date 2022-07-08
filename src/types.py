import pygame

class Type(pygame.sprite.Sprite):
    def __init__(self, x, y, img_file, int_val):
        #0 = X, 1 = O
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect_x = x
        self.rect_y = y
        self.int_val = int_val
        self.curr_state = ""
        self.curr_type = ""

    def position(self):
        pos_file = open("position.txt", "w")
        if self.int_val == 0:
            self.curr_type = "X"
        elif self.int_val == 1:
            self.curr_type = "O"
        self.curr_state = f" Position of {self.curr_type} is: "+ "(" + str(self.rect_x) + ", " + str(self.rect_y) + ")"
        pos_file.write(self.curr_state)
        pos_file.close()


