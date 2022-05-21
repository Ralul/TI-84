
def RangeIs (Nominal):


    if(Nominal <= 3):
        Nominal_range = 0

    elif (Nominal <= 6):
        Nominal_range = 1

    elif (Nominal <= 10):
        Nominal_range = 2

    elif (Nominal <= 18):
        Nominal_range = 3

    elif (Nominal <= 30):
        Nominal_range = 4

    elif (Nominal <= 50):
        Nominal_range = 5

    elif (Nominal <= 80):
        Nominal_range = 6

    elif (Nominal <= 120):
        Nominal_range = 7

    elif (Nominal <= 180):
        Nominal_range = 8

    elif (Nominal <= 250):
        Nominal_range = 9

    elif (Nominal <= 315):
        Nominal_range = 10

    elif (Nominal <= 400):
        Nominal_range = 11

    elif (Nominal <= 500):
        Nominal_range = 12

    elif (Nominal <= 630):
        Nominal_range = 13

    elif (Nominal <= 800):
        Nominal_range = 14

    elif (Nominal <= 1000):
        Nominal_range = 15

    elif (Nominal <= 1250):
        Nominal_range = 16

    elif (Nominal <= 1600):
        Nominal_range = 17

    elif (Nominal <= 2000):
        Nominal_range = 19

    elif (Nominal <= 3150):
        Nominal_range = 20


    return Nominal_range

def ToleranceIs (IT,RangeNumber):

    Nominal_range_0_3       = [0.3,0.5,0.8,1.2,2,3,4,6,10,14,25,40,60,100,140,250,400,600,1000,1400]
    Nominal_range_3_6       = [0.4,0.6,1,1.5,2.5,4,5,8,12,18,20,48,75,120,180,300,480,750,1200,1800]
    Nominal_range_6_10      = [0.4,0.6,1,1.5,2.5,4,6,9,15,22,36,58,90,150,220,360,580,900,1500,2200]
    Nominal_range_10_18     = [0.5,0.8,1.2,2,3,5,8,11,18,27,43,70,110,180,270,430,700,1100,1800,2700]
    Nominal_range_18_30     = [0.6,1,1.5,2.5,4,6,9,13,21,33,52,84,130,210,330,520,840,1300,2100,3300]
    Nominal_range_30_50     = [0.6,1,1.5,2.5,4,7,11,16,25,39,62,100,160,250,390,620,1000,1600,2500,3900]
    Nominal_range_50_80     = [0.8,1.2,2,3,5,8,13,19,30,46,74,120,190,300,460,740,1200,1900,3000,4600]
    Nominal_range_80_120    = [1,1.5,2.5,4,6,10,15,22,35,54,87,140,220,350,540,870,1400,2200,3500,5400]
    Nominal_range_120_180   = [1.2,2,3.5,5,8,12,18,25,40,63,100,160,250,400,630,1000,1600,2500,4000,6300]
    Nominal_range_180_250   = [2,3,4.5,7,10,14,20,29,46,72,115,185,290,460,720,1150,1850,2900,4600,7200]
    Nominal_range_250_315   = [2.5,4,6,8,12,16,23,32,52,81,130,210,320,520,810,1300,2100,3200,5200,8100]
    Nominal_range_315_400   = [3,5,7,9,13,18,25,36,57,89,140,230,360,570,890,1400,2300,3600,5700,8900]
    Nominal_range_400_500   = [4,6,8,10,15,20,27,40,63,97,155,250,400,630,970,1550,2500,4000,6300,9700]
    Nominal_range_500_630   = [0,0,9,11,16,22,32,44,70,110,175,280,440,700,1100,1750,2800,4400,7000,11000]
    Nominal_range_630_800   = [0,0,10,13,18,25,36,50,80,125,200,320,500,800,1250,2000,3200,500,8000,12500]
    Nominal_range_800_1000  = [0,0,11,15,21,28,40,56,90,140,230,360,560,900,1400,2300,3600,5600,9000,14000]
    Nominal_range_1000_1250 = [0,0,13,18,24,33,47,66,105,165,260,420,660,1050,1650,2600,4200,6600,10500,16500]
    Nominal_range_1250_1600 = [0,0,15,21,29,39,55,78,125,195,310,500,780,1250,1950,3100,5000,7800,12500,19500]
    Nominal_range_1600_2000 = [0,0,18,25,35,46,65,92,150,230,370,600,920,1500,2300,3700,6000,9200,15000,23000]
    Nominal_range_2000_2500 = [0,0,22,30,41,55,78,110,175,280,440,700,1100,1750,2800,4400,7000,11000,17500,28000]
    Nominal_range_2500_3150 = [0,0,26,36,50,68,96,135,210,330,540,860,1350,2100,3300,5400,8600,13500,21000,33000]

    Tolerance = [Nominal_range_0_3,Nominal_range_3_6,Nominal_range_6_10,Nominal_range_10_18,Nominal_range_18_30,Nominal_range_30_50,Nominal_range_50_80,Nominal_range_80_120,Nominal_range_120_180,Nominal_range_180_250,Nominal_range_250_315,Nominal_range_315_400,Nominal_range_400_500,Nominal_range_500_630,Nominal_range_630_800,Nominal_range_800_1000,Nominal_range_1000_1250,Nominal_range_1250_1600,Nominal_range_1600_2000,Nominal_range_2000_2500,Nominal_range_2500_3150]

    return Tolerance[RangeNumber][IT+1]

