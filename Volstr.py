import math

# the display can show a maximum of 32x10 characters


# User Input if the Value not unknown type zero

V = float(input("volume V:"))
if (V != 0):
    VolumeIsDefined = True
else:
    VolumeIsDefined = False

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

A = float(input("area A"))
if (A != 0):
    AreaIsDefined = True
else:
    AreaIsDefined = False

Q = float(input("Volstr Q:"))
if (Q != 0):
    VPTIsDefined = True
else:
    VPTIsDefined = False

# Select the Corect Prozess with an IF ELSE statement
# V and t       (1)
# v and A       (2)
# v and t and A (3)
# Q and v       (4)
# V and t and A (5)
# Q and A       (6)
# V and v and A (7)

# V and t is Defined (1)
if (VolumeIsDefined and TimeIsDefined == True):
    Q = V / t

# v and A is Defined (2)
if (SpeedIsDefined and AreaIsDefined == True):
    Q = v * A

# v and t and A is Defined (3)
if (SpeedIsDefined and TimeIsDefined and AreaIsDefined == True):
    V = v * t * A

# Q and v is Defined (4)
if (VPTIsDefined and SpeedIsDefined):
    A = Q / v

# V and t and A is Defined (5)
if (VolumeIsDefined and TimeIsDefined and AreaIsDefined == True):
    v = V / (t * A)

# Q and A is Defined (6)
if (VPTIsDefined and AreaIsDefined == True):
    v = Q / A

# V and v and A is Defined (7)
if (VolumeIsDefined and SpeedIsDefined and AreaIsDefined == True):
    t = V / (v * A)

#User Output

print("Volume   V: ",V)
print("time     t: ",t)
print("speed    v: ",v)
print("area     A: ",A)
print("Volstr   Q: ",Q)
