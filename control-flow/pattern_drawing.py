length = int(input("Enter the size of the pattern: "))
counter = length
while counter > 0:
    for i in range(0, length):
        print("*", end="")
    print()
    counter -= 1
    
