import os


class GameStatus:
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings

        # Игра Alien Invasion запускается в неактивном состоянии.
        self.game_active = False
        self.choosing_active = False

        # Инициализирует статистику, изменяющуюся в ходе игры.
        self.ships_left = self.settings.ship_limit
        self.score = 0

        # Рекорд не должен сбрасываться.
        self.high_score = 0
        self.download_results()

        self.level = 1

    def reset_status(self):
        """Сбрасывает количество жизней корабля."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def download_results(self):
        """Загружает максимальный рекорд."""
        if os.stat("files/data.txt").st_size != 0:
            with open("files/data.txt", "r") as file:
                self.high_score = int(file.readlines()[0])

    def save_results(self):
        """Сохраняет максимальный рекорд."""
        if os.stat("files/data.txt").st_size != 0:
            with open("files/data.txt", "r") as file:
                data = int(file.readlines()[0])
        else:
            data = 0
        new_data = self.high_score
        with open("files/data.txt", "w") as file:
            file.write(str(new_data if new_data > data else data))
