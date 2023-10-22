from models.button import ChooseButton


class ChooseLevel:
    """Класс для создания выбора уровня сложности."""

    def __init__(self, ai_game):
        self.levels = [
            ChooseButton(ai_game, "Normal", (
                ai_game.settings.screen_width * 0.3,
                ai_game.settings.screen_height // 2
            )
                         ),
            ChooseButton(ai_game, "Hard", (
                ai_game.settings.screen_width * 0.55,
                ai_game.settings.screen_height // 2
            )
                        )
        ]
        self.title = ChooseButton(ai_game, "Выберите уровень сложности:", (
                ai_game.settings.screen_width * 0.43,
                ai_game.settings.screen_height * 0.3
            )
        )

    def draw_buttons(self):
        """Рисует кнопки выбора."""
        for level in self.levels:
            level.draw_button()

    def draw_title(self):
        """Рисует заголовок."""
        self.title.draw_button()
