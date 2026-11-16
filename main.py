import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from logger import log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width: 1280")
    print("Screen height: 720")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt:float = 0.0
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    #creating the groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    #giving values to the groups
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    while True:
      log_state()
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
      dt = clock.tick(60) / 1000
      updatable.update(dt)

      
      for asteroid in asteroids:
        for shot in shots:
           if shot.collides_with(asteroid):
              log_event("asteroid_shot")
              asteroid.split()
              shot.kill()
        if player.collides_with(asteroid):
           log_event("player_hit")
           print("Game over!")
           sys.exit()


      screen.fill("black")

      for sprite in drawable:
        sprite.draw(screen)

      pygame.display.flip()
      

if __name__ == "__main__":
    main()
