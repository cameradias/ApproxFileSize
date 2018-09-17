import firstprogram
from Input import inputInt

n = inputInt()
while (n != -1):
    print(firstprogram.approximate_size(n))
    # print(approximate_size(n,False))
    n = inputInt()

print("Quiting main")
