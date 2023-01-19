import sys
import json


def task3(tests, values):
    for testsItem in tests:
        for valuesItem in values:
            if testsItem['id'] == valuesItem['id']:
                testsItem['value'] = valuesItem['value']
        if 'values' in testsItem:
            task3(testsItem['values'], values)
    return tests


if sys.argv[1].split("\\")[-1] == 'values.json':
    tests_file = sys.argv[2]
    values_file = sys.argv[1]
else:
    tests_file = sys.argv[1]
    values_file = sys.argv[2]

with open(tests_file) as tests_data:
    testsData = json.load(tests_data)
with open(values_file) as values_data:
    valuesData = json.load(values_data)

report = task3(testsData['tests'], valuesData['values'])

report_json = json.dumps({'tests': report})

with open('report.json', 'w') as report_data:
    report_data.write(report_json)
