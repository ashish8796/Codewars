import math
circle_radius, number_of_sides = 3, 3


def area_of_polygon_inside_circle(circle_radius, number_of_sides):
    area = .5 * number_of_sides * circle_radius**2 * math.sin((2*math.pi)/number_of_sides)
    return float("%.3f" % round(area, 3))


print(area_of_polygon_inside_circle(circle_radius, number_of_sides))