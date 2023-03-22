import json
import pygame

default_options = {
    "screen_size": "medium",
    "volume": 10,
    "color_blind": False,
    "key_bindings": {
        "up": "up",
        "down": "down",
        "left": "left",
        "right": "right",
        "return": "return",
    },
}


def load_options_json():
    try:
        with open("options.json", "r") as f:
            options = json.load(f)
        validate_options(options)
        save_options_json(options)
    except Exception:
        options = default_options
        save_options_json(options)
    return options


def validate_options(options):
    validate_key(options)
    validate_value(options)


def validate_value(options):
    if options["screen_size"] not in ["small", "medium", "large"]:
        options["screen_size"] = "medium"
    if options["volume"] not in range(0, 11):
        options["volume"] = 10
    if options["color_blind"] not in [True, False]:
        options["color_blind"] = False
    for key in options["key_bindings"]:
        try:
            pygame.key.key_code(options["key_bindings"][key])
        except Exception:
            options["key_bindings"][key] = default_options["key_bindings"][key]


def validate_key(options):
    for key, value in options.items():
        if key not in default_options:
            options.pop(key)

    for key, value in default_options.items():
        if key not in options:
            options[key] = value

    for key, value in options["key_bindings"].items():
        if key not in default_options["key_bindings"]:
            options["key_bindings"].pop(key)

    for key, value in default_options["key_bindings"].items():
        if key not in options["key_bindings"]:
            options["key_bindings"][key] = value


def save_options_json(options):
    with open("options.json", "w") as f:
        json.dump(options, f)
