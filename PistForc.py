import math

# the display can show a maximum of 32x10 characters

print("you need only two values")

# User Input if the Value not unknown type zero
pCalculationPath = ("")
FCalculationPath = ("")
ACalculationPath = ("")

p = float(input("p :"))
if (p != 0):
    pIsDefined = True
else:
    pIsDefined = False

F = float(input("F :"))
if (F != 0):
    FIsDefined = True
else:
    FIsDefined = False

A = float(input("A :"))
if (A != 0):
    AIsDefined = True
else:
    AIsDefined = False

#Variables p F A

# Select the Corect Prozess with an IF ELSE statement and print the Resulut
# p + F   (1)
# p + A   (2)
# F + A   (3)

# p + F   (1)
if (pIsDefined and FIsDefined == True):
    A = F / p

    ACalculationPath = ("A = F / p")

# p + A   (2)
if (pIsDefined and AIsDefined == True):
    F = p * A

    FCalculationPath = ("F = p * A")

# F + A   (3)
if (FIsDefined and AIsDefined == True):
    p = F / A

    pCalculationPath = ("p = F / A")

print("p : ", p)
print("F : ", F)
print("A : ", A)


print(pCalculationPath)
print(FCalculationPath)
print(ACalculationPath)