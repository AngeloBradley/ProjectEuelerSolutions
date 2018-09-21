collection  = [0]
def append_fibValue(fibValue):
    collection.append(fibValue)
    return fibValue

def fib(n):
    if n == 1:
        return 1
    if n < len(collection): 
        return collection[n]
    else:
         return append_fibValue(fib(n - 1) + fib(n - 2))


sum = 0
counter = 1
while True:
    num = fib(counter)
    counter += 1
    if num > 4000000:
        break
    if num % 2 == 0:
        sum += num

print(sum)