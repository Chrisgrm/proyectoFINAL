import pygame

pygame.init ()
anchoPantalla = 1130
altoPantalla = 640
win= pygame.display.set_mode ((anchoPantalla, altoPantalla))
pygame.display.set_caption("Zombiesssss")
clock = pygame.time.Clock()


bg = pygame.image.load('imagenes/Background2.png')
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
        
        self.right_states = {0: (0, 64, 32, 32), 1: (32, 64, 32, 32), 2: (64, 64, 32, 32)}
        self.vel = 5
        self.right = False
        self.hitbox = (self.rect.x, self.rect.y, 32, 32)
        
        
        
                
               
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
##        jumpCount = 5
##        isJump = False
        if direction == 'left' and self.rect.x>0:
            self.clip(self.left_states)
            self.rect.x -= self.vel
            jugador.right = False
        if direction == 'right' and self.rect.x<1100:
            self.clip(self.right_states)
            self.rect.x += self.vel
            jugador.right = True
        

        
            
##            
##        if direction == 'salto':            
##            isJump = True
##            if (isJump):
##                if jumpCount >= -5 :
##                    neg =1
##                    if jumpCount < 0:
##                        neg = -1
##                    self.clip(self.stand_state)
##                    self.rect.y -= (jumpCount ** 2) /2 * neg
##                    jumpCount -= 1
##                else:
##                    isJump= False
##                    jumpCount = 5
##                    
          

       
            
                    

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
class enemigo(object):
    def __init__(self, position):
        
        self.sheet = pygame.image.load('imagenes/zombie.jpg')
        self.sheet.set_clip(pygame.Rect(32, 0 , 32 ,32))        
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.image.set_colorkey((0,0,0))
        self.frame = 0
        self.left_states = {0: (0, 32 , 32, 32), 1: (32, 32, 32, 32), 2: (64, 32, 32, 32)}
        self.hitbox = (self.rect.x, self.rect.y, 32, 32)
        self.right_states = {0: (0, 64, 32, 32), 1: (32, 64, 32, 32), 2: (64, 64, 32, 32)}
        self.vel = 2
        self.right = False
        self.vidaBox = (self.rect.x, self.rect.y, 32, 10)
        self.golpe = False
        self.vida = 10

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
    def move_towards_player(self, jugador):
        
        dx = self.rect.x - jugador.rect.x
        
       
        if (dx<0):            
             self.rect.x += self.vel
             self.clip(self.right_states)
        elif (self.rect.x + 1 > dx):
             self.clip(self.left_states)
             self.rect.x -= self.vel


        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((0,0,0))


    def hit(self):
        self.vida -= 1
        self.golpe = True
        print('hit')

   
        
        
                
       
      
        
    

    
class proyectil(object):
    def __init__(self, x,y, radio, color, lado ):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.lado = lado
        self.vel = 8 * lado
        self.numBalas = 1

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radio)

#mainloop
run = True
loopDisparo = 0 
balas = []
jugador = personaje((anchoPantalla/2 , 520))
##zombie = enemigo((100, 520))
zombies = []

for i in range(3):
        x=100
        zombies.append(enemigo ((x,520)) )
        print (i)

while run:

    if loopDisparo >0:
        loopDisparo +=1
    if loopDisparo >3:
        loopDisparo = 0
    
    for event in pygame.event.get():
         if event. type == pygame.QUIT:
            run = False
####    for bala in balas:
##        if bala.y - bala.radio < zombie.hitbox[1] + zombie.hitbox[3] and bala.y + bala.radio > zombie.hitbox[1]:
##            if bala.x + bala.radio > zombie.hitbox[0] and bala.x - bala.radio < zombie.hitbox[0] + zombie.hitbox[2]:
##                zombie.hit()
##                balas.pop(balas.index(bala))
##        if bala.x <anchoPantalla and bala.x >0:
##            bala.x += bala.vel
##        else:
##            balas.pop(balas.index(bala))
    keys = pygame.key.get_pressed()

    for z in zombies:
        z = enemigo((100, 520))
        win.blit(z.image, z.rect)
    

    if jugador.right == True:
        lado = 1
    else:
        lado = -1

    if keys[pygame.K_z] and loopDisparo == 0:
        if len(balas)< 6:
            balas.append(proyectil (round(jugador.rect.x), round(jugador.rect.y+15), 5, (0,0,0), lado))
        loopDisparo = 1 

    

    jugador.handle_event(event)
##    zombie.move_towards_player(jugador)
    win.blit (bg, (0,0))
    win.blit(jugador.image, jugador.rect)
    jugador.hitbox = (jugador.rect.x, jugador.rect.y, 32, 32)
##    zombie.hitbox = (zombie.rect.x, zombie.rect.y, 32, 32)
    
##        pygame.draw.rect(win, (255,0,0), (zombie.hitbox[0], zombie.hitbox[1] - 10, 35 , 5))
##        pygame.draw.rect(win, (0,255,0), (zombie.hitbox[0], zombie.hitbox[1] - 10, 35 - ((35/10) * (10 - zombie.vida)) , 5))
##    if zombie.vida <0:
##        zombie.remove(zombie)
##    pygame.draw.rect(win, (255,0,0), jugador.hitbox, 2)
##    win.blit(zombie.image, zombie.rect)
    for bala in balas:
        bala.draw(win)
    pygame.display.flip()
    clock.tick(27)



    

    
    

pygame.quit()          
