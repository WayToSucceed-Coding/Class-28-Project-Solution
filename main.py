import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save The Spaceship")

# Load images
background = pygame.image.load("bg.png") 
spaceship = pygame.image.load("spaceship.png") 
meteor_img = pygame.image.load("meteor.png") 
star_img = pygame.image.load("star.png") 

# Resize images
spaceship = pygame.transform.scale(spaceship, (100, 100))
meteor_img = pygame.transform.scale(meteor_img, (100, 100))
star_img = pygame.transform.scale(star_img, (100, 100))

class SpaceObject:
    def __init__(self,type):
        self.x = random.randint(0, WIDTH - 100)
        self.y = -50
        self.speed_y = random.randint(3, 7)
        self.type=type

    def draw(self):
        if self.type=='meteor':
            screen.blit(meteor_img, (self.x, self.y))
        else:
            screen.blit(star_img,(self.x,self.y))

    def move(self):
        self.y +=self.speed_y

# Game loop
running = True

# spaceship position 
spaceship_x = WIDTH // 2
spaceship_y = HEIGHT - 100

objects=[]

spawn_interval=2000

last_spawn_time=0

while running:
    screen.blit(background, (0, 0))  # Draw background
    screen.blit(spaceship, (spaceship_x, spaceship_y))  # Draw spaceship

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    current_time=pygame.time.get_ticks()

    if (current_time-last_spawn_time)>spawn_interval or last_spawn_time==0:

        type=random.choice(['meteor','star'])
        obj=SpaceObject(type)

        objects.append(obj)

        last_spawn_time=current_time
        
    objects=[obj for obj in objects if not obj.y>HEIGHT]

    for obj in objects:
        obj.draw()
        obj.move()

    
    pygame.display.update()

pygame.quit()
