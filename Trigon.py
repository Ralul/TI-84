import math

# the display can show a maximum of 32x10 characters
print("[A]***\n"
      "  *   *****     (c)\n"
      " (b)       *****\n"
      "  *             *****\n"
      "  * 90°              *****\n"
      "[C]**********(a)***********[B]\n")

print("enter the values,\nif you do not know it, enter 0")

# User Input if the Value not unknown type zero

angel_A = float(input("Angel A:"))
if (angel_A != 0):
    angle_A_isDefined = True
else:
    angle_A_isDefined = False

angel_B = float(input("Angel B:"))
if (angel_B != 0):
    angle_B_isDefined = True
else:
    angle_B_isDefined = False

side_a = float(input("Side a"))
if (side_a != 0):
    side_a_isDefined = True
else:
    side_a_isDefined = False

side_b = float(input("Side b"))
if (side_b != 0):
    side_b_isDefined = True
else:
    side_b_isDefined = False

side_c = float(input("Side c"))
if (side_c != 0):
    side_c_isDefined = True
else:
    side_c_isDefined = False

# Select the Corect Prozess with an IF ELSE statement
# Side a and Side b   (1)
# Side a and Side c   (2)
# Side a and Angel A  (3)
# Side a and Angel B  (4)
# Side b and Side c   (5)
# Side b and Angel A  (6)
# Side b and Angel B  (7)
# Side c and Angel A  (8*)
# Side c and Angel B  (9*)
# Angel A and Angel B (10)


# Side a and Side b  (1)
if (side_a_isDefined and side_b_isDefined == True):
    angel_A = math.degrees(math.atan(side_a / side_b))
    angel_B = math.degrees(math.atan(side_b / side_a))
    side_c = math.sqrt((side_a ** 2) + (side_b ** 2))
    print("method (1)")

# Side a and Side c  (2)
elif (side_a_isDefined and side_c_isDefined == True):
    angel_A = math.degrees(math.asin(side_a / side_c))
    angel_B = math.degrees(math.acos(side_a / side_c))
    side_b = math.sqrt((side_c ** 2) - (side_a ** 2))
    print("method (2)")

# Side a and Angel A (3)
elif (side_a_isDefined and angle_A_isDefined == True):
    angel_B = 90 - angel_A
    side_b = side_a / math.tan(math.radians(angel_A))
    side_c = side_a / math.sin(math.radians(angel_A))
    print("method (3)")

# Side a and Angel B (4)
elif (side_a_isDefined and angle_B_isDefined == True):
    angel_A = 90 - angel_B
    side_b = side_a * math.tan(math.radians(angel_B))
    side_c = side_a / math.cos(math.radians(angel_B))
    print("method (4)")

# Side b and Side c   (5)
elif (side_b_isDefined and side_c_isDefined == True):
    angel_A = math.degrees(math.acos(side_b / side_c))
    angel_B = math.degrees(math.asin(side_b / side_c))
    side_a = math.sqrt((side_c**2) - (side_b**2))
    print("method (5)")

# Side b and Angel A  (6)
elif (side_b_isDefined and angle_A_isDefined == True):
    angel_B = 90 - angel_A
    side_a = math.tan(math.radians(angel_A)) * side_b
    side_c = side_b / math.cos (math.radians(angel_A))
    print("method (6)")

# Side b and Angel B  (7)
elif (side_b_isDefined and angle_B_isDefined):
    angel_A = 90 - angel_B
    side_a = side_b / math.tan(math.radians(angel_B))
    side_c = side_b / math.sin(math.radians(angel_B))
    print("method (7)")

# Side c and Angel A  (8*)
elif (side_c_isDefined and angle_A_isDefined == True):
    angel_B = 90 - angel_A
    side_a = side_c * math.sin(math.radians(angel_A))
    side_b = side_c * math.cos(math.radians(angel_A))

# Side c and Angel B  (9*)
elif (side_c_isDefined and angle_B_isDefined == True):
    angel_A = 90 - angel_B
    side_a = side_c * math.cos(math.radians(angel_B))
    side_b = side_c * math.sin(math.radians(angel_B))

# Angel A and Angel B (10)
elif (angle_A_isDefined and angle_B_isDefined == True):
    print("the triangle is not defined")

else:
    print("ERROR: no suitable method")

# Print result of the Calculation
print("--------------------------------")
print("Angel A: ", angel_A)
print("Angel B: ", angel_B)
print("Side a: ", side_a)
print("Side b: ", side_b)
print("Side c: ", side_c)
