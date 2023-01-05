import random 


liste=[]

for i in range (0,1):
    z=random.randint(0,10000)
    liste.append(z)

liste.sort()
print(liste)


aranan_sayi=int(input("aradığınız sayıyı giriniz: "))
uzunluk=len(liste)
maksimum=uzunluk-1
minimum=0
ortanca=int(maksimum/2)

a=0
while a==0:
    
    print(ortanca)
    o=ortanca
    
    if (aranan_sayi>liste[ortanca]):
        minimum=ortanca
        maksimum

    elif (aranan_sayi<liste[ortanca]):
        maksimum=ortanca
        minimum

    elif(aranan_sayi==liste[ortanca]):
        print("aradığınız sayıyı buldunuz") 
        a+=1

    ortanca=int((minimum+maksimum)/2)
    if (o==ortanca):
        a+=1      
