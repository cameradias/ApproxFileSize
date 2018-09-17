def inputInt():
    while (True):
        try:
            return int(input("Enter size in bytes (-1 to quit): "))
        except ValueError:
            print("Enter only integers")