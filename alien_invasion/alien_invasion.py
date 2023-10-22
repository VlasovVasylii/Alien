import pygame
from settings import Settings
from aliens_fleet import AliensFleet
from models.ship import Ship
from models.button import PlayButton
from time import sleep
from game_status import GameStatus
from choosing_level import ChooseLevel
from scoreboard import ScoreBoard
from checking_events import CheckEvents


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

        # Создание обработчика событий.
        self.checker_events = CheckEvents(self)

        # Создание экземпляра для хранения игровой статистики и панели результатов,
        # загрузка результатов прошлых игр.
        self.status = GameStatus(self)
        self.score_board = ScoreBoard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Инициализация объекта флота и его создание.
        self.aliens_fleet = AliensFleet(self)
        self.aliens_fleet.create_fleet()

        # Создание кнопки Play.
        self.play_button = PlayButton(self, "Play")

        # Создание выбора настроек сложности.
        self.choose_levels = ChooseLevel(self)

    def start_new_level(self):
        """Уничтожение существующих снарядов и создание нового флота."""
        self.bullets.empty()
        self.aliens_fleet.create_fleet()
        self.settings.increase_speed()

        # Увеличение уровня.
        self.status.level += 1
        self.score_board.prep_level()

    def _check_bullet_alien_collisions(self):
        """Обработка коллизий снарядов с пришельцами."""
        # Удаление снарядов и пришельцев, участвующих в коллизиях.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.status.score += self.settings.alien_points * len(aliens)
            self.score_board.prep_score()
            self.score_board.check_high_score()

        if not self.aliens:
            self.start_new_level()

    def _check_aliens_bottom(self):
        """Проверяет, добрались ли пришельцы до нижнего края экрана."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Происходит то же, что при столкновении с кораблем.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Обрабатывает столкновение корабля с пришельцем."""
        if self.status.ships_left > 1:
            # Уменьшение ships_left и обновление панели счёта.
            self.status.ships_left -= 1
            self.score_board.prep_ships()

            # Очистка списка пришельцев и снарядов.
            self.aliens.empty()
            self.bullets.empty()

            # Создание нового флота и размещение корабля в центре.
            self.aliens_fleet.create_fleet()
            self.ship.center_ship()

            # Пауза.
            sleep(0.5)
        else:
            self.status.game_active = False
            pygame.mouse.set_visible(True)

    def _update_bullets(self):
        """Обновляет позиции снарядов и уничтожает старые снаряды."""
        # Обновление позиций снарядов.
        self.bullets.update()

        # Удаление снарядов, вышедших за край экрана.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _update_aliens(self):
        """
        Проверяет, достиг ли флот края экрана,
        с последующим обновлением позиций всех пришельцев во флоте.
        """
        self.aliens_fleet.check_fleet_edges()
        self.aliens.update()

        # Проверка коллизий "пришелец — корабль".
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Проверить, добрались ли пришельцы до нижнего края экрана.
        self._check_aliens_bottom()

    def _update_screen(self):
        """Обновляет изображения на экране и отображает новый экран."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Вывод информации о счёте.
        self.score_board.show_score()

        # Если игра неактивна:
        if not self.status.game_active:
            if not self.status.choosing_active:
                self.play_button.draw_button()
            else:  # Кнопки выбора уровня сложности отображаются в том случае,
                # если игра в процессе выбора уровня сложности.
                self.choose_levels.draw_buttons()
                self.choose_levels.draw_title()

        pygame.display.flip()

    def run_game(self):
        """Запуск игрового цикла игры."""
        while True:
            # отслеживание событий клавиатуры и мышки
            self.checker_events.check_events()

            if self.status.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    game = AlienInvasion()
    game.run_game()
