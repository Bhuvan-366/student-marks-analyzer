from analyzer import calculate_average, find_topper


def test_calculate_average():
    students = [
        {"name": "A", "marks": 90},
        {"name": "B", "marks": 80},
        {"name": "C", "marks": 95}
    ]

    assert round(calculate_average(students),2) == 88.33


def test_find_topper():
    students = [
        {"name": "A", "marks": 90},
        {"name": "B", "marks": 80},
        {"name": "C", "marks": 95}
    ]

    topper = find_topper(students)

    assert topper["name"] == "C"
    assert topper["marks"] == 95