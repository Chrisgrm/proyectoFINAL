import pygame


class personaje(pygame.sprite.Sprite):

    
    
    def __init__(self, position):
        
        self.sheet = pygame.image.load('imagenes/son.png')
        self.sheet.set_clip(pygame.Rect(32, 0 , 32 ,32))        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.image.set_colorkey((100,200,100))
        self.frame = 0
        self.left_states = {0: (0, 32 , 32, 32), 1: (32, 32, 32, 32), 2: (64, 32, 32, 32)}
        self.stand_state = {0: (32, 0 , 32 ,32)}
        self.right_states = {0: (0, 64, 32, 32), 1: (32, 64, 32, 32), 2: (64, 64, 32, 32)}
        self.vel = 5
        
                
               
    def get_frame(self, frame_set):
        
        self.frame += 1
        
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clippped_rect))
        return clipped_rect

    def update(self, direction):
        jumpCount = 5
        isJump = False
        if direction == 'left' and self.rect.x>0:
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right' and self.rect.x<1100:
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'stand':
            self.clip(self.stand_state)

        
            
            
        if direction == 'salto':            
            isJump = True
            if (isJump):
                if jumpCount >= -5 :
                    neg =1
                    if jumpCount < 0:
                        neg = -1
                    self.clip(self.stand_state)
                    self.rect.y -= (jumpCount ** 2) /2 * neg
                    jumpCount -= 1
                else:
                    isJump= False
                    jumpCount = 5
                    
          

       
            
                    

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((100,200,100))

    def handle_event(self, event):

        keys = pygame.key.get_pressed()

        if event.type ==pygame.KEYDOWN:
            
            if event.key ==pygame.K_LEFT:
                self.update('left')
            if event.key ==pygame.K_RIGHT:
                self.update('right')
                
            if keys[pygame.K_SPACE]:
                self.update('salto')
                
           

##        if event.type ==pygame.KEYUP:
##            self.update ('stand')
            

        
                         
    
                         
                         
