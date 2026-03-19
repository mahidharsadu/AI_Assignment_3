import random

SIZE = 10

grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]

def add_dynamic_obstacle():
    x = random.randint(0, SIZE - 1)
    y = random.randint(0, SIZE - 1)

    grid[x][y] = 1

    print(f"Dynamic obstacle appeared at ({x},{y})")

print("UGV navigating battlefield\n")

for i in range(5):
    add_dynamic_obstacle()
    print("Recalculating shortest path...\n")

print("UGV reached goal")
