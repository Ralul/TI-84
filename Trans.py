import math

# the display can show a maximum of 32x10 characters


# User Input if the Value not unknown type zero

n1 = float(input("n1 :"))
if (n1 != 0):
    n1IsDefined = True
else:
    n1IsDefined = False

n2 = float(input("n2 :"))
if (n2 != 0):
    n2IsDefined = True
else:
    n2IsDefined = False

d1 = float(input("d1 z1:"))
if (d1 != 0):
    d1IsDefined = True
else:
    d1IsDefined = False

d2 = float(input("d2 / z2:"))
if (d2 != 0):
    d2IsDefined = True
else:
    d2IsDefined = False

i = float(input("i :"))
if (i != 0):
    iIsDefined = True
else:
    iIsDefined = False

# Select the Corect Prozess with an IF ELSE statement and print the Resulut
# n1 + n2 + d1  (1)
# n1 + n2 + d2  (2)
# n1 + d1 + d2  (3)
# n1 + n2 + d2  (4)
# n1 + n2 + i   (5)
# n2 + d1 + i   (6)
# d1 + d2 + i   (7)
# n1 + d2 + i   (8)
# n2 + d2 + i   (9)
# n1 + d1 + i   (10)
# n1 + i   (11)
# n1 + i   (12)
# n1 + i   (13)
# n1 + i   (14)
# n1 + n1  (15)
# d1 + d2   (16)
# ERROR or you are an Idiont (17)

# n1 + n2 + d1  (1)
if (n1IsDefined and n2IsDefined and d1IsDefined == True):
    d2 = (n1*d1) / n2
    i = n1 / n2

# n1 + n2 + d2  (2)
elif (n1IsDefined and n2IsDefined and d2IsDefined == True):
    d1 = (n2*d2) / n1
    i = d2 / d1

# n1 + d1 + d2  (3)
elif (n1IsDefined and d1IsDefined and d2IsDefined == True):
    n2 = (n1*d1) / d2
    i = d2 / d1

# n1 + n2 + d2  (4)
elif (n1IsDefined and n2IsDefined and d2IsDefined == True):
    d1 = (n2*d2) / n1
    i = n1 / n2

# n1 + n2 + i   (5)
elif (n1IsDefined and n2IsDefined and iIsDefined == True):
    print("d1 and d2 is not calculable ")

# n2 + d1 + i   (6)
elif (n2IsDefined and d1IsDefined and iIsDefined == True):
    n1 = n2 * i
    d2 = d1 * i

# n1 + n2 + i   (7)
elif (n1IsDefined and n2IsDefined and iIsDefined == True):
    print("n1 and n2 is not calculable ")

# n1 + d2 + i   (8)
elif (n1IsDefined and d2IsDefined and iIsDefined == True):
    n2 = n1 / i
    d1 = d2 / i

# n2 + d2 + i   (9)
elif (n2IsDefined and d2IsDefined and iIsDefined == True):
    n1 = n2 * i
    d1 = d2 * i

# n1 + d1 + i   (10)
elif (n1IsDefined and d1IsDefined and iIsDefined == True):
    n2 = n1 / i
    d2 = d1 / i

# n1 + i   (11)
elif (n1IsDefined and iIsDefined == True):
    n2 = n1 / i
    print("d is not calculable, not enougt data")

# n2 + i   (12)
elif (n2IsDefined and iIsDefined == True):
    n1 = n2 * i
    print("d is not calculable, not enougt data")

# d1 + i   (11)
elif (d1IsDefined and iIsDefined == True):
    d2 = d1 * i
    print("n is not calculable, not enougt data")

# d2 + i   (12)
elif (d2IsDefined and iIsDefined == True):
    d1 = d2 / i
    print("n is not calculable, not enougt data")

# n1 + n1  (15)
elif (n1IsDefined and n2IsDefined == True):
    i = n1 / n2
    print("n is not calculable, not enougt data")

# d1 + d2   (16)
elif (d1IsDefined and d2IsDefined == True):
    i = d2 / d1
    print("d is not calculable, not enougt data")

else:
    print("you are an incompetent idiot!")


print("n1 : ",n1)
print("n2 : ",n2)
print("d1 / z1 : ",d1)
print("d2 / z2 : ",d2)
print("i : ",i)