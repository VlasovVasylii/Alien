import pygame
from settings import Settings
from aliens_fleet import AliensFleet
from models.ship import Ship
from models.button import PlayButton
from damage_mechanics import CollisionMechanics
from game_status import GameStatus
from choosing_level import ChooseLevel
from scoreboard import ScoreBoard
from checking_events import CheckEvents
from updates import Update


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

        # Создание интерфейса обновления игры.
        self.updator = Update(self)

        # Создание интерфейса обработки коллизий.
        self.collisions = CollisionMechanics(self)

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

    def run_game(self):
        """Запуск игрового цикла игры."""
        while True:
            # отслеживание событий клавиатуры и мышки
            self.checker_events.check_events()

            if self.status.game_active:
                self.ship.update()
                self.updator.update_bullets()
                self.updator.update_aliens()

            self.updator.update_screen()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    game = AlienInvasion()
    game.run_game()