# make red.svg, yellow.svg, green.svg by using each blue.svg in the each assets/cards folder
# and the color values are in card_vals.md
from bs4 import BeautifulSoup

blue_vals = {
    "linearGradient": ["rgb(74, 74, 208)", "rgb(83, 83, 157)", "rgba(0, 0, 0, 1)"],
    "radialGradient": ["rgb(255, 255, 255)", "rgb(170, 170, 225)"],
    "edge": ["rgba(55, 55, 150, 0.65)", "rgba(55, 55, 150, 0.35)"],
}

red_vals = {
    "linearGradient": ["rgb(208, 74, 74)", "rgb(157, 83, 83)", "rgba(0, 0, 0, 1)"],
    "radialGradient": ["rgb(255, 255, 255)", "rgb(225, 170, 170)"],
    "edge": ["rgba(150, 55, 55, 0.65)", "rgba(150, 55, 55, 0.35)"],
}

name_list = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "block",
    "buy-2",
    "buy-4",
    "change-color",
    "reverse",
]


# change each blue svg's color values to other colors
def change_color(card_name, color_name, color_vals):
    blue_file = f"assets/cards/{card_name}/blue.svg"
    with open(blue_file, "r") as f:
        soup = BeautifulSoup(f, "xml")
        # change linear Gradient colors
        linear_Gradient = soup.find("linearGradient")
        for i, stop in enumerate(linear_Gradient.find_all("stop")):
            stop["stop-color"] = color_vals["linearGradient"][i]
        # change radial Gradient colors
        radial_Gradient = soup.find("radialGradient")
        for i, stop in enumerate(radial_Gradient.find_all("stop")):
            stop["stop-color"] = color_vals["radialGradient"][i]
        # change edge's css colors
        style = soup.find("style")

    with open(f"assets/cards/{card_name}/{color_name}.svg", "w") as f:
        f.write(str(soup))


# add css to each svg file(add style tag)
def add_css(card_name, color_name):
    svg_file = f"assets/cards/{card_name}/{color_name}.svg"
    css_file = f"assets/css/{color_name}.css"
    with open(svg_file, "r") as f:
        soup = BeautifulSoup(f, "xml")
        style = soup.new_tag("style")
        with open(css_file, "r") as f:
            style.string = f.read()
        soup.svg.append(style)
    with open(svg_file, "w") as f:
        f.write(str(soup))


# def run():
#     for card_name in name_list:
#         change_color(red_vals, "red", card_name)
#         change_color(yellow_vals, "yellow", card_name)
#         change_color(green_vals, "green", card_name)
#         if card_name == "buy-4" or card_name == "change-color":
#             change_color(black_vals, "black", card_name)
def add_css_run():
    for card_name in name_list:
        add_css(card_name, "blue")
        add_css(card_name, "red")
        add_css(card_name, "yellow")
        add_css(card_name, "green")
        if card_name == "buy-4" or card_name == "change-color":
            add_css(card_name, "black")


if __name__ == "__main__":
    # run()
    add_css_run()
