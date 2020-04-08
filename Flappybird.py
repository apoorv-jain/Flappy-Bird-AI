import neat
import pygame
from Pipe import *
import random as rand
from random import *
from Bird import *
import numpy as np
import os
from Slider import *
GRAVITY=2    # gravity for the birds
SCREENWIDTH, SCREENHEIGHT = 400,600 #dimensions of the window
PIPE_VELOCITY = 1.5 # Velocity of the pipe
PIPE_WIDTH = 30 #Width of the pipe
PIPE_GAP = 120 # Gap between the heights of the pipe
PIPE_RANGE = 200 # Range of the center of the gap of pipes from center
PIPES_DIST= 160 # Distance of two adjacent pipes
BIRD_RADIUS = 10 # Radius of the bird as a circle
BIRD_TERMINAL_VELOCITY = 7 # Max velocity of the bird
BIRD_JUMP = 5 # Acceleration of the jumping of the bird
BIRD_POSX = int(SCREENWIDTH/4) # Initial position of the bird
BIRD_SIZE_BUFFER = 2 # To compensate for proper collision detection
SLIDER_BUFFER = 60 # The distance of slider's center from the right hand side of the screen
TOTAL_BIRDS = 50 # Amount of birds in 1 generation
FPS=30 #Initial FPS
GEN=0 # To store the gen number
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 15) # For the Score display
clock=pygame.time.Clock()
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption('Flappy Bird')
SCREEN.fill((135,206,235)) #color of the background
slider = Slider(SCREEN , 30 , 500 , (SCREENWIDTH - SLIDER_BUFFER , 30) , 60) #Slider
def closestPipe(pipes): # calculation of the next pipe to the bird
    min_dist=SCREENWIDTH
    nearest_pipe=None
    for pipe in pipes:
        if pipe.posx+PIPE_WIDTH/2-BIRD_POSX > 0 and pipe.posx+PIPE_WIDTH/2-BIRD_POSX < min_dist:
            min_dist=pipe.posx+PIPE_WIDTH/2-BIRD_POSX
            nearest_pipe=pipe
    return nearest_pipe
def eval_genomes(genomes, config): # part of NEAT implementation
    run=True
    pipes=[]
    birds=[]
    nets=[]
    ge=[]
    global GEN,FPS
    GEN+=1

    Last_pipe = None
    pipes=reset(TOTAL_BIRDS)
    for _,g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        bird=Bird(SCREEN,(BIRD_POSX, int(SCREENHEIGHT/2)),
                    BIRD_RADIUS,BIRD_TERMINAL_VELOCITY,GRAVITY,BIRD_JUMP,
                    BIRD_SIZE_BUFFER)
        birds.append(bird)
        g.fitness = 0
        ge.append(g)
    MAX_SCORE=0
    ACTUAL_MAX=0
    while run and len(birds) > 0 : # while there are birds alive
        FPS = slider.get_value()
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
        if Last_pipe == None or Last_pipe.posx < SCREENWIDTH - PIPES_DIST:
            rand_pipe=int(rand.randrange(-1*PIPE_RANGE/2,PIPE_RANGE/2,1))+SCREENHEIGHT/2 # Making pipes
            Last_pipe= Pipe(PIPE_WIDTH,SCREEN,(SCREENWIDTH-PIPE_WIDTH/2,rand_pipe),PIPE_VELOCITY,PIPE_GAP)
            pipes.append(Last_pipe)
            nextPipe=closestPipe(pipes)
        SCREEN.fill((135,206,235))
        for pipe in pipes:
            pipe.draw()
            pipe.update()
            if pipe.out_of_screen():
                pipes.remove(pipe)
        for x,bird in enumerate(birds):
            if bird.AI_SCORE>MAX_SCORE:
                MAX_SCORE=bird.AI_SCORE
            if bird.score > ACTUAL_MAX:
                ACTUAL_MAX=bird.score
            xs=(nextPipe.posx,
                (nextPipe.posy-(PIPE_GAP/2)),
                bird.posy,
                bird.velocity,
                (nextPipe.posy+(PIPE_GAP/2)))
            ge[x].fitness += 0.1
            prediction= nets[x].activate(xs)
            if  prediction[0] > 0.5:
                bird.jump() # movement of the bird
            bird.update(pipes)
            if (bird.ScoreCheck):
                ge[x].fitness +=5
            bird.draw()
            if bird.checkColiision(closestPipe(pipes)):
                ge[x].fitness -=2
                birds.remove(bird)
                nets.pop(x)
                ge.pop(x)
        textsurface = myfont.render("Score: "+str(int(ACTUAL_MAX)), False, (0, 0, 0))
        SCREEN.blit(textsurface,(20,30))
        slider.draw()
        FPS = slider.get_value()
        print(clock.get_fps(),FPS)
        pygame.display.flip() # reseting the screen
    clock.tick(FPS)
def reset(TOTAL_BIRDS):   # To reset the game at each gen
    pipes=[]
    SCREEN.fill((135,206,235))
    Last_pipe = None
    return pipes
def run(config_file): # Loading the architecture of the network
    config=neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                config_file)
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    winner = p.run(eval_genomes,50)
    print('\nBest genome:\n{!s}'.format(winner))


if __name__ == '__main__':

    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)
