import sys
import pygame


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    @staticmethod
    def run_game():
        """Запуск игрового цикла игры."""
        while True:
            # отслеживание событий клавиатуры и мышки
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # отображение последнего прорисованного экрана
            pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуск игры
    game = AlienInvasion()
    game.run_game()