def FundamentalDeviationFromShaftIs (ToleranceClass,IT,RangeNumber,Tolerance):

    if (ToleranceClass == "d"):
        dataString = [-20,-30,-40,-50,-65,-80,-100,-120,-145,-170,-190,-210,-230,-260,-290,-320,-350,-390,-430,-480,-520]
    elif (ToleranceClass == "e"):
        dataString = [-14,-20,-25,-32,-40,-50,-60,-72,-85,-100,-110,-125,-135,-145,-160,-170,-195,-220,-240,-260,-290]
    elif (ToleranceClass == "f"):
        dataString = [-6,-10,-13,-16,-20,-25,-30,-36,-43,-50,-56,-62,-68,-76,-80,-86,-98,-110,-120,-130,-145]
    elif (ToleranceClass == "g"):
        dataString = [-2,-4,-5,-6,-7,-9,-10,-12,-14,-15,-17,-18,-20,-22,-24,-26,-28,-30,-32,-34,-38]
    elif (ToleranceClass == "h"):
        dataString = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif (ToleranceClass == "js"):
        return (Tolerance /2)*-1

    elif (ToleranceClass == "k" and IT >= 4 & IT <= 7):
        # IT 4 to 7
        dataString = [0,1,1,1,2,2,2,3,3,4,4,4,5,0,0,0,0,0,0,0,0]

    elif (ToleranceClass == "k"):
        dataString = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif (ToleranceClass == "m"):
        dataString = [2,4,6,7,8,9,11,13,15,17,20,21,23,26,30,34,40,48,58,68,76]
    elif (ToleranceClass == "n"):
        dataString = [4,8,10,12,15,17,20,23,27,31,34,37,40,44,50,56,66,78,92,110,135]
    elif (ToleranceClass == "p"):
        dataString = [6,12,15,18,22,26,32,37,43,50,56,62,68,78,88,100,120,140,170,195,240]
    elif (ToleranceClass == "r"):
        dataString = [10,15,19,23,28,34,41,51,63,77,94,108,126,150,175,210,250,300,370,440,550]
    elif (ToleranceClass == "s"):
        dataString = [14,19,23,28,35,43,53,71,92,122,158,190,232,280,340,430,520,640,820,1000,1250]


    return dataString[RangeNumber]

