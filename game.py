import pgzrun

# -- Resolution
WIDTH= 800
HEIGHT= 600

lines=4

center = [400,300]

# -- sprites du jeu
player=Actor("woman")
player.pos=[400,500]

axe= Actor("axe 60")
axe.pos=[400,420]
axe.speed=[3,-3]
axe.is_moving= False


bricks=[]
for x in range(0, WIDTH,100):
    for y in range(0,30*lines,50):
        brick=Actor("viking 80x60", anchor=["left","top"])
        brick.pos=[x,y]
        bricks.append(brick)

def update():

    if axe.is_moving:
        x=axe.pos[0] +axe.speed[0]
        y= axe.pos[1] +axe.speed[1]
        axe.pos=[x,y]

    # -- check speed x
    if axe.pos[0] - 10 <=0 or axe.pos[0]+10 >= WIDTH:
        axe.speed[0]*=-1

# -- check speed y
    if axe.pos[1] - 10 <=0:
        axe.speed[1]*=-1

    if axe.pos[1]+10 >= HEIGHT:
        axe.speed=[3,-3]
        axe.is_moving= False

    # -- check collision avec player
    if axe.colliderect(player):
        axe.speed[1]*= -1

    # check collision avec briques
    bricks_to_remove=[]
    for brick in bricks:
        if axe.colliderect(brick):
            axe.speed[1] *= -1
            bricks_to_remove.append(brick)

    for brick in bricks_to_remove:
        bricks.remove(brick)

    axe.angle+=1


def draw():
    screen.clear()
    
    for brick in bricks:
        brick.draw()
    player.draw()
    axe.draw()
    # screen.draw.circle(center,50, "green")

#fonction jouée lorsque la souris est bougé.
#pos représente la position de la souris
def on_mouse_move(pos):
    player.pos=pos[0], player.pos[1]
    if not axe.is_moving:
        axe.pos= player.pos[0], player.pos[1] -50

def on_mouse_up():
    axe.is_moving= True

# -- Lance le jeu
pgzrun.go()