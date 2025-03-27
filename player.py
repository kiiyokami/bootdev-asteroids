from circleshape import *
import pygame

class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.speed = 5
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        return (
            self.position + forward * self.radius,
            self.position - forward * self.radius - right,
            self.position - forward * self.radius + right
        )
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, angle):
        self.rotation += angle

    def move(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        # if keys[pygame.K_w]:
        #     self.y -= self.speed
        # if keys[pygame.K_s]:
        #     self.y += self.speed
