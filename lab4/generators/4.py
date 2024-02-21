def square_generator(a, b):
    for num in range(a, b+1):
        yield num*num

a = int(input()) 
b = int(input())
for s in square_generator(a, b):
    print(s)