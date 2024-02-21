def gen34(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def main():
    n = int(input())
    g = gen34(n)
    print(end="")
    for num in g:
        print(num, end=", ")

if __name__ == "__main__":
    main()