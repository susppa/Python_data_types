data = [
    {"student": "Alice", "subject": "Math", "grade": 5},
    {"student": "Bob", "subject": "Math", "grade": 4},
    {"student": "Alice", "subject": "History", "grade": 3},
    {"student": "Bob", "subject": "History", "grade": 5},
]


def get_marks_list(data):
    marks_by_subject = {}
    for item in data:
        if item['subject'] not in marks_by_subject:
            marks_by_subject[item['subject']] = {}
        marks_by_subject[item['subject']][item['student']] = item['grade']
    return marks_by_subject


print(get_marks_list(data))
