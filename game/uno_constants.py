COLORS = ["red", "yellow", "green", "blue"]
ALL_COLORS = COLORS + ["black"]
NUMBERS = list(range(10)) + list(range(1, 10))
COLOR_ACTION_VALUES = ["skip", "reverse", "draw2"]
WILD_ACTION_VALUES = ["color_change", "draw4", "bonus", "reload"]
CARD_ABBREVIATIONS = {
    "skip": "S",
    "reverse": "R",
    "draw2": "+2",
    "draw4": "+4",
    "color_change": "C",
    "reload": "L",
    "bonus": "$",
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
