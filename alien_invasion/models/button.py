import pygame.font


class Button:
    """Базовый класс кнопки."""
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Назначение размеров и свойств кнопок.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Построение объекта rect кнопки.
        self.rect = pygame.Rect(0, 0, self.width, self.height)

    def _prep_message(self, message):
        """Преобразует message в прямоугольник и выравнивает текст по центру."""
        self.message_image = self.font.render(
            message, True, self.text_color, self.button_color
        )
        self.message_image_rect = self.message_image.get_rect()
        self.message_image_rect.center = self.rect.center

    def draw_button(self):
        # Отображение пустой кнопки и вывод сообщения.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.message_image, self.message_image_rect)


class PlayButton(Button):
    def __init__(self, ai_game, message):
        """Инициализирует атрибуты кнопки начала игры."""
        super().__init__(ai_game)

        # Изменение позиции прямоугольника
        self.rect.center = self.screen_rect.center

        # Сообщение кнопки создаётся один раз
        self._prep_message(message)


class ChooseButton(Button):
    """Создаёт кнопку выбора уровня сложности."""

    def __init__(self, ai_game, message, coordinates):
        super().__init__(ai_game)

        # Изменение позиции прямоугольника
        self.rect.move_ip(coordinates[0], coordinates[1])

        # Сообщение кнопки создаётся один раз
        self._prep_message(message)
