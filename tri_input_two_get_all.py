import math


def solve_right_triangle_two_sides(value1, value2, value1_type, value2_type):
    globals()[value1_type] = value1
    globals()[value2_type] = value2

    if 'h' in globals():
        hypotenuse = globals()['h']
        if 'o' in globals():
            opposite = globals()['o']
            adjacent = math.sqrt(hypotenuse**2 - opposite**2)
            angle_a = math.degrees(math.asin(opposite / hypotenuse))
            angle_b = 90 - angle_a
        elif 'a' in globals():
            adjacent = globals()['a']
            opposite = math.sqrt(hypotenuse**2 - adjacent**2)
            angle_a = math.degrees(math.acos(adjacent / hypotenuse))
            angle_b = 90 - angle_a
    else:
        opposite = globals()['o']
        adjacent = globals()['a']
        hypotenuse = math.sqrt(opposite**2 + adjacent**2)
        angle_a = math.degrees(math.atan(opposite / adjacent))
        angle_b = 90 - angle_a

    return {
        'Angle A (deg)': angle_a,
        'Angle B (deg)': angle_b,
        'Hypotenuse': hypotenuse,
        'Adjacent': adjacent,
        'Opposite': opposite
    }


def solve_right_triangle_one_angle(value1, value2, value1_type, value2_type):

    angle = value1
    side = value2
    side_type = value2_type

    if side_type == 'h':
        hypotenuse = side
        opposite = hypotenuse * math.sin(math.radians(angle))
        adjacent = hypotenuse * math.cos(math.radians(angle))

    elif side_type == 'o':
        opposite = side
        hypotenuse = opposite / math.sin(math.radians(angle))
        adjacent = hypotenuse * math.cos(math.radians(angle))
    elif side_type == 'a':
        adjacent = side
        hypotenuse = adjacent / math.cos(math.radians(angle))
        opposite = hypotenuse * math.sin(math.radians(angle))
    else:
        raise ValueError("Invalid input types.")

    angle_a = angle
    angle_b = 90 - angle_a

    return {
        'Angle A (deg)': angle_a,
        'Angle B (deg)': angle_b,
        'Hypotenuse': hypotenuse,
        'Adjacent': adjacent,
        'Opposite': opposite
    }


# Example usage
question_type = input(
    "Do you have an angle want to input? Type ('Yes','No'): ").strip().lower()
if question_type == "no":
    print("Enter the type and value for the first side:")
    value1_type = input(
        "Type ('H: hypotenuse', 'O: opposite', 'A: adjacent'): ").strip().lower()
    value1 = float(input("Value: "))

    print("Enter the type and value for the second side:")
    value2_type = input(
        "Type ('H: hypotenuse', 'O: opposite', 'A: adjacent'): ").strip().lower()
    value2 = float(input("Value: "))

    result = solve_right_triangle_two_sides(
        value1, value2, value1_type, value2_type)

else:
    print("Enter the angle:")
    value1_type = "angle"
    value1 = float(input("Value: "))

    print("Enter the type and value for side:")
    value2_type = input(
        "Type ('H: hypotenuse', 'O: opposite', 'A: adjacent'): ").strip().lower()
    value2 = float(input("Value: "))

    result = solve_right_triangle_one_angle(
        value1, value2, value1_type, value2_type)

print("\nSolved triangle:")
print(f"Angle A: {result['Angle A (deg)']:.2f}°")
print(f"Angle B: {result['Angle B (deg)']:.2f}°")
print(f"Hypotenuse: {result['Hypotenuse']:.4f}")
print(f"Adjacent: {result['Adjacent']:.4f}")
print(f"Opposite: {result['Opposite']:.4f}")
