def getIndex(index: int, current_index: int, length: int) -> int:
    return (length + current_index) % index - 1


def findCircularPath(n: int, m: int) -> str:
    res = '1'
    massive: list[str] = [str(i) for i in range(1, n+1)]
    current_index = 0
    while True:
        new_index = getIndex(n, current_index, m)
        if new_index == 0:
            return res
        res += massive[new_index]
        current_index = new_index


def main():
    while True:
        print("Введите длину массива и длину обхода через пробел:")
        n, m = map(int, input().split())
        print(findCircularPath(n, m))


if __name__ == '__main__':
    main()
