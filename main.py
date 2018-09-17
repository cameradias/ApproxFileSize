import firstprogram
b = True
n = 0
while(b == True):
    n = input("Enter -1 to quit")
    n=int(n)
    if(n == -1):
        b = False
        break

    print(firstprogram.approximate_size(n))
    #print(approximate_size(n,False))
    #print (n)

print("Quiting main")
