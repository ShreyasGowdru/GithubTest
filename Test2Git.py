import json

sample = '{"name": "shreyas", "age": 27}'

data = json.loads(sample)
print(data)
print(list(data.keys()))
print(list(data.values()))