def findFibonacciSeries(n):
    a, b = 0, 1
    series = [a]
    while b < n:
        series.append(b)

        # Expression on the right is first evaluated and then assignment is done.
        a, b = b, a+b
    return series


print(findFibonacciSeries(100))
