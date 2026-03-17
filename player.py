from circleshape import CircleShape
from constants import *
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x = x
        self.y = y
    rotation = 0

    # in the Player class

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]    

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        Player.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector


# Using some hints at the top of https://discord.com/channels/551921866173054977/1470501913874141408 I was
# able to get this to shoot "more" as expected.  It seems awful fast, but mayb that's tweaked later.  My
# suspicion is this is a bug on my side -- even though it's fun.

    def shoot(self):
        shot = Shot(self.position, self.position, SHOT_RADIUS)
        shot_vector = pygame.Vector2(0, 1)
        shot_rotated_vector = shot_vector.rotate(Player.rotation)
        shot.velocity = shot_rotated_vector * PLAYER_SHOOT_SPEED


# This version makes the shot at a set distance away from the play, but in the direction the player is facing.
#
#    def shoot(self):
#        shot = Shot(self.position, self.position, SHOT_RADIUS)
#        unit_vector = pygame.Vector2(0,1)
#        rotated_vector = unit_vector.rotate(self.rotation)
#        rotated_with_speed_vector = rotated_vector * PLAYER_SHOOT_SPEED
#        shot.position += rotated_with_speed_vector
    
'''
    def shoot(self):
        Shot(self.position, self.position, SHOT_RADIUS)
        unit_vector = pygame.Vector2(0,1)
        rotated_vector = unit_vector.rotate(self.rotation)

        #self.position += 
'''

