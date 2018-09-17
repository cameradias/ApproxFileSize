import firstprogram

n = int(input("Enter size in bytes (-1 to quit): "))
while (n != -1):
    print(firstprogram.approximate_size(n))
    # print(approximate_size(n,False))
    n = int(input("Enter size in bytes (-1 to quit): "))

print("Quiting main")
