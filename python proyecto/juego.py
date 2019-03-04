import pygame,random

pygame.init ()
anchoPantalla = 1130
altoPantalla = 640
win= pygame.display.set_mode ((anchoPantalla, altoPantalla))
pygame.display.set_caption("Zombiesssss")
clock = pygame.time.Clock()
fuente= pygame.font.Font('Macabre.otf', 60)
fuentedead= pygame.font.Font('Macabre.otf', 120)


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
        self.vida = 100
        self.municion=1
        self.daño=1
        
        
                
               
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

        if direction == 'left' and self.rect.x>0:
            self.clip(self.left_states)
            self.rect.x -= self.vel
            jugador.right = False
        if direction == 'right' and self.rect.x<1100:
            self.clip(self.right_states)
            self.rect.x += self.vel
            jugador.right = True

        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.image.set_colorkey((100,200,100))

    def handle_event(self, event):
        keys =pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.update('left')
        elif keys [pygame.K_RIGHT]:
            self.update('right')

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
        self.vel = 3
        self.right = False
        
  
        self.golpe = False
        self.vida = 20

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
        self.vida -= jugador.daño
        self.golpe = True
       
        

    def dibujar (self, win):
        
        win.blit(self.image, self.rect)
        self.hitbox = (self.rect.x, self.rect.y, 32, 32)

class objeto(object):
    def __init__(self):
        self.x = random.randrange(0,1130,5)
        
        self.tipo = random.randrange(2,3)
        
        self.color =(0,0,0)
        if self.tipo == 0:
            self.color = (255,255,255)
            jugador.vida +=10
            
            
        elif self.tipo == 1:
            self.color = (0,74,22)
            jugador.municion +=1
            
            
        else:
            self.color = (230,117,0)
            jugador.daño +=1
            
            
               
            

    def draw(self,win):
        pygame.draw.rect(win, self.color , (self.x,532,25,20))
        
    def lugarCaja (self):
        self.x = random.randrange(0,1110,5)
        
    
class proyectil(object):
    def __init__(self, x,y, radio, color, lado ):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.lado = lado
        self.vel = 8 * lado
        

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radio)


run = True
loopDisparo = 0 
balas = []
jugador = personaje((565 , 520))
zombies = []
horda =0
jumpCount = 7
isJump = False
nuevaronda=0
o=objeto()           

#mainloop
while run:
    tomado=True
    win.blit (bg, (0,0))   

    if len(zombies)==0:
        
        horda +=1
        xd=1350
        xi=-300        
        for i in range(horda):           
            zombies.append(enemigo ((xd,520)))            
            xd += 50
        for i in range(horda):
            zombies.append (enemigo((xi,520)) )
            xi -= 50
    if nuevaronda != horda:                
        if(tomado):
            o.draw(win)            
            if (round(o.x))==(round(jugador.rect.x)):
                  tomado=False
                  o=objeto()
                  nuevaronda = horda   

    if loopDisparo >0:
        loopDisparo +=1
    if loopDisparo >3:
        loopDisparo = 0
    
    for event in pygame.event.get():
         if event. type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    for zombie in zombies:
        for bala in balas:
            
        
            if bala.y - bala.radio < zombie.hitbox[1] + zombie.hitbox[3] and bala.y + bala.radio > zombie.hitbox[1]:
                if bala.x + bala.radio > zombie.hitbox[0] and bala.x - bala.radio < zombie.hitbox[0] + zombie.hitbox[2]:
                    zombie.hit()
                    balas.pop(balas.index(bala))
        zombie.move_towards_player(jugador)
        
        if zombie.vida <= 0:
            zombies.pop(zombies.index(zombie))

        if ((round(jugador.rect.x)-15) < round(zombie.rect.x) < (round(jugador.rect.x)+15) and (jugador.rect.y==zombie.rect.y)):

            jugador.vida -= 1
            

    if jugador.vida <=0:
        jugador.rect.y = -1000
        textdead = fuentedead.render('ESTAS MUERTO ' ,1 ,(189,4,9))
        win.blit(textdead, ((anchoPantalla/2)-150,250))
        zombie.vel = 5
           
            
    if jugador.right == True:
        lado = 1
    else:
        lado = -1
    
    if keys[pygame.K_z] and loopDisparo == 0:
        if len(balas)< jugador.municion:
            balas.append(proyectil (round(jugador.rect.x), round(jugador.rect.y+15), 5, (0,0,0), lado))
        loopDisparo = 1

    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:

        if jumpCount >= -7:
            neg = 1
            if jumpCount < 0:
                neg = -1
            jugador.rect.y -= (jumpCount ** 2) * neg
            jumpCount -= 1
                  
        else:
            isJump = False
            jumpCount = 7
    

    
    win.blit(jugador.image, jugador.rect)
    jugador.handle_event(event)
    jugador.hitbox = (jugador.rect.x, jugador.rect.y, 32, 32)  

    for bala in balas:
        if bala.x <anchoPantalla and bala.x >0:
            bala.x += bala.vel
        else:
            balas.pop(balas.index(bala))
        bala.draw(win)

    for zombie in zombies:
        zombie.dibujar(win)
        
        if zombie.golpe == True:
            
            pygame.draw.rect(win, (189,4,9), (zombie.hitbox[0], zombie.hitbox[1] - 10, 35 , 5))
            pygame.draw.rect(win, (115,98,98), (zombie.hitbox[0], zombie.hitbox[1] - 10, 35 - ((35/20) * (20 - zombie.vida)) , 5))

    text = fuente.render('OLEADA '+ str(horda) ,1 ,(189,4,9))
    win.blit(text, ((anchoPantalla/2)-40,30))

   
    
                             
    pygame.display.flip()

    clock.tick(27)

   
    

    
    

pygame.quit()          
