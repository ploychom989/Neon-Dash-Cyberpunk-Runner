# ui.py - จัดการ Interface และข้อความ
import pygame
from settings import *

class UI:
    def __init__(self):
        self.font = pygame.font.Font(None, 40) # ใช้ Font มาตรฐาน
        self.big_font = pygame.font.Font(None, 80)

    def draw_score(self, surface, score):
        score_surf = self.font.render(f'SCORE: {score}', True, COLOR_TEXT)
        # ใส่เงาให้ตัวหนังสือ
        shadow_surf = self.font.render(f'SCORE: {score}', True, (0, 100, 100))
        surface.blit(shadow_surf, (22, 22))
        surface.blit(score_surf, (20, 20))

    def draw_game_over(self, surface, score):
        # สร้างพื้นหลังโปร่งแสงมืดๆ
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(150)
        overlay.fill((0,0,0))
        surface.blit(overlay, (0,0))

        # ข้อความ Game Over
        game_over_surf = self.big_font.render('GAME OVER', True, COLOR_ENEMY)
        game_over_rect = game_over_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
        
        # คะแนนสุดท้าย
        score_surf = self.font.render(f'Final Score: {score}', True, COLOR_TEXT)
        score_rect = score_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 20))
        
        # คำแนะนำเริ่มใหม่
        restart_surf = self.font.render('Press SPACE to Restart', True, COLOR_PLAYER)
        restart_rect = restart_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 80))

        surface.blit(game_over_surf, game_over_rect)
        surface.blit(score_surf, score_rect)
        surface.blit(restart_surf, restart_rect)
