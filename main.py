import pygame

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *



def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updateable, drawable)
   

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0
    ast_field = AsteroidField()

    while True:
        screen.fill("black")
        updateable.update(dt)
        for ast in asteroids:
            if ast.collides_with(player):
                print("Game over!")
                exit()
        
        for ast in asteroids:
            for shot in shots:
                if shot.collides_with(ast):
                    ast.split()
                    shot.kill()

        for item in drawable:
            item.draw(screen)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
