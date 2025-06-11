# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroidfield import AsteroidField
from asteroid import Asteroid
from Shot import Shot
def main():
	pygame.init()
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	dt = 0
	asteroids = pygame.sprite.Group()
	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = (updatable)
	asteroidfield = AsteroidField()
	shots = pygame.sprite.Group()
	Shot.containers = (shots, updatable, drawable)
	while True:
		for event in pygame.event.get():
    		  if event.type == pygame.QUIT:
        	    return
		screen.fill("black")
		updatable.update(dt)
		for asteroid in asteroids:
			if asteroid.collision(player) == True:
				print("Game Over!")
				sys.exit()
		for asteroid in asteroids:
			for shot in shots:
				if asteroid.collision(shot) == True:
					asteroid.split()
		for obj in drawable:
			obj.draw(screen)
		pygame.display.flip()
		dt = clock.tick(60) / 1000












if __name__ == "__main__":
    main()
