import math

# the display can show a maximum of 32x10 characters


# User Input if the Value not unknown type zero

s = float(input("Distance s:"))
if (s != 0):
    DistanceIsDefined = True
else:
    DistanceIsDefined = False

t = float(input("time t:"))
if (t != 0):
    TimeIsDefined = True
else:
    TimeIsDefined = False

v = float(input("speed v:"))
if (v != 0):
    SpeedIsDefined = True
else:
    SpeedIsDefined = False

# Select the Corect Prozess with an IF ELSE statement and print the Resulut
# v and t   (1)
# v and s   (2)
# t and s   (3)

if (SpeedIsDefined and TimeIsDefined == True):
    s = v * t
    print("s: ",s)

elif (SpeedIsDefined and DistanceIsDefined == True):
    t = s / v
    print("t: ",t)

elif (TimeIsDefined and DistanceIsDefined == True):
    v = s / t
    print("v: ",v)

