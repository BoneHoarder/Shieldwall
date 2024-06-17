import pgzrun
from random import randint, choice
from pgzhelper import *

WIDTH = 800
HEIGHT = 600
# center = [400, 300]
game_state=0

def draw_title():
    screen.clear()

    title.draw()

def update_title():
    global game_state
    start=pygame.key.get_pressed()
    
    if start[pygame.K_KP_ENTER]:
        game_state+=1
        
#variables
axe_speed_options=[3,-3]
rnd_speed= choice(axe_speed_options)
axe_speed=[1,-5]
axe_life=3

player_life=3
# bonus_speed=[0,3]
axe_docked= True
stationary_axe= False


#sprites
all_vikings = []
all_berserk=[]
all_shields=[]
for x in range(8):
    for y in range(3):
        viking = Actor("bloodyviking", anchor=["right", "top"])
        viking.pos = [x * 100, y * 30]
        all_vikings.append(viking)

for x in range(5):
    for y in range(4,5):
        berserk = Actor("berserk 60x80", anchor=["right", "top"])
        berserk.pos = [x * 150, y * 30]
        all_berserk.append(berserk)

hostile_axes=[]
enemy_axe= Actor("fireaxe")
hostile_axes.append(enemy_axe)

enemy_axe2= Actor("fireaxe")
hostile_axes.append(enemy_axe)

enemy_axe3= Actor("fireaxe")
hostile_axes.append(enemy_axe)


player = Actor("shieldmaiden")
player.pos = [400, 550]

dragonshield= Actor("dragonshield")
dragonshield.pos= [600, 300]
all_shields.append(dragonshield)

dragonshield2= Actor("dragonshield")
dragonshield2.pos= [730, 300]
all_shields.append(dragonshield2)

dragonshield3= Actor("dragonshield")
dragonshield3.pos= [220, 300]
all_shields.append(dragonshield3)

dragonshield4= Actor("dragonshield")
dragonshield4.pos= [80, 300]
all_shields.append(dragonshield4)

axe= Actor("axe")

#background
battlefield= Actor("battlefield3")
mediumhealth= Actor("battlefieldmediumblood")
critical= Actor("battlefieldcriticalblood")
title=Actor("title")
wasted=Actor("wasted")
won=Actor("won")

def draw():
    global game_state

    if game_state==0:
        draw_title()
    elif game_state==1:
        draw_1()
    elif game_state==2:
        draw_2()
    elif game_state==3:
        draw_3()
    elif game_state==4:
        draw_4()
    elif game_state==5:
        draw_5()

def draw_1():
    screen.clear()
    battlefield.draw()

    player.draw()

    for brick in all_vikings:
        brick.draw()
    
    for superbrick in all_berserk:
        superbrick.draw()

    for shield in all_shields:
        shield.draw()
    
    for enemy in hostile_axes:
        enemy.draw()
    
    enemy_axe.draw()

    axe.draw()

def draw_2():
    screen.clear()
    mediumhealth.draw()

    player.draw()

    for brick in all_vikings:
        brick.draw()
    
    for superbrick in all_berserk:
        superbrick.draw()

    for shield in all_shields:
        shield.draw()
    
    for enemy in hostile_axes:
        enemy.draw()

    axe.draw()

def draw_3():
    screen.clear()
    critical.draw()

    player.draw()

    for brick in all_vikings:
        brick.draw()
    
    for superbrick in all_berserk:
        superbrick.draw()

    for shield in all_shields:
        shield.draw()
    
    for enemy in hostile_axes:
        enemy.draw()

    axe.draw()

def draw_4():
    screen.clear()
    won.draw()

def draw_5():
    screen.clear()
    wasted.draw()

def on_mouse_move(pos):
    player.pos = [pos[0], player.pos[1]]

    if(player.pos[0]<=75):
        player.pos=[75,player.pos[1]]
    elif player.pos[0]>=725:
        player.pos=(725, player.pos[1])


def update():
    #déplacement de la hache par frame
    global game_state

    if len(all_vikings)==3:
        game_state=4
    
    if game_state==0:
        update_title()
    elif game_state==1:
        update_1()
    elif game_state==2:
        update_2()
    elif game_state==3:
        update_3()
    
def update_1():
    #déplacement de la hache par frame
    global axe_speed, game_state
    axe_speed=[1,-5]
    
    if len(all_vikings)==3:
        game_state=4
    

    if axe_docked and stationary_axe== False:
        axe.pos=[player.pos[0],player.pos[1]-50]
    elif stationary_axe:
        axe.angle=0
    else:
        axe.pos= axe.pos[0]+1, axe.pos[1]+axe_speed[1]
        axe.angle+=2

    axe_retrieval() 

    shield_bashing(dragonshield)
    shield_bashing(dragonshield2)
    shield_bashing(dragonshield3)
    shield_bashing(dragonshield4)

    check_borders()

    check_enemy_collision()

    check_player_collision()

    if all_berserk:
        rnd_berserk=choice(all_berserk)
        hostile(enemy_axe,player,rnd_berserk, axe)
    


