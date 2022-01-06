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

a = float(input("acceleration a:"))
if (a != 0):
    AccelIsDefined = True
else:
    AccelIsDefined = False

# Select the Corect Prozess with an IF ELSE statement and print the resulut
# v and t   (1)
# v and s   (2)
# v and a   (3)
# s and t   (4)
# s and a   (5)
# a and t   (6)

# v and t is Defineded (1)
if (SpeedIsDefined and TimeIsDefined == True):
    s = 0.5* v * t
    a = v / t

elif (SpeedIsDefined and DistanceIsDefined == True):
    t = s / v


elif (TimeIsDefined and DistanceIsDefined == True):
    v = s / t


print ("Distance        s: ",s)
print ("time            t: ",t)
print ("speed           v: ",v)
print ("acceleration    a: ",a)