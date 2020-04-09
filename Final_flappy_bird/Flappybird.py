import pygame
from Pipe import *
import random
from Bird import *
GRAVITY=2    # gravity for the birds
SCREENWIDTH, SCREENHEIGHT = 400,600 #dimensions of the window
PIPE_VELOCITY = 1.5 # Velocity of the pipe
PIPE_WIDTH = 30 #Width of the pipe
PIPE_GAP = 90 # Gap between the heights of the pipe
PIPE_RANGE = 250 # Range of the center of the gap of pipes from center
PIPES_DIST= 220 # Distance of two adjacent pipes
BIRD_RADIUS = 10 # Radius of the bird as a circle
BIRD_TERMINAL_VELOCITY = 7 # Max velocity of the bird
BIRD_JUMP = 17   # Acceleration of the jumping of the bird
BIRD_POSX = int(SCREENWIDTH/4) # Initial position of the bird
BIRD_SIZE_BUFFER = 2 # To compensate for proper collision detection
FPS=30 #Initial FPS
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
clock=pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Flappy Bird')
SCREEN.fill((135,206,235))
def closestPipe(pipes):
    min_dist=SCREENWIDTH
    nearest_pipe=None
    for pipe in pipes:
        if pipe.posx+PIPE_WIDTH/2-BIRD_POSX > 0 and pipe.posx+PIPE_WIDTH/2-BIRD_POSX < min_dist:
            min_dist=pipe.posx+PIPE_WIDTH/2-BIRD_POSX
            nearest_pipe=pipe
    return nearest_pipe
def main():
    run=True
    pipes=[]
    Last_pipe = None
    bird=Bird(SCREEN,(BIRD_POSX, int(SCREENHEIGHT/2)),BIRD_RADIUS,BIRD_TERMINAL_VELOCITY,GRAVITY,BIRD_JUMP,BIRD_SIZE_BUFFER)
    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type==pygame.KEYDOWN and (event.key==pygame.K_SPACE or event.key==pygame.K_DOWN):
                # print("jump")
                bird.jump()
        if Last_pipe == None or Last_pipe.posx < SCREENWIDTH - PIPES_DIST:
            rand_pipe=int(random.randrange(-1*PIPE_RANGE/2,PIPE_RANGE/2,1))+SCREENHEIGHT/2
            Last_pipe= Pipe(PIPE_WIDTH,SCREEN,(SCREENWIDTH-PIPE_WIDTH/2,rand_pipe),PIPE_VELOCITY,PIPE_GAP)
            pipes.append(Last_pipe)
        clock.tick(FPS)
        SCREEN.fill((135,206,235))
        for pipe in pipes:
            pipe.draw()
            pipe.update()
            if pipe.out_of_screen():
                pipes.remove(pipe)
        bird.update(pipes)
        bird.draw()
        if bird.checkColiision(closestPipe(pipes)):
             bird.reset()
             pipes=reset()
             Last_pipe=None
        textsurface = myfont.render(str(bird.score), False, (0, 0, 0))
        SCREEN.blit(textsurface,(20,30))
        pygame.display.flip()
def reset():
    pipes=[]
    SCREEN.fill((135,206,235))
    Last_pipe = None
    return pipes
main()
