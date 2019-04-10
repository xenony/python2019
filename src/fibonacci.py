def generateFibonacci(n):
    count = 0
    num_list = []
    a, b = 1, 1
    while count < n:
        num_list.append(a)
        a, b = b, a + b
        count += 1
    print(num_list)
    return(num_list)


generateFibonacci(1)

generateFibonacci(10)

generateFibonacci(50)
