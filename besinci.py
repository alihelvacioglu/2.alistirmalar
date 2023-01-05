def asal(y):
    if y<1:
        return False
    for i in range(2,int(y**(0.5)+1)):
        if y%i==0:
            return False
    return True

def super_asal(x):
    x=str(x)
    basamak=len(x)
    if len(x)==1:
        return asal(int(x))
    if asal(int(x)):
        return super_asal(x[:basamak-1])
    else:
        return False

for i in range(10000,100000):
    if super_asal(i):
        print(i)


