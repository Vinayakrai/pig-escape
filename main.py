import pygame
import random
from tkinter import messagebox

screen_size=[360,600]
screen=pygame.display.set_mode(screen_size)
pygame.font.init()

background=pygame.image.load('background.jpg')
baby=pygame.image.load('baby.png')
pig=pygame.image.load('pig.png')

keep_alive=True
clock=pygame.time.Clock()
score=0

def display_score(score):
  font = pygame.font.SysFont('Comic Sans MS', 30)
  score_text='Score: '+str(score)
  text_img=font.render(score_text, True, (0,255, 0))
  screen.blit(text_img, [20,10])

def random_offset():
  return -1*random.randint(100, 2000)

def update_chicken_position(idx):
  global score
  if pig_y[idx]>600:
    pig_y[idx]=random_offset()
    score=score+5
    print('Score', score)
  else:
    pig_y[idx]=pig_y[idx]+5

def crashed(idx):
  global score
  global keep_alive
  score=score-10
  pig_y[idx]=random_offset()
  if score<-50:
    keep_alive=False
    message1= messagebox.askretrycancel("Game Over", "Do you want to retry again?")
    if message1:
      keep_alive=True
      score=0
      pygame.scre
    else:
      pygame.quit()


pig_y=[random_offset(), random_offset() ,random_offset(), random_offset()]  #Increase number of pigs by increasing size of array

baby_x=180

while keep_alive:
  pygame.event.get()
  keys=pygame.key.get_pressed()
  if keys[pygame.K_RIGHT] and baby_x<270:
    baby_x=baby_x+7 #Move baby right
  elif keys[pygame.K_LEFT] and baby_x>20:
    baby_x=baby_x-7  #Move baby left
  screen.blit(background, [0,0]) #Block image transfer

  update_chicken_position(0)
  update_chicken_position(1)
  update_chicken_position(2)
  update_chicken_position(3)

  screen.blit(baby, [baby_x,350])
  screen.blit(pig, [20, pig_y[0]])
  screen.blit(pig, [100, pig_y[1]])
  screen.blit(pig, [180, pig_y[2]])
  screen.blit(pig, [260, pig_y[3]])

  if pig_y[0]>500 and baby_x<50:
    crashed(0)
  if pig_y[1]>500 and baby_x>70 and baby_x<130:
    crashed(1)
  if pig_y[2]>500 and baby_x>150 and baby_x<210:
    crashed(2)
  if pig_y[3]>500 and baby_x>230 and baby_x<290:
    crashed(3)

  display_score(score)

  pygame.display.update()
  clock.tick(50)  #Reduce speed of falling of pigs