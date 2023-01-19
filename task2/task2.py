import sys


def task2(x, y, xc, yc, r):
    s = ((x - xc) ** 2 + (y - yc) ** 2) ** 0.5
    if s == r:
        return 0
    if s < r:
        return 1
    return 2


with open(sys.argv[1]) as circleFile:
    circleData = circleFile.read().split('\n')
with open(sys.argv[2]) as pointsFile:
    pointsData = pointsFile.read().split('\n')

x, y = circleData[0].split(' ')
r = circleData[1]
result = []

for cords in pointsData:
    xc, yc = cords.split(' ')
    result.append(str(task2(float(x), float(y), float(xc), float(yc), float(r))))

print("\n".join(result))
