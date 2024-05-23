import json


def getJsonSerializer(path: str):
    with open(path, 'r') as file:
        return json.load(file)


def getValues(values: dict) -> dict[int, str]:
    res = {}
    for value in values['values']:
        res[value['id']] = value['value']
    return res


def addData(tests: list, val: dict):
    res: list = []

    for test in tests:
        if "value" in test.keys():
            test['value'] = val[test['id']]
            res.append(test)
        if "values" in test.keys():
            addData(test['values'], val)
    return {"tests": res}


def writeToFile(path: str, data: dict):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)


def main():
    path_tests: str = input("введите путь к файлу tests.json: ")
    path_values: str = input("введите путь к файлу values.json: ")
    path_report: str = input("введите путь к файлу report.json: ")
    tests: dict = getJsonSerializer(path_tests)  # преобразуем в словарь
    values: dict = getJsonSerializer(path_values)  # преобразуем в словарь
    my_values: dict = getValues(values)  # подготавливаем словарь значений
    report: dict = addData(tests["tests"], my_values)  # добавляем значения
    writeToFile(path_report, report)  # сохраняем в файл


if __name__ == '__main__':
    main()
