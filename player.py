# player.py - จัดการตัวละครของผู้เล่น
import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # สร้างตัวละครสี่เหลี่ยม
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(COLOR_PLAYER)
        
        # เพิ่มเอฟเฟกต์แสงเรือง (Glow border)
        pygame.draw.rect(self.image, (255, 255, 255), (0, 0, PLAYER_WIDTH, PLAYER_HEIGHT), 2)
        
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        
        # หางแสง (Trail effect)
        self.trail = [] 

    def update(self):
        # รับค่าปุ่มกด
        keys = pygame.key.get_pressed()
        
        # ขยับซ้าย
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= PLAYER_SPEED
        # ขยับขวา
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += PLAYER_SPEED
            
        # สร้างเอฟเฟกต์หาง (เก็บตำแหน่งปัจจุบันไว้)
        self.trail.append(self.rect.center)
        if len(self.trail) > 5: # เก็บแค่ 5 เฟรมล่าสุด
            self.trail.pop(0)

    def draw_trail(self, surface):
        # วาดหางแสงให้ดูมีความเร็ว
        for point in self.trail:
            pygame.draw.circle(surface, (0, 100, 100), point, PLAYER_WIDTH // 4)
