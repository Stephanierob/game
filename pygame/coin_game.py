from random import randint

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False
fox = Actor("fox")

coin = Actor("coin")
coin.ps = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def timeup():
    global game_over
    game_over = True

def update():
    pass

clock.schedule(time_up, 7.0)
place_coin()




