import sys
import math

circle_file = sys.argv[1]
points_file = sys.argv[2]

with open('circle.txt', 'r') as f:
    x_circle, y_circle = f.readline().strip().split()
    x_circle, y_circle = int(x_circle), int(y_circle)
    radius = f.readline().strip()
    radius = int(radius)

with open('points.txt', 'r') as f:
    points = []
    for line in f:
        parts = line.strip().split()
        x = int(parts[0])
        y = int(parts[1])
        points.append((x, y))

    #  c = sqrt(x**2 + y**2)
        widhtX = x - x_circle
        heightY = y - y_circle
        hypot = math.sqrt(widhtX ** 2 + heightY ** 2)

        if hypot < radius:
            print(1)
        elif hypot == radius:
            print(0)
        else:
            print(2)




