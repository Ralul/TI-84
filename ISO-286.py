#List
#tolerance grades

# Nominal_range_ , IT grades
def ToleranceIs (Nominal,IT):

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

    print ("Toleranc is: ",Tolerance[Nominal_range][IT+1],"µm")
    return Tolerance[Nominal_range][IT+1]


Nominal = float(input("Nominal:"))
IT_Toleranc = int(input("IT_Toleranc:"))

i= ToleranceIs(Nominal,IT_Toleranc)


print (i)


