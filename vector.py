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


def vector_add_sub(add_sub, length_1, angle_1, length_2, angle_2):
    if add_sub == "a":
        sign = 1
    elif add_sub == 's':
        sign = -1
    else:
        return ("Only can input A or S")

    angle_rad_1 = math.radians(angle_1)
    angle_rad_2 = math.radians(angle_2)

    vector_length_1_x = length_1 * math.cos(angle_rad_1)
    vector_length_1_y = length_1 * math.sin(angle_rad_1)
    vector_length_2_x = sign * length_2 * math.cos(angle_rad_2)
    vector_length_2_y = sign * length_2 * math.sin(angle_rad_2)

    vector_r_x = vector_length_1_x + vector_length_2_x
    vector_r_y = vector_length_1_y + vector_length_2_y
    vector_r = math.sqrt(vector_r_x ** 2 + vector_r_y ** 2)
    angle = math.degrees(math.atan2(vector_r_y, vector_r_x))

    return {
        "vector_length_1_x": vector_length_1_x,
        "vector_length_1_y": vector_length_1_y,
        "vector_length_2_x": vector_length_2_x,
        "vector_length_2_y": vector_length_2_y,
        "vector_r_x": vector_r_x,
        "vector_r_y": vector_r_y,
        "vector_r": vector_r,
        "angle": angle
    }


add_sub = input("Enter the sign(A: add, S: substract: ))").strip().lower()
length_1 = float(input("Enter the first vector's length: "))
angle_1 = float(input("Enter the first vector's angle: "))
length_2 = float(input("Enter the second vector's length: "))
angle_2 = float(input("Enter the second vector's angle: "))

result = vector_add_sub(add_sub, length_1, angle_1, length_2, angle_2)
print(result)
