from unittest import TestCase
import copy

from task3 import getJsonSerializer, getValues, addData


class TestTask3(TestCase):
    path_tests: str = "/home/user_dmitrii/dev/test/Performance-Lab/task3/data/tests.json"
    path_values: str = "/home/user_dmitrii/dev/test/Performance-Lab/task3/data/values.json"
    path_report: str = "/home/user_dmitrii/dev/test/Performance-Lab/task3/data/report.json"

    dict_tests: dict = {
        "tests": [{
            "id": 2,
            "title": "Smoke test",
            "value": ""
        }, {
            "id": 41,
            "title": "Debug test",
            "value": ""
        }, {
            "id": 73,
            "title": "Performance test",
            "value": "",
            "values": [{
                "id": 345,
                "title": "Maxperf",
                "value": "",
                "values": [{
                    "id": 230,
                    "title": "Percent",
                    "values": [{
                        "id": 234,
                        "title": "200",
                        "value": ""
                    }, {
                        "id": 653,
                        "title": "300",
                        "value": ""
                    }]
                }]
            }, {
                "id": 110,
                "title": "Stability test",
                "value": "",
                "values": [{
                    "id": 261,
                    "title": "Percent",
                    "values": [{
                        "id": 238,
                        "title": "160",
                        "value": ""
                    }, {
                        "id": 690,
                        "title": "240",
                        "value": ""
                    }]
                }]
            }]
        }, {
            "id": 122,
            "title": "Security test",
            "value": "",
            "values": [{
                "id": 5321,
                "title": "Confidentiality",
                "value": ""
            }, {
                "id": 5322,
                "title": "Integrity",
                "value": ""
            }]
        }]
    }
    dict_values: dict = {
        "values": [{
            "id": 2,
            "value": "passed"
        }, {
            "id": 41,
            "value": "passed"
        }, {
            "id": 73,
            "value": "passed"
        }, {
            "id": 110,
            "value": "failed"
        }, {
            "id": 122,
            "value": "failed"
        }, {
            "id": 234,
            "value": "passed"
        }, {
            "id": 238,
            "value": "passed"
        }, {
            "id": 345,
            "value": "passed"
        }, {
            "id": 653,
            "value": "passed"
        }, {
            "id": 690,
            "value": "failed"
        }, {
            "id": 5321,
            "value": "passed"
        }, {
            "id": 5322,
            "value": "failed"
        }]
    }
    dict_report: dict = {
        "tests": [{
            "id": 2,
            "title": "Smoke test",
            "value": "passed"
        }, {
            "id": 41,
            "title": "Debug test",
            "value": "passed"
        }, {
            "id": 73,
            "title": "Performance test",
            "value": "passed",
            "values": [{
                "id": 345,
                "title": "Maxperf",
                "value": "passed",
                "values": [{
                    "id": 230,
                    "title": "Percent",
                    "values": [{
                        "id": 234,
                        "title": "200",
                        "value": "passed"
                    }, {
                        "id": 653,
                        "title": "300",
                        "value": "passed"
                    }]
                }]
            }, {
                "id": 110,
                "title": "Stability test",
                "value": "failed",
                "values": [{
                    "id": 261,
                    "title": "Percent",
                    "values": [{
                        "id": 238,
                        "title": "160",
                        "value": "passed"
                    }, {
                        "id": 690,
                        "title": "240",
                        "value": "failed"
                    }]
                }]
            }]
        }, {
            "id": 122,
            "title": "Security test",
            "value": "failed",
            "values": [{
                "id": 5321,
                "title": "Confidentiality",
                "value": "passed"
            }, {
                "id": 5322,
                "title": "Integrity",
                "value": "failed"
            }]
        }]
    }
    dict_id_values: dict = {
        2: "passed",
        41: "passed",
        73: "passed",
        110: "failed",
        122: "failed",
        234: "passed",
        238: "passed",
        345: "passed",
        653: "passed",
        690: "failed",
        5321: "passed",
        5322: "failed"
    }

    def test_getJsonSerializer(self):
        self.maxDiff = None
        self.assertEqual(getJsonSerializer(self.path_tests), self.dict_tests)
        self.assertEqual(getJsonSerializer(self.path_values), self.dict_values)

    def test_getValues(self):
        self.assertEqual(getValues(self.dict_values), {
            2: "passed",
            41: "passed",
            73: "passed",
            110: "failed",
            122: "failed",
            234: "passed",
            238: "passed",
            345: "passed",
            653: "passed",
            690: "failed",
            5321: "passed",
            5322: "failed"
        })

    def test_addData(self):
        tests: dict = copy.deepcopy(self.dict_tests)
        values: dict = self.dict_id_values
        self.assertEqual(addData(tests["tests"], values), self.dict_report)
