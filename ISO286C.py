ES = int(input("ES:"))
EI = int(input("EI:"))

es = int(input("es"))
ei = int(input("ei"))

#Spielpassung
HS = ES - ei
MS = EI - es
#Übermasspassung
HU = es - EI
MU = ei - ES

if (HS >= 0 and MS >= 0):
    print("Spielpassung")
    print ("Höstspiel HS:", HS)
    print ("Mindestspiel MS:", MS)

if (HU >= 0 and MU >= 0):
    print("Übermasspassung")
    print ("Höchstübermass HU:", HU)
    print ("Mindestübermass MU:", MU)

if (HS >= 0 and HU >= 0):
    print("Übergagspassung")
    print ("Höchstübermass MU:", HS)
    print ("Mindestspiel MS:", HU)
