"""
PSA 4 - Question 5: Dictionaries, Sets, Nested Data and Data Consistency
Department of Computer Science and Engineering - Cybersecurity
JAIN (Deemed-to-be University)
"""

def find_common_courses(registrations, target="Arun", min_common=2):
    """
    Identifies all students sharing at least `min_common` distinct courses
    with the target student.
    - Excludes target student.
    - Eliminates duplicate course registrations.
    - Returns dictionary with student names as keys and alphabetically sorted lists
      of common courses as values.
    """
    common_students = {}

    # Guard check: Ensure target exists in registrations
    if target not in registrations:
        return common_students

    # Precompute unique courses of the target student using a set
    target_courses = set(registrations[target])

    for student, courses in registrations.items():
        # Exclude target student
        if student == target:
            continue

        # Set intersection automatically eliminates duplicate registrations
        # and finds distinct common courses
        common = target_courses & set(courses)

        # Threshold check: "at least two distinct courses" means >= 2
        if len(common) >= min_common:
            # Sort common courses alphabetically for consistency
            common_students[student] = sorted(common)

    return common_students


def run_tests():
    print("=" * 60)
    print("QUESTION 5: COURSE REGISTRATION TEST EXECUTION")
    print("=" * 60)

    registrations = {
        "Arun": ["Python", "Java", "SQL", "Python"],
        "Bala": ["Python", "C", "SQL"],
        "Charan": ["Java", "Python", "SQL"],
        "Divya": ["Python", "Java"],
        "Ezhil": ["C", "Java", "Java"]
    }

    # Test Case 1: Provided Dataset with target = "Arun"
    result = find_common_courses(registrations, target="Arun", min_common=2)
    expected = {
        "Bala": ["Python", "SQL"],
        "Charan": ["Java", "Python", "SQL"],
        "Divya": ["Java", "Python"]
    }

    print("\n[Test Case 1 - Provided Dataset]")
    print("Target:", "Arun")
    print("Actual Output:  ", result)
    print("Expected Output:", expected)

    assert result == expected, f"Test Case 1 Failed! Got {result}"

    # Test Case 2 (Edge Case): Student with duplicate courses in registrations
    # Ezhil had ["C", "Java", "Java"] - only shares 1 distinct course ("Java"), should not qualify
    assert "Ezhil" not in result, "Ezhil with only 1 distinct common course should not qualify!"

    # Test Case 3 (Edge Case): Non-existent target
    result_missing = find_common_courses(registrations, target="NonExistent")
    print("\n[Test Case 3 - Target Not Found]")
    print("Output for 'NonExistent':", result_missing)
    assert result_missing == {}, "Non-existent target should return empty dictionary!"

    # Test Case 4 (Edge Case): Target herself/himself excluded
    assert "Arun" not in result, "Target student must never appear in the output!"

    print("\nAll Test Cases Passed Successfully!\n" + "=" * 60)


if __name__ == "__main__":
    registrations = {
        "Arun": ["Python", "Java", "SQL", "Python"],
        "Bala": ["Python", "C", "SQL"],
        "Charan": ["Java", "Python", "SQL"],
        "Divya": ["Python", "Java"],
        "Ezhil": ["C", "Java", "Java"]
    }
    result = find_common_courses(registrations, target="Arun", min_common=2)
    print("Common courses:", result)
    print()
    run_tests()
