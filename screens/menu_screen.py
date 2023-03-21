import pygame
from utils.constants import SCREEN as S
from screens.screen import Screen


class MenuScreen(Screen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.title_params = self.rect_params | {
            "x": "center",
            "y": S.TITLE_Y,
            "font_size": 100,
            "text_color": "green",
        }
        self.button_sections, self.texts = [], []
        self.hovered_button = None
        self.button_key_pos = (0, 0)

    def process_events(self):
        for event in pygame.event.get():
            self.handle_quit_event(event)
            # Mouse Controls
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                for section in self.button_sections:
                    for button in section:
                        if button.is_on_mouse(pos):
                            self.handle_hover(button)
                        else:
                            self.handle_unhover(button)
            elif event.type == pygame.MOUSEBUTTONUP:
                self.handle_click(self.hovered_button)

                # Keyboard Controls
            elif event.type == pygame.KEYDOWN:
                # Find Button hovered and get pos, if none (0,0)
                for i, section in enumerate(self.button_sections):
                    for j, button in enumerate(section):
                        if self.hovered_button == button:
                            self.button_key_pos = (i, j)
                            break
                # Hover when move key pressed
                if event.key == pygame.K_UP:
                    self.move_up()
                elif event.key == pygame.K_DOWN:
                    self.move_down()
                elif event.key == pygame.K_LEFT:
                    self.move_left()
                elif event.key == pygame.K_RIGHT:
                    self.move_right()
                # Select if enter
                elif event.key == pygame.K_RETURN:
                    self.handle_click(self.hovered_button)

    def update(self):
        for text in self.texts:
            text.update()
        for section in self.button_sections:
            for button in section:
                button.update()

    def draw(self):
        super().draw()
        for text in self.texts:
            text.draw(self.screen)
        for section in self.button_sections:
            for button in section:
                button.draw(self.screen)

    def handle_hover(self, button):
        self.hovered_button = button
        button.hover()

    def handle_unhover(self, button):
        if self.hovered_button == button:
            self.hovered_button = None
        button.unhover()

    def handle_click(self, button):
        pass

    def handle_key_hover(self, x, y):
        self.button_key_pos = (x, y)
        if self.hovered_button is not None:
            self.hovered_button.unhover()
        self.hovered_button = self.button_sections[x][y]
        self.hovered_button.hover()

    def move_up(self):
        x, y = self.button_key_pos
        x = (x - 1) % len(self.button_sections)
        self.handle_key_hover(x, y)

    def move_down(self):
        x, y = self.button_key_pos
        x = (x + 1) % len(self.button_sections)
        self.handle_key_hover(x, y)

    def move_left(self):
        x, y = self.button_key_pos
        y = (y - 1) % len(self.button_sections[x])
        self.handle_key_hover(x, y)

    def move_right(self):
        x, y = self.button_key_pos
        y = (y + 1) % len(self.button_sections[x])
        self.handle_key_hover(x, y)
