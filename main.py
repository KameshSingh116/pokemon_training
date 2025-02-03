#Radhe Radhe 
num=int(input("Enter the number of pokemion:"))
powers=[]
for i in range(num):
    power=int(input("Enter the power of pokemon:"))
    powers.append(power)

mini, maxi=0,0

for power in powers:
    if mini==0 and maxi==0:
        mini,maxi=powers[0],powers[0]
        print(mini,maxi)

    else:
        mini=min(mini,power)
        maxi=max(maxi,power)
        print(mini,maxi)
