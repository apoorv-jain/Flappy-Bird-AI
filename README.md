# Flappy-bird-AI
This is an implementation of FlappyBird the Game in python. I didn't find a good replacement for this game which could have the changes in properties of the game, thus had to create the game myself. Feel free to use the code. I was trying to build an AI bot for playing Flappybird using Reinforcement Learning. But as I said before I couldn't find one.

I had already tried open-AI gym but wasn't successful. So if you just want to have the game in the vanilla form feel free to play it by downloading it. I have added a requirements.txt file to help anyone get this game up and running without any hassle. If you want to see th game's AI th code also been included already.

I used **PYGAME** to build the game and **NEAT** to implement the AI.

NEAT - NEAT (NeuroEvolution of Augmenting Topologies) is a method developed by Kenneth O. Stanley for evolving arbi- trary neural networks. NEAT-Python is a pure Python implementation of NEAT, with no dependencies other than the Python standard library. [LINK OF THE ORIGINAL PAPER](http://nn.cs.utexas.edu/downloads/papers/stanley.cec02.pdf)

[PYGAME](https://www.pygame.org/docs/) Documentation 

To Play or use it the game use the following steps :-

1. Install pip or the PyPI installer(Generally included in python) else can be done by typing on Windows Command Prompt
(And I assume you have already setup python and set it as the PATH)

``` 
        --  pip install pip    
```

(Yes for the recursive commands)
 
2. Download or clone the code and navigate to that directory in Command Prompt And type

```
        -- pip install -r requirements.txt
```

3. And if you want to play the game use the **Flappy-Bird-Game** directory and run 
```
        -- python FlappyBird.py
```
else if you want to run The AI use the  directory **Flappy-Bird-AI** and run the same command in command prompt.
