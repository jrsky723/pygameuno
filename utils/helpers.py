import os
import pygame
import json

# Image helper functions


def load_image(file_path):
    full_path = os.path.join("assets", file_path)
    return pygame.image.load(full_path).convert_alpha()


# Options helper functions


def load_options():
    try:
        with open("options.json", "r") as f:
            options = json.load(f)
        options = validate_options(options)
    except FileNotFoundError:
        options = {
            "screen_size": "small",
            "volume": 100,
            "color_blind": False,
        }
        save_options(options)
    return options


def validate_options(options):
    if options["screen_size"] not in {"small", "medium", "large"}:
        options["screen_size"] = "small"
    if not 0 <= options["volume"] <= 100:
        options["volume"] = 100
    if not isinstance(options["color_blind"], bool):
        options["color_blind"] = False
    save_options(options)
    return options


def save_options(options):
    with open("options.json", "w") as f:
        json.dump(options, f)
