# add two fectors

import math


def vector_length_decomposite(length, angle):
    angle_rad = math.radians(angle)
    vector_length_x = length * math.cos(angle_rad)
    vector_length_y = length * math.sin(angle_rad)

    return {
        "vector_length_x": vector_length_x,
        "vector_length_y": vector_length_y
    }


length = float(input("Enter the vector's length: "))
angle = float(input("Enter the vector's angle: "))

result = vector_length_decomposite(length, angle)
print(result)
