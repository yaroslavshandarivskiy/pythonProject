# зробив тільки з k=2

n = int(input("Enter stairs: "))
k = int(input("Enter steps: "))


def ways(n):
    if n in (1, 2):
        return 1
    return ways(n - 1) + ways(n - 2)


if k == 2:
    print("Ways for this operation is ", ways(n + 1))

