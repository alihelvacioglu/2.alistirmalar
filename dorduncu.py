def fibonacci(a,b,terim):
  if terim-1 > 0 :
        if a == 1 and b == 1:
            print(1,end =" ")
        print(b,end =" ")
        a,b =b,a+b
        terim-= 1
        return fibonacci(a,b,terim)

fibonacci(1,1,30)           
