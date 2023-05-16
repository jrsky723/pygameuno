import json
import pygame

DEFAULT_OPTIONS = {
    "screen_size": "medium",
    "color_blind": False,
    "sound": {
        "volume": 10,
        "music": 10,
        "effects": 10,
    },
    "key_bindings": {
        "up": "up",
        "down": "down",
        "left": "left",
        "right": "right",
        "return": "return",
        "draw": "d",
        "escape": "escape",
        "uno": "u",
    },
}


def load_options_json():
    try:
        with open("options.json", "r") as f:
            options = json.load(f)
        validate_options(options)
        save_options_json(options)
    except Exception:
        options = DEFAULT_OPTIONS
        save_options_json(options)
    return options


def validate_options(options):
    validate_key(options)
    validate_value(options)


def validate_value(options):
    if options["screen_size"] not in ["small", "medium", "large"]:
        options["screen_size"] = "medium"
    for value in options["sound"]:
        if options["sound"][value] not in range(0, 11):
            options["sound"][value] = 10
    if options["color_blind"] not in [True, False]:
        options["color_blind"] = False
    for key in options["key_bindings"]:
        try:
            pygame.key.key_code(options["key_bindings"][key])
        except Exception:
            options["key_bindings"][key] = DEFAULT_OPTIONS["key_bindings"][key]


def validate_key(options):
    for key, value in options.items():
        if key not in DEFAULT_OPTIONS:
            options.pop(key)

    for key, value in DEFAULT_OPTIONS.items():
        if key not in options:
            options[key] = value

    for key, value in options["key_bindings"].items():
        if key not in DEFAULT_OPTIONS["key_bindings"]:
            options["key_bindings"].pop(key)

    for key, value in DEFAULT_OPTIONS["key_bindings"].items():
        if key not in options["key_bindings"]:
            options["key_bindings"][key] = value


def save_options_json(options):
    with open("options.json", "w") as f:
        json.dump(options, f)
