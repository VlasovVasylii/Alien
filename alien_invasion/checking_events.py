import pygame
import sys
from models.bullet import Bullet


class CheckEvents:

    def __init__(self, ai_game):
        """Инициализирует проверку событий."""
        self.ai_game = ai_game

    def check_events(self):
        """Обрабатывает нажатия клавиш и события мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.ai_game.status.save_results()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not self.ai_game.status.choosing_active:
                    self._check_play_button(mouse_pos)
                else:
                    self._choosing_level(mouse_pos)

    def _check_keydown_events(self, event):
        """Реагирует на нажатие клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ai_game.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ai_game.ship.moving_left = True
        elif event.key == pygame.K_q:
            self.ai_game.status.save_results()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()

    def _check_keyup_events(self, event):
        """Реагирует на опускание клавиш."""
        if event.key == pygame.K_RIGHT:
            self.ai_game.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ai_game.ship.moving_left = False

    def fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets."""
        if self.ai_game.status.game_active:
            if len(self.ai_game.bullets) < self.ai_game.settings.bullet_allowed:
                new_bullet = Bullet(self.ai_game)
                self.ai_game.bullets.add(new_bullet)

    def _check_play_button(self, mouse_pos):
        """Запускает новую игру при нажатии кнопки Play."""
        button_clicked = self.ai_game.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.ai_game.status.game_active:
            # Запускает процесс выбора уровня сложности.
            self.ai_game.status.choosing_active = True

    def _choosing_level(self, mouse_pos):
        """Создаёт возможность выбора уровня сложности."""
        if not self.ai_game.status.game_active:
            for ind, button in enumerate(self.ai_game.choose_levels.levels):
                button_clicked = button.rect.collidepoint(mouse_pos)
                if button_clicked:
                    # Сброс игровых настроек.
                    self.ai_game.settings.initialize_dynamic_settings()
                    self.ai_game.settings.change_level(ind)
                    self.start_game()

    def prep_images(self):
        """Подготавливает изображения score_board."""
        self.ai_game.score_board.prep_score()
        self.ai_game.score_board.prep_level()
        self.ai_game.score_board.prep_ships()
        self.ai_game.score_board.prep_high_score()

    def start_game(self):
        """Запускает новую игру после выбора уровня сложности."""
        # Сброс игровой статистики.
        self.ai_game.status.reset_status()
        self.ai_game.status.game_active = True
        self.ai_game.status.choosing_active = False
        self.prep_images()

        # Очистка списка пришельцев и снарядов.
        self.ai_game.aliens.empty()
        self.ai_game.bullets.empty()

        # Создание нового флота и размещение корабля в центре.
        self.ai_game.create_fleet()
        self.ai_game.ship.center_ship()

        # Указатель мыши скрывается.
        pygame.mouse.set_visible(False)
