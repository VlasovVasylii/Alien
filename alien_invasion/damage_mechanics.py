import pygame
from time import sleep


class CollisionMechanics:
    """Класс реализует обработку коллизий объектов."""
    
    def __init__(self, ai_game):
        self.ai_game = ai_game
        
    def check_bullet_alien_collisions(self):
        """Обработка коллизий снарядов с пришельцами."""
        # Удаление снарядов и пришельцев, участвующих в коллизиях.
        collisions = pygame.sprite.groupcollide(self.ai_game.bullets, self.ai_game.aliens, True, True)
    
        if collisions:
            for aliens in collisions.values():
                self.ai_game.status.score += self.ai_game.settings.alien_points * len(aliens)
            self.ai_game.score_board.prep_score()
            self.ai_game.score_board.check_high_score()
    
        if not self.ai_game.aliens:
            self.ai_game.start_new_level()

    def check_aliens_bottom(self):
        """Проверяет, добрались ли пришельцы до нижнего края экрана."""
        screen_rect = self.ai_game.screen.get_rect()
        for alien in self.ai_game.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Происходит то же, что при столкновении с кораблем.
                self.ship_hit()
                break

    def ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем."""
        if self.ai_game.status.ships_left > 1:
            # Уменьшение ships_left и обновление панели счёта.
            self.ai_game.status.ships_left -= 1
            self.ai_game.score_board.prep_ships()
    
            # Очистка списка пришельцев и снарядов.
            self.ai_game.aliens.empty()
            self.ai_game.bullets.empty()
    
            # Создание нового флота и размещение корабля в центре.
            self.ai_game.aliens_fleet.create_fleet()
            self.ai_game.ship.center_ship()
    
            # Пауза.
            sleep(0.5)
        else:
            self.ai_game.status.game_active = False
            pygame.mouse.set_visible(True)
