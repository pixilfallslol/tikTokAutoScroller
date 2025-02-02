import pyautogui
import time
import random
import pygame 
import sys

print(input('Make sure your on the tiktok desktop website before running this, if your on it then you can hit enter to close this message.')) 

pygame.init()

W_W = 800
W_H = 600
WHITE = (255,255,255)
BUTTON_SHADE_LIGHT = (170,170,170)
BUTTON_SHADE_DARK = (100,100,100) 

surface = pygame.display.set_mode((W_W, W_H))
smallfont = pygame.font.SysFont('Comic Sans MS',35) 
text = smallfont.render('start' , True , WHITE) 
times = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
x = 2519
y = 780
startPressed = False
stopPressed = False # TODO: Add stop logic and fix issue with gui failing.

def clickAfterTime():
    if startPressed:
        while True:
            timeSleep = random.choice(times)
            print(timeSleep)
            time.sleep(timeSleep)
            pyautogui.click(x, y)
            print('clicked')   

while True: 
    for ev in pygame.event.get():
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
              
        if ev.type == pygame.MOUSEBUTTONDOWN: 
              
            if W_W/2 <= mouse[0] <= W_W/2+140 and W_H/2 <= mouse[1] <= W_H/2+40:              
                startPressed = True 
                  
    surface.fill((WHITE)) 
      
    mouse = pygame.mouse.get_pos() 
 
    if W_W/2 <= mouse[0] <= W_W/2+140 and W_H/2 <= mouse[1] <= W_H/2+40: 
        pygame.draw.rect(surface,BUTTON_SHADE_LIGHT,[W_W/2,W_H/2,140,40]) 
          
    else: 
        pygame.draw.rect(surface,BUTTON_SHADE_DARK,[W_W/2,W_H/2,140,40]) 
      
    surface.blit(text , (W_W/2+50,W_H/2)) 
            
    clickAfterTime()
      
    pygame.display.update()
           