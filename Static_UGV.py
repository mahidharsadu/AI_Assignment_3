import random

SIZE = 10

grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

def generate_obstacles():
    for i in range(SIZE):
        for j in range(SIZE):
            if random.randint(0, 4) == 0:  
                grid[i][j] = 1
            else:
                grid[i][j] = 0

def print_grid():
    for i in range(SIZE):
        for j in range(SIZE):
            print(grid[i][j], end=" ")
        print()

generate_obstacles()

print("Battlefield grid:")
print_grid()

print("\nStart node: (0,0)")
print("Goal node: (9,9)")
print("UGV navigates avoiding obstacles")
