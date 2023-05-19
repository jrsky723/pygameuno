import pygame
from game.uno_game import UnoGame
from game.story_mode.uno_game_yellow import UnoGameYellow
from game.story_mode.uno_game_blue import UnoGameBlue
from game.story_mode.uno_game_green import UnoGameGreen
from game.story_mode.uno_game_red import UnoGameRed
from screens.screen import Screen
from screens.menus.end_menu_ import EndMenuScreen
from screens.menus.paused_menu import PausedMenuScreen
from renders.card import Card
from renders.text_box import TextBox
from renders.button import Button
from renders.rect import Rect
from utils.timer import Timer
from utils.color_conversion import rgb
from animations.move_animation import MoveAnimation
from utils.constants import SCREEN as S, SIZE_RATIO as SR, SOUND, MUSIC
from game.uno_constants import COLORS
import copy, time


class GameScreen(Screen):
    def __init__(self, screen, clock, options, game_info):
        super().__init__(screen, clock, options)
        pygame.mixer.music.load(MUSIC.GAME_BACKGROUND)
        pygame.mixer.music.play(-1)
        self.max_players = 6
        self.game_info = game_info
        if game_info["mode"] == "story":
            if game_info["zone"] == "red_zone":
                self.game = UnoGameRed(game_info["players"])
            elif game_info["zone"] == "green_zone":
                self.game = UnoGameGreen(game_info["players"])
            elif game_info["zone"] == "blue_zone":
                self.game = UnoGameBlue(game_info["players"])
            elif game_info["zone"] == "yellow_zone":
                self.game = UnoGameYellow(game_info["players"])
        else:
            self.game = UnoGame(game_info["players"])
        self.my_player = self.game.get_player()
        self.coms = self.game.get_com_players()
        self.surfaces = []
        self.my_hand_surface = None
        self.board_surface = None
        self.com_hand_surfaces = []
        self.pos = {
            "discard": (500, 200),
            "deck": (300, 200),
            "my_hand": (0, S.HEIGHT_BASE * (7 / 10)),
            "com_hand": (S.WIDTH_BASE * (3 / 4), 0),
            "com_hand_gap": (S.HEIGHT_BASE / 5),
        }

        # Board
        self.uno_button = None
        self.deck_render = None
        self.message_box = None

        # message_box
        self.message_timer = Timer()
        self.message_time = 2

        # color_picker
        self.color_picker_on = False
        self.color_picker_buttons = []
        self.color_picker_text = None
        self.hovered_color_picker_button_idx = None
        self.hovered_color_picker_button = None

        self.card_renders = []
        self.animation_card_renders = []

        #  hover, click
        self.my_hand_card_renders = []

        # handling turns
        self.turn_started = False
        self.turn_timer = Timer()
        self.my_turn_time, self.com_turn_time = 20, 2

        # handling game event
        # TODO: show direction in screen
        self.direction = self.game.get_direction()
        self.animations = []

        # sound
        self.sounds = {
            "card_move": pygame.mixer.Sound(SOUND.CARD_MOVE),
            "card_flip": pygame.mixer.Sound(SOUND.CARD_FLIP),
            "error": pygame.mixer.Sound(SOUND.ERROR),
            "uno": pygame.mixer.Sound(SOUND.UNO),
        }
        self.update_options()
        # card_selection
        self.hovered_card_render = None
        self.hovered_card_render_idx = None

        # create
        self.create_surfaces()
        self.create_board()

    # region Create functions

    def create_surfaces(self):
        self.board_surface_const = {
            "pos": (0, 0),
            "size": (self.screen_width * (3 / 4), self.screen_height * (7 / 10)),
        }
        self.my_hand_surface_const = {
            "pos": (0, self.screen_height * (7 / 10)),
            "size": (self.screen_width * (3 / 4), self.screen_height * (3 / 10)),
        }
        self.com_hand_surface_const = {
            "pos": (self.screen_width * (3 / 4), 0),
            "size": (self.screen_width / 4, self.screen_height / 5),
            "gap": (self.screen_height / 5),
        }
        self.my_hand_surface = pygame.Surface(self.my_hand_surface_const["size"])
        self.board_surface = pygame.Surface(self.board_surface_const["size"])
        self.com_hand_surfaces = []
        for _ in range(self.max_players - 1):
            self.com_hand_surfaces.append(
                pygame.Surface(self.com_hand_surface_const["size"])
            )
        self.surfaces = [
            self.my_hand_surface,
            self.board_surface,
        ] + self.com_hand_surfaces

    def create_hand_cards(self, screen_pos, player, is_me):
        x, y = screen_pos
        player_hand = player.get_hand()
        if is_me:
            C_WIDTH, C_HEIGHT, C_X, C_Y = 80, 110, x + 80, y + 70
            if len(player_hand) > 7:
                C_GAP = C_WIDTH * 1.1 / (len(player_hand) / 7)
            else:
                C_GAP = C_WIDTH * 1.1
            FONT_SIZE = 38
        else:
            C_WIDTH, C_HEIGHT, C_X, C_Y = 40, 60, x + 30, y + 50
            if len(player_hand) > 7:
                C_GAP = C_WIDTH * 0.6 / (len(player_hand) / 7)
            else:
                C_GAP = C_WIDTH * 0.6
            FONT_SIZE = 20
        card_params = {
            "width": C_WIDTH,
            "height": C_HEIGHT,
            "y": C_Y,
            "face_up": True,
            "font_size": FONT_SIZE,
        } | self.rect_params

        for i, card in enumerate(player_hand):
            card_params["x"] = C_X + i * C_GAP
            card_render = Card(
                **card_params,
                card=card,
            )
            self.card_renders.append(card_render)
            if is_me:
                self.my_hand_card_renders.append(card_render)

        next_card_pos = (C_X + (len(player_hand)) * C_GAP, C_Y)
        next_card_pos_repositioned = tuple(
            x * SR[self.screen_size] for x in next_card_pos
        )
        player.set_next_card_pos(next_card_pos_repositioned)

    def create_card_renders(self):
        self.card_renders, self.my_hand_card_renders = [], []
        # My hand
        self.create_hand_cards(self.pos["my_hand"], self.my_player, True)
        # com hands
        for i, com in enumerate(self.coms):
            self.create_hand_cards(
                (
                    self.pos["com_hand"][0],
                    self.pos["com_hand"][1] + i * self.pos["com_hand_gap"],
                ),
                com,
                False,
            )
        # top discard card
        if self.game.top_discard_card() is not None:
            top_discard_card_render = Card(
                x=self.pos["discard"][0],
                y=self.pos["discard"][1],
                width=80,
                height=110,
                face_up=True,
                card=self.game.top_discard_card(),
                **self.rect_params,
            )
            self.card_renders.append(top_discard_card_render)

    ## Create board functions

    def create_top_discard_card_color(self):
        self.top_discard_card_color = Rect(
            x=650,
            y=200,
            width=50,
            height=50,
            background_color="dark_gray",
            border_width=3,
            **self.rect_params,
        )

    def create_uno_button(self):
        self.uno_button = Button(
            x=650,
            y=270,
            width=70,
            height=40,
            background_color="white",
            text="UNO",
            font_size=20,
            text_color="black",
            hover_background_color="darken",
            **self.rect_params,
        )

    def create_deck_render(self):
        self.deck_render = Rect(
            x=self.pos["deck"][0],
            y=self.pos["deck"][1],
            width=80,
            height=110,
            background_color="black",
            border_width=3,
            **self.rect_params,
        )

    def create_color_picker(self):
        self.color_picker_text = TextBox(
            x=350,
            y=380,
            font_size=20,
            text="Pick a color",
            **self.rect_params,
        )

        for i, color in enumerate(COLORS):
            self.color_picker_buttons.append(
                Button(
                    x=350 + i * 60,
                    y=410,
                    width=50,
                    height=50,
                    background_color=color,
                    border_width=3,
                    hover_background_color="darken",
                    **self.rect_params,
                )
            )

    def create_message_box(self):
        self.message_box = TextBox(
            x=350,
            y=80,
            font_size=30,
            text="",
            **self.rect_params,
        )

    def create_board(self):
        self.create_uno_button()
        self.create_deck_render()
        self.create_color_picker()
        self.create_message_box()

    # endregion

    # region Draw functions

    ## Draw player functions

    def draw_players(self):
        self.draw_player(self.my_hand_surface, self.my_player, is_me=True)
        for i, com in enumerate(self.coms):
            self.draw_player(self.com_hand_surfaces[i], com, is_me=False)

    def draw_player(self, surface, player, is_me):
        FONT_SIZE = 35 if is_me else 20
        text_params = {"font_size": FONT_SIZE, "reposition": False} | self.rect_params
        self.draw_player_turn(surface, player.get_is_turn())
        self.draw_player_name(surface, player.name, text_params)
        self.draw_player_card_number(surface, len(player.hand), text_params)
        if player.is_turn:
            self.draw_turn_timer(surface, text_params)
        pass

    def draw_player_turn(self, surface, is_turn):
        # draw turn indicator
        if is_turn:
            pygame.draw.rect(
                surface,
                "red",
                (
                    0,
                    0,
                    surface.get_width(),
                    surface.get_height(),
                ),
                3,
            )

    def draw_player_name(self, surface, player_name, text_params):
        S_HEIGHT = surface.get_height()
        player_name_text = TextBox(
            text=player_name, x=13, y=S_HEIGHT * 0.1, **text_params
        )
        player_name_text.draw(surface)

    def draw_player_card_number(self, surface, card_number, text_params):
        S_WIDTH, S_HEIGHT = surface.get_width(), surface.get_height()
        card_number_text = TextBox(
            text=f"[{card_number}]",
            x=S_WIDTH * 0.8,
            y=S_HEIGHT * 0.1,
            **text_params,
        )
        card_number_text.draw(surface)

    def draw_turn_timer(self, surface, text_params):
        S_WIDTH, S_HEIGHT = surface.get_width(), surface.get_height()
        timer_text = TextBox(
            text=f"{1+int(self.turn_timer.get_remaining_time())}",
            x=S_WIDTH * 0.8,
            y=S_HEIGHT * 0.4,
            **text_params,
        )
        timer_text.draw(surface)

    def draw_board(self):
        self.draw_top_discard_card_color(self.board_surface, self.game.get_top_color())
        self.uno_button.draw(self.board_surface)
        self.deck_render.draw(self.board_surface)
        self.message_box.draw(self.board_surface)
        if self.color_picker_on:
            self.draw_color_picker(self.board_surface)

    def draw_color_picker(self, surface):
        self.color_picker_text.draw(surface)
        for button in self.color_picker_buttons:
            button.draw(surface)

    def draw_top_discard_card_color(self, surface, color):
        rect_render = Rect(
            x=650,
            y=200,
            width=50,
            height=50,
            background_color=color if color is not None else "dark_gray",
            border_width=3,
            **self.rect_params,
        )
        rect_render.draw(surface)

    def draw_surfaces(self):
        # blit surfaces
        self.screen.blit(self.my_hand_surface, self.my_hand_surface_const["pos"])
        self.screen.blit(self.board_surface, self.board_surface_const["pos"])
        for i, com_surface in enumerate(self.com_hand_surfaces):
            self.screen.blit(
                com_surface,
                (
                    self.com_hand_surface_const["pos"][0],
                    i * self.com_hand_surface_const["gap"],
                ),
            )
        # fill surfaces & add inner border
        for surface in self.surfaces:
            surface.fill(self.background_color)
            self.add_inner_border(surface, rgb("white"), 3)

    def add_inner_border(self, surface, color, width):
        pygame.draw.rect(
            surface,
            color,
            (0, 0, surface.get_width(), surface.get_height()),
            width,
        )

    def draw_card_renders(self):
        for card_render in self.card_renders:
            card_render.draw(self.screen)
        if self.hovered_card_render is not None:
            self.hovered_card_render.draw(self.screen)

    def draw_animations(self):
        for animation in self.animations:
            animation.draw(self.screen)

    def draw(self):
        super().draw()
        self.draw_surfaces()
        self.draw_board()
        self.draw_players()
        self.draw_card_renders()
        self.draw_animations()

    # endregion

    # region Main Loop
    def main_loop(self):
        super().main_loop()

    def run(self):
        try:
            self.start_game()
        except Exception as e:
            print(e)
        super().run()

    def update(self):
        super().update()
        self.game.set_game_time(time.time())
        self.update_animations_finished()
        for card_render in self.card_renders:
            card_render.update()
        self.update_hovered_card_render()
        if self.color_picker_on:
            self.update_color_picker_button()

    # endregion

    # Events
    def process_events(self):
        super().process_events()
        if self.turn_timer.is_finished():
            self.game.turn_time_out()
            self.end_turn()
        self.add_game_animations()
        if self.animations:
            self.turn_timer.pause()
            return
        self.turn_timer.resume()
        self.process_game_events()
        if self.message_timer.is_finished():
            self.hide_message()

    # region Animations
    def add_game_animations(self):
        for info in self.game.get_animation_infos():
            if info["type"] == "card_move":
                self.add_card_move_animation(info)
        self.game.set_animation_infos([])
        self.create_card_renders()

    def add_card_move_animation(self, info):
        obj = self.find_card_render(info["card"])
        src_pos = (obj.x, obj.y)
        dest_pos = self.find_dest_pos(info["dest"])
        self.animations.append(
            MoveAnimation(
                obj=obj,
                src_pos=src_pos,
                dest_pos=dest_pos,
                duration=info["duration"],
                delay=info["delay"],
                move_info=info,
            )
        )

    def find_card_render(self, card):
        for card_render in self.card_renders:
            if card_render.card == card:
                return card_render
        deck_render_copy = copy.deepcopy(self.deck_render)
        self.animation_card_renders.append(deck_render_copy)
        return deck_render_copy

    def card_move_animation_update(self, animation):
        info = animation.move_info
        animation.set_dest_pos(self.find_dest_pos(info["dest"]))

    def find_dest_pos(self, dest):
        if dest == "deck":
            return self.update_pos(self.pos["deck"])
        elif dest == "discard":
            return self.update_pos(self.pos["discard"])
        elif dest.startswith("player"):
            if dest == "player_0":
                return self.my_player.get_next_card_pos()
            else:
                return self.coms[int(dest[-1]) - 1].get_next_card_pos()

    def update_pos(self, pos):
        result = tuple(x * SR[self.screen_size] for x in pos)
        return result

    def update_animations_finished(self):
        animations = []
        for i, animation in enumerate(self.animations):
            if i != 0:
                animation.set_start_time(self.animations[i - 1].get_start_time())
            if animation.__class__.__name__ == "MoveAnimation":
                if animation.move_info["type"] == "card_move":
                    self.card_move_animation_update(animation)
            animation.update()
            if animation.is_delay_finished() and not animation.get_sound_played():
                self.play_animation_sound(animation)
            if animation.is_finished():
                self.game.update_by_animtaion_info(animation.move_info)
            else:
                animations.append(animation)
        self.animations = animations

    # endregion

    def process_game_events(self):
        for event_info in self.game.get_game_event_infos():
            if event_info["type"] == "player_win":
                self.game_over()
            if event_info["type"] == "color_change_request":
                self.color_picker_on = True
            if event_info["type"] == "uno_called":
                self.show_message(
                    f"{event_info['value'].get_name()} called uno!",
                    time=self.message_time,
                )
        self.game.set_game_event_infos([])

        game_time = self.game.get_game_time()
        for uno_called_time in self.game.get_uno_called_times():
            if uno_called_time["time"] < game_time:
                self.game.uno_called(uno_called_time["player"])
                break

    def show_message(self, message, time=1):
        self.message_timer.set_timer(time)
        self.message_timer.start()
        self.message_box.set_text(message)
        self.message_box.set_visible(True)

    def hide_message(self):
        self.message_box.set_visible(False)
        self.message_timer.reset()

    # region game events
    def start_game(self):
        self.game.start_game()
        self.my_turn()

    def my_turn(self):
        self.turn_timer.set_timer(self.my_turn_time)
        self.turn_timer.start()

    def com_turn(self):
        self.turn_timer.set_timer(self.com_turn_time)
        self.turn_timer.start()

    def end_turn(self):
        self.game.next_turn()
        current_player = self.game.get_current_player()
        if not self.game.check_uno_called(current_player):
            self.show_message(
                f"{current_player.get_name()} didn't call uno!",
                time=self.message_time,
            )
            self.end_turn()
        if self.game.get_current_player() == self.my_player:
            self.my_turn()
        else:
            self.com_turn()

    def game_over(self):
        self.running = False
        end_menu_screen = EndMenuScreen(
            self.screen, self.clock, self.options, self.game.get_winner()
        )
        end_menu_screen.run()

    # endregion

    # Sound
    def play_animation_sound(self, animation):
        animation.set_sound_played(True)
        # CHECK ANIMATION CLASS NAME
        if animation.__class__.__name__ == "MoveAnimation":
            self.sounds["card_move"].play()

    # region User Input

    ## mouse Input
    def handle_mouse_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            pos = event.pos
            self.find_hoverd_card_idx(pos)
            self.handle_uno_button_hover(pos)
            if self.color_picker_on:
                self.find_hovered_color_picker_button_idx(pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_click(event)

    def handle_uno_button_hover(self, pos):
        if self.uno_button.is_on_mouse(pos):
            self.uno_button.hover()
            self.uno_button.update()
        else:
            self.uno_button.unhover()
            self.uno_button.update()

    def find_hoverd_card_idx(self, pos):
        for i, card_render in enumerate(self.my_hand_card_renders):
            if card_render.is_on_mouse(pos):
                self.hovered_card_render_idx = i
                return
        self.hovered_card_render_idx = None

    def find_hovered_color_picker_button_idx(self, pos):
        for i, button in enumerate(self.color_picker_buttons):
            if button.is_on_mouse(pos):
                self.hovered_color_picker_button_idx = i
                return
        self.hovered_color_picker_button_idx = None

    def handle_mouse_click(self, event):
        if self.animations:
            return
        if self.uno_button.is_on_mouse(event.pos):
            self.uno()
        if self.color_picker_on:
            if self.hovered_color_picker_button_idx is not None:
                self.color_pick(self.hovered_color_picker_button_idx)
        else:
            if self.hovered_card_render:
                self.card_play(self.hovered_card_render)
            if self.deck_render.is_on_mouse(event.pos):
                self.draw_card_from_deck()

    def escape(self):
        pause_screen = PausedMenuScreen(self.screen, self.clock, self.options)
        pause_screen_options = pause_screen.run()
        self.options = pause_screen_options
        self.update_options()
        self.create_surfaces()
        self.create_board()

    def uno(self):
        is_uno = self.game.uno_called(self.my_player)
        if is_uno:
            self.sounds["uno"].play()
        else:
            self.sounds["error"].play()

    def color_pick(self, idx):
        color = COLORS[idx]
        self.game.set_top_color(color)
        self.color_picker_on = False
        self.end_turn()

    def card_play(self, card_render):
        try:
            if self.game.get_current_player() == self.my_player:
                played = self.game.play_card(self.my_player, card_render.card)
                if played:
                    self.hovered_card_render = None
                    self.sounds["card_flip"].play()
                    if self.game.get_game_event_infos() == []:
                        self.end_turn()
                else:
                    self.sounds["error"].play()
        except Exception as e:
            print(e)

    def draw_card_from_deck(self):
        try:
            if self.game.get_current_player() == self.my_player:
                self.game.draw_card(self.my_player)
                self.end_turn()
                self.sounds["card_flip"].play()
        except Exception as e:
            print(e)

    def return_down(self):
        if self.color_picker_on:
            if self.hovered_color_picker_button_idx is not None:
                self.color_pick(self.hovered_color_picker_button_idx)
        elif self.hovered_card_render:
            self.card_play(self.hovered_card_render)

    def idx_left(self, idx):
        if idx is None or idx == 0:
            return 0
        else:
            return idx - 1

    def idx_right(self, idx, max_idx):
        if idx is None:
            return 0
        if idx < max_idx - 1:
            return idx + 1
        else:
            return idx

    def move_left(self):
        if self.color_picker_on:
            self.hovered_color_picker_button_idx = self.idx_left(
                self.hovered_color_picker_button_idx
            )
        else:
            self.hovered_card_render_idx = self.idx_left(self.hovered_card_render_idx)

    def move_right(self):
        if self.color_picker_on:
            self.hovered_color_picker_button_idx = self.idx_right(
                self.hovered_color_picker_button_idx, len(COLORS)
            )
        else:
            self.hovered_card_render_idx = self.idx_right(
                self.hovered_card_render_idx, len(self.my_hand_card_renders)
            )

    def update_hovered_card_render(self):
        if self.my_hand_card_renders == []:
            self.hovered_card_render_idx = None
            self.hovered_card_render = None
            return
        if self.hovered_card_render_idx is None:
            self.hovered_card_render = None
        else:
            if self.hovered_card_render_idx >= len(self.my_hand_card_renders):
                self.hovered_card_render_idx = len(self.my_hand_card_renders) - 1
            self.hovered_card_render = self.my_hand_card_renders[
                self.hovered_card_render_idx
            ]
            self.hovered_card_render.hover()
            self.hovered_card_render.update()

    def update_color_picker_button(self):
        for button in self.color_picker_buttons:
            button.unhover()
            button.update()
        if self.hovered_color_picker_button_idx is None:
            self.hovered_color_picker_button = None
        else:
            self.hovered_color_picker_button = self.color_picker_buttons[
                self.hovered_color_picker_button_idx
            ]
            self.hovered_color_picker_button.hover()
            self.hovered_color_picker_button.update()

    # endregion
