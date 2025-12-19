# main.py - ไฟล์หลักสำหรับรันเกม
import pygame
import sys
from settings import *
from player import Player
from enemy import Enemy
from ui import UI

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Neon Dash: Python Game")
        self.clock = pygame.time.Clock()
        self.ui = UI()
        
        # สถานะเกม
        self.game_active = True
        self.score = 0
        self.start_time = 0
        self.speed_boost = 0
        
        # Setup ตัวละครและกลุ่ม Sprite
        self.player = Player()
        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(self.player)
        
        self.enemy_group = pygame.sprite.Group()
        
        # Timer สำหรับปล่อยศัตรู
        self.enemy_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.enemy_timer, ENEMY_SPAWN_TIME)

    def reset_game(self):
        self.game_active = True
        self.score = 0
        self.speed_boost = 0
        self.start_time = pygame.time.get_ticks()
        self.enemy_group.empty()
        self.player.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)

    def run(self):
        while True:
            # 1. Event Loop (รับค่าปุ่มกด/ปิดหน้าต่าง)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                if self.game_active:
                    if event.type == self.enemy_timer:
                        # ปล่อยศัตรู และเพิ่มความยากขึ้นเรื่อยๆ ตามคะแนน
                        self.enemy_group.add(Enemy(self.speed_boost))
                else:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        self.reset_game()

            # 2. Update Logic
            self.screen.fill(COLOR_BG) # ล้างหน้าจอ
            
            if self.game_active:
                # คำนวณคะแนนตามเวลา
                self.score = (pygame.time.get_ticks() - self.start_time) // 100
                # เพิ่มความยากทุกๆ 500 คะแนน
                self.speed_boost = self.score // 500 

                # อัพเดทตำแหน่ง
                self.player_group.update()
                self.enemy_group.update()
                
                # เช็คการชน (Collision)
                if pygame.sprite.spritecollide(self.player_group.sprite, self.enemy_group, False):
                    self.game_active = False # Game Over

                # วาดกราฟิก
                self.player.draw_trail(self.screen) # วาดหางก่อนตัว
                self.player_group.draw(self.screen)
                self.enemy_group.draw(self.screen)
                self.ui.draw_score(self.screen, self.score)
                
            else:
                # หน้าจอ Game Over
                self.ui.draw_game_over(self.screen, self.score)

            # 3. อัพเดทหน้าจอ
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
