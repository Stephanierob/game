my_character = Actor('character')
my_character.pos = 100, 50

WIDTH = 500
HEIGHT = my_character.height + 20

def draw():
    screen.clear()
    screen.fill((255, 255, 255))
    my_character.draw()

def update():
    my_character.left = my_character.left + 2
    if my_character.left > WIDTH:
        my_character.right = 0

def on_mouse_down(pos):
    if my_character.collidepoint(pos):
        set_my_character_hurt()

def set_my_character_hurt():
    my_character.image = 'my_character_hurt'
    sounds.eep.play()

def set_my_character_normal():
    my_character.image = 'my_character'
