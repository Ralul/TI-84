def RangeIs (Nominal):
    Nominal_range = 0

    i = [3,6,10,18,30,50,65,80,100,120,140,160,180,200,225,250,280,315,355]
    x = 0
    while i[x] < Nominal:
        x = x+1
    return x

def ToleranceIs (IT,RangeNumber):

    A = [0.3,0.5,0.8,1.2,2,3,4,6,10,14,25,40,60,100,140,250,400,600,1000,1400]
    B = [0.4,0.6,1,1.5,2.5,4,5,8,12,18,20,48,75,120,180,300,480,750,1200,1800]
    C = [0.4,0.6,1,1.5,2.5,4,6,9,15,22,36,58,90,150,220,360,580,900,1500,2200]
    D = [0.5,0.8,1.2,2,3,5,8,11,18,27,43,70,110,180,270,430,700,1100,1800,2700]
    E = [0.6,1,1.5,2.5,4,6,9,13,21,33,52,84,130,210,330,520,840,1300,2100,3300]
    F = [0.6,1,1.5,2.5,4,7,11,16,25,39,62,100,160,250,390,620,1000,1600,2500,3900]
    G = [0.8,1.2,2,3,5,8,13,19,30,46,74,120,190,300,460,740,1200,1900,3000,4600]
    H = [1,1.5,2.5,4,6,10,15,22,35,54,87,140,220,350,540,870,1400,2200,3500,5400]
    I = [1.2,2,3.5,5,8,12,18,25,40,63,100,160,250,400,630,1000,1600,2500,4000,6300]
    J = [2,3,4.5,7,10,14,20,29,46,72,115,185,290,460,720,1150,1850,2900,4600,7200]
    K = [2.5,4,6,8,12,16,23,32,52,81,130,210,320,520,810,1300,2100,3200,5200,8100]
    L = [3,5,7,9,13,18,25,36,57,89,140,230,360,570,890,1400,2300,3600,5700,8900]

    Tolerance = [A,B,C,D,E,F,G,G,H,H,I,I,I,J,J,J,K,K,L,L]

    return Tolerance[RangeNumber][IT+1]

