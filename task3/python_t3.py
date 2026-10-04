list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]


def find_coincidences(list1, list2):
    coincidences = []
    for item in list1:
        if item in list2:
            coincidences.append(item)
    return coincidences


def find_unique(list1, list2):
    unique = []
    for item in list1:
        if item not in list2:
            unique.append(item)
    for item in list2:
        if item not in list1:
            unique.append(item)
    return unique


print(f'Elements present in both lists: {find_coincidences(list1, list2)}')
print(f'Elements unique to each list: {find_unique(list1, list2)}')
