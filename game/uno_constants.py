COLORS = ["red", "yellow", "green", "blue"]
ALL_COLORS = COLORS + ["black"]
NUMBERS = list(range(10)) + list(range(1, 10))
COLOR_ACTION_VALUES = ["skip", "reverse", "draw2", "reload"]
WILD_ACTION_VALUES = ["color_change", "draw4", "alpha"]
CARD_ABBREVIATIONS = {
    "skip": "S",
    "reverse": "RV",
    "draw2": "+2",
    "draw4": "+4",
    "color_change": "CC",
    "reload": "RL",
    "alpha": "&",
}
CARD_VALUES = {
    "skip": 20,
    "reverse": 20,
    "draw2": 20,
    "color_change": 50,
    "draw4": 50,
    "give": 50,
    "reload": 50,
}
