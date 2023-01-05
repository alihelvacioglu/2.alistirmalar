# def reculsive_toplama(x):
#     if x<0:
#         return "pozitif sayı giriniz"
#     elif x==0:
#         return 0
#     else:
#         if x==1:
#             return 1
#         else:
#             return x+reculsive_toplama(x-1)            

# reculsive_toplama(7)

def toplama(N):
    if N<0:
        return "Pozitif sayı giriniz."
    elif N == 0:
        return 0
    else:
        if N == 1:
            return 1
        else:
            return N+toplama(N-1)

toplama(9)