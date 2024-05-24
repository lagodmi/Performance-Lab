def getXYR(path: str) -> list[float, float, float]:
    with open(path, 'r') as file:
        return [float(i) for i in file.read().split()]


def getPoints(path: str) -> list[tuple[float, float]]:
    with open(path, 'r') as file:
        return [tuple(map(float, line.strip().split())) for line in file]


def is_point_inside_circle(
    x: float,
    y: float,
    radius: float,
    point_x: float,
    point_y: float,
) -> int:
    distance = (point_x - x)**2 + (point_y - y)**2
    if distance < radius**2:
        return 1  # Точка внутри окружности
    elif distance == radius**2:
        return 0  # Точка лежит на окружности
    else:
        return 2  # Точка вне окружности


def main():
    x: float
    y: float
    radius: float
    path: str = input(
        "Введите путь к файлу с координатами центра окружности и его радиусом: ")  # путь к файлу
    x, y, radius = getXYR(path)  # получаем координаты и радиус
    path_points: list = input("Введите путь к файлу с точками: ")
    points = getPoints(path_points)  # получаем точки
    for point in points:
        point_x, point_y = point
        print(is_point_inside_circle(x, y, radius, point_x, point_y))


if __name__ == '__main__':
    main()
