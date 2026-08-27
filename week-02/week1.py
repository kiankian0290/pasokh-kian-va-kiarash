def average(scores: list[float]) -> float:
    """Return the average of a list of numbers.

    Args:
        scores: e.g. [82, 91, 76]

    Returns:
        The mean of scores, e.g. 83.0

    WORKED EXAMPLE: this one is done for you. Use it as the pattern
    (signature, docstring, TODO -> real code) for every function below.
    """
    return sum(scores) / len(scores)


def add_average_to_students(students: list[dict]) -> None:
    """Add key 'average' to each student dict, in place.

    Args:
        students: e.g. [{"name": "Sara", "scores": [82, 91, 76]}, ...]
                  Use the `average` function above, don't recompute
                  the mean by hand here.

    Returns:
        None. Modifies each dict in `students` by adding an "average" key,
        e.g. {"name": "Sara", "scores": [82, 91, 76], "average": 83.0}
    """
    # TODO
    pass


def top_student(students: list[dict]) -> str:
    """Return the name of the student with the highest average.

    Args:
        students: list of student dicts that already have an "average" key
                  (call add_average_to_students first).

    Returns:
        The student's name, e.g. "Niloofar"
    """
    # TODO
    pass


def passing_students(students: list[dict], threshold: float = 60) -> list[str]:
    """Return the names of students whose average is >= threshold.

    Args:
        students: list of student dicts that already have an "average" key.
        threshold: minimum passing average (default 60).

    Returns:
        List of names, in the same order as `students`,
        e.g. ["Sara", "Ali", "Niloofar"]
    """
    # TODO
    pass


def class_average(students: list[dict]) -> float:
    """Return the average of all students' averages.

    Args:
        students: list of student dicts that already have an "average" key.

    Returns:
        A single float, e.g. 75.4
    """
    # TODO
    pass


def print_report(students: list[dict]) -> None:
    """Print each student's name, average, and Pass/Fail status.

    Args:
        students: list of student dicts that already have an "average" key.
                  A student passes if average >= 60 (reuse passing_students
                  or the same threshold logic).

    Returns:
        None. Just prints one line per student, e.g.:
        Sara: 83.0 (Pass)
    """
    # TODO
    pass


def most_consistent_student(students: list[dict]) -> str:
    """Return the name of the student with the smallest score range (max - min).

    Args:
        students: e.g. [{"name": "Sara", "scores": [82, 91, 76]}, ...]

    Returns:
        The student's name, e.g. "Niloofar"
    """
    # TODO (optional)
    pass