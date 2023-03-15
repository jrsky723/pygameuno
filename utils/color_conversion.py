def darken_color(color, amount):
    return tuple([max(0, c * amount) for c in color])
