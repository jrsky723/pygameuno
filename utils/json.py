import pygame
import json
import os

JSON_PATH = os.path.join(os.path.dirname(__file__), "..", "jsons")


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


DEFAULT_ACHIEVEMENTS = {
    "single player mode": {
        "wins": 0,
        "story mode": {
            "red": 0,
            "green": 0,
            "yellow": 0,
            "blue": 0,
        },
        "in game": {
            "wins with in 10 turns": 0,
            "wins with no function card": 0,
            "wins with no actiion card": 0,
        },
    }
}

DEFAULT_JSON = {
    "options": DEFAULT_OPTIONS,
    "achievements": DEFAULT_ACHIEVEMENTS,
}


def load_json(json_name):
    try:
        with open(os.path.join(JSON_PATH, json_name + ".json"), "r") as f:
            data = json.load(f)
            if json_name == "options":
                data = validate_json_keys(data, DEFAULT_JSON["options"])
                data = validate_options_value(data)
            elif json_name == "achievements":
                data = validate_json_keys(data, DEFAULT_JSON["achievements"])
                data = validate_achievements_value(data)
            save_json(json_name, data)
    except Exception:
        data = DEFAULT_JSON[json_name.split(".")[0]]
        save_json(json_name, data)
    return data


def save_json(json_name, data):
    if not os.path.exists(JSON_PATH):
        os.makedirs(JSON_PATH)
    with open(os.path.join(JSON_PATH, json_name + ".json"), "w") as f:
        json.dump(data, f)


### options.json


def validate_json_keys(target_json, default_json):
    corrected_json = {}  # 수정된 객체를 저장할 새 딕셔너리

    all_keys = set(default_json.keys()).union(target_json.keys())

    for key in all_keys:
        if key in corrected_json:
            # 이미 검사한 키는 무시하고 다음 키로 넘어갑니다.
            continue
        if key in target_json and key in default_json:
            if isinstance(default_json[key], dict) and isinstance(
                target_json[key], dict
            ):
                corrected_value = validate_json_keys(
                    target_json[key], default_json[key]
                )
                corrected_json[key] = corrected_value
            elif isinstance(default_json[key], dict):
                corrected_json[key] = default_json[key]
            else:
                corrected_json[key] = target_json[key]
        elif key in default_json:
            corrected_json[key] = default_json[key]
        else:
            continue

    # corrected_json의 키의 순서를 default_json의 키의 순서와 동일하게 만듭니다.
    corrected_json = {key: corrected_json[key] for key in default_json.keys()}

    return corrected_json


def validate_options_value(options):
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
            options["key_bindings"][key] = DEFAULT_JSON["options"]["key_bindings"][key]

    return options


### achievements.json


def validate_achievements_value(achievements):
    # check all values in achievements are unsigned int, if value is dict, check it recursively
    for key in achievements:
        if isinstance(achievements[key], dict):
            achievements[key] = validate_achievements_value(achievements[key])
        elif not isinstance(achievements[key], int) or achievements[key] < 0:
            achievements[key] = 0
    return achievements
