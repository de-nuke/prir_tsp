import math


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def rgb(pos):
    r = g = b = 0
    temperature = (pos + 1) / 10 * 255
    if temperature <= 127:
        r = temperature * 2
        g = 255
    else:
        r = 255
        g = (255 - temperature) * 2

    sr = '{:02x}'.format(int(r))
    sg = '{:02x}'.format(int(g))
    sb = '{:02x}'.format(int(b))
    return '#' + sr + sg + sb
