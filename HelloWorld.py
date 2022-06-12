String = input("gib ein")
Nominal = String
K = ''
# loop for all characters
for ele in String:
    if ele.isdigit():
        String = String.replace(ele, K)
print("The resultant string : " + str(String))
x = Nominal.rsplit(String)
print(x)
