def build_roster(registrations):
    """
    Given a list of (student_id, course_id) pairs, build a course roster.

    The result should be a dictionary where:
      - each key is a course id (string)
      - each value is a sorted list of unique student ids (strings)
        enrolled in that course.

    Duplicate registrations for the same pair should appear only once.
    """

    roster = {}

    # Step 1: Build dictionary course_id -> set of unique student_ids
    for student_id, course_id in registrations:
        if course_id not in roster:
            roster[course_id] = set()
        roster[course_id].add(student_id)

    # Step 2: Convert each set to sorted list
    result = {course: sorted(students) for course, students in roster.items()}

    return result


if __name__ == "__main__":
    # Optional manual test
    sample = [
        ("s1", "CS101"),
        ("s2", "CS101"),
        ("s1", "MATH200"),
        ("s1", "CS101"),
    ]
    print(build_roster(sample))
