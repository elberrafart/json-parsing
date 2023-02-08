import json

courses = '{"name": "RazRafart","languages": ["Java", "Python"]}'

# loads method parse json string and returns dict

dict_courses = json.loads(courses)

# print(type(dict_courses))
# print(dict_courses["languages"][1])


# -----------Parse content present in Json file--------------
def print_json_file(json_file, desired_output):
    with open(json_file) as file:
        data = json.load(file)
        print(data)
        print(type(data[desired_output]))

#Prints Los Angeles Kings
#If value is a string then use string
#If option is within list use index
with open("example.json") as file:
    data = json.load(file)
    teams = data["quiz"]["sport"]["q1"]["options"]
    #Iterating through teams
    for team in teams:
        print(team)
        if team == "Los Angeles Kings":
            print("Go Team!")

#Prints Questions
print(data["quiz"]["maths"]["q1"]["question"])

#Prints 4
print(data["quiz"]["maths"]["q2"]["options"][3])

print(data["quiz"])
