class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует статические настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (222, 222, 222)

        # Настройки корабля
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_width = 4
        self.bullet_height = 7
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Настройки пришельцев
        self.fleet_drop_speed = 10

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5

        # Инициализирует настройки, изменяющиеся в ходе игры.
        self.ship_speed_factor = 0.4
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.1

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Подсчёт очков.
        self.alien_points = 10
        self.alien_points_factor = 1

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 0.4
        self.bullet_speed_factor = 0.5
        self.alien_speed_factor = 0.1

        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1

        # Подсчёт очков.
        self.alien_points = 10

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def change_level(self, level):  # Установка уровня сложности(0 - нормальный,
        # 1 - сложный).
        if level == 0:
            self.ship_limit = 3
            self.speedup_scale = 1.1
            self.alien_points = 10
            self.score_scale = 1.5

        else:
            self.ship_limit = 1
            self.speedup_scale = 1.25
            self.alien_points = 15
            self.score_scale = 2
