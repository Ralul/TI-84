import math

# the display can show a maximum of 32x10 characters

print("you need only two values")

# User Input if the Value not unknown type zero
vCalculationPath = ("")
nCalculationPath = ("")
dCalculationPath = ("")
TCalculationPath = ("")
wCalculationPath = ("")


v = float(input("v :"))
if (v != 0):
    vIsDefined = True
else:
    vIsDefined = False

n = float(input("n :"))
if (n != 0):
    nIsDefined = True
else:
    nIsDefined = False

d = float(input("d :"))
if (d != 0):
    dIsDefined = True
else:
    dIsDefined = False

T = float(input("T :"))
if (T != 0):
    TIsDefined = True
else:
    TIsDefined = False

w = float(input("w :"))
if (w != 0):
    wIsDefined = True
else:
    wIsDefined = False

# Select the Corect Prozess with an IF ELSE statement and print the Resulut
# d + v   (1)
# d + n   (2)
# d + T   (3)
# d + w   (4)
# v + n   (5)
# v + T   (6)
# v + w   (7)
# n + T   (8)
# n + w   (9)
# T + w   (10)


# d + v   (1)
if (dIsDefined and vIsDefined == True):
    n = v / (math.pi * d)
    T = 1 / n
    w = 2 * math.pi * n

# d + n   (2)
elif (dIsDefined and nIsDefined == True):
    v = d * math.pi * n
    T = 1 /n
    w = 2 * math.pi * n

# d + T   (3)
elif (dIsDefined and TIsDefined == True):
    n = 1 / T
    v = d * math.pi * n
    w = 2 * math.pi * n

# d + w   (4)
elif (dIsDefined and wIsDefined == True):
    n = w / (2 * math.pi)
    v = d * math.pi * n
    T = 1 / n

# v + n   (5)
elif (vIsDefined and nIsDefined == True):
    d = v  / (math.pi * n)
    T = 1 /n
    w = 2 * math.pi * n

# v + T   (6)
elif (vIsDefined and TIsDefined == True):
    n = 1 / T
    d = v / (n * math.pi)
    w = 2 * math.pi * n

# v + w   (7)
elif (vIsDefined and wIsDefined == True):
    n = w / (2 * math.pi)
    d = v / (n * math.pi)
    T = 1 / n

# n + T   (8)
elif (nIsDefined and TIsDefined == True):
    w = 2 * math.pi * n
    print("not enough Data")

# n + w   (9)
elif (nIsDefined and wIsDefined == True):
    T = 1/n
    print("not enough Data")

# T + w   (10)
elif (TIsDefined and wIsDefined == True):
    n = w / (2 * math.pi)
    print("not enough Data")

else:
    print("ERROR")

print("d : ", d)
print("v : ", v)
print("n : ", n)
print("T : ", T)
print("w : ", w)

print(dCalculationPath)
print(vCalculationPath)
print(nCalculationPath)
print(TCalculationPath)
print(wCalculationPath)