def update_2():
    #déplacement de la hache par frame
    global axe_speed, game_state

    if len(all_vikings)==3:
        game_state=4

    axe_speed=[1,-5]
    if axe_docked and stationary_axe== False:
        axe.pos=[player.pos[0],player.pos[1]-50]
    elif stationary_axe:
        axe.angle=0
    else:
        axe.pos= axe.pos[0]+1, axe.pos[1]+axe_speed[1]
        axe.angle+=2

    axe_retrieval() 

    shield_bashing(dragonshield)
    shield_bashing(dragonshield2)
    shield_bashing(dragonshield3)
    shield_bashing(dragonshield4)

    check_borders()

    check_enemy_collision()

    check_player_collision()

    if all_berserk:
        rnd_berserk=choice(all_berserk)
        hostile(enemy_axe2,player,rnd_berserk, axe)
    else:
        hostile_axes.remove(enemy_axe2)
    
    shield_bashing(dragonshield)

def update_3():
    #déplacement de la hache par frame
    global axe_speed, game_state
    if len(all_vikings)==3:
        game_state=4

    axe_speed=[1,-5]
    
    if axe_docked and stationary_axe== False:
        axe.pos=[player.pos[0],player.pos[1]-50]
    elif stationary_axe:
        axe.angle=0
    else:
        axe.pos= axe.pos[0]+1, axe.pos[1]+axe_speed[1]
        axe.angle+=2

    axe_retrieval() 

    shield_bashing(dragonshield)
    shield_bashing(dragonshield2)
    shield_bashing(dragonshield3)
    shield_bashing(dragonshield4)

    check_borders()

    check_enemy_collision()

    check_player_collision()

    if all_berserk:
        rnd_berserk=choice(all_berserk)
        hostile(enemy_axe2,player,rnd_berserk, axe)
    else:
        hostile_axes.remove(enemy_axe2)

    shield_bashing(dragonshield)

#listes bonus
speed_bonus=[]

# helpers
def check_enemy_collision():

    global axe_speed,axe_life, game_state


    for viking in all_vikings:
        if axe.colliderect(viking):
            all_vikings.remove(viking)
            axe_life-=1

            axe_speed = axe_speed[0], axe_speed[1]* -1

    

    for viking in all_berserk:
        if axe.colliderect(viking):
            all_berserk.remove(viking)
            axe_life-=1
            #ajout brique
            new_berserk=Actor("berserk 60x80",anchor=["left", "top"])
            new_berserk.pos=viking.pos
            all_vikings.append(new_berserk)
            axe_speed = axe_speed[0], axe_speed[1]* -1
            
            break
    
    # if axe.colliderect(enemy_axe):
    #     axe_life=0
    
def shield_bashing(self):
    global axe_speed

    
    shield_life=5
    
    speed_options=[-5,-10,-15, 5, 10,15]
    rnd_options=choice(speed_options)

    if axe.colliderect(self):
        axe.pos= axe.pos[0]+(rnd_options), axe.pos[1]+axe_speed[1]
        shield_life-=1
        axe_speed=axe_speed[0]*2, axe_speed[1]*2
    
    if shield_life==0:
        all_shields.remove(self)

def hostile(self,player,enemy,weapon):
        global game_state, player_life

        strike=True
        speed=[4,5]
        hostile_speed=choice(speed)

        while strike == True:
            self.y = self.y + hostile_speed
            self.x= self.x + randint(-2,2)
            self.angle+=2
            if self.pos[1]+10 >= HEIGHT:
                self.pos=(enemy.x+50,enemy.y+55)
            strike=False
        
        if self.colliderect(weapon):
            self.pos= (enemy.x+50,enemy.y+55)

        # -- check collision avec player
        if self.colliderect(player) and game_state<4:
            game_state+=1
            player_life-=1
            hostile_axes.remove(self)
                  

def axe_retrieval():
    global axe_life, axe_docked, axe_speed, stationary_axe
    
    axe_position=[100, 700, 150, 750, 200, 600, 350, 550]
    rnd_pos=choice(axe_position)

    if axe_life==0 and axe_docked== False:
        axe.pos=[rnd_pos,520]
        axe_speed= [0,0]
        axe.angle=0
        stationary_axe= True
        axe_life=3

def on_mouse_up():
    global axe_docked
    axe_docked= False

def check_player_collision():
    global axe_speed, stationary_axe, axe_docked, rnd_speed
    if axe.colliderect(player):
        axe_speed = axe_speed[0], abs(axe_speed[1])* -1
        if stationary_axe:
            stationary_axe= False
            axe_docked= True
            axe_speed=[rnd_speed,-3]


def check_borders():
    global axe_speed, axe_life
    if axe.pos[0] <= 0 or axe.pos[0]>= WIDTH:
        # axe_speed = axe_speed[0]* -1, axe_speed[1]
        axe_life= 0

    if axe.pos[1] <= 0:
        axe_life=0
    elif axe.pos[1]>= HEIGHT:
        axe_life= 0


def move_bonus():
    global axe_speed
    for bonus in speed_bonus:
        if bonus.colliderect(player):
            speed_bonus.remove(bonus)
            axe_speed=axe_speed[0]*2, axe_speed[1]*2
            break
        else:
            bonus.pos=[bonus.pos[0]+bonus_speed[0], bonus.pos[1]+bonus_speed[1]]

pgzrun.go()