def solution():
    a, b = map(int, input().split())
    return (a + b) * (a - b)


if __name__ == "__main__":
    print(solution())
