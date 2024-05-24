def getArray(path: str) -> list[int]:
    with open(path, 'r') as file:
        return [int(i) for i in file.read().split()]


def getMedian(nums: list[int]) -> float:
    n = len(nums)
    nums.sort()
    if n % 2 != 0:
        return nums[n // 2]
    return (nums[n // 2 - 1] + nums[n // 2]) // 2


def steps(nums: list[int], median: float) -> int:
    steps = 0
    for num in nums:
        steps += abs(num - median)
    return steps


def main():
    path: str = input("Введите путь к файлу: ")  # путь к файлу
    nums: list[int] = getArray(path)  # получаем массив из файла
    median: float = getMedian(nums)  # получаем медиану
    print(steps(nums, median))  # выводим количество шагов


if __name__ == '__main__':
    main()
