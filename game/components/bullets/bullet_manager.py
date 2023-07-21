import pygame

from game.utils.constants import SCREEN_HEIGHT

class BulletManager:
    def __init__(self):
        self.player_bullets = []
        self.enemy_bullets = []

    def update(self, game):
        # Lista para almacenar los enemigos que deben eliminarse
        enemies_to_remove = []
        
        # Actualizar balas del jugador
        for bullet in self.player_bullets:
            bullet.update()
            if bullet.rect.y < 0:
                self.player_bullets.remove(bullet)
            else:
                # Comprobar colisión de bala del jugador con enemigos
                for enemy in game.enemy_manager.enemies:
                    if bullet.rect.colliderect(enemy.rect) and bullet.owner == 'player':
                        enemies_to_remove.append(enemy)
                        game.update_score()
                        self.player_bullets.remove(bullet)

        # Eliminar enemigos que deben ser eliminados
        for enemy in enemies_to_remove:
            game.enemy_manager.enemies.remove(enemy)
                
        # Actualizar balas del enemigo
        for bullet in self.enemy_bullets:
            bullet.update()
            if bullet.rect.y >= SCREEN_HEIGHT:
                self.enemy_bullets.remove(bullet)

            # Comprobar colisión de bala del enemigo con el jugador
            if bullet.rect.colliderect(game.player.rect) and bullet.owner == 'enemy':
                game.death_count += 1
                self.enemy_bullets.remove(bullet)
                game.playing = False

  
    def draw(self, screen):
        for bullet in self.player_bullets:
            bullet.draw(screen)

        for bullet in self.enemy_bullets:
            bullet.draw(screen)

    def add_bullet(self, bullet):
        if bullet.owner == 'player' and len(self.player_bullets) <1:
            self.player_bullets.append(bullet)
        if bullet.owner == 'enemy' and len(self.enemy_bullets) < 1:
            self.enemy_bullets.append(bullet)           
            