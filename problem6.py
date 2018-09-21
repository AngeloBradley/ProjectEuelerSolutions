sumSquares = 0
squareSums = 0

for x in range(1, 101):
    sumSquares += (x * x)
    squareSums += x

squareSums = squareSums * squareSums

print(squareSums - sumSquares)