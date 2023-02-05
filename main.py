import json

courses = '{"name": "RazRafart","languages": ["Java", "Python"]}'

#loads method parse json string and returns dict

dict_courses = json.loads(courses)

print(type(dict_courses))
print(dict_courses["languages"][0])