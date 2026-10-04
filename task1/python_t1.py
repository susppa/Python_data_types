students = [
    {"name": "Alice", "grades": [5, 4, 5, 3]},
    {"name": "Bob", "grades": [4, 4, 4, 5]},
    {"name": "Charlie", "grades": [5, 5, 5, 5]},
]


def create_mean_mark_dict(input_dict):
    return {element['name']: sum(element['grades']) / len(element['grades']) for element in input_dict}


def find_best_student(input_dict):
    name = max(input_dict, key=input_dict.get)
    return name


print(create_mean_mark_dict(students))
print(f'{find_best_student(create_mean_mark_dict(students))} has the best mark grades!')
