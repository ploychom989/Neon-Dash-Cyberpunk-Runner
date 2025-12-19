# settings.py - เก็บการตั้งค่าทั้งหมดของเกม
import pygame

# ขนาดหน้าจอ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# สี (R, G, B) สไตล์ Neon Cyberpunk
COLOR_BG = (10, 10, 20)      # สีพื้นหลังเกือบดำ
COLOR_PLAYER = (0, 255, 255) # สีฟ้า Cyan นีออน
COLOR_ENEMY = (255, 0, 100)  # สีชมพู Magenta นีออน
COLOR_TEXT = (255, 255, 255) # สีขาว
COLOR_PARTICLE = (0, 255, 255)

# การตั้งค่าตัวผู้เล่น
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 50
PLAYER_SPEED = 8

# การตั้งค่าศัตรู
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
ENEMY_SPEED_START = 5
ENEMY_SPAWN_TIME = 1000 # มิลลิวินาที (1 วินาที)
