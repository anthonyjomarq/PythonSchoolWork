# Get tree height from user
height = int(input('Enter height of tree: '))
for i in range(1, height+1):
    for j in range(1, (height - i) + 1):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end="")
    print()
for i in range(height-1, 0, -1):
    for j in range(1, (height - i) + 1):
        print(" ", end="")
    for k in range(1, i + 1):
        print("*", end="")
    print()
