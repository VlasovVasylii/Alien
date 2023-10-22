class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (222, 222, 222)

        # Настройки корабля
        self.ship_speed = 0.4
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_speed = 1
        self.bullet_width = 4
        self.bullet_height = 7
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # Настройки пришельцев
        self.alien_speed = 0.1
        self.fleet_drop_speed = 20
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
