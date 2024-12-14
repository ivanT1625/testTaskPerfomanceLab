import math
import sys

def check_position(circle, points):
    cx, cy, r = circle
    results = []
    for x,y in points:
        squared_distance = (x - cx) ** 2 + (y - cy) ** 2
        if squared_distance == r ** 2:
            results.append(0)
        elif squared_distance < r ** 2:
            results.append(1)
        else:
            results.append(2)
    
    return results

if __name__ == "__main__":
    circle_file = sys.argv[1]
    with open(circle_file, 'r') as file:
        cx, cy = map(float, file.readline().strip().split())
        r = float(file.readline().strip())

    points_file = sys.argv[2]
    with open(points_file, 'r') as file:
        points = [tuple(map(float, line.strip().split())) for line in file]

    results = check_position((cx, cy, r), points)

    for result in results:
        print(result)
