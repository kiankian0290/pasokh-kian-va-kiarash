def average(scores: list[float]) -> float:
    """Return the average of a list of numbers."""
    return sum(scores) / len(scores)


def add_average_to_students(students: list[dict]) -> None:
    """Add key 'average' to each student dict, in place."""
    for student in students:
        student["average"] = average(student["scores"])


def top_student(students: list[dict]) -> str:
    """Return the name of the student with the highest average."""
    best = max(students, key=lambda s: s["average"])
    return best["name"]


def passing_students(students: list[dict], threshold: float = 60) -> list[str]:
    """Return the names of students whose average is >= threshold."""
    return [s["name"] for s in students if s["average"] >= threshold]


def class_average(students: list[dict]) -> float:
    """Return the average of all students' averages."""
    if not students:  # اگر لیست خالی بود، از تقسیم بر صفر جلوگیری کن
        return 0.0
    return sum(s["average"] for s in students) / len(students)


def print_report(students: list[dict]) -> None:
    """Print each student's name, average, and Pass/Fail status."""
    for s in students:
        status = "Pass" if s["average"] >= 60 else "Fail"
        print(f"{s['name']}: {s['average']:.1f} ({status})")


def most_consistent_student(students: list[dict]) -> str:
    """Return the name of the student with the smallest score range (max - min)."""
    best = min(students, key=lambda s: max(s["scores"]) - min(s["scores"]))
    return best["name"]

# داده‌های نمونه
students = [
    {"name": "Sara", "scores": [82, 91, 76]},
    {"name": "Ali", "scores": [100, 95, 88]},
    {"name": "Niloofar", "scores": [60, 65, 70]},
    {"name": "Reza", "scores": [50, 55, 60]},
]

# ۱. اول میانگین‌ها رو اضافه کن
add_average_to_students(students)

# ۲. حالا خروجی‌ها رو بگیر
print("بترین دانشجو:", top_student(students))
print("دانشجویان قبول شده:", passing_students(students))
print("معدل کل کلاس:", class_average(students))
print("\n--- گزارش نهایی ---")
print_report(students)
print("\nبا ثبات‌ترین دانشجو:", most_consistent_student(students))