def FundamentalDeviationFromHoleIs (ToleranceClass,IT,RangeNumber,Tolerance):

    # Delta
    Delta = []

    if (IT == 3):
        Delta = [0,1,1,1,1.5,1.5,2,2,2,2,3,3,3,3,3,3,4,4,4,4]
    elif (IT == 4):
        Delta = [0,1.5,1.5,2,2,3,3,3,4,4,4,4,4,4,4,4,4,4,5,5]
    elif (IT == 5):
        Delta = [0,1,2,3,3,4,5,5,5,5,6,6,6,6,6,6,7,7,7,7]
    elif (IT == 6):
        Delta = [0,3,3,3,4,5,6,6,7,7,7,7,7,9,9,9,9,9,11,11]
    elif (IT == 7):
        Delta = [0,4,6,7,8,9,11,11,13,13,15,15,15,17,17,17,20,20,21,21]
    elif (IT == 8):
        Delta = [0,6,7,9,12,14,16,16,19,19,23,23,23,26,26,26,29,29,32,32]

    if (ToleranceClass == "D"):
        dataString = [20,30,40,50,65,80,100,100,120,120,145,145,145,170,170,170,190,190,210,210]
    elif (ToleranceClass == "E"):
        dataString = [14,20,25,32,40,50,60,60,72,72,85,85,85,100,100,100,110,110,125,125]
    elif (ToleranceClass == "F"):
        dataString = [6,10,13,16,20,25,30,30,36,36,43,43,43,50,50,50,56,56,62,62]
    elif (ToleranceClass == "G"):
        dataString = [2,4,5,6,7,9,10,10,12,12,14,14,14,15,15,15,17,17,18,18]
    elif (ToleranceClass == "H"):
        dataString = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif (ToleranceClass == "JS"):
        return (Tolerance /2)*-1

    elif (ToleranceClass == "K" and IT >= 3 and IT <= 8):
        dataString = [0,-1,-1,-1,-2,-2,-2,-2,-3,-3,-3,-3,-3,-4,-4,-4,-4,-4,-4,-4]
        return dataString[RangeNumber] + Delta[RangeNumber]

    elif (ToleranceClass == "M" and IT >= 3 and IT <= 8):
        dataString = [-2,-4,-6,-7,-8,-9,-11,-13,-13,-15,-15,-15,-17,-17,-17,-20,-20,-21,-21]
        return dataString[RangeNumber] + Delta[RangeNumber]
    elif (ToleranceClass == "M" and IT >= 9):
        dataString = [-2,-4,-6,-7,-8,-9,-11,-13,-13,-15,-15,-15,-17,-17,-17,-20,-20,-21,-21]

    elif (ToleranceClass == "N" and IT >= 3 and IT <= 8):
        dataString = [-4,-8,-10,-12,-15,-17,-20,-20,-23,-23,-27,-27,-27,-31,-31,-31,-34,-34,-37,-37]
        return dataString[RangeNumber] + Delta[RangeNumber]
    elif (ToleranceClass == "N" and IT >= 9):
        dataString = [-4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif (ToleranceClass == "P"):
        dataString = [-6,-12,-15,-18,-22,-26,-32,-32,-37,-37,-43,-43,-43,-50,-50,-50,-53,-53,-62,-62]
    elif (ToleranceClass == "R"):
        dataString = [-10,-11,-13,-16,-20,-25,-30,-32,-38,-41,-48,-50,-53,-60,-63,-67,-74,-78,-87,-93]

    return dataString[RangeNumber]

def FundamentalDeviationFromShaftIs (ToleranceClass,IT,RangeNumber,Tolerance):

    if (ToleranceClass == "d"):
        dataString = [-20,-30,-40,-50,-65,-80,-100,-100,-120,-120,-145,-145,-145,-170,-170,-170,-190,-190,-210,-210]
    elif (ToleranceClass == "e"):
        dataString = [-14,-20,-25,-32,-40,-50,-60,-60,-72,-72,-85,-85,-85,-100,-100,-100,-110,-110,-125,-125]
    elif (ToleranceClass == "f"):
        dataString = [-6,-10,-13,-16,-20,-25,-30,-30,-36,-36,-43,-43,-43,-50,-50,-50,-56,-56,-62,-62]
    elif (ToleranceClass == "g"):
        dataString = [-2,-4,-5,-6,-7,-9,-10,-10,-12,-12,-14,-14,-14,-15,-15,-15,-17,-17,-18,-18]
    elif (ToleranceClass == "h"):
        dataString = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif (ToleranceClass == "js"):
        return (Tolerance /2)*-1

    elif (ToleranceClass == "k" and IT >= 4 & IT <= 7):
        # IT 4 to 7
        dataString = [0,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,4,4,4]

    elif (ToleranceClass == "k"):
        dataString = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif (ToleranceClass == "m"):
        dataString = [2,4,6,7,8,9,11,11,13,13,15,15,15,17,17,17,20,20,21,21]
    elif (ToleranceClass == "n"):
        dataString = [4,8,10,12,15,17,20,20,23,23,27,27,27,31,31,31,34,34,37,37]
    elif (ToleranceClass == "p"):
        dataString = [6,12,15,18,22,26,32,32,37,37,43,43,43,50,50,50,56,56,62,62]
    elif (ToleranceClass == "r"):
        dataString = [10,15,19,23,28,34,41,43,51,54,63,65,68,77,80,84,94,98,108,114]
    elif (ToleranceClass == "s"):
        dataString = [14,19,23,28,35,43,53,59,71,79,92,100,108,122,130,140,158,170,190,208]

    return dataString[RangeNumber]

def LimitFromHoleIs(Nominal, ToleranceClass, FundamentalDeviation, Tolerance):
    ES = 0
    EI = 0

    if (
            ToleranceClass == "H" or ToleranceClass == "D" or ToleranceClass == "E" or ToleranceClass == "F" or ToleranceClass == "G"):

        ES = FundamentalDeviation + Tolerance
        EI = FundamentalDeviation

    elif (
            ToleranceClass == "K" or ToleranceClass == "M" or ToleranceClass == "N" or ToleranceClass == "P" or ToleranceClass == "R" or ToleranceClass == "S"):

        EI = FundamentalDeviation - Tolerance
        ES = FundamentalDeviation

    elif (ToleranceClass == "JS"):
        EI = FundamentalDeviation
        ES = FundamentalDeviation + Tolerance

    return (ES, EI)

def LimitFromShaftIs (Nominal,ToleranceClass,FundamentalDeviation,Tolerance):

    es = 0
    ei = 0

    if(ToleranceClass == "d" or ToleranceClass == "e" or ToleranceClass == "f" or ToleranceClass == "g" or ToleranceClass == "h"):

        ei = FundamentalDeviation - Tolerance
        es = FundamentalDeviation

    elif (ToleranceClass == "k" or ToleranceClass == "m" or ToleranceClass == "n" or ToleranceClass == "p" or ToleranceClass == "r" or ToleranceClass == "s"):

        es = FundamentalDeviation + Tolerance
        ei = FundamentalDeviation

    elif (ToleranceClass == "js"):
        ei = FundamentalDeviation + Tolerance
        es = FundamentalDeviation


    return (es,ei)


Nominal = float(input("Nominal:"))                  #[Ø50]

IT_ToleranceShaft = int(input("IT_ToleranceShaft:"))           #[3]
ToleranceClassShaft = str(input("ToleranceClassShaft:"))      #[h]

IT_ToleranceHole = int(input("IT_ToleranceHole:"))           #[8]
ToleranceClassHole = str(input("ToleranceClassHole:"))      #[JS]

RangeNumber = RangeIs(Nominal)

#Calculate Shaft
ToleranceShaft = ToleranceIs(IT_ToleranceShaft,RangeNumber)
FundamentalDeviationFromShaft = FundamentalDeviationFromShaftIs(ToleranceClassShaft,IT_ToleranceShaft,RangeNumber,ToleranceShaft)
LimitFromShaft = LimitFromShaftIs(Nominal,ToleranceClassShaft,FundamentalDeviationFromShaft,ToleranceShaft)

#Calculate Hole
ToleranceHole = ToleranceIs(IT_ToleranceHole,RangeNumber)
FundamentalDeviationFromHole = FundamentalDeviationFromHoleIs(ToleranceClassHole,IT_ToleranceHole,RangeNumber,ToleranceHole)
LimitFromHole = LimitFromHoleIs(Nominal,ToleranceClassHole,FundamentalDeviationFromHole,ToleranceHole)

print ("RangeNumber:", RangeNumber)
print ("Shaft----------------")
print ("TolerancShaftAsMue:", ToleranceShaft)
print ("FundamentalDeviationFromShaft:", FundamentalDeviationFromShaft)
print ("Lower limit deviation ei:",LimitFromShaft[1])
print ("Upper limit deviation es:",LimitFromShaft[0])

print ("Hole-----------------")
print ("TolerancHoleAsMue:", ToleranceHole)
print ("FundamentalDeviationFromHole:", FundamentalDeviationFromHole)
print ("Lower limit deviation EI:",LimitFromHole[1])
print ("Upper limit deviation ES:",LimitFromHole[0])