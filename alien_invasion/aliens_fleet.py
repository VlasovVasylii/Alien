from models.alien import Alien


class AliensFleet:
    """Класс реализует флот инопланетян и работу с ними."""

    def __init__(self, ai_game):
        self.ai_game = ai_game

    def create_alien(self, alien_number, row_number):
        """Создание пришельца и размещение его в ряду"""
        alien = Alien(self.ai_game)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row_number + alien_height
        self.ai_game.aliens.add(alien)

    def create_fleet(self):
        """Создание флота вторжения."""
        # Создание пришельца и вычисление количества пришельцев в ряду
        # Интервал между соседними пришельцами равен ширине пришельца.
        alien = Alien(self.ai_game)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.ai_game.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        """Определяет количество рядов, помещающихся на экране."""
        ship_height = self.ai_game.ship.rect.height
        available_space_y = (
                self.ai_game.settings.screen_height - (3 * alien_height) - ship_height
        )
        number_rows = available_space_y // (3 * alien_height)

        # Создание флота вторжения.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self.create_alien(alien_number, row_number)

    def check_fleet_edges(self):
        """Реагирует на достижение пришельцем края экрана или его коллизии с
        элементами scoreboard."""
        for alien in self.ai_game.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                return
        for sprite in self.ai_game.aliens.sprites():
            if self.ai_game.score_board.level_rect.colliderect(sprite.rect) \
                    or self.ai_game.score_board.score_rect.colliderect(sprite.rect):
                self.change_fleet_direction()
                return

    def change_fleet_direction(self):
        """Опускает весь флот и меняет направление флота."""
        for alien in self.ai_game.aliens.sprites():
            alien.rect.y += self.ai_game.settings.fleet_drop_speed
        self.ai_game.settings.fleet_direction *= -1
