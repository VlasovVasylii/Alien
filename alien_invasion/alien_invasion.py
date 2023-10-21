import sys
import pygame
from settings import Settings


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        # Назначение цвета фона.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Запуск игрового цикла игры."""
        while True:
            # отслеживание событий клавиатуры и мышки
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При каждом проходе цикла перерисовывается экран.
            self.screen.fill(self.bg_color)

            # отображение последнего прорисованного экрана
            pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    game = AlienInvasion()
    game.run_game()
