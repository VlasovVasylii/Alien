import pygame


class Update:
    """Класс реализует обновление процесса игры."""

    def __init__(self, ai_game):
        self.ai_game = ai_game

    def update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.ai_game.bullets.update()

        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.ai_game.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.ai_game.bullets.remove(bullet)

        self.ai_game.collisions.check_bullet_alien_collisions()

    def update_aliens(self):
        """
        Проверяет, достиг ли флот края экрана,
        с последующим обновлением позиций всех пришельцев во флоте.
        """
        self.ai_game.aliens_fleet.check_fleet_edges()
        self.ai_game.aliens.update()

        # Проверка коллизий "пришелец — корабль".
        if pygame.sprite.spritecollideany(self.ai_game.ship, self.ai_game.aliens):
            self.ai_game.collisions.ship_hit()

        # Проверить, добрались ли пришельцы до нижнего края экрана.
        self.ai_game.collisions.check_aliens_bottom()

    def update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.ai_game.screen.fill(self.ai_game.settings.bg_color)
        self.ai_game.ship.blitme()
        for bullet in self.ai_game.bullets.sprites():
            bullet.draw_bullet()
        self.ai_game.aliens.draw(self.ai_game.screen)

        # Вывод информации о счёте.
        self.ai_game.score_board.show_score()

        # Если игра неактивна:
        if not self.ai_game.status.game_active:
            if not self.ai_game.status.choosing_active:
                self.ai_game.play_button.draw_button()
            else:  # Кнопки выбора уровня сложности отображаются в том случае,
                # если игра в процессе выбора уровня сложности.
                self.ai_game.choose_levels.draw_buttons()
                self.ai_game.choose_levels.draw_title()

        pygame.display.flip()
