import pygame, random, sys

from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()

game_seed = random.randrange(1, 100000, 1) * random.randrange(1, 100000, 1)
print(f"Seed: {game_seed}")
random.seed(game_seed)

w, h = 600, 400

game_display = pygame.display.set_mode((w, h))

pygame.display.set_caption("Duong Nguyen Xuan - PYGAME08")


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.state = "start"
        self.image = pygame.image.load("./Asset/plane.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [40, 112]

    def update(self):
        # key
        key = pygame.key.get_pressed()

        if self.state == "start":
            if key:
                self.state = "ingame"

        elif self.state == "ingame":
            if key[pygame.K_a] and self.rect.x > 0:
                self.rect.x -= 3
            elif key[pygame.K_d] and self.rect.x < w:
                self.rect.x += 3
            if key[pygame.K_w] and self.rect.y > 0:
                self.rect.y -= 3
            elif key[pygame.K_s] and self.rect.y < w:
                self.rect.y += 3

        coll = pygame.sprite.spritecollide(self, rocket_gr, False)
        if coll and not self.state == "start":
            sys.exit()


class Rocket(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./Asset/rocket.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [w + 10, random.randrange(1, h, 1)]

    def update(self):
        # key
        if self.rect.x < 0:
            self.kill()
        else:
            self.rect.x -= 5

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("./Asset/cloud.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [w + 10, random.randrange(1, h, 1)]

    def update(self):
        # key
        if self.rect.x < 0:
            self.kill()
        else:
            self.rect.x -= 1


player = Player()

player_gr = pygame.sprite.Group()
rocket_gr = pygame.sprite.Group()
cloud_gr = pygame.sprite.Group()
player_gr.add(player)

fps = 60

last_spawn_rocket = 0
last_spawn_cloud = 0

while True:

    current = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    game_display.fill((135, 204, 248))

    player_gr.draw(game_display)
    player.update()

    rocket_gr.update()
    rocket_gr.draw(game_display)

    cloud_gr.update()
    cloud_gr.draw(game_display)

    if current - last_spawn_rocket > random.randint(1000,2500):
        rocket = Rocket()
        rocket_gr.add(rocket)
        print("Spawn rocket")
        last_spawn_rocket = current

    if current - last_spawn_cloud > random.randint(4000,5000):
        cloud = Cloud()
        cloud_gr.add(cloud)
        print("Spawn cloud")
        last_spawn_cloud = current


    clock.tick(fps)
    pygame.display.update()
