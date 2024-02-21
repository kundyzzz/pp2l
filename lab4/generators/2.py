def gen(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i
limit = int(input())
ev= gen(limit)
print(','.join(map(str, ev)))