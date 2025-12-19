# enemy.py - จัดการสิ่งกีดขวาง
import pygame
import random
from settings import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed_boost):
        super().__init__()
        self.image = pygame.Surface((ENEMY_WIDTH, ENEMY_HEIGHT))
        self.image.fill(COLOR_ENEMY)
        
        # วาดลายกากบาทบนศัตรูเพื่อให้ดูมีดีเทล
        pygame.draw.line(self.image, (255, 255, 255), (0,0), (ENEMY_WIDTH, ENEMY_HEIGHT), 3)
        pygame.draw.line(self.image, (255, 255, 255), (ENEMY_WIDTH,0), (0, ENEMY_HEIGHT), 3)

        self.rect = self.image.get_rect()
        
        # สุ่มตำแหน่งแนวนอน
        self.rect.x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
        self.rect.y = -ENEMY_HEIGHT # เริ่มต้นเหนือหน้าจอ
        
        self.speed = ENEMY_SPEED_START + speed_boost

    def update(self):
        self.rect.y += self.speed
        
        # ถ้าตกเลยขอบล่างจอ ให้ลบตัวเองทิ้ง (เพื่อคืนหน่วยความจำ)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
