def getArray(path: str) -> list[int]:
    with open(path, 'r') as file:
        return [int(i) for i in file.read().split()]


def arithmeticMean(array: list[int]) -> float:
    return sum(array) / len(array)


def makeMove(array: list[int], mean: float) -> list[int]:
    min_number: int = array[0]
    max_number: int = array[-1]
    if abs(min_number - mean) > max_number - mean:
        array[0] += 1
    else:
        array[-1] -= 1
    return array


def equalityTest(array: list[int]) -> bool:
    return len(set(array)) == 1


def main():
    path: str = input("Введите путь к файлу: ")  # путь к файлу
    array: list[int] = getArray(path)  # получаем массив из файла
    res: bool = equalityTest(array)  # проверяем равенство элементов массива
    counter: int = 0  # счетчик количества перестановок массива
    while not res:
        sort_arr: list[int] = sorted(array)  # сортируем массив
        mean = arithmeticMean(array)  # получаем среднее арифметическое
        new_array: list[int] = makeMove(sort_arr, mean)  # коррекция
        res = equalityTest(new_array)  # проверяем равенство
        array = new_array  # перезаписываем массив
        counter += 1
    print(counter)


if __name__ == '__main__':
    main()
