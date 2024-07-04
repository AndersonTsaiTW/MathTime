import math

angle = eval(input("Enter angle by degree: "))


sin_value = math.sin(math.radians(angle))
cos_value = math.cos(math.radians(angle))
tan_value = math.tan(math.radians(angle))
cot_value = 1 / tan_value
sec_value = 1 / cos_value
csc_value = 1 / sin_value

print(f"Sin: {sin_value}, Cos: {cos_value}")
print(f"Tan: {tan_value}, Cot: {cot_value}")
print(f"Sec: {sec_value}, Csc: {csc_value}")
