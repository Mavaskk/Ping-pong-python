import pygame
import random
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
myFont = pygame.font.SysFont('futura', 30)   #assegno font
gioco = True

print()
class Player():
    def __init__(self,nGiocatore):
        self.nGiocatore = nGiocatore
        self.punteggioAggiungere = 0
        

    def aggiornaPunteggio(self,n):
        self.punteggioAggiungere += n
    def font(self):

        if self.nGiocatore == 1:
            x = 200
        if self.nGiocatore == 2:
            x = 400
        surface =myFont.render(f"Giocatore {self.nGiocatore} ", True, (0, 255, 0), None)  #assegno colore e testo
        screen.blit(surface, (x, 10)) #posiziono font
        

    def punteggio(self):
        if self.nGiocatore == 1:
            x = 265
        if self.nGiocatore == 2:
            x = 465
        # print(self.punteggioAggiungere)
        surface = myFont.render(f"{int(self.punteggioAggiungere)}   ", True, (0, 255, 0), None)  #assegno colore e testo
        screen.blit(surface, (x, 40)) #posiziono font

class Rettangolo():
    def __init__(self,x,h,nRett):
        self.h = h   
        self.xRett = x
        self.nRett = nRett
    
      
        
    def disegnaRett(self):
        self.rettangolo = pygame.draw.rect(screen,self.colore(), pygame.Rect(self.xRett,self.h,15,150))
        return self.rettangolo

    def bloccoBordi(self):
            if self.h >= 440:
                # print(self.h)
                self.h = 449
            if self.h <= -1:
                
                self.h = 0


    
    def colore(self):
        if self.nRett == 1:
            coloreRettangolo = (255,0,0)
        if self.nRett == 2:
            coloreRettangolo = (0,0,255)
        return coloreRettangolo

    def rimbalzo(self,palla):
        
        if 0 <= palla.x  <= 15 and self.h <= palla.y <= self.h + 150:
            palla.speed_x = -palla.speed_x
            # print("Rimbalzo sinistro")
        if 785 <= palla.x  <= 800 and self.h <= palla.y <= self.h + 150:
            palla.speed_x = -palla.speed_x
            # print("Rimbalzo destro")
        

class Pallina():
    
    def __init__(self, x,y,speedX, speedY, ):
        self.x = x
        self.y = y
        self.speed_x = speedX
        self.speed_y = speedY
        
    def disegnaPallina(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 20)
        

    def accentraPalla(self):
         self.x = 400
         self.y = 300
         velY = (-6,-8,6,)
         velX = (-6,-8,6,)
         self.speed_x = random.choice(velY)
         self.speed_y = random.choice(velX)
    
    def movimentoPalla(self):
        self.x += self.speed_x
        self.y += self.speed_y
        return self.x,self.y
    
    def rimbalzo(self):
        if self.x <= -10 or self.x >= 800:
            self.accentraPalla()
        if self.x <= 0:
            Giocatore2.aggiornaPunteggio(0.5)
            Giocatore2.punteggio()
        if self.x >= 790:
            Giocatore1.aggiornaPunteggio(0.5)
            Giocatore1.punteggio()
        if self.y <= 0 or self.y >= 600:
            self.speed_y = -self.speed_y       
        return self.speed_y
Giocatore2 = Player(2,)
Giocatore1 = Player(1,)

palla = Pallina(300,200,-6,8)
rett1 = Rettangolo(0,225,1)
rett2 = Rettangolo(785,225,2)

while gioco:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gioco = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_s:
                rett1.h += 100
            if event.key == pygame.K_w:
                rett1.h -= 100
            if event.key == pygame.K_DOWN:
                rett2.h += 100
            if event.key == pygame.K_UP:
                rett2.h -= 100
    
        # if event.type == pygame.KEYUP:
        #     if event.key == pygame.K_s:
        #         rett1.h +=50
        #     if event.key == pygame.K_w:
        #         rett1.h -= 50
        #     if event.key == pygame.K_DOWN:
        #         rett2.h +=50
        #     if event.key == pygame.K_UP:
        #         rett2.h -= 50
    palla.movimentoPalla()
    

    palla.rimbalzo()
    rett1.rimbalzo(palla)
    rett2.rimbalzo(palla)
    rett1.bloccoBordi()
    rett2.bloccoBordi()    
    screen.fill((0,0,0))
    
    Giocatore1.font()
    Giocatore2.font()
    Giocatore1.punteggio()
    Giocatore2.punteggio()
    rett1.colore()
   
    rett1.disegnaRett()
    rett2.disegnaRett()
    
    palla.disegnaPallina()
    
    pygame.display.flip()
    
    clock.tick(60)


pygame.quit()