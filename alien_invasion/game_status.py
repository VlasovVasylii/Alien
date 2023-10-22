class GameStatus:
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False

        # Инициализирует статистику, изменяющуюся в ходе игры.
        self.ships_left = self.settings.ship_limit

    def reset_status(self):
        """Сбрасывает количество жизней корабля."""
        self.ships_left = self.settings.ship_limit