def FundamentalDeviationFromHoleIs (ToleranceClass,IT,RangeNumber,Tolerance):

    # Delta
    if ToleranceClass(ToleranceClass == "K" or ToleranceClass == "M" or ToleranceClass == "N"):
        if (IT == 3):
            Delta = [0, 1, 1, 1, 1.5, 1.5, 2, 2, 3, 3, 4, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0]
        elif (IT == 4):
            Delta = [0,1.5,1.5,2,2,3,3,4,4,4,4,5,5,0,0,0,0,0,0,0,0]
        elif (IT == 5):
            Delta = [0,1,2,3,3,4,5,5,6,6,7,7,7,0,0,0,0,0,0,0,0]
        elif (IT == 6):
            Delta = [0,3,3,3,4,5,6,7,7,9,9,11,13,0,0,0,0,0,0,0,0]
        elif (IT == 7):
            Delta = [0,4,6,7,8,9,11,13,15,17,20,21,23,0,0,0,0,0,0,0,0]
        elif (IT == 8):
            Delta = [0,6,7,9,12,14,16,19,23,26,29,32,34,0,0,0,0,0,0,0,0]

    elif (ToleranceClass == "D"):
        dataString = [20,30,40,50,65,80,100,120,145,170,190,210,230,260,290,320,350,390,430,480,520]
    elif (ToleranceClass == "E"):
        dataString = [14,20,25,32,40,50,60,72,85,100,110,125,135,145,160,170,195,220,240,260,290]
    elif (ToleranceClass == "F"):
        dataString = [6,10,13,16,-20,-25,-30,-36,-43,-50,-56,-62,-68,-76,-80,-86,-98,-110,-120,-130,-145]
    elif (ToleranceClass == "G"):
        dataString = [2,4,5,6,7,9,10,12,14,15,17,18,20,22,24,26,28,30,32,34,38]
    elif (ToleranceClass == "H"):
        dataString = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif (ToleranceClass == "JS"):
        return (Tolerance /2)*-1

    elif (ToleranceClass == "K" and IT >= 3 & IT <= 8):
        dataString = [0,-1,-1,-1,-2,-2,-2,-3,-3,-4,-4,-4,-5,0,0,0,0,0,0,0,0]
        return dataString[RangeNumber] + Delta
    elif (ToleranceClass == "K"):
        dataString = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif (ToleranceClass == "M" and IT >= 3 & IT <= 8):
        dataString = [-2,-4,-6,-7,-8,-9,-11,-13,-15,-17,-20,-21,-23,-26,-30,-34,-40,-48,-58,-68,-76]
        return dataString[RangeNumber] + Delta
    elif (ToleranceClass == "M"):
        dataString = [-2,-4,-6,-7,-8,-9,-11,-13,-15,-17,-20,-21,-23,-26,-30,-34,-40,-48,-58,-68,-76]


    elif (ToleranceClass == "N" and IT >= 3 & IT <= 8):
        dataString = [0,-1,-1,-1,-2,-2,-2,-3,-3,-4,-4,-4,-5,0,0,0,0,0,0,0,0]
        return dataString[RangeNumber] + Delta
    elif (ToleranceClass == "N"):
        dataString = [-4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    elif (ToleranceClass == "P"):
        dataString = [-6,-12,-15,-18,-22,-26,-32,-37,-43,-50,-53,-62,-68,-78,-88,-100,-120,-140,-170,-195,-240]
    elif (ToleranceClass == "R"):
        dataString = [-10,-15,-19,-23,-28,-34,-41,-51,-63,-77,-94,-108,-126,-150,-175,-210,-250,-300,-370,-440,-550]
    elif (ToleranceClass == "S"):
        dataString = [-14,-19,-23,-28,-35,-43,-53,-71,-92,-122,-158,-190,-232,-280,-340,-430,-520,-640,-820,-1000,-1250]

    return dataString[RangeNumber]

def LimitFromShaftIs (Nominal,ToleranceClass,FundamentalDeviation,Tolerance):

    es = 0
    ei = 0

    if(ToleranceClass == "d" or ToleranceClass == "e" or ToleranceClass == "f" or ToleranceClass == "g" or ToleranceClass == "h"):

        ei = FundamentalDeviation
        es = FundamentalDeviation - Tolerance

    elif (ToleranceClass == "k" or ToleranceClass == "m" or ToleranceClass == "n" or ToleranceClass == "p" or ToleranceClass == "r" or ToleranceClass == "s"):

        es = FundamentalDeviation
        ei = FundamentalDeviation + Tolerance

    elif (ToleranceClass == "js"):
        ei = FundamentalDeviation
        es = FundamentalDeviation + Tolerance


    return (es,ei)


Nominal = float(input("Nominal:"))                  #[Ø50]

#IT_ToleranceShaft = int(input("IT_ToleranceShaft:"))           #[3]
#ToleranceClassShaft = str(input("ToleranceClassShaft:"))      #[h]

IT_ToleranceHole = int(input("IT_ToleranceHole:"))           #[8]
ToleranceClassHole = str(input("ToleranceClassHole:"))      #[JS]

RangeNumber = RangeIs(Nominal)

#Calculate Shaft
#ToleranceShaft = ToleranceIs(IT_ToleranceShaft,RangeNumber)
#FundamentalDeviationFromShaft = FundamentalDeviationFromShaftIs(ToleranceClassShaft,IT_ToleranceShaft,RangeNumber,ToleranceShaft)
#LimitFromShaft = LimitFromShaftIs(Nominal,ToleranceClassShaft,FundamentalDeviationFromShaft,ToleranceShaft)

#Calculate Hole
ToleranceHole = ToleranceIs(IT_ToleranceHole,RangeNumber)
FundamentalDeviationFromHole = FundamentalDeviationFromHoleIs(ToleranceClassHole,IT_ToleranceHole,RangeNumber,ToleranceHole)


print ("RangeNumber:", RangeNumber)
print ("*********************************")
#print ("TolerancShaftAsMue:", ToleranceShaft)
#print ("FundamentalDeviationFromShaft:", FundamentalDeviationFromShaft)
#print ("Lower limit deviation ei:",LimitFromShaft[0])
#print ("Upper limit deviation es:",LimitFromShaft[1])
print ("*********************************")
print ("TolerancHoleAsMue:", ToleranceHole)
print ("FundamentalDeviationFromHole:", FundamentalDeviationFromHole)
#print ("Lower limit deviation EI:",LimitFromShaft[0])
#print ("Upper limit deviation ES:",LimitFromShaft[1])

