items = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("tomato", "vegetable"),
    ("milk", "dairy")
]


def get_categorized_items(items):
    rezult = {}
    for item, category in items:
        if category not in rezult:
            rezult[category] = []
        rezult[category].append(item)
    return rezult


print(get_categorized_items(items))
