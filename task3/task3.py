import json
import sys

values_json = sys.argv[1]
tests_json = sys.argv[2]
report_json = sys.argv[3]

with open(tests_json, "r", encoding="UTF-8") as f:
    tests_data = json.load(f)

with open(values_json, "r", encoding="UTF-8") as f:
    values_data = json.load(f)

values = dict()
for el in values_data['values']: # заполняем values, где ключи - id, значения - passed/failed
    values[el['id']] = el['value']


def fill(test):
    if isinstance(test, dict):
        if 'id' in test: # если в элементе есть ключ id
            test_id = test['id']
            test['value'] = values.get(test_id) # присваиваем значение из словаря values
        for k in test:
            fill(test[k])
    elif isinstance(test, list):
        for el in test:
            fill(el)

fill(tests_data)

with open(report_json, "w", encoding="UTF-8") as f_out:
    json.dump(tests_data, f_out, ensure_ascii=False, indent=2)