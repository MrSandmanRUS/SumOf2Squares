import math


def above(r, diff, x, y, x_list, y_list):
    if y > x:
        return
    elif y * y < diff:
        above(r, diff, x, y + 1, x_list, y_list)
    elif y * y == diff:
        x_list.append(x)
        y_list.append(y)
        between(r, x - 1, y + 1, x_list, y_list)
    else:
        between(r, x - 1, y, x_list, y_list)


def between(r, x, y, x_list, y_list):
    diff = r - x * x
    above(r, diff, x, y, x_list, y_list)


def squares(r):
    x_list = []
    y_list = []
    first_x = int(math.sqrt(r))
    between(r, first_x, 0, x_list, y_list)
    return x_list, y_list


x_list, y_list = squares(1105)
print("x_list = ", x_list)
print("y_list = ", y_list)