import math
from sympy import Rational, sqrt

# 将字符串座标转换为 sympy 表达式并存储在变量中
a = eval(input("Enter x: "))
b = eval(input("Enter y: "))

# 计算斜边
hypotenuse = sqrt(a**2 + b**2)

# 计算三角函数值并保留分数形式
sin_value = b / hypotenuse
cos_value = a / hypotenuse
tan_value = b / a
cot_value = 1 / tan_value
sec_value = 1 / cos_value
csc_value = 1 / sin_value

print(f"Sin: {sin_value}, Cos: {cos_value}")
print(f"Tan: {tan_value}, Cot: {cot_value}")
print(f"Sec: {sec_value}, Csc: {csc_value}")
