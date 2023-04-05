import pygame
from utils.constants import SCREEN as S
from screens.screen import Screen


class MenuScreen(Screen):
    def __init__(self, screen, options):
        super().__init__(screen, options)
        self.title_params = self.rect_params | {
            "x": "center",
            "y": S.TITLE_Y,
            "font_size": 80,
            "text_color": "green",
        }
        self.button_sections, self.texts = [], []
        self.hovered_button = None
        self.button_key_pos = None

    def find_hovered_button(self, pos):
        for i, section in enumerate(self.button_sections):
            for j, button in enumerate(section):
                if button.is_on_mouse(pos):
                    self.button_hover(button)
                    self.button_key_pos = (i, j)
                else:  # If not hovered, unhover
                    self.button_unhover(button)

    def handle_mouse_event(self, event):
        # Mouse MOTION
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            self.find_hovered_button(pos)
        # Mouse CLICKS
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.button_click_down(self.hovered_button)
        elif event.type == pygame.MOUSEBUTTONUP:
            self.button_click_up(self.hovered_button)

    def handle_key_event(self, event):
        if event.type == pygame.KEYDOWN:
            self.handle_movement(event)
            self.handle_return_down(event)
        elif event.type == pygame.KEYUP:
            self.handle_return_up(event)

    def move_up(self):
        x = self.button_key_pos[0] - 1 if self.button_key_pos is not None else 0
        self.change_key_cursor(x, 0)

    def move_down(self):
        x = self.button_key_pos[0] + 1 if self.button_key_pos is not None else 0
        self.change_key_cursor(x, 0)

    def move_left(self):
        x = self.button_key_pos[0] if self.button_key_pos is not None else 0
        y = self.button_key_pos[1] - 1 if self.button_key_pos is not None else 0
        self.change_key_cursor(x, y)

    def move_right(self):
        x = self.button_key_pos[0] if self.button_key_pos is not None else 0
        y = self.button_key_pos[1] + 1 if self.button_key_pos is not None else 0
        self.change_key_cursor(x, y)

    def return_down(self):
        self.button_click_down(self.hovered_button)

    def return_up(self):
        self.button_click_up(self.hovered_button)

    def change_key_cursor(self, x, y):
        x, y = self.key_bound_check(x, y)
        self.button_key_pos = (x, y)
        if self.hovered_button is not None:
            self.hovered_button.unhover()
        self.hovered_button = self.button_sections[x][y]
        self.hovered_button.hover()

    def key_bound_check(self, x, y):
        x = x % len(self.button_sections)
        y = y % len(self.button_sections[x])
        return x, y

    def update(self):
        super().update()
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

    def button_hover(self, button):
        self.hovered_button = button
        button.hover()

    def button_unhover(self, button):
        if self.hovered_button == button:
            self.hovered_button = None
            self.button_key_pos = None
        button.unhover()

    def button_click_down(self, button):
        button.click() if button else None

    def button_click_up(self, button):
        if button is not None:
            button.unclick()
            if button.text == "BACK":
                self.back()
