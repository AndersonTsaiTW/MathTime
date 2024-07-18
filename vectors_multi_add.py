import math


def vector_length_decompose(length, angle):
    angle_rad = math.radians(angle)
    vector_length_x = length * math.cos(angle_rad)
    vector_length_y = length * math.sin(angle_rad)

    return {
        "vector_length_x": vector_length_x,
        "vector_length_y": vector_length_y
    }


more_vector = True
vectors_x = []
vectors_y = []

while more_vector:
    length = float(input("Enter the vector's length: "))
    angle = float(input("Enter the vector's angle: "))

    decomposed_vector = vector_length_decompose(length, angle)
    vectors_x.append(decomposed_vector["vector_length_x"])
    vectors_y.append(decomposed_vector["vector_length_y"])

    ask_more_vector = input(
        "Do you have more vector? (Y: yes ; N: no): ").strip().upper()
    if ask_more_vector == "Y":
        more_vector = True
    elif ask_more_vector == "N":
        more_vector = False
    else:
        print("Wrong answer, please enter 'Y' or 'N'.")

vectors_x_sum = sum(vectors_x)
vectors_y_sum = sum(vectors_y)
vector_r_length = math.sqrt(vectors_x_sum ** 2 + vectors_y_sum ** 2)
angle = math.degrees(math.atan2(vectors_y_sum, vectors_x_sum))
angle_positive = angle % 360

print("Magnitude of the vector: ", vector_r_length)
print("Angle of the vector: ", angle_positive)
