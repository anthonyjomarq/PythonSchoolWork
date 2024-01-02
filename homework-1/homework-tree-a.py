# Get tree height from user
height = int(input('Enter height of tree: '))
# Draw one row for every unit of height
for i in range(1, height+1):
    for j in range(1, i+1):
        print("*", end="")
    print()
for i in range(height-1, 0, -1):
    for j in range(1,i+1):
        print("*", end="")
    